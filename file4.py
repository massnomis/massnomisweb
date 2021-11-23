a = 1
import streamlit as st

import plotly

import plotly.express as px

import statsmodels.api as sm

import pandas as pd

import json

    def app():

        

    t_f = False

    st.sidebar.write("Choose y-axis scale")

    check = st.sidebar.checkbox("Linear/Log")

    if check: 

        t_f = True

    

df = px.bar(df,x = "DATE" , y = ETHEREUM_UNIQUE_WALLETS , title = "" , orientation = "v" , template = "plotly_white" ,  width = 1000, height = 600, log_y = t_f)