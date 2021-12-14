import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("PSP ETH mid december")

query_id = "a8a3db40-176d-45a0-9cc1-342657888efe"
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
PSP daily interactions
""")





df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DATE",
    y = "N_ACTIVE_ADDRESSES",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "35b81a08-13c3-4d76-93f6-4c1223212cfb"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
Para weekly vol""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "TRANSACTIONS",
    orientation = "v",
    color = "PLATFORM",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

query_id = "35b81a08-13c3-4d76-93f6-4c1223212cfb"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
Para weekly vol-pool_name""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "USD_VOL",
    orientation = "v",
    color = "POOL_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


# query_id = "35b81a08-13c3-4d76-93f6-4c1223212cfb"
# df = pd.read_json(
#     f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
# convert_dates=["TIMESTAMP_NTZ"],
# )


# st.markdown("""
# Para weekly vol-platform""")


# df = px.bar(
#     df, #this is the dataframe you are trying to plot
#     x = "DAYZ",
#     y = "USD_VOL",
#     orientation = "v",
#     color = "POOL_NAME",
#     template = "plotly_white",
#     width = 1000,
#     height = 600,
#     log_y = t_f
# )
# st.plotly_chart(df)



query_id = "c6898f55-e472-4d32-92b4-164d2924e989"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
PSP CLAIMZ
""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "CLAIMZ",
    orientation = "v",
    # color = "TO_ADDRESS_NAME",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)



query_id = "87104b96-4852-4e27-9d32-52e300b9a7d5"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
txs by event, PSP""")


df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "TXS",
    orientation = "v",
    color = "EVENT_NAME",
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
