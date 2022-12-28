from bs4 import BeautifulSoup
import requests
import sys

PAGE_URL = 'https://www.amazon.com/SteelSeries-Apex-Gaming-Keyboard-Anti-Ghosting/dp/B09FTNMT84/ref=sr_1_1_sspa'

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept-Language': 'en-US, en;q=0.5'})

r = requests.get(PAGE_URL, headers=HEADERS)

if (not r.ok):
    print("Status code is not 20*:", r.status_code)
    sys.exit()


soup = BeautifulSoup(r.text, 'html.parser')

price_whole = soup.find('span', 'a-price-whole').get_text()
price_fraction = soup.find('span', 'a-price-fraction').get_text()
full_price = price_whole + price_fraction

print(full_price)
