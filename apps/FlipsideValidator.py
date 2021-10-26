import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("FLIPSIDE AS A VALIDATOR")

    query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    

    st.dataframe(df)

    st.markdown("""
    """)


    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = ["LUNA_IN_TODAY","LUNA_OUT"],
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    st.subheader('LUNA IN AND OUT EH?')



    query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = ["LUNA_IN_TODAY_USD","LUNA_OUT_USD"],
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df) 
    st.subheader('Same but USD')




    query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = ["RUNNING_LUNA","RUNNING_LUNA_OUT"],
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    st.subheader('RUNNING SUMS')

    # ------------------------------------------------



    query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = ["RUNNING_LUNA_OUT_USD","RUNNING_LUNA_USD"],
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
    st.subheader('Same but USD')

# DAYZZZ	LUNA_IN_TODAY	LUNA_IN_TODAY_USD	RUNNING_LUNA	RUNNING_LUNA_USD	LUNA_OUT	LUNA_OUT_USD
# 	DAILY_NET_LUNA	DAILY_NET_LUNA_USD	RUNNING_LUNA_OUT	RUNNING_LUNA_OUT_USD	COMISH_DAYZZ	COMISH_USD
    # query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    # df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    # convert_dates=["TIMESTAMP_NTZ"],
    # )
    # df = px.scatter(
    #     df, #this is the dataframe you are trying to plot
    #     x = "DAYZZZ",
    #     y = "",
    #     # color = "SUM_rank",
    #     orientation = "v",
    #     template = "plotly_white",
    #     width = 1000,
    #     height = 600,
    #     log_y = t_f
    # )
    # st.plotly_chart(df)  
    # st.subheader('')



    # query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    # df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    # convert_dates=["TIMESTAMP_NTZ"],
    # )
    # df = px.scatter(
    #     df, #this is the dataframe you are trying to plot
    #     x = "DAYZZZ",
    #     y = "",
    #     # color = "user_count",
    #     orientation = "v",
    #     template = "plotly_white",
    #     width = 1000,
    #     height = 600,
    #     log_y = t_f
    # )
    # st.plotly_chart(df)     
    # st.subheader('')
 
    # #   
    query_id = "15c9687f-19ef-471e-bb6d-33f2cc01afc4"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "COMISH_DAYZZ",
        y = "COMISH_USD",
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
    st.subheader('COMMISION')

# DAYZZZ	LUNA_IN_TODAY	LUNA_IN_TODAY_USD	RUNNING_LUNA	RUNNING_LUNA_USD	LUNA_OUT	LUNA_OUT_USD
# 	DAILY_NET_LUNA	DAILY_NET_LUNA_USD	RUNNING_LUNA_OUT	RUNNING_LUNA_OUT_USD	COMISH_DAYZZ	COMISH_USD
    # ------------------------------------------------

