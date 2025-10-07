import pandas as pd
import streamlit as st
import yfinance as yf
import numpy as np

import plotly.graph_objects as go

st.set_page_config(
    page_title="Análise Estatística - BBAS3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

bbas3 = yf.download("BBAS3.SA", start="2000-01-01", end="2025-01-01")
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
    '31/03/2007': '0.00B',
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


# def classificar_governo(ano):
#     if 2003 <= ano <= 2010:
#         return "Governo Lula"
#     elif 2011 <= ano <= 2016:
#         return "Governo Dilma"
#     elif 2017 <= ano <= 2018:
#         return "Governo Temer"
#     elif 2019 <= ano <= 2022:
#         return "Governo Bolsonaro"
#     elif 2023 <= ano <= 2025:
#         return "Governo Lula"
#     else:
#         return "Outro"


precos_fechamento = bbas3['Close'].resample('QE').last()
precos_fechamentoIbov = ibov['Close'].resample('QE').last()

df_cotacoes = pd.DataFrame(precos_fechamento)
df_cotacoes_ibov = pd.DataFrame(precos_fechamentoIbov)

df_cotacoes = df_cotacoes.iloc[16:]
df_cotacoes_ibov = df_cotacoes_ibov.iloc[16:]

df_cotacoes.index = pd.to_datetime(df_cotacoes.index)
df_cotacoes_ibov.index = pd.to_datetime(df_cotacoes_ibov.index)

df_cotacoes["BBAS3.SA"] = round(df_cotacoes.iloc[:, 0], 2)

df_lucro_bbas3 = pd.DataFrame.from_dict(lucro_liquido_bbas3, orient='index', columns=['valor'])
df_lucro_bbas3.index = pd.to_datetime(df_lucro_bbas3.index, format='%d/%m/%Y', dayfirst=True)

df_cotacoes['Período Governo'] = df_cotacoes.index.year.map(lambda ano: (
    "Governo Lula" if 2003 <= ano <= 2010 else
    "Governo Dilma" if 2011 <= ano <= 2016 else
    "Governo Temer" if 2017 <= ano <= 2018 else
    "Governo Bolsonaro" if 2019 <= ano <= 2022 else
    "Governo Lula" if 2023 <= ano <= 2025 else
    "Outro"
))

df_cotacoes.insert(0, 'Período Governo', df_cotacoes.pop('Período Governo'))

df_lucro_bbas3['valor_numerico'] = df_lucro_bbas3["valor"].str.replace('B', '', regex=False).astype(float)
df_lucro_bbas3 = df_lucro_bbas3.sort_index()

df_lucro_bbas3_q = df_lucro_bbas3['valor_numerico'].copy()
df_lucro_bbas3_q.index = df_lucro_bbas3_q.index.to_period('Q').to_timestamp(how='end')


df_cotacoes['Lucro_Liquido BBAS3'] = df_lucro_bbas3['valor_numerico'].reindex(df_cotacoes.index).values
df_cotacoes["IBOVESPA"] = df_cotacoes_ibov['^BVSP'].reindex(df_cotacoes.index).values


df_bbas3 = pd.DataFrame({
    'Trimestre': df_cotacoes.index,
    'Ativo': 'BBAS3.SA',
    'Preço': df_cotacoes['BBAS3.SA'].values,
    'Lucro': df_cotacoes['Lucro_Liquido BBAS3'].values,
    'IBOVESPA': df_cotacoes['IBOVESPA'].values,
    'Período Governo': df_cotacoes['Período Governo'].values
})

df_bbas3['Trimestre'] = pd.to_datetime(df_bbas3['Trimestre']).dt.to_period('Q')
df_bbas3['Trimestre'] = df_bbas3['Trimestre'].apply(
    lambda p: f"Q{p.quarter} {p.start_time.strftime('%m-%Y')}"
)

st.write("### Análise Estatística - BBAS3")
st.write(df_bbas3)

media_preco = df_cotacoes['BBAS3.SA'].mean()
mediana_preco = df_cotacoes['BBAS3.SA'].median()
moda_preco = df_cotacoes['BBAS3.SA'].mode()[0]
std_preco = df_cotacoes['BBAS3.SA'].std()
var_preco = df_cotacoes['BBAS3.SA'].var()   
min_preco = df_cotacoes['BBAS3.SA'].min()
max_preco = df_cotacoes['BBAS3.SA'].max()
range_preco = max_preco - min_preco


st.subheader("Estatísticas Descritivas do Preço da Ação BBAS3")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Média de Preço", value=f"Média: {media_preco:.2f}")
with col2:  
    st.metric(label="Mediana de Preço", value=f"Mediana: {mediana_preco:.2f}")
with col3:
    st.metric(label="Desvio Padrão do Preço", value=f"Desvio Padrão: {std_preco:.2f}")

col4, col5, col6 = st.columns(3)
with col4:
    st.metric(label="Moda do Preço", value=f"Moda: {moda_preco:.2f}")
with col5:
    st.metric(label="Variância do Preço", value=f"Variância: {var_preco:.2f}")
with col6:
    st.metric(label="Amplitude do Preço", value=f"Amplitude: {range_preco:.2f}")


fig = go.Figure(data=[go.Bar(
    x=df_cotacoes.index,
   y = np.round(df_cotacoes['BBAS3.SA'].values, 2)
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
