import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   



    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0a70ffca-17a3-4cd8-8b42-d0820c7dbc48/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    
    st.markdown("""
    ### Eth - Matic Vol - Base Table
    """)

    st.dataframe(vol_flipside_df)

    st.markdown("""
    """)
    

    st.sidebar.header("Choose Columns:")
    columns = st.sidebar.multiselect(
        "Select the columns to plot",
        options = vol_flipside_df.columns,
        default = vol_flipside_df.columns.max()
    )


    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = columns,
        #color = columns,
        title = "<b>DIY / Choose your own adventure - Eth/Matic</b>",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(eth_matic_graph)

    