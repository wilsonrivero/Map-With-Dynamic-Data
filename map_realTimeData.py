from random import randint
import dash
from dash.dependencies import Output, Input
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html


df = px.data.gapminder().query("year == 2007")

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Dash map'),
    dcc.Interval(id='interval'),
    dcc.Graph(
        id='map',
    )
])

database = {
    'iso_alpha':[],
    'cases':[]
}

def updateDataBase(values):
    country = list(df['iso_alpha'])
    countries = country[randint(0,141)]
    if countries not in database['iso_alpha']:
        database['iso_alpha'].append(countries)
        database['cases'].append(randint(1, 10000))




@app.callback(
    Output('map', 'figure'),
    Input('interval', 'n_intervals')
)
def realTimeUpdateGraph (n_intervals):
    updateDataBase(n_intervals)
    graph = px.scatter_geo(database, locations='iso_alpha', size='cases')
    return graph


app.run_server()
