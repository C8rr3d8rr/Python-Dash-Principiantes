# ============================
# Dashboard con Dash en Python (con archivo Excel)
# ============================
# pip install dash plotly pandas openpyxl

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Paso 1: Cargar datos desde Excel
df = pd.read_excel(r"") --> Ruta del archivo

# Paso 2: Crear gráficos con Plotly
fig_line = px.line(
    df,
    x="Mes",
    y=["Ventas", "Costos"],
    title="Comparación Ventas vs Costos"
)

fig_bar = px.bar(df, x="Mes", y="Costos", title="Costos por Mes", color="Mes")
fig_pie = px.pie(df, names="Categoria", title="Distribución por Categoría")

# Paso 3: Inicializar la app Dash
app = dash.Dash(__name__)

# Paso 4: Estructura del layout
app.layout = html.Div(
    style={"backgroundColor": "#111111", "padding": "20px"},
    children=[
        html.H1(
            "Dashboard de Ejemplo con Excel",
            style={
                "textAlign": "center",
                "fontWeight": "bold",
                "textDecoration": "underline",
                "color": "white"
            }
        ),

        html.Div([
            html.H3("📈 Ventas vs Costos (Líneas)",
                    style={
                        "textAlign": "center",
                        "fontWeight": "bold",
                        "textDecoration": "underline",
                        "color": "white"
                    }),
            dcc.Graph(figure=fig_line)
        ], style={"width": "48%", "display": "inline-block"}),

        html.Div([
            html.H3("📊 Gráfico de Barras",
                    style={
                        "textAlign": "center",
                        "fontWeight": "bold",
                        "textDecoration": "underline",
                        "color": "white"
                    }),
            dcc.Graph(figure=fig_bar)
        ], style={"width": "48%", "display": "inline-block"}),

        html.Div([
            html.H3("🥧 Gráfico de Pastel",
                    style={
                        "textAlign": "center",
                        "fontWeight": "bold",
                        "textDecoration": "underline",
                        "color": "white"
                    }),
            dcc.Graph(figure=fig_pie)
        ], style={"width": "48%", "margin": "auto"})
    ]
)

# Paso 5: Correr el servidor
if __name__ == "__main__":
    app.run(debug=True)
