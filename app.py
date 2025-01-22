import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


df = pd.DataFrame({
    "Categoria": ['A', 'B', 'C', 'D'],
    "Valor": [10, 20, 30, 40]
})

fig = px.bar(df, x='Categoria', y='Valor', title='Exemplo de Gráfico de Barras')

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Dashboard ."),
    dcc.Graph(figure=fig),  
])



app.run(debug=True)
