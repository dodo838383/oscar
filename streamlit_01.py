import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pickle

pickle_in = open('oscar.pkl', 'rb')
oscar = pickle.load(pickle_in)
st.title("Previsão de prêmio")

with st.form ('Frame'):
    collection = st.number_input('Digite a coleção de sua escolha:')
    budget = st.number_input('Digite o valor do orçamento do filme:') 
    Time_taken =  st.number_input('Digite a duração do filme:')
    botao = st.form_submit_button('Enviar Informações')

def premio(collection, budget, Time_taken, modelo=oscar):
    var_1 = oscar.predict(collection, budget, Time_taken, oscar)
    return var_1

if botao:
    st.write(var_1)