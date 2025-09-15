import pandas as pd
import streamlit as st
import numpy as np
import requests
import zipfile
import io
import csv

st.set_page_config(
    page_title="Análise da Renda de Cada Estado x Número de Matrículas no Ensino Fundamental ",
    layout="wide",
    initial_sidebar_state="collapsed"
)


link = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
link_demonstracao_financeira_zip = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip"
arquivo = "dfp_cia_aberta_DRE_con_2024.csv"

# Aqui começa a buscar o código da cvm que precisa pra buscar as demonstrações de resultados
r = requests.get(link)

r.text.split('\n')

empresas = []

for i in r.text.split('\n'):
    empresas.append(i.strip().split(';'))

listagem_empresas = pd.DataFrame(empresas[1:], columns=empresas[0])



searchFor = ["BANCO DO BRASIL S.A."]

bba3_dados = listagem_empresas[listagem_empresas.DENOM_SOCIAL.str.contains("|".join(searchFor), na=False)]

data_registro_bolsa = bba3_dados["DT_REG"]
codigo_bbas3_cvm = bba3_dados["CD_CVM"].iloc[0]


st.dataframe(bba3_dados)


#Aqui começa a buscar os demonstrativos financeiros
arquivo_zipado = requests.get(link_demonstracao_financeira_zip)

zf = zipfile.ZipFile(io.BytesIO(arquivo_zipado.content))

with zf.open(arquivo) as dre_file:
    text_content = io.TextIOWrapper(dre_file, encoding='ISO-8859-1')
    csv_reader = csv.reader(text_content, delimiter=';')
    lines = list(csv_reader)

conta_lucro_liquido = "Lucro ou Prejuízo Líquido Consolidado do Período"

df_dre = pd.DataFrame(lines[1:], columns=lines[0])

df_dre = df_dre[df_dre.DS_CONTA == conta_lucro_liquido]

df_dre_bbas3 = df_dre[df_dre.CD_CVM == '00' + codigo_bbas3_cvm]

bbas3_lucro_2023 = round(pd.to_numeric(df_dre_bbas3['VL_CONTA'].iloc[0]), 2)
bbas3_lucro_2024 = round(pd.to_numeric(df_dre_bbas3['VL_CONTA'].iloc[1]), 2)


st.write(bbas3_lucro_2023, bbas3_lucro_2024)


