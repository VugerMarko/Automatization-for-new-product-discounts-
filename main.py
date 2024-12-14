from bs4 import BeautifulSoup
import requests
import csv


base_url = "https://www.muziker.hr/elektricne-gitare-svi-oblici"

page = 1
n = 0

with open('guitar.csv', 'w', newline='', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
    
        csvwriter.writerow(['ID', 'Guitar Name', 'Model', 'Price', 'Old Price', 'Discount', 'Status'])
    
        while True:
            url = ""

            if page != 1:
                    url = f"{base_url}?page={page}"
            else:
                url = base_url
                
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                guitars = soup.findAll("div", attrs={"class":"mzkr-col-6 mzkr-col-sm-4 mzkr-col-xxl-3 mzkr-d-flex"})
                
                for guitar in guitars:
                    
                    n += 1
                    print(f'new guitar +{n}')
                    
                    h4tag_name = guitar.find("h4")
                    name = h4tag_name.text.strip() if h4tag_name else 'N/A'
                    
                    if ' ' in name:
                        name, model = name.split(' ', 1)
                    else:
                        name, model = name
                    
                    print(name, model)
                    
                    price_tag = guitar.find('div', class_='price mzkr-mr-1')
                    dual_price_tag = price_tag.find('div', class_='dual-price lh-1 mzkr-mb-1')
                    
                    stock_status = guitar.find('div', class_='stock-status')
                    status = stock_status.text.strip() if stock_status else 'N/A'
                    
                    discount_badge = guitar.find('div', class_='badge badge-discount')
                    old_price = guitar.find('p', class_='text-crossed mzkr-mr-1')
                    
                    discount = discount_badge.text.strip() if discount_badge else 'N/A'
                    old = old_price.text.strip() if old_price else 'N/A'
                    
                    
                    if price_tag and dual_price_tag:
                        content_before_dual = []
                        for content in price_tag.contents:
                            if content == dual_price_tag:
                                break
                            content_before_dual.append(content)
                        price = ''.join(str(c).strip() for c in content_before_dual if str(c).strip())
                            
                    csvwriter.writerow([n, name, model, price, old, discount, status])

                if not guitars:
                    print("no more products. Stopping pagination.")
                    break

            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

            page += 1

