#Sandbox
import yahoofinanceAPI as yfa
import norwegianStocks as nws

#Variables
testStocks = ["DNB.OL", "NEL.OL", "EQNR.OL"]
allNorwegianStocks = nws.get_tickers()


def test_list(stock_tickers):
        viable_stocks = []
        for ticker in stock_tickers:
            live_price = yfa.get_live_price(ticker)
            future_est = yfa.get_future_estval(ticker)
            print("\n")
            print("{0}".format(ticker))
            if future_est > live_price:
                viable_stocks.append(ticker)
        print(viable_stocks)
        return viable_stocks

test_list(testStocks)
#test_list(allNorwegianStocks)
