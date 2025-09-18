import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import requests



st.set_page_config(
    page_title="Análise Estatística - BBAS3 e ITUB4",
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
    elif 2023 <= ano <= 2025:
        return "Governo Lula"
    else:
        return "Outro"

bbas3 = yf.download("BBAS3.SA", start="2000-01-01", end="2025-01-01")
itub4 = yf.download("ITUB4.SA", start="2000-01-01", end="2025-01-01")
ibov = yf.download("^BVSP", start="2000-01-01", end="2025-01-01")
lucro_liquido_bbas3 = {
    '31/12/2024': '4.37B',
    '30/09/2024': '5.27B',
    '30/06/2024': '8.70B',
    '31/03/2024': '8.03B',
    '31/12/2023': '6.77B',
    '30/09/2023': '8.04B',
    '30/06/2023': '8.36B',
    '31/03/2023': '6.69B',
    '31/12/2022': '7.35B',
    '30/09/2022': '7.51B',
    '30/06/2022': '8.20B',
    '31/03/2022': '4.57B',
    '31/12/2021': '10.64B',
    '30/09/2021': '4.54B',
    '30/06/2021': '5.57B',
    '31/03/2021': '4.16B',
    '31/12/2020': '4.15B',
    '30/09/2020': '3.04B',
    '30/06/2020': '3.16B',
    '31/03/2020': '3.19B',
    '31/12/2019': '8.70B',
    '30/09/2019': '4.16B',
    '30/06/2019': '4.20B',         
    '31/03/2019': '3.92B',
    '31/12/2018': '6.12B',
    '30/09/2018': '3.09B',
    '30/06/2018': '3.11B',
    '31/03/2018': '2.73B',
    '31/12/2017': '2.93B',
    '30/09/2017': '2.81B',
    '30/06/2017': '2.62B',
    '31/03/2017': '2.39B',
    '31/12/2016': '-0.67B',
    '30/09/2016': '2.22B',
    '30/06/2016': '2.44B',
    '31/03/2016': '2.31B',
    '31/12/2015': '6.37B',
    '30/09/2015': '3.01B',
    '30/06/2015': '2.93B',
    '31/03/2015': '5.68B',
    '31/12/2014': '4.15B',
    '30/09/2014': '2.74B',
    '30/06/2014': '2.79B',
    '31/03/2014': '2.77B',
    '31/12/2013': '2.74B',
    '30/09/2013': '2.69B',
    '30/06/2013': '7.45B',
    '31/03/2013': '2.58B',
    '31/12/2012': '3.54B',
    '30/09/2012': '2.80B',
    '30/06/2012': '3.00B',
    '31/03/2012': '2.55B',
    '31/12/2011': '4.98B',
    '30/09/2011': '2.89B',  
    '30/06/2011': '3.33B',
    '31/03/2011': '2.93B',
    '31/12/2010': '3.59B',
    '30/09/2010': '2.62B',
    '30/06/2010': '2.73B',
    '31/03/2010': '2.35B',
    '31/12/2009': '4.16B',
    '30/09/2009': '1.98B',
    '30/06/2009': '2.35B',
    '31/03/2009': '1.67B',
    '31/12/2008': '2.94B',
    '30/09/2008': '1.87B',
    '30/06/2008': '1.64B',
    '31/03/2008': '2.35B',
    '31/12/2007': '1.22B',
    '30/09/2007': '1.36B',
    '30/06/2007': '2.48B',
    '31/12/2006': '1.25B',
    '30/09/2006': '0.90B',
    '30/06/2006': '1.55B',
    '31/03/2006': '2.34B',
    '31/12/2005': '0.73B',
    '30/09/2005': '1.44B',
    '30/06/2005': '1.01B',
    '31/03/2005': '0.96B',
    '31/12/2004': '0.77B',
    '30/09/2004': '0.83B',
    '30/06/2004': '0.80B',
    '31/03/2004': '0.61B',
}

lucro_liquido_itub4 = {
    '31/12/2024': '11.84B',
    '30/09/2024': '10.37B',
    '30/06/2024': '10.07B',
    '31/03/2024': '9.81B',
    '31/12/2023': '8.77B',
    '30/09/2023': '8.36B',
    '30/06/2023': '8.62B',
    '31/03/2023': '7.36B',
    '31/12/2022': '7.50B',
    '30/09/2022': '8.09B',
    '30/06/2022': '7.46B',
    '31/03/2022': '6.65B',
    '31/12/2021': '6.60B',
    '30/09/2021': '6.08B',
    '30/06/2021': '8.40B',
    '31/03/2021': '5.68B',
    '31/12/2020': '8.98B',
    '30/09/2020': '4.73B',
    '30/06/2020': '1.72B',
    '31/03/2020': '3.46B',
    '31/12/2019': '8.67B',
    '30/09/2019': '5.17B',
    '30/06/2019': '6.53B',         
    '31/03/2019': '6.75B',
    '31/12/2018': '6.65B',
    '30/09/2018': '6.13B',
    '30/06/2018': '5.76B',
    '31/03/2018': '6.39B',
    '31/12/2017': '5.49B',
    '30/09/2017': '6.05B',
    '30/06/2017': '6.37B',
    '31/03/2017': '6.00B',
    '31/12/2016': '5.99B',
    '30/09/2016': '5.56B',
    '30/06/2016': '6.00B',
    '31/03/2016': '5.71B',
    '31/12/2015': '5.02B',
    '30/09/2015': '9.20B',
    '30/06/2015': '5.85B',
    '31/03/2015': '5.67B',
    '31/12/2014': '6.35B',
    '30/09/2014': '5.89B',
    '30/06/2014': '4.77B',
    '31/03/2014': '4.55B',
    '31/12/2013': '4.91B',
    '30/09/2013': '4.29B',
    '30/06/2013': '3.75B',
    '31/03/2013': '3.48B',
    '31/12/2012': '9.21B',
    '30/09/2012': '2.78B',
    '30/06/2012': '2.71B',
    '31/03/2012': '3.43B',
    '31/12/2011': '2.90B',
    '30/09/2011': '3.81B',  
    '30/06/2011': '3.60B',
    '31/03/2011': '3.53B',
    '31/12/2010': '2.27B',
    '30/09/2010': '3.03B',
    '30/06/2010': '3.16B',
    '31/03/2010': '3.23B',
    '31/12/2009': '3.21B',
    '30/09/2009': '2.27B',
    '30/06/2009': '2.57B',
    '31/03/2009': '2.01B',
    '31/12/2008': '1.87B',
    '30/09/2008': '1.85B',
    '30/06/2008': '2.04B',
    '31/03/2008': '2.04B',
    '31/12/2007': '2.03B',
    '30/09/2007': '2.43B',
    '30/06/2007': '2.11B',
    '31/12/2006': '1.90B',
    '30/09/2006': '0.07B',
    '30/06/2006': '1.50B',
    '31/03/2006': '1.46B',
    '31/12/2005': '1.42B',
    '30/09/2005': '1.35B',
    '30/06/2005': '1.33B',
    '31/03/2005': '1.14B',
    '31/12/2004': '1.03B',
    '30/09/2004': '0.92B',
    '30/06/2004': '0.94B',
    '31/03/2004': '0.87B',
}


precos_fechamento = bbas3['Close'].resample('YE').last()
precos_fechamento_itub4 = itub4['Close'].resample('YE').last()
precos_fechamentoIbov = ibov['Close'].resample('YE').last()

df_cotacoes = pd.DataFrame(precos_fechamento)
df_cotacoes_itub = pd.DataFrame(precos_fechamento_itub4)
df_cotacoes = df_cotacoes.iloc[4:]
df_cotacoes_itub = df_cotacoes_itub.iloc[4:]
df_cotacoes_itub.index = df_cotacoes_itub.index.year


df_cotacoes_ibov = pd.DataFrame(precos_fechamentoIbov)
df_cotacoes_ibov = df_cotacoes_ibov.iloc[4:]
df_cotacoes.index = df_cotacoes.index.year
df_cotacoes_ibov.index = df_cotacoes_ibov.index.year
df_cotacoes["BBAS3.SA"] = round(df_cotacoes["BBAS3.SA"], 2)

# CORREÇÃO: Processamento do lucro
df_lucro_bbas3 = pd.DataFrame.from_dict(lucro_liquido_bbas3, orient='index', columns=['valor'])
df_lucro_bbas3.index = pd.to_datetime(df_lucro_bbas3.index, format='%d/%m/%Y')
df_lucro_itub4 = pd.DataFrame.from_dict(lucro_liquido_itub4, orient='index', columns=['valor'])
df_lucro_itub4.index = pd.to_datetime(df_lucro_itub4.index, format='%d/%m/%Y')

# Extrair o ano para uma coluna temporária
df_lucro_bbas3['ano'] = df_lucro_bbas3.index.year
df_lucro_itub4['ano'] = df_lucro_itub4.index.year

# Converter valores para numéricos
df_lucro_bbas3['valor_numerico'] = df_lucro_bbas3["valor"].str.replace('B', '').astype(float)
df_lucro_itub4['valor_numerico'] = df_lucro_itub4["valor"].str.replace('B', '').astype(float)

df_cotacoes['Período_Governo'] = df_cotacoes.index.map(classificar_governo)

# Agrupar por ano e somar
lucro_anual_bbas3 = df_lucro_bbas3.groupby('ano')['valor_numerico'].sum()
df_cotacoes['Lucro_Liquido BBAS3'] = lucro_anual_bbas3
lucro_anual_itub4 = df_lucro_itub4.groupby('ano')['valor_numerico'].sum()
df_cotacoes['Lucro_Liquido ITUB4'] = lucro_anual_itub4
df_cotacoes["IBOVESPA"] = df_cotacoes_ibov['^BVSP']
df_cotacoes["ITUB4"] = round(df_cotacoes_itub['ITUB4.SA'], 2)

df_cotacoes.insert(0, 'Período_Governo', df_cotacoes.pop('Período_Governo'))
df_cotacoes.insert(1, 'ITUB4.SA', df_cotacoes.pop('ITUB4'))

# DataFrame para BBAS3
df_bbas3 = pd.DataFrame({
    'Ano': df_cotacoes.index,
    'Ativo': 'BBAS3.SA',
    'Preço': df_cotacoes['BBAS3.SA'],
    'Lucro': df_cotacoes['Lucro_Liquido BBAS3'],
    'IBOVESPA': df_cotacoes['IBOVESPA'],
    'Período_Governo': df_cotacoes['Período_Governo']
})

# DataFrame para ITUB4
df_itub4 = pd.DataFrame({
    'Ano': df_cotacoes.index,
    'Ativo': 'ITUB4.SA',
    'Preço': df_cotacoes['ITUB4.SA'],
    'Lucro': df_cotacoes['Lucro_Liquido ITUB4'],
    'IBOVESPA': df_cotacoes['IBOVESPA'],
    'Período_Governo': df_cotacoes['Período_Governo']
})

# Junta os dois
df_long = pd.concat([df_bbas3, df_itub4], ignore_index=True)

st.write(df_long)

# df_cotacoes["LUCRO_LIQUIDO"] = lucro_liquido_bbas3.values()
 

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
