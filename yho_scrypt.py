import pandas_datareader.data as web
import datetime


start = datetime.datetime(2018, 1 , 1)
end = datetime.datetime.now()
ticker = 'BTC-USD'

df = web.DataReader(ticker, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)


print(df.head())