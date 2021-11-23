import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json
def app():
    query_id ="5b7c6f3a-2ab1-45b7-be8e-165b620b36ea"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)    

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    df = px.bar(df, x = "DAY" , y = "DAY" , title = "DAY" , orientation = "v" , template = "plotly_white" ,  width = 1000, height = 600, log_y = t_f)
import streamlit as st

import plotly

import plotly.express as px

import statsmodels.api as sm

import pandas as pd

import json

def app():

    query_id ="5b7c6f3a-2ab1-45b7-be8e-165b620b36ea"

    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",

    convert_dates=["TIMESTAMP_NTZ"],

)    



    t_f = False

    st.sidebar.write("Choose y-axis scale")

    check = st.sidebar.checkbox("Linear/Log")

    if check: 

        t_f = True

    df = px.bar(df, x = "DAY" , y = "DAY" , title = "DAY" , orientation = "v" , template = "plotly_white" ,  width = 1000, height = 600, log_y = t_f)

import streamlit as st



import plotly



import plotly.express as px



import statsmodels.api as sm



import pandas as pd



import json



def app():



    query_id ="5b7c6f3a-2ab1-45b7-be8e-165b620b36ea"



    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",



    convert_dates=["TIMESTAMP_NTZ"],



)    







    t_f = False



    st.sidebar.write("Choose y-axis scale")



    check = st.sidebar.checkbox("Linear/Log")



    if check: 



        t_f = True



    df = px.bar(df, x = "DAY" , y = "DAY" , title = "DAY" , orientation = "v" , template = "plotly_white" ,  width = 1000, height = 600, log_y = t_f)