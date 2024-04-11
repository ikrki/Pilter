import os

import pandas as pd
import openpyxl
from openpyxl.reader.excel import load_workbook


def write_to_excel(title, description, names, institutions, output_file):
    maxlen = max(len(description), len(names), len(institutions))
    title_padded = [title] + [''] * (maxlen - 1)
    description_padded = description + [''] * (maxlen - len(description))
    names_padded = names + [''] * (maxlen - len(names))
    institutions_padded = institutions + [''] * (maxlen - len(institutions))
    df = pd.DataFrame({
        "Title": title_padded,
        "Description": description_padded,
        "Name": names_padded,
        "Institution": institutions_padded
    })

    try:
        existing_df = pd.read_excel(output_file)
        df = pd.concat([existing_df, pd.DataFrame({col: [''] for col in df.columns})] + [df],
                       ignore_index=True)
        df.to_excel(output_file, index=False)
    except FileNotFoundError:
        df.to_excel(output_file, index=False)

    print(f"Data for '{title}' has been written to {output_file}")


def adjust_column_widths(output_file):
    if os.path.exists(output_file):
        wb = load_workbook(output_file)
        ws = wb.active
        ws.column_dimensions['A'].width = 40
        ws.column_dimensions['B'].width = 60
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 30
        wb.save(output_file)
