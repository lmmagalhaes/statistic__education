import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import requests



st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)

bbas3 = yf.download("BBAS3.SA", start="2000-01-01", end="2025-01-01")
ibov = yf.download("^BVSP", start="2000-01-01", end="2025-01-01")



precos_fechamento = bbas3['Close'].resample('Y').last()
precos_fechamentoIbov = ibov['Close'].resample('Y').last()

df_cotacoes = pd.DataFrame(precos_fechamento)
df_cotacoes_ibov = pd.DataFrame(precos_fechamentoIbov)
df_cotacoes.index = df_cotacoes.index.year
df_cotacoes_ibov.index = df_cotacoes_ibov.index.year
df_cotacoes.rename(columns={'Close': 'Fechamento'}, inplace=True)
df_cotacoes["BBAS3.SA"] = round(df_cotacoes["BBAS3.SA"], 2)
df_cotacoes["IBOVESPA"] = df_cotacoes_ibov['^BVSP']


st.write(df_cotacoes)




fig = go.Figure(data=[go.Bar(
    x=df_cotacoes.index,
    y=round(df_cotacoes['BBAS3.SA'],2),

)])

fig.update_layout(
    title="Comparação",
    xaxis_title="Ano",
    yaxis_title="Preço da Ação",
    xaxis=dict(tickangle=-45),
    template="plotly_white",
    height=600,
    width=900
)

st.plotly_chart(fig, use_container_width=True)


""""
Primeiro vou buscar as cotações de BBAS3 ao longo dos anos

Depois vou pegar o lucro da empresa ao longo dos anos
Vou ter o ano e a ação

Vou pegar o indice bovespa ao longo dos anos



"""
