import plotly
import streamlit as st
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
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
    



    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = "AVG(STETH_WETH)",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)


    query_id = "7a5f2ddb-e8f0-4f90-aee7-220264b8f958"
    df2 = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)


    df2 = px.line(
        df2, #this is the dataframe you are trying to plot
        x = "DAYZZZ",
        y = "AVG(INV)",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(df2)



# DAYZZZ	AVG(STETH_WETH)	AVG(MADAYLWETH_STETH)	AVG(MA3DAYLWETH_STETH)	AVG(INV)	
# AVG(MADAYLSTETH_WETH)	AVG(MA3DAYLSTETH_WETH)	AVG(MAWEEKLSTETH_WETH)	AVG(WETH_STETH)	AVG(OUTAVGETH)
# 	AVG(OUTMEDETH)	AVG(OUTSTDDEVETH)	AVG(INSUMWETH)	AVG(INAVGWETH)	AVG(INMEDWETH)	AVG(INSTDDEVWETH)	AVG(OUTSUMSTETH)	AVG(OUTSUMWETH)	AVG(OUTAVGSTETH)	
# AVG(OUTMEDSTETH)	AVG(OUTSTDDEVSTETH)	AVG(INSUMSTETH)	AVG(INAVGSTETH)	AVG(INMEDSTETH)	AVG(INSTDDEVSTETH)    # 
# https://app.flipsidecrypto.com/velocity/queries/7a5f2ddb-e8f0-4f90-aee7-220264b8f958