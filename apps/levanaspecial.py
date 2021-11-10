import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("Levana NFT SPECIAL")
    st.title("LOTTA STATZ, ENJOY")




    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6a7f6ed6-6cef-4444-8cc9-295ffb1f7fc3/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
 

    




    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "LATEST_UPDATED_TIME",
        y = "TOTAL_UST_DEPOSITED",
        #color = columns,
        title="title",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/bdb477df-fe29-4c6c-ba6f-93d6240d13f6/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "HOUR",
        y = "UST_DEPOSITED",
        #color = columns,
        title="LVN UST DEP HR",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/75b36db6-6dce-4cf2-903e-09b9f4883ad0/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TYPE",
        y = "COUNT",
        #color = columns,
        title="LVN TX v ADDY",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c53e40e5-76ad-4fd0-b74e-615c7dff8f2f/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "BLOCK",
        y = "COUNT(TX_ID)",
        #color = columns,
        title="BUCKETS",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a2fe2f2f-57e6-4493-a2cb-9652cc1a08cd/data/latest')
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "EACH_HOUR",
        y = ["CEILING_PRICE","FLOOR_PRICE"],
        #color = columns,
        title="FLOOR CEILING",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3f76bfd3-3801-49f3-bce4-7ef9553f0bbc/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "TYPE",
        y = "NUMBER",
        #color = columns,
        title=" OWNERS DAATA",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

# LVN UST DEP
# https://api.flipsidecrypto.com/api/v2/queries/6a7f6ed6-6cef-4444-8cc9-295ffb1f7fc3/data/latest
# LATEST_UPDATED_TIME	TOTAL_UST_DEPOSITED
# 
# LVN UST DEP HR
# https://api.flipsidecrypto.com/api/v2/queries/bdb477df-fe29-4c6c-ba6f-93d6240d13f6/data/latest
# HOUR	UST_DEPOSITED
# 
# LVN TX v ADDY
# https://api.flipsidecrypto.com/api/v2/queries/75b36db6-6dce-4cf2-903e-09b9f4883ad0/data/latest
# TYPE	COUNT
# 
# 
# BUCKETS
# BLOCK	COUNT(TX_ID)
# https://api.flipsidecrypto.com/api/v2/queries/c53e40e5-76ad-4fd0-b74e-615c7dff8f2f/data/latest
# 
# 
# FLOOR CEILING
# EACH_HOUR	CEILING_PRICE	FLOOR_PRICE
# https://api.flipsidecrypto.com/api/v2/queries/a2fe2f2f-57e6-4493-a2cb-9652cc1a08cd/data/latest
# 
# 
# OWNERS DAATA
# TYPE	NUMBER
# https://api.flipsidecrypto.com/api/v2/queries/3f76bfd3-3801-49f3-bce4-7ef9553f0bbc/data/latest
#
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9b894986-5420-40a9-b502-04fe51274995/data/latest')
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "NUMBER_OF_SHOWERS_WON",
        y = "TOTAL_UST",
        color = "LEGENDARY_OWNERS",
        title=" WHOM DAATA",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
# whom
# https://api.flipsidecrypto.com/api/v2/queries/9b894986-5420-40a9-b502-04fe51274995/data/latest
# LEGENDARY_OWNERS  NUMBER_OF_SHOWERS_WON RATIO TOTAL_UST
# 
