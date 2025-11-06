import yfinance as yf

data = yf.download("9984.T", period="5d", interval="1d")
print(data.tail())
