import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2018, 1 , 1)
end = datetime.datetime.now()
ticker = 'BTC-USD'
df = web.DataReader(ticker, 'yahoo', start, end)



app = dash.Dash()

app.layout = html.Div(children=[ html.H1(children='Interactive Real Time Price Charts'),
                                 html.Div(children=[html.H2(children='''CryptoCurrencies''')]),
                                 dcc.Graph(id='real-time-graph',
                                           figure = {
                                               'data': [
                                                   {'x': df.index, 'y': df.Close, 'type': 'line', 'name': ticker}],
                                               'layout': { 'title': ticker }})])

def update_value(input_data):
    return 'Input: {}'.format(input_data)


if __name__ == '__main__':
    app.run_server(debug=True)















# app.layout = html.Div(children=[
#     html.H1('Interactive Table'),
#     dcc.Graph(id='example',
#         figure ={
#             'data': [
#                 {'x':[1,2,3,4,5,6], 'y':[5,8,9,6,3], 'type':'line', 'name':'boats'},
#                 {'y':[1,2,3,4,5], 'y':[7,8,2,5,6], 'type':'bar', 'name':'cars'},],
#                 'layout': {'title': 'Basic Dash Ex'
#                 }
#             })
#     ])

