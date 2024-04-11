import os
import time
import PyPDF2
import requests
from selenium import webdriver
import excel_writer


def download_file(url: str, destination: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully to '{destination}'")
    else:
        print(f"Failed to download file from '{url}', status code: {response.status_code}")


def get_pdf_files(urls: [str], name: str, start_at: int = 1):
    driver = webdriver.Edge()
    hrefs = []
    for url in urls:
        driver.get(url)
        elements = driver.find_elements(
            by="xpath",
            value="//ul[@class='publ-list']//li[@class='entry inproceedings']//nav//ul//li[1]//div[@class='head']//a"
        )
        for element in elements:
            href = element.get_attribute("href")
            print(href)
            hrefs.append(element.get_attribute("href"))
    driver.quit()

    pdf_urls = []
    for href in hrefs:
        url = "https://dl.acm.org/doi/pdf" + href[href.find("doi.org") + 7:]
        print(url)
        pdf_urls.append(url)

    for i in range(start_at - 1, len(pdf_urls)):
        path='papers/'+name
        if not os.path.exists(path): os.makedirs(path)
        print(f"Downloading [{str(i + 1)} / {str(len(pdf_urls))}] ...")
        time.sleep(10)
        download_file(pdf_urls[i], path + "/" + str(i + 1) + ".pdf")


def safe_append(lines: [], str):
    temp = ""
    for char in str:
        if 32 <= ord(char) < 128:
            temp += char
    lines.append(temp)


def search_pdf(file_path: str, keyword: str, output_file: str):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        lines = []
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines += text.split('\n')

        extracted_lines = []
        for i in range(len(lines)):
            if keyword in lines[i]:
                if i > 0: safe_append(extracted_lines, lines[i - 1])
                safe_append(extracted_lines, lines[i])
                if i < len(lines): safe_append(extracted_lines, lines[i + 1])
                print(f"Keyword '{keyword}' found on line: {lines[i]}")

        info = []
        if len(extracted_lines) > 0:
            for line in lines:
                if 'abstract' in line.lower() or len(info) > 20: break
                safe_append(info, line)

            for info_line in info: print(info_line + '\n')
            title=''
            if len(info)>0: title=info[0]
            excel_writer.write_to_excel(title, extracted_lines, [], info, output_file)


def read_pdfs(name, keyword, start_at=1, end_at=1000):
    path='papers/'+name
    files = os.listdir(path)
    for i in range(start_at - 1, min(end_at, len(files))):
        print(f"Searching in [{str(i + 1)} / {str(len(files))}] ({files[i]}) of '{name}' ...")
        search_pdf(path + "/" + files[i], keyword, path + ".xlsx")
    excel_writer.adjust_column_widths(path + ".xlsx")
