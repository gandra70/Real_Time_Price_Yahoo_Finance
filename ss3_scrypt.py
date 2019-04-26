import dash
import datetime
import pandas_datareader.data as web
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# ------ choose your external design ------ #
# https://codepen.io/chriddyp/pen/bWLwgP.css

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


colors = {
    'background': '#000000' ,
    'text': '#ffffff '
}



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']},
    children=[html.H1(children='Get Real Time Price From Yahoo',
                      style = {
                          'textAling': 'center',
                          'color': colors['text']
                      }
                      ),dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
              html.Div(children='Dash: Python web app',
                       style = {
                           'textAling': 'center',
                           'color': colors['text']
                       })

    ]
)
@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input', component_property='value')])

def update_value(input_data):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)


    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)