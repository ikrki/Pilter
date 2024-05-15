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

if __name__ == '__main__':
    #############Usage:###############
    # pdf_reader.get_pdf_files(asplos2024,"asplos2024")
    # pdf_reader.read_pdfs("asplos2024",keyword)
    # web_reader.read_papers(hpca2024, keyword, "hpca2024")
    for title in titles:
        excel_reader.collect_stats(files,title)
    # excel_reader.collect_stats(files,titles[4])
    pass
