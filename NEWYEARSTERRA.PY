import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

st.title("TERRA NEW YEARS")

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/1b560f22-5db3-483a-9e96-c7951f1ea1b4/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
BOR
""")


t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True

df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["AVG_BOR","MED_BOR","DIST_SENDER","BOR_TX_ID_CNT"],
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/1b560f22-5db3-483a-9e96-c7951f1ea1b4/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)



st.markdown("""
BOR SUM
""")


df = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "BOR_SUM",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/f57ab3c9-70da-478f-af91-65abe40fe34d/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)

st.markdown("""
DEP
""")

df = px.line(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = ["AVG_DEP","MED_DEP","DIST_SENDER","DEP_TX_ID_CNT"],
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/f57ab3c9-70da-478f-af91-65abe40fe34d/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
DEP SUM
""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "DEP_SUM",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/b6aa0f5b-5138-4a87-8a30-efb01cd2b21d/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
LIQUIDATIONS usd""")

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "SUM(LIQUIDATED_AMOUNT_USD)",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/b6aa0f5b-5138-4a87-8a30-efb01cd2b21d/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
LIQUIDATIONS """)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAYZ",
    y = "SUM(LIQUIDATED_AMOUNT)",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)
# b6aa0f5b-5138-4a87-8a30-efb01cd2b21d
# DAYZ	SUM(LIQUIDATED_AMOUNT)	SUM(LIQUIDATED_AMOUNT_USD)	ROUGH_PRICE	SUM(REPAY_AMOUNT)	SUM(REPAY_AMOUNT_USD)  count(distinct(tx_id))

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/ab33e3c0-cf26-4fa3-a66a-4b5c5652f05d/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
LIQUIDATIONS""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "BLOCK_HOUR",
    y = "PCTLUNA",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

# ab33e3c0-cf26-4fa3-a66a-4b5c5652f05d
# BLOCK_HOUR	PRICEYLUNA	MAXLUNA	MINLUNA	STLUNA	PCTLUNA

df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/691fbee0-848d-4e15-972d-9c87335a0fb5/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
ANC-UST""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/fbc1b4c3-91e7-4b3e-9628-0825e163c104/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
anchor lp staking""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/4184bbb7-adf2-4ad0-a6df-139c6130fb2a/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
ANC GOV""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)




df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/4d8a8da0-5b17-4f59-9d04-ac4d43b0ec61/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
anc AUST""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/f3ee63e3-3e38-41f9-aa49-c61287c63336/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
ANC BETH""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/652df6cc-7249-4c9d-98ce-d3b7d0961790/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
BLUNA""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)


df = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/438c151d-2612-45dc-b1a0-7230f2cd07e4/data/latest",
convert_dates=["TIMESTAMP_NTZ"],
)


st.markdown("""
ANC ANC""")
# st.dataframe(df)

df = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "FIRST_TRANSACTION_DATE",
    y = "NEW_USERS",
    # color = "COL_NAME",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(df)

