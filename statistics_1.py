import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)


df_edu = pd.read_csv( "amostra.csv",
    encoding="utf-8",  
    sep=",",             
    low_memory=False )

df_edu = df_edu.drop(df_edu.columns[0], axis=1)

st.write(df_edu)

amostra = 51

df_sample = (
    df_edu.groupby(df_edu.index, group_keys=False)
    .apply(lambda x: x.sample(max(1, int(amostra * len(x) / len(df_edu))), random_state=42))
)

df_compare = df_sample.groupby("Sigla").sum()



fig = go.Figure(data=[go.Bar(
    x=df_compare.index,
    y=df_compare['Quantidade Notebook'],

)])

fig.update_layout(
    title="Quantidade de computadores portáteis por UF",
    xaxis_title="UF",
    yaxis_title="Quantidade de computadores",
    xaxis=dict(tickangle=-45),
    template="plotly_white",
    height=600,
    width=900
)

st.plotly_chart(fig, use_container_width=True)


""""
Primeira coisa que precisamos fazer é selecionar os dados de forma randômica do dataframe apresentado.
Essa amostra deve homogênea com relação as UFs

"""
