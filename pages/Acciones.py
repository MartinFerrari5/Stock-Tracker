"""
Pagina donde se muestran los Tickers de las acciones
con el nombre de las empresas

Ej: AAPL -> Apple

"""
# Importar librerias a utilizar
import streamlit as st
import pandas as pd

# Importar udf (user defined functions)
from functions.stock_functions import get_ticker, clean_dataset

st.set_page_config(
    page_title= 'Stock Tracker',
    page_icon= '📈',
    layout= 'wide'
)


filtered_stocks_df = clean_dataset()

# Titulo de la nueva pagina
st.title('Registro de Acciones')

options = st.multiselect(
    "Elige tu accion favorita",
    filtered_stocks_df['Compañia'],
    max_selections=5,
    placeholder="Introduce el nombre de la compañia"
)


# Tabla con informacion de las acciones
st.dataframe(get_ticker(options,filtered_stocks_df),height=800, width=800)