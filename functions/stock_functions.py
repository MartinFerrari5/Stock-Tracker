import pandas as pd
import streamlit as st
import yfinance as yf
# Importar dataset
stocks_df = pd.read_csv("./datasets/companies.csv").set_index('ticker')
def clean_dataset():
    """ Filtrar por las acciones con mas de 100.000.000 de market cap
    market cap = cantidad de acciones * valor de la accion
    Renombrar columnas e indice """
    
    try:
        filtered_stocks_df = stocks_df[stocks_df['market cap'] > 100000000000].rename(columns={'short name': 'Compañia','market cap': 'Capitalizacion (USD)'})
        filtered_stocks_df.index.name = 'Ticker'
        return filtered_stocks_df
    except Exception as e:
        print('Error al limpiar el dataset', e)


def period():

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
    except:
        print('Error al obtener el periodo de el dataset')

def get_ticker(options,stocks_df):
    
    try:
        if options:
            return stocks_df[stocks_df['Compañia'].isin(options)][['Compañia','Capitalizacion (USD)']]
        return stocks_df[['Compañia','Capitalizacion (USD)']]
    except Exception as e:
        print('Error al obtener el ticker', e)

def selected_stocks_function(options):
    try:
        if options:
            tickers = [i[:i.find(' ')] for i in options]
        df = []
        for t in tickers:
            df_new = yf.Ticker(t).history(period=st.session_state.period).reset_index()
            df_new['Ticker'] = t
            df.append(df_new)
        df = pd.concat(df)
        pivot_df = df.pivot_table(index='Date', columns='Ticker',values='Close')
        print(pivot_df)
        return pivot_df
    except:
        print('Error al obtener las acciones')