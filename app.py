import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Exemplo de dados
df = pd.DataFrame({
    "Categoria": ['A', 'B', 'C', 'D'],
    "Valor": [10, 20, 30, 40]
})

fig = px.bar(df, x='Categoria', y='Valor', title='Exemplo de Gráfico de Barras')

app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div([
    html.H1("Meu Dashboard em Python"),
    dcc.Graph(figure=fig),  # Exibindo o gráfico
])

# Rodando o servidor

app.run_server(debug=True)
