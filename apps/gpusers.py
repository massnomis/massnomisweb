
import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
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
    # st.selectbox('Select', [1,2,3])



    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = "SUM",
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)




    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = "AVG_Value_Z_Score_(Skew)",
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)

    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["AVG"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["Median"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)  
# ,"Median"
    query_id = "11a317b4-dd02-41de-97ae-bc038ef27272"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "first_interaction",
        y = ["tx_countz"],
        color= "SUM_RANK",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)   
# USERZ	SUM_RANK	user	
# first_interaction	tx_countz	
# SUM	AVG	Median	
# STD DEV	Z_P1	Z_N1	
# AVG_Value_Z_Score_(Skew)


    # ------------------------------------------------
