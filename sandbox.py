#Sandbox
import yahoofinanceAPI as yfa
import norwegianStocks as nws

#Variables
testStocks = ["DNB.OL", "NEL.OL", "EQNR.OL"]
allNorwegianStocks = nws.get_tickers()


def test_list(stock_tickers):
        for ticker in stock_tickers:
            print("\n")
            print("{0}".format(ticker))
            yfa.check_future_estval(ticker)

#test_list(testStocks)
test_list(allNorwegianStocks)
