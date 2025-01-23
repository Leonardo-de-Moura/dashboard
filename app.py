import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


df = pd.DataFrame({
    "categoria": ['A', 'B', 'C', 'D'],
    "valor": [15, 25, 40, 50]
})

fig = px.bar(df, x='categoria', y='valor', title='exemplo de grafico usando dash')

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("dashboard"),
    dcc.Graph(figure=fig),  
])



app.run(debug=True, host="localhost")
