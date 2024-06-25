import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.sahaistanbul.org.tr/kume-firmalari/"
data = []

for page in range(1, 28):  # 27 sayfa olduğu varsayılıyor
    url = f"{base_url}{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    company_links = soup.select("a.card.shadow-sm")
    print(f"Page {page}: Found {len(company_links)} companies.")  

    for link in company_links:
        company_url = link['href']
        company_response = requests.get(company_url)
        company_soup = BeautifulSoup(company_response.content, "html.parser")

        name_tag = company_soup.select_one("div.titles h1")
        name = name_tag.text.strip() if name_tag else None

        contact_info = company_soup.select("ul.iletisim-bilgileri li")
        phone = contact_info[0].text.strip() if len(contact_info) > 0 else None
        email = contact_info[1].text.strip() if len(contact_info) > 1 else None
        website = contact_info[2].find("a")['href'] if len(contact_info) > 2 and contact_info[2].find("a") else None
        address = contact_info[3].text.strip() if len(contact_info) > 3 else None

        product_groups = []
        product_groups_tags = company_soup.select("div#pills-profile h4")
        for tag in product_groups_tags:
            product_groups.append(tag.text.strip())

        company_info = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Website": website,
            "Address": address,
            "Product Groups": ", ".join(product_groups)
        }

        print(company_info)
        data.append(company_info)

df = pd.DataFrame(data)

df.to_excel("company_data.xlsx", index=False)
print("Data has been successfully written to company_data.xlsx")
