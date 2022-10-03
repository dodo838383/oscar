import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import pickle

with st.form ('Frame'):
    collection = st.number_input('Digite a coleção de sua escolha:')
    budget = st.number_input('Digite o valor do orçamento do filme:') 
    Time_taken =  st.number_input('Digite a duração do filme:')
    