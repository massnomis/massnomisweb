import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("ENS mid december")

query_id = "a8ece130-7ad1-4cf4-a260-14d83fb03c49"
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
ENS CLAIMS
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "AMT",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "36c75b7e-b89e-4c73-ac9a-a9a214e093c5"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
ENS PRICE""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "HOUR",
    y = "PRICE",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




query_id = "54293e31-e10c-4677-bfbf-5b8af31aa52e"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
NEW REGISTRATIONS
""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "COUNT(DISTINCT(TX_ID))",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "40388abb-c656-4fab-b7bd-8a32d3aeea18"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
GAS FEE vs REGISTRATION FEE""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["SUM(AMOUNT_USD)","SUM(FEE_USD)"],
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



# query_id = "2ca64776-431b-42ff-b0e6-7f324b4aed35"
# df = pd.read_json(
#     f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
# convert_dates=["TIMESTAMP_NTZ"],
# )

# df = px.bar(
#     df, #this is the dataframe you are trying to plot
#     x = "HOURZ",
#     y = "WETH",
#     orientation = "v",
#     # color = "TO_ADDRESS_NAME",
#     template = "plotly_white",
#     width = 1000,
#     height = 600,
#     log_y = t_f
# )
# st.plotly_chart(df)
