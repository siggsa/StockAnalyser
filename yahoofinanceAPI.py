"""
Yahoo finance API import. 
@Author Sigurd Aleksander Sagstad
"""
import norwegianStocks as nws
import yahoo_fin.stock_info as si
import pandas as pd
#import yfinance as yf

USD_TO_NOK = si.get_live_price("NOK=X") #Live price of USD in NOK

def return_info(ticker, parameter):
    try:
        quote = si.get_quote_table(ticker)
    except:
        print("Quote not found. Exit.")
        return None
    try:
        analysts_data = si.get_analysts_info(ticker)
    except:
        print("Analyst data not found. Exit.")
        return None
    
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

def check_valid_return(ticker):
    if return_info(ticker, "liveprice") == None:
        return False
    if return_info(ticker, "pe") == None:
        return False
    if return_info(ticker, "eps") == None:
        return False
    return True

def return_est_val(ticker):
    if check_valid_return(ticker) == False:
        print("Not valid return. Exit.")
        return
    live_val = return_info(ticker, "liveprice")
    est_val = return_info(ticker, "pe") * return_info(ticker, "eps")
    print("Live value: {0} \nEstimated value: {1}".format(live_val,est_val))

def all_info(ticker):
    print(si.get_quote_table(ticker))

def check_future_estval(ticker):
    if check_valid_return(ticker) == False:
        print("Not valid return. Exit.")
        return
    live_val = return_info(ticker, "liveprice")
    future_val = return_info(ticker, "1yest")
    print("Live value: {0} \n1 year future estimated value: {1}".format(live_val,future_val))
    
    
