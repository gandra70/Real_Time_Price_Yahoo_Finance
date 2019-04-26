

from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='76XSYD32JHMX16ZAY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))