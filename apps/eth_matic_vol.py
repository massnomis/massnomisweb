import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("Eth - Matic Vol")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/5a7ac116-7647-44ce-a421-1316b0974b28")




    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')

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
    




    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_ETH",
        y = ["PRICE_ETH","MAX_ETH_PRICE","MIN_ETH_PRICE"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph)


    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_ETH",
        y = ["STDDEV_ETH_PRICE"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph)

    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_ETH",
        y = ["PCT_ETH"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph)

    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_MATIC",
        y = ["AVERAGE_MATIC_PRICE","MAX_MATIC","MIN_MATIC"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph)
    
    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_MATIC",
        y = ["STD_MATIC"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph) 
    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.line(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_MATIC",
        y = ["PCT_MATIC"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph) 

    vol_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5a7ac116-7647-44ce-a421-1316b0974b28/data/latest')
    eth_matic_graph = px.scatter(
        vol_flipside_df, #this is the dataframe you are trying to plot
        x = "BLOCK_HOUR_MATIC",
        y = ["PCT_MATIC","PCT_ETH"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(eth_matic_graph) 

    # ------------------------------------------------
# BLOCK_HOUR_ETH	
# PRICE_ETH	
# MAX_ETH_PRICE	
# MIN_ETH_PRICE	
# STDDEV_ETH_PRICE
# PCT_ETH	
# BLOCK_HOUR_MATIC
# AVERAGE_MATIC_PRICE	
# MAX_MATIC
# MIN_MATIC	
# STD_MATIC
# PCT_MATIC

