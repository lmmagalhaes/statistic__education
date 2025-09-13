import pandas as pd
import streamlit as st
import numpy as np
import requests
import zipfile
import io

st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)


link = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
link_demonstracao_financeira_zip = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip"
arquivo = "dfp_cia_aberta_DRE_con_2025.csv"

r = requests.get(link)
arquivo_zipado = requests.get(link_demonstracao_financeira_zip)

zf = zipfile.ZipFile(io.BytesIO(arquivo_zipado.content))
dre = zf.open(arquivo)

dre_lines = dre.readlines()

lines = [i.strip().decode("ISO-8859-1") for i in dre_lines]
lines = [i.split(b";") for i in dre_lines]

df_dre = pd.DataFrame(lines[1:], columns=lines[0])

r.text.split('\n')

empresas = []

for i in r.text.split('\n'):
    empresas.append(i.strip().split(';'))

listagem_empresas = pd.DataFrame(empresas[1:], columns=empresas[0])



searchFor = ["BANCO DO BRASIL S.A."]

bba3_dados = listagem_empresas[listagem_empresas.DENOM_SOCIAL.str.contains("|".join(searchFor), na=False)]

data_registro_bolsa = bba3_dados["DT_REG"]
codigo_bbas3_vcm = bba3_dados["CD_CVM"]


st.dataframe(bba3_dados)