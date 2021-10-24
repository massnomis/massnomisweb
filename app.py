import streamlit as st
from multiapp import MultiApp
from apps import beth,flashy,thorchain,aave_migration,bluna,compare,eth_fees,eth_matic_vol,extra,GPdata,gpusers,home,loop1,loop2,polygon_fees,steth
# import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.markdown("""
# 
""")

# Add all your application here
app.add_app("home", home.app)

app.add_app("beth", beth.app)

app.add_app("bluna", bluna.app)

app.add_app("compare", compare.app)

app.add_app("eth_fees", eth_fees.app)

app.add_app("eth_matic_vol", eth_matic_vol.app)

app.add_app("extra", extra.app)

app.add_app("GPdata", GPdata.app)

app.add_app("gpusers", gpusers.app)

app.add_app("loop1", loop1.app)

app.add_app("loop2", loop2.app)

app.add_app("polygon_fees", polygon_fees.app)

app.add_app("steth", steth.app)

app.add_app("aave_migration", aave_migration.app)

app.add_app("flashy", flashy.app)

app.add_app("thorchain", thorchain.app)






# The main app
app.run()