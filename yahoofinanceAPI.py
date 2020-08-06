"""
Yahoo finance API import. 
@Author Sigurd Aleksander Sagstad
"""

import yahoo_fin.stock_info as si
import pandas as pd
#import yfinance as yf

USD_TO_NOK = 9.25 

def return_info(ticker, parameter):
    quote = si.get_quote_table(ticker)
    analysts_data = si.get_analysts_info(ticker)
    switcher = {
        "liveprice": si.get_live_price(ticker),
        "pe": quote["PE Ratio (TTM)"],
        "eps": quote["EPS (TTM)"],
        "1yest": quote["1y Target Est"],
        "prevclose": quote["Previous Close"],
        "open": quote["Open"],
        "bid": quote["Bid"],
        "ask": quote["Ask"],
        "dayrange": quote["Day's Range"],
        "52week": quote["52 Week Range"],
        "volume": quote["Volume"],
        "avgvolume": quote["Avg. Volume"],
        "beta": quote["Beta (5Y Monthly)"],
        "earningsdate": quote["Earnings Date"],
        "exday": quote["Ex-Dividend Date"],
        "fwddiv": quote["Forward Dividend & Yield"],
        "growthrate": analysts_data["Growth Estimates"]
    }
    func = switcher.get(parameter, lambda: "Invalid parameter")
    # print(quote)
    # print("-----------------------------------------------------------------------------")
    # print(analysts_data)
    return func

print(return_info("BIOT.ST", "growthrate"))

def return_est_val(ticker):


    estval = return_info(ticker, "pe") * return_info(ticker, "eps")
    print(estval)

#return_est_val("dnb.ol")


#print(quote["PE Ratio (TTM)"]) 
#print(quote["EPS (TTM)"])
#print(quote["1y Target Est"]) 

#----------------------------
