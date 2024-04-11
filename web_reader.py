import time

from selenium import webdriver
import excel_writer


def read_papers(url: str, keyword: str, name: str, start_at: int = 1):
    output_file = 'papers/'+ name + ".xlsx"
    driver = webdriver.Edge()
    driver.get(url)
    elements = driver.find_elements(
        by="xpath",
        value="//ul[@class='publ-list']//li[@class='entry inproceedings']//nav//ul//li[1]//div[@class='head']//a"
    )
    hrefs = []
    for element in elements:
        hrefs.append(element.get_attribute("href"))
    i = start_at - 2
    while i < len(elements) - 1:
        i += 1
        print(f"Reading the [{str(i + 1)} / {str(len(elements))}] paper of '{name}' ...")
        url = hrefs[i]
        print(url)
        try:
            driver.get(url)
        except:
            i -= 1
            continue

        print("Got page")
        try:
            driver.find_element(by="class name", value="shutpage-background")
            print("IEEE unavailable, refreshing...")
            i -= 1
            time.sleep(5)
            continue
        except:
            pass

        try:
            accept_button = driver.find_element(by="css selector", value="button.osano-cm-accept-all")
            accept_button.click()
            print("Closed bottom dialog.")
        except:
            pass

        time.sleep(1)
        descriptions = []
        authors = []
        institutions = []
        xpath_query = f"//p[contains(., '{keyword}')]"
        print("Searching for keyword...")
        matching_elements = driver.find_elements(by="xpath", value=xpath_query)
        for element in matching_elements:
            descriptions.append(element.text)
            print(element.text)
        print(f"Number of occurrences of '{keyword}': {len(matching_elements)}")
        time.sleep(5)
        if len(matching_elements) == 0: continue
        print("Found keyword. Extracting author information...")
        try:
            close_button = driver.find_element(by="class name", value="osano-cm-dialog__close.osano-cm-close")
            close_button.click()
            print("Closed bottom dialog.")
        except:
            pass

        time.sleep(1)
        driver.find_element(by="id", value="authors-header").click()
        time.sleep(1)

        authors_containers = driver.find_elements(by="class name", value="authors-accordion-container")
        for authors_container in authors_containers:
            divs_inside_col = authors_container.find_element(by="class name", value="col-24-24").find_elements(
                by="tag name", value="div")
            span_text = divs_inside_col[0].find_element(by="tag name", value="a").find_element(by="tag name",
                                                                                               value="span").text

            print("Author:", span_text)
            authors.append(span_text)

            nested_div_text = divs_inside_col[1].find_element(by="tag name", value="div").text
            print("Institute:", nested_div_text)
            institutions.append(nested_div_text)

        title = driver.find_element(by="xpath",
                                    value="//div[@class='document-header-title-container col']//div//h1//span").text
        print("Title:", title)
        excel_writer.write_to_excel(title, descriptions, authors, institutions, output_file)

    excel_writer.adjust_column_widths(output_file)
    driver.quit()
