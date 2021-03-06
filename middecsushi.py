import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("SUSHI ETH mid december")

query_id = "6b94a94d-f8f3-4856-a3a7-fc655cb9ac6c"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True


#-------------------------------------------------------




st.markdown("""

What Pool is Hot right now? On ethereum lets look at LP actions, by count.

""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "COUNT(TO_ADDRESS_NAME)",
    orientation = "v",
    color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "712872e7-ca98-4504-8afd-5ddf5c3e41d0"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.dataframe(df)

st.markdown("""
and the same thing for polygon
""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "COUNT(TO_ADDRESS_NAME)",
    orientation = "v",
    color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




query_id = "2ca64776-431b-42ff-b0e6-7f324b4aed35"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



st.markdown("""
When sushi and ETH were both in freefall in december 8th, sushi breifly jumped against ETH. The price here is how many SUSHI in 1 ETH

""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "HOURZ",
    y = "P",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "2ca64776-431b-42ff-b0e6-7f324b4aed35"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
in the SUSHI-WETH pool, lets look at inflow and outflow for sushi
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "HOURZ",
    y = "SUSHI",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "2ca64776-431b-42ff-b0e6-7f324b4aed35"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
in the SUSHI-WETH pool, lets look at inflow and outflow for WETH
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "HOURZ",
    y = "WETH",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
