import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import json
import requests
import warnings
warnings.filterwarnings('ignore')
#%%
st.title("Web Deployment")


#%%
model=pickle.load(open('model.pkl','rb'))
tecrube=st.number_input("Tecrube",1,10)
yazılı=st.number_input("Sınav",1,10)
mulakat=st.number_input("Mulakat",1,10)

if st.button("Tahmin"):
    tahmin=model.predict([[tecrube,yazılı,mulakat]])
    tahmin=round(tahmin[0],2)
    st.write(  "Tahmin: ",tahmin)