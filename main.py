import excel_reader
import pdf_reader
import web_reader

# acm
asplos2019 = ["https://dblp.uni-trier.de/db/conf/asplos/asplos2019.html"]
isca2019 = ["https://dblp.uni-trier.de/db/conf/isca/isca2019.html"]
micro2019 = ["https://dblp.uni-trier.de/db/conf/micro/micro2019.html"]
dac2019 = ["https://dblp.uni-trier.de/db/conf/dac/dac2019.html"]
# ieee
hpca2019 = "https://dblp.uni-trier.de/db/conf/hpca/hpca2019.html"
ispass2019 = "https://dblp.uni-trier.de/db/conf/ispass/ispass2019.html"
iiswc2019 = "https://dblp.uni-trier.de/db/conf/iiswc/iiswc2019.html"
iccad2019 = "https://dblp.uni-trier.de/db/conf/iccad/iccad2019.html"

asplos2024 = ["https://dblp.uni-trier.de/db/conf/asplos/asplos2024-1.html",
              "https://dblp.uni-trier.de/db/conf/asplos/asplos2024-2.html",
              "https://dblp.uni-trier.de/db/conf/asplos/asplos2024-3.html"]

hpca2024 = "https://dblp.uni-trier.de/db/conf/hpca/hpca2024.html"

hpca2025="https://dblp.uni-trier.de/db/conf/hpca/hpca2025.html"

asplos2025=["https://dblp.uni-trier.de/db/conf/asplos/asplos2025-1.html"]

keyword = "simulator"


class Item:
    def __init__(self, url, name, index):
        self.url = url
        self.name = name
        self.index = index


acm = [
    Item(asplos2019, "asplos2019", 1),
    Item(isca2019, "isca2019", 1),
    Item(micro2019, "micro2019", 1),
    Item(dac2019, "dac2019", 1)
]
ieee = [
    Item(hpca2019, "hpca2019", 1),
    Item(ispass2019, "ispass2019", 1),
    Item(iiswc2019, "iiswc2019", 1),
    Item(iccad2019, "iccad2019", 1)
]

files = ["模拟2019.xlsx", "模拟2020.xlsx", "模拟2021.xlsx", "模拟2022.xlsx", "模拟2023.xlsx"]
titles = ["使用工具",
          "公司",
          "公司/学校"
          ]

import requests

if __name__ == '__main__':
    # 2025.4.24:requests.get寄了，加header也不行
    # url="https://dl.acm.org/doi/pdf/10.1145/3669940.3707248"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    #     'Referer': 'https://dl.acm.org/doi/10.1145/3669940.3707248',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, br'
    # }
    #
    # response = requests.get(url, headers=headers)
    # print(response.status_code)   # 403!

    #############Usage:###############
    # pdf_reader.get_pdf_files(asplos2025,"asplos2025")
    pdf_reader.read_pdfs("hpca2025",keyword)
    # web_reader.read_papers(hpca2025, keyword, "hpca2025")
    # for title in titles:
        # excel_reader.collect_stats(files,title)
    # excel_reader.collect_stats(files,titles[0])
    pass
