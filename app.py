import streamlit as st
from streamlit import session_state as sts
import pandas as pd
import os

st.set_page_config(page_title='Consulta Caixas', page_icon='📦')

######################################################

def listas():

    listas = os.listdir(r'files')
    sts.listas = [lista[:-5] for lista in listas]

def lista_caixas():

    listas = os.listdir(r'files')
    df = pd.DataFrame()

    for lista in listas:

        df_temp = pd.read_excel(rf'files/{lista}', usecols=['Caixa', 'Destino'], dtype='string')
        df_temp['lista'] = lista[:-5]

        df = pd.concat([df, df_temp], ignore_index=True)

    sts.df = df

def consulta_caixa():

    if sts.caixa in set(sts.df_filtrado['Caixa']):
        return True

######################################################

if 'listas' not in sts: listas()
if 'lista' not in sts: sts.lista = sts.listas[0]
if 'df' not in sts: lista_caixas()
if 'caixa' not in sts: sts.caixa = ''
if 'destino' not in sts: sts.destino = ''

sts.df_filtrado = sts.df[sts.df['lista'] == sts.lista]

######################################################

if len(sts.caixa) == 8:

    if consulta_caixa():
        st.toast(body=sts.df_filtrado[sts.df_filtrado['Caixa'] == sts.caixa]['Destino'].iloc[0], icon='✅')

    else:
        st.toast(body=f'Armazenar!', icon='⚠️')

    sts.caixa = ''

######################################################

st.selectbox(label='Lista Coleta', options=sts.listas, key='lista')

st.text_input(label='Caixa', key='caixa', max_chars=8)
st.text(f'Total de caixas: {len(sts.df_filtrado):,}'.replace(",", "."))
