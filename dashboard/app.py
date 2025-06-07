import dash
from dash import dcc, html
import plotly.graph_objs as go

cnn_accuracy = 0.85
xgb_accuracy = 0.80
combined_accuracy = 0.88

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tableau de Bord - Reconnaissance Produits", style={'textAlign': 'center'}),
    dcc.Graph(
        figure={
            'data': [
                go.Bar(name='CNN (Images)', x=['Modèles'], y=[cnn_accuracy]),
                go.Bar(name='XGBoost (Tabulaire)', x=['Modèles'], y=[xgb_accuracy]),
                go.Bar(name='Fusion', x=['Modèles'], y=[combined_accuracy]),
            ],
            'layout': go.Layout(
                title='Précision des Modèles',
                yaxis={'title': 'Précision'},
                barmode='group'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)