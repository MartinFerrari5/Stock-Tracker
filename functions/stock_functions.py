import pandas as pd
import streamlit as st
import yfinance as yf
# Importar dataset
stocks_df = pd.read_csv("./datasets/companies.csv").set_index('ticker')
def clean_dataset():
    """ 
    Filtrar por las acciones con mas de 100.000.000 de market cap
    market cap = cantidad de acciones * valor de la accion
    Renombrar columnas e indice
    
    """
    
    try:
        filtered_stocks_df = stocks_df[stocks_df['market cap'] > 100000000000].rename(columns={'short name': 'Compañia','market cap': 'Capitalizacion (USD)'})
        filtered_stocks_df.index.name = 'Ticker'
        return filtered_stocks_df
    except Exception as e:
        st.error('Error al limpiar el dataset', e)


def period():
    """
    Muestra una fila de botones en la interfaz para seleccionar un período de tiempo
    y guarda la selección en `st.session_state`.

    Opciones disponibles:
        - Día ('1d')
        - Semana ('1wk')
        - Mes ('1mo')
        - Año ('1y')
        - 5 Años ('5y')

    Si no se ha seleccionado un período previamente, se establece por defecto en '1y'.

    Return:
        str: El período seleccionado, almacenado en st.session_state.period.

    Error:
        Imprime un mensaje si ocurre una excepción.
    """
    try:
        if 'period' not in st.session_state:
            st.session_state.period = '1y'
            
        day, week, month, year,five_years = st.columns(5)

        if day.button('Dia', key='day',use_container_width=True):
            st.session_state.period = '1d'
        if week.button('Semana',use_container_width=True):
            st.session_state.period = '1wk'
        if month.button('Mes',use_container_width=True):
            st.session_state.period = '1mo'
        if year.button('Año',use_container_width=True):
            st.session_state.period = '1y'
        if five_years.button('5 Años',use_container_width=True):
            st.session_state.period = '5y'
        
        return st.session_state.period
    except Exception as e:
        st.error('Error al obtener el periodo', e)

def get_ticker(options,stocks_df):
    """
    Filtra el DataFrame de acciones según las compañías seleccionadas.

    Si se proporcionan compañías en options, devuelve solo las filas correspondientes a esas compañías.
    Si `options` está vacío o es None, devuelve todas las compañías con su capitalización.

    Args:
        options (list or None): Lista de nombres de compañías seleccionadas.
        stocks_df (pd.DataFrame): DataFrame que contiene al menos las columnas 'Compañia' y 'Capitalizacion (USD)'.

    Returns:
        pd.DataFrame: Subconjunto del DataFrame original con las columnas 'Compañia' y 'Capitalizacion (USD)'.

    Error:
        Imprime un mensaje de error si ocurre una excepción durante el filtrado.
    """
    try:
        if options:
            return stocks_df[stocks_df['Compañia'].isin(options)][['Compañia','Capitalizacion (USD)']]
        return stocks_df[['Compañia','Capitalizacion (USD)']]
    except Exception as e:
        st.error(f'Error al obtener el ticker: {e}')

def selected_stocks_function(options):
    """
    Obtiene el historial de precios de cierre para una lista de acciones seleccionadas
    y devuelve un DataFrame pivoteado con fechas como índices y tickers como columnas.

    La función extrae el símbolo (ticker) desde cada string en options, consulta los
    datos históricos usando Yahoo Finance (yfinance) según el período especificado en
    st.session_state.period, y los organiza en formato tabla con los precios de cierre.

    Args:
        options (list of str): Lista de strings con nombre de acciones, donde el ticker
                               está al inicio (antes del primer espacio).

    Returns:
        pd.DataFrame: DataFrame pivoteado con fechas como índice, tickers como columnas
                      y valores correspondientes al precio de cierre ('Close').

    Error:
        Imprime un mensaje de error  si ocurre alguna excepción.
    """
    try:
        if options:
            tickers = [i[:i.find(' ')] for i in options]
            df = []
            for t in tickers:
                df_new = yf.Ticker(t).history(period=st.session_state.period).reset_index()
                df_new['Ticker'] = t
                df.append(df_new)
            df = pd.concat(df)
            df['Date'] = df.Date.dt.strftime('%Y-%m-%d')
            pivot_df = df.pivot_table(index='Date', columns='Ticker',values='Close')
            return pivot_df
    except Exception as e:
        st.error('Error al obtener la accion', e)