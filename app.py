# app.py
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data
df = px.data.gapminder().query("year == 2007")

# Initialize the app
app = dash.Dash(__name__)
server = app.server  # Needed for Azure deployment

# Layout
app.layout = html.Div([
    html.H1("Gapminder Dashboard", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia'
    ),
    
    dcc.Graph(id='scatter-plot')
])

# Callback
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('continent-dropdown', 'value')]
)
def update_graph(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                     size='pop', color='country', hover_name='country',
                     log_x=True, size_max=60)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

