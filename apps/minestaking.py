import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("MINE STAKING")
    st.title("LOTTA STATZ, ENJOY")




    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9be81293-066d-4435-a638-6152093109e1/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
 

    




    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = "RUNNING",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9be81293-066d-4435-a638-6152093109e1/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["AMOUNT_STAKED","AMOUNT_UNSTAKEDN"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)    

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9be81293-066d-4435-a638-6152093109e1/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["NET"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9be81293-066d-4435-a638-6152093109e1/data/latest')
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["AMOUNT_STAKED","RUNNING","AMOUNT_UNSTAKEDN","NET"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df) 



    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/31f56a18-518b-4b95-9c1a-641e10c034be/data/latest')
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = ["AMOUNT_STAKED","AMOUNT_UNSTAKEDN"],
        color = "FROMM",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df) 
    

# DAYZ	FROMM	AMOUNT_STAKED	AMOUNT_UNSTAKEDN

    # ------------------------------------------------
# DAYZ	AMOUNT_STAKED	AMOUNT_UNSTAKED	NET	RUNNING
