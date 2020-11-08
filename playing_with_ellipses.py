import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

import flask
import pandas as pd
import time
import os

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app', server=server)

app.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Coke', 'value': 'COKE'}
        ],
        value='TSLA'
    ),
    dcc.Graph(id='my-graph')
], className="container")


@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    fig = go.Figure()

    # Create scatter trace of text labels
    fig.add_trace(go.Scatter(
        x=[1.5, 3.5],
        y=[0.75, 2.5],
        text=["Unfilled Circle",
              "Filled Circle"],
        mode="text",
    ))

    # Set axes properties
    fig.update_xaxes(range=[0, 4.5], zeroline=False)
    fig.update_yaxes(range=[0, 4.5])

    # Add circles
    fig.add_shape(type="circle",
                  xref="x", yref="y",
                  x0=1, y0=1, x1=3, y1=3,
                  line_color="LightSeaGreen",
                  )
    fig.add_shape(type="circle",
                  xref="x", yref="y",
                  fillcolor="PaleTurquoise",
                  x0=3, y0=3, x1=4, y1=4,
                  line_color="LightSeaGreen",
                  )

    # Set figure size
    fig.update_layout(width=800, height=800)

    return fig


if __name__ == '__main__':
    app.run_server()
