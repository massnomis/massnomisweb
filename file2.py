import streamlit as st
from extra import file3.py
app = MultiApp()
st.set_page_config(layout="wide")
st.markdown("""
# 
""")
app.add_app("file1.py",file1.py.app)