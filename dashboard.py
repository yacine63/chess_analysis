import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd
import matplotlib.pyplot as plt

import fonctions
import preprocessing_steps
import stats

games_df = pd.read_csv("yacine_games.csv") 
print(games_df.head(3))

games_df = preprocessing_steps.preprocess(games_df) ; print(games_df.head(3))

white = games_df[games_df["white"]=="yacine63"]
black = games_df[games_df["black"]=="yacine63"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
fig = px.bar(white, x="opening", color="resultat", barmode="group", title="Yacine's perfomance with white")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)