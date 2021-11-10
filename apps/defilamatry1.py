import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
    st.title("YEET")

    df = pd.read_json(f"https://api.llama.fi/charts",
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


    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "date",
        y = ["totalLiquidityUSD"],
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)
    st.subheader('TX count, user count')

# https://api.llama.fi/protocols
# https://api.llama.fi/tvl/:slug
# https://api.llama.fi/charts/:chain
# https://api.llama.fi/protocol/:slug

    df = pd.read_json(f"https://api.llama.fi/charts/Terra")
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = "SUM",
        # color = "user_count",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.dataframe(df)





#     query_id = "0a70ffca-17a3-4cd8-8b42-d0820c7dbc48"
#     df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
#     convert_dates=["TIMESTAMP_NTZ"],
#     )
#     df = px.scatter(
#         df, #this is the dataframe you are trying to plot
#         x = "DAYZ",
#         y = ["Median","AVG"],
#         # color = "user_count",
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)
#     st.subheader('Mean and median: Median under mean, both rising until october 7, then both get closer to each other, tho mean is more volatile')




#     query_id = "0a70ffca-17a3-4cd8-8b42-d0820c7dbc48"
#     df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
#     convert_dates=["TIMESTAMP_NTZ"],
#     )
#     df = px.scatter(
#         df, #this is the dataframe you are trying to plot
#         x = "DAYZ",
#         y = "AVG_Value_Z_Score_(Skew)",
#         # color = "user_count",
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)  
#     st.subheader('SKEW: The launch as expected was more expensive and volatile than expected, but by october 8, some hours were boring and underperforming, but it really varied by time')


#     query_id = "0a70ffca-17a3-4cd8-8b42-d0820c7dbc48"
#     df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
#     convert_dates=["TIMESTAMP_NTZ"],
#     )
#     df = px.scatter(
#         df, #this is the dataframe you are trying to plot
#         x = "DAYZ",
#         y = "RUNNING_SKEW",
#         # color = "SUM_rank",
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)  
#     st.subheader('RUNNING SKEW: 70 total standard deviations off from 24*14 hours .Not too bad. Late october 10 was bad')



#     query_id = "0a70ffca-17a3-4cd8-8b42-d0820c7dbc48"
#     df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
#     convert_dates=["TIMESTAMP_NTZ"],
#     )
#     df = px.scatter(
#         df, #this is the dataframe you are trying to plot
#         x = "DAYZ",
#         y = "RUNNING_SUM",
#         # color = "user_count",
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)     
#     st.subheader('RUNNIng SUM: Hit 400k really quickly, then calmed down')
 
#     #   
#     query_id = "0a70ffca-17a3-4cd8-8b42-d0820c7dbc48"
#     df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
#     convert_dates=["TIMESTAMP_NTZ"],
#     )
#     df = px.scatter(
#         df, #this is the dataframe you are trying to plot
#         x = "DAYZ",
#         y = "RUNNING_COUNTZ",
#         # color = "user_count",
#         orientation = "v",
#         template = "plotly_white",
#         width = 1000,
#         height = 600,
#         log_y = t_f
#     )
#     st.plotly_chart(df)  
#     st.subheader('Tx count sum:Jump on october 7th wasnt that much of a result of new users, just higher prices')

# # DAYZ	tx_countz	user_count	SUM	AVG	Median	STD DEV	Z_P1	Z_N1	AVG_Value_Z_Score_(Skew)	RUNNING_SKEW	RUNNING_SUM	RUNNING_COUNTZ
#     # ------------------------------------------------

