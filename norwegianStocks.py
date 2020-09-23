#All companies listed at Norwegian stock market.

import requests as r
from lxml import html
import pandas as pd
print("Something")
page = r.get("https://en.wikipedia.org/wiki/Banana")
#page = r.get("http://www.nasdaqomxnordic.com/shares/listed-companies/norwegian-listed-shares")
#tree = html.fromstring(page.content)
page.close
if page.status_code == 200:
    rest = page.text
    stripped = r.sub('>[^<+?{}', ''
#print()
"""
data = pd.DataFrame(
    [[j.text_context() for j in i.getchildren() [:-1]] for i in trs],
    columns = ["name", "symbol", "currency", "isin", "sector", "icb"]
    )

data["tickers"] = ["-".join(i.split(" "))+".OL" for i in data["symbol"].values]

"""
