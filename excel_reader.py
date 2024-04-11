import os
import re
import pandas as pd


class Simulator:
    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count


def collect_stats(files: [], title: str):
    dic = {}
    for file in files:
        file_path = 'input/' + file
        excel_file = pd.ExcelFile(file_path)
        sheets = excel_file.sheet_names
        for sheet in sheets:
            data = pd.read_excel(excel_file, sheet_name=sheet)
            data.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
            print(f'========{file} : {sheet}========')
            column = None
            try:
                column = data[title]
            except:
                print("not exist")
                continue
            print(column)

            for item in column:
                names = re.split("[,，、/&+]", str(item))
                for name in names:
                    if len(name) == 0: continue
                    # print(name)
                    if name[-1] == '2' or name[-1] == '3':
                        name = name[:-1]
                    s = name.lower().replace(' ', '').replace('-', '')
                    if s in dic:
                        dic[s].count += 1
                    else:
                        dic[s] = Simulator(name, 1)

    sorted_dict = sorted(dic.items(), key=lambda x: x[1].count, reverse=True)
    sum = 0
    for key, value in sorted_dict:
        sum += value.count
    print(f"Total: {sum}")
    if not os.path.exists('result'): os.makedirs('result')
    output_file = f'result/{title.replace('/', '-')}.txt'
    with open(output_file, "w", encoding='utf-8') as file:
        # Iterate over the sorted dictionary
        for key, value in sorted_dict:
            # Write each key-value pair to the file in the specified format
            file.write(f"{value.name} {value.count}\n")
            # print(f"{value.name} : {value.count}")
        file.write(f"Total: {sum}")
