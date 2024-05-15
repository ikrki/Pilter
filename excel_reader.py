import os
import re
import pandas as pd


class Simulator:
    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count

def collect_stats(files: [], title: str):
    dic = {}
    conf_dict = {}
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

            for i in range(len(column)):
                item=column[i]
                type=str(data['类别'][i])
                if 'RTL' in type:
                    print("skipped "+type)
                    continue
                names = re.split("[,，、/&+]", str(item)) if not title=="公司/学校" else [str(item)]
                for name in names:
                    if len(name) == 0: continue
                    if name[-1] == '2' or name[-1] == '3':
                        name = name[:-1]
                    s = name.lower().replace(' ', '').replace('-', '')

                    if not sheet in conf_dict: conf_dict[sheet] = 0
                    if not s=='nan': conf_dict[sheet] += 1

                    if s in dic:
                        dic[s].count += 1
                    else:
                        dic[s] = Simulator(name, 1)

    sorted_dict = sorted(dic.items(), key=lambda x: x[1].count, reverse=True)
    sum = 0
    for key, value in sorted_dict:
        if key == 'nan': continue
        sum += value.count

    print(f"Total: {sum}")
    if not os.path.exists('result'): os.makedirs('result')
    output_file = f'result/{title.replace('/', '-')}.txt'
    with open(output_file, "w", encoding='utf-8') as file:
        for key, value in sorted_dict:
            if key == 'nan': continue
            file.write(f"{value.name} {value.count}\n")
        file.write(f"Total: {sum}\n")
        if not title=='公司/学校':return
        for key, value in conf_dict.items():
            file.write(f"{key} {value}\n")

