#All companies listed at Norwegian stock market, data from wikipedia.

import requests as r
from lxml import html
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Oslo_Stock_Exchange"
page = r.get(url)
page.close()

data = pd.read_html(page.text)
data_combined = data[1].iloc[:, :-2].copy()

tickers_data = data[1].iloc[:, 1].copy().values.flatten()
tickers = []
for ticker in tickers_data:
    tickers.append(ticker.replace("OSE: ", "")) 
    
#print(tickers)

