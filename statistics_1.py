import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)


df_edu = pd.read_csv( "microdados_ed_basica_2024.csv",
    encoding="latin1",  
    sep=";",             
    low_memory=False )

colum = df_edu.columns

comp_cols = [col for col in df_edu.columns if col.startswith("QT_COMP")]

description = ['Sigla', 'Município', 'Quantidade Notebook', 'Número de Matrículas do Ensino Fundamental']

df_filtered = df_edu[['SG_UF', 'NO_MUNICIPIO', 'QT_COMP_PORTATIL_ALUNO', 'QT_MAT_FUND']]

df_filtered = df_filtered.dropna()

amostra = 51

df_sample = (
    df_filtered.groupby("SG_UF", group_keys=False)
    .apply(lambda x: x.sample(max(1, int(amostra * len(x) / len(df_filtered))), random_state=42))
)


df_sample.columns = description
df_compare = df_sample.groupby("Sigla").sum()

st.write(df_sample)

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