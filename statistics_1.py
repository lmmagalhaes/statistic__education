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

def classificar_governo(ano):
    if 2003 <= ano <= 2010:
        return "Governo Lula"
    elif 2011 <= ano <= 2016:
        return "Governo Dilma"
    elif 2017 <= ano <= 2018:
        return "Governo Temer"
    elif 2019 <= ano <= 2022:
        return "Governo Bolsonaro"
    else:
        return "Outro"

bbas3 = yf.download("BBAS3.SA", start="2000-01-01", end="2025-01-01")
ibov = yf.download("^BVSP", start="2000-01-01", end="2025-01-01")
lucro_liquido_bbas3 = {
    '31/12/2024': '26.36B',
    '30/09/2024': '28.76B',
    '30/06/2024': '31.53B',
    '31/03/2024': '31.20B',
    '31/12/2023': '29.86B',
    '30/09/2023': '30.31B',
    '30/06/2023': '29.83B',
    '31/03/2023': '29.73B',
    '31/12/2022': '27.63B',
    '30/09/2022': '27.32B',
    '30/06/2022': '23.37B',
    '31/03/2022': '19.23B',
    '31/12/2021': '18.34B',
    '30/09/2021': '17.39B',
    '30/06/2021': '15.89B',
    '31/03/2021': '13.48B',
    '31/12/2020': '11.85B',
    '30/09/2020': '15.00B',
    '30/06/2020': '16.13B',
    '31/03/2020': '17.17B',
    '31/12/2019': '16.40B',
    '30/09/2019': '16.00B',
    '30/06/2019': '14.93B',         
    '31/03/2019': '13.84B',
    '31/12/2018': '13.83B',
    '30/09/2018': '11.98B',
    '30/06/2018': '11.70B',
    '31/03/2018': '11.21B',
    '31/12/2017': '10.63B',
    '30/09/2017': '8.79B',
    '30/06/2017': '8.20B',
    '31/03/2017': '8.01B',
    '31/12/2016': '7.03B',
    '30/09/2016': '9.46B',
    '30/06/2016': '10.25B',
    '31/03/2016': '10.74B',
    '31/12/2015': '14.07B',
    '30/09/2015': '14.65B',
    '30/06/2015': '14.35B',
    '31/03/2015': '14.21B',
    '31/12/2014': '11.85B',
    '30/09/2014': '11.40B',
    '30/06/2014': '11.34B',
    '31/03/2014': '16.00B',
    '31/12/2013': '10.44B',
    '30/09/2013': '16.67B',
    '30/06/2013': '16.79B',
    '31/03/2013': '12.34B',
    '31/12/2012': '11.25B',
    '30/09/2012': '11.45B',
    '30/06/2012': '11.54B',
    '31/03/2012': '11.87B',
    '31/12/2011': '12.68B',
    '30/09/2011': '13.16B',  
    '30/06/2011': '12.89B',
    '31/03/2011': '12.28B',
    '31/12/2010': '11.30B',
    '30/09/2010': '11.86B',
    '30/06/2010': '11.21B',
    '31/03/2010': '10.83B',
    '31/12/2009': '10.15B',
    '30/09/2009': '8.94B',
    '30/06/2009': '8.82B',
    '31/03/2009': '8.12B',
    '31/12/2008': '8.80B',
    '30/09/2008': '7.08B',
    '30/06/2008': '6.57B',
    '31/03/2008': '6.00B',
    '31/12/2007': '5.06B',
    '30/09/2007': '5.09B',
    '30/06/2007': '4.63B',
    '31/12/2006': '6.04B',
    '30/09/2006': '5.53B',
    '30/06/2006': '6.06B',
    '31/03/2006': '5.53B',
    '31/12/2005': '4.15B',
    '30/09/2005': '4.19B',
    '30/06/2005': '3.58B',
    '31/03/2005': '3.37B',
    '31/12/2004': '3.02B',
    '30/09/2004': '2.89B',
    '30/06/2004': '2.72B',
    '31/03/2004': '2.52B',
}


precos_fechamento = bbas3['Close'].resample('YE').last()
precos_fechamentoIbov = ibov['Close'].resample('YE').last()

df_cotacoes = pd.DataFrame(precos_fechamento)
df_cotacoes = df_cotacoes.iloc[4:]


df_cotacoes_ibov = pd.DataFrame(precos_fechamentoIbov)
df_cotacoes_ibov = df_cotacoes_ibov.iloc[4:]
df_cotacoes.index = df_cotacoes.index.year
df_cotacoes_ibov.index = df_cotacoes_ibov.index.year
df_cotacoes["BBAS3.SA"] = round(df_cotacoes["BBAS3.SA"], 2)

# CORREÇÃO: Processamento do lucro
df_lucro_bbas3 = pd.DataFrame.from_dict(lucro_liquido_bbas3, orient='index', columns=['valor'])
df_lucro_bbas3.index = pd.to_datetime(df_lucro_bbas3.index, format='%d/%m/%Y')

# Extrair o ano para uma coluna temporária
df_lucro_bbas3['ano'] = df_lucro_bbas3.index.year

# Converter valores para numéricos
df_lucro_bbas3['valor_numerico'] = df_lucro_bbas3["valor"].str.replace('B', '').astype(float)
df_cotacoes['Período_Governo'] = df_cotacoes.index.map(classificar_governo)

# Agrupar por ano e somar
lucro_anual = df_lucro_bbas3.groupby('ano')['valor_numerico'].sum()
df_cotacoes['Lucro_Liquido BBAS3'] = lucro_anual
df_cotacoes["IBOVESPA"] = df_cotacoes_ibov['^BVSP']

df_cotacoes.insert(0, 'Período_Governo', df_cotacoes.pop('Período_Governo'))





# df_cotacoes["LUCRO_LIQUIDO"] = lucro_liquido_bbas3.values()
 
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
