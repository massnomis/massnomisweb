import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("OHM, a DEEPER look")
t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/1ecec2cc-b801-42fe-9eac-661ae5f1efff/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------


st.dataframe(df)

st.markdown("""
VOLATILITY of OHM and Comps
""")





df = px.line(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["WBTC_VOL","OHM_VOL","WETH_VOL","SHIB_VOL","RAI_VOL"],
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f

)
st.plotly_chart(df)



df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/691ccd29-7ee6-4b70-bf3d-9b2a0a7fd38b/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
OHM BOND DEPOSITS
""")





df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZZ",
    y = "DIST_ADDY_BOND",
    color = "BOND",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
    
)
st.plotly_chart(df)




df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7432ab18-cbee-4a73-8f78-bed5fe50ddc6/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
BOND REDEMPTIONS
""")





df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "DIST_ADDY_REDEEM",
    color = "BOND",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
    
)
st.plotly_chart(df)



df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/0946fb3a-1223-4af2-b027-d6f813e9c993/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



st.markdown("""
NET CHANGES
""")





df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "NET",
    color = "BOND",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
    
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/875806f0-fc1d-4ac5-9525-b961aaf6131b/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



#-------------------------------------------------------



# st.markdown("""
# TEST""")





# df = px.scatter(
#     df, #this is the dataframe you are trying to plot
#     x = "DAYZ",
#     y = "DIST_ADDY",
#     color = "BOND",
#     orientation = "v",
#     template = "plotly_white",
#     width = 1000,
#     height = 600,
#     log_y = t_f
    
# )
# st.plotly_chart(df)
# ,"TXN_VOLUME"]