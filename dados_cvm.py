import pandas as pd
import streamlit as st
import numpy as np
import requests

st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)


link = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"

r = requests.get(link)

r.text.split('\n')

empresas = []

for i in r.text.split('\n'):
    empresas.append(i.strip().split(';'))

listagem_empresas = pd.DataFrame(empresas[1:], columns=empresas[0])

st.dataframe(listagem_empresas)

