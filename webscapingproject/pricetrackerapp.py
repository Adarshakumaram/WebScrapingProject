import requests
from bs4 import BeautifulSoup #butifulshoup

#URL = 'https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=sr_1_1_sspa?dchild=1&keywords=m31&qid=1620652811&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKSjlGUDk4UUpDMkUmZW5jcnlwdGVkSWQ9QTA5NTUxNzExREJYS0g5TERKWDZPJmVuY3J5cHRlZEFkSWQ9QTA4MTk1OTAyTzZUUlZFMDk0U0lRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
#URL = 'https://www.amazon.in/Samsung-Galaxy-Midnight-Blue-Storage/dp/B07HGJJ559/ref=sr_1_1_sspa?dchild=1&keywords=m21&qid=1620653402&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTUQ4Qk5OOEVKN0lMJmVuY3J5cHRlZElkPUEwNzI4MTU3Q1dLSlhJM0lKWlBZJmVuY3J5cHRlZEFkSWQ9QTAzNTQzNzQxU1RaVzU5VDJaSjNCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
#URL = 'https://www.amazon.in/Test-Exclusive-557/dp/B077PWJ8RS/ref=sr_1_2?dchild=1&keywords=note+9+pro+max&qid=1620654191&sr=8-2'
products_to_track = [
    {
       "product_url": "https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=sr_1_1_sspa?dchild=1&keywords=m31&qid=1620652811&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKSjlGUDk4UUpDMkUmZW5jcnlwdGVkSWQ9QTA5NTUxNzExREJYS0g5TERKWDZPJmVuY3J5cHRlZEFkSWQ9QTA4MTk1OTAyTzZUUlZFMDk0U0lRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
       # "name": "Mef"
       "name":"Samsung M31",
        "target_price": 14500
    },
    {"product_url": "https://www.amazon.in/Samsung-Galaxy-Midnight-Blue-Storage/dp/B07HGJJ559/ref=sr_1_1_sspa?dchild=1&keywords=m21&qid=1620653402&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTUQ4Qk5OOEVKN0lMJmVuY3J5cHRlZElkPUEwNzI4MTU3Q1dLSlhJM0lKWlBZJmVuY3J5cHRlZEFkSWQ9QTAzNTQzNzQxU1RaVzU5VDJaSjNCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
    "name": "Samsung M21",
    "target_price":  14000
    },
    {
    "product_url": "https://www.amazon.in/Test-Exclusive-557/dp/B077PWJ8RS/ref=sr_1_2?dchild=1&keywords=note+9+pro+max&qid=1620654191&sr=8-2",
    "name" : "Redmi note9",
    "target_price": 15000
    }
]
def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    #print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()

result_file = open('my_result_file.txt','w')
try:
    for every_product in products_to_track:
        p_p_r = give_product_price(every_product.get("product_url"))  # product_price_returned
        print(p_p_r + " - " + every_product.get("name"))
        m_p_p = p_p_r[2:]
        m_p_p = m_p_p.replace(',', '')
        print(m_p_p)
        m_p_p = float(m_p_p)

        if m_p_p < every_product.get("target_price"):  # my_product_price
            print("Available at your price")
            result_file.write(
                every_product.get("name") + '\t' + ' Available at Target price' +' Current Price - ' + str(m_p_p)+"\n")
        else:
            print("Still at current price")

finally:
    result_file.close()


