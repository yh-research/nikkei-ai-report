import yfinance as yf


print("株価データを取得中...")
data = yf.download("7203.T", period="1d", interval="1h")
print("最新データ: ")
print(data.tail())
