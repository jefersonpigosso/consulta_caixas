import streamlit as st
from streamlit import session_state as sts
import pandas as pd

st.set_page_config(page_title='Consulta Caixas', page_icon='📦')

######################################################

def lista_caixas():
    sts.df = pd.read_excel(r'files/lista.xlsx', dtype='string')

def consulta_caixa():

    if sts.caixa in set(sts.df['Caixa']):
        return True

######################################################

if 'df' not in sts:
    lista_caixas()
if 'caixa' not in sts:
    sts.caixa = ''

######################################################

if len(sts.caixa) == 8:

    if consulta_caixa():
        st.toast(body=f'Separar!', icon='✅')

    else:
        st.toast(body=f'Armazenar!', icon='⚠️')
    
    sts.caixa = ''

######################################################

st.text_input(label='Caixa', key='caixa', max_chars=8)
st.text(f'Total de caixas: {len(sts.df):,}'.replace(",", "."))
