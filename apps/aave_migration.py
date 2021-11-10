import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json



def app():

    st.title("AAVE VERSION MIGRATION")
    st.markdown(
        """
        @massnomis
        """
    )


    st.markdown(
        """
    AAVE, the money marklet protocl has seen, so far, three seperate versions. These are v1, v2, and AAVE AMM.
    Today We will look at selected dates with selected coins (stables), when v2 launched incentives (in stkAAVE) in April 2021, stuff began to change, and funds were moved around
    The Two metrics are as follows:
    Total Supply, The amount of deposits in the protocol
    TVL, The amount supplied MINUS the borrowed amount. This is roughly the avalible (borrowable) liquidity.
        """
    )

    st.header("DAI MIGRATION")
    # load tax query into pandas
    query_id = "d507c67b-9962-4308-a634-1b66df53ad4f"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
        convert_dates=["TIMESTAMP_NTZ"],
    )
    st.write(df)
    st.write("DAI, a stablecoin minted in MAKERDAO by locking up collateral has always been hard to come by (needs to be overcollateralized)")
    st.write("This Being Said, it has an LTV of 75%")

    dai1 = px.bar(
        df,
        x="DATE",
        y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"],
        color_discrete_map={
            'AMM_TVL_SHARE': 'red',
            'VONE_TVL_SHARE': 'green',
            'VTWO_TVL_SHARE': 'blue'
        }
    )

    st.markdown(
        """
    Starting with The TVL share, we see the volatility that the version migration has on new rewards in markets
        """
    )
    st.plotly_chart(dai1, use_container_width=True)

    st.markdown(
        """
    Next, we Have Supply. This is more straightworward and has a better flow.
        """
    )
    dai2 = px.bar(
        df,
        x="DATE",
        y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"],
        color_discrete_map={
            'AMM_SUPPLY_SHARE': 'red',
            'VONE_SUPPLY_SHARE': 'green',
            'VTWO_SUPPLY_SHARE': 'blue'
        }
    )

    st.plotly_chart(dai2, use_container_width=True)

    st.header("USDT")
    # load tax query into pandas
    query_id = "07ed5e15-9d63-458e-bf7f-c21b5c449e8a"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
        convert_dates=["TIMESTAMP_NTZ"],
    )
    st.write(df)
    st.markdown(
        """
    Next is Tether. This coin is mintable (for exchanges and whales), but holds zero collateral value. This makes it less apetizing for farming.
        """
    )

    USDT1 = px.bar(
        df,
        x="DATE",
        y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"],
        color_discrete_map={
            'AMM_TVL_SHARE': 'red',
            'VONE_TVL_SHARE': 'green',
            'VTWO_TVL_SHARE': 'blue'
        }
    )
    st.markdown(
        """
    Starting with The TVL share, we see the volatility that the version migration has on new rewards in markets
        """
    )
    st.plotly_chart(USDT1, use_container_width=True)
    st.markdown(
        """
    Since it cannot be used as collateral, market forces are much more visible. The volatility in TVL is wayyyy more than DAI and I consider it to be the most true.
        """
    )
    USDT2 = px.bar(
        df,
        x="DATE",
        y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"],
        color_discrete_map={
            'AMM_SUPPLY_SHARE': 'red',
            'VONE_SUPPLY_SHARE': 'green',
            'VTWO_SUPPLY_SHARE': 'blue'
        }
        
    )
    st.markdown(
        """
    If you look at the actual supply share, it tells the same story as DAI
        """
    )
    st.plotly_chart(USDT2, use_container_width=True)




    st.header("USDC MIGRATION")
    # load tax query into pandas
    query_id = "c9ec4820-97ac-4ca9-8014-d7e2d4e3e3c3"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
        convert_dates=["TIMESTAMP_NTZ"],
    )
    st.write(df)
    st.write("TVL")

    USDC1 = px.bar(
        df,
        x="DATE",
        y=["AMM_TVL_SHARE",	"VONE_TVL_SHARE","VTWO_TVL_SHARE"],
        color_discrete_map={
            'AMM_TVL_SHARE': 'red',
            'VONE_TVL_SHARE': 'green',
            'VTWO_TVL_SHARE': 'blue'
        }
    )
    st.markdown(
        """
    Lastly we have USDC. The easiest to mint for regular people, it has a collateral value of 82.5%
        """
    )
    st.plotly_chart(USDC1, use_container_width=True)

    USDC2 = px.bar(
        df,
        x="DATE",
        y=["AMM_SUPPLY_SHARE",	"VONE_SUPPLY_SHARE","VTWO_SUPPLY_SHARE"],
        color_discrete_map={
            'AMM_SUPPLY_SHARE': 'red',
            'VONE_SUPPLY_SHARE': 'green',
            'VTWO_SUPPLY_SHARE': 'blue'
        }
    )
    st.markdown(
        """
    Becasue it has collateral value, it is ideal for farming. You can fold your position.
        """
    )
    st.plotly_chart(USDC2, use_container_width=True)

    st.markdown(
        """
    The volatility here is the least. Makes sense, as the asset is the most abundant.
    We see that the move from v1 to v2 is the most well executed and quickest, as farmers and strategies work with efficiency.
        """
    )




    st.header("ALL TOGETHER")
    query_id = "9ce49ac8-d158-4443-b9b2-aa09d75d6755"
    df = pd.read_json(
        f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
        convert_dates=["TIMESTAMP_NTZ"],
    )
    st.write(df)

    st.markdown(
        """
    Finally lets look at these are raw values and not as relative percentages. We shall start with liquidity
        """
    )

    USDC2 = px.line(
        df,
        x="DATE",
        y=["STVL"],
        color = "RESERVE_NAMEI"
    )
    st.plotly_chart(USDC2, use_container_width=True)

    st.markdown(
        """
    Liquidity actually increases here, markets are not just siphoning from each other, the new rewards are bringing in more capital.
    In The chart below (Total supply), we see that across the board all assets grow, even though DAI does strugle to react to market demand.    
        """
    )

    USDC2 = px.bar(
        df,
        x="DATE",
        y=["SSUPPLY"],
        color = "RESERVE_NAMEI"
    )
    st.plotly_chart(USDC2, use_container_width=True)

    st.markdown(
        """
    THANK YOU SER
        """
    )