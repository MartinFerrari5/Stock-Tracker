# Importar librerias a utilizar
import streamlit as st
import yfinance as yf
# Importar udf (user defined functions)
from functions.stock_functions import period, clean_dataset,selected_stocks_function

# Configuarcion de la pagina
st.set_page_config(
    page_title= 'Stock Tracker',
    page_icon= '📈',
    layout= 'wide'
)

# Titulo de la pagina
st.title('Stock Tracker')

# Filtrado del dataset
filtered_stocks_df = clean_dataset()
filtered_stocks_df['ticker_company'] = filtered_stocks_df.index + ' - ' + filtered_stocks_df['Compañia']

# Input para la seleccion de acciones
options = st.multiselect(
    "Elige un accion para graficar su desempeño",
    filtered_stocks_df['ticker_company'],
    max_selections=3,
    placeholder="Introduce el nombre de la compañia",
    default=['AAPL - Apple']
)

# Seleccion del periodo (1 dia, 1 semana, 1 mes, 1 año, 5 años)
stock_period = period()

# Resultado de la eleccion de acciones
selected_stocks  = selected_stocks_function(options)

# Grafico de linea
if options:
    st.line_chart(selected_stocks, x_label="Fecha", y_label="Precio de Cierre")
