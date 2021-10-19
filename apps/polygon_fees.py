import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("Polygon Fees")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/5b112bae-b1e2-446c-b458-1eb31900d06e")



    poly_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5b112bae-b1e2-446c-b458-1eb31900d06e/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    
    st.markdown("""
    ### Polygon Fees and Transactions - Base Table
    """)

    st.dataframe(poly_fees_flipside_df)

    st.markdown("""
    """)
    




    polygon_fees_graph = px.line(
        poly_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "POLYGON_DAY",
        y = "transaction_count",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(polygon_fees_graph)

    poly_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5b112bae-b1e2-446c-b458-1eb31900d06e/data/latest')
    polygon_fees_graph = px.line(
        poly_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "POLYGON_DAY",
        y = ["pfees_usdavg","pfees_usdmed"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(polygon_fees_graph)    

    poly_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5b112bae-b1e2-446c-b458-1eb31900d06e/data/latest')
    polygon_fees_graph = px.line(
        poly_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "POLYGON_DAY",
        y = ["pfees_usd"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(polygon_fees_graph)  

    poly_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5b112bae-b1e2-446c-b458-1eb31900d06e/data/latest')
    polygon_fees_graph = px.line(
        poly_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "POLYGON_DAY",
        y = ["pZ1","pZn1"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(polygon_fees_graph) 
    # ------------------------------------------------
# polygon_day
# transaction_count
# pfees_usd
# pfees_usdavg
# pfees_usdmed
# pfees_usdstd
# pZ1
# pZn1
