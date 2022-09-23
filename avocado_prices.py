from gc import callbacks
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

avocado = pd.read_csv('avocado.csv')

app = Dash()

app.layout = html.Div(
    [html.H1('Avocado Price Dashboard'),
    dcc.Dropdown(id = 'dropdown_city', options = sorted(avocado['geography'].unique())),
    dcc.Graph(id = 'display_graph'),
    ]
)

@app.callback(
    Output('display_graph', 'figure'),
    Input('dropdown_city', 'value')
)

def update_graph(selected_city):
    filtered_avocado = avocado[avocado['geography'] == selected_city]
    graph = px.line(filtered_avocado, x = 'date', y = 'average_price', color = 'type')
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)