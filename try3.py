
import time
import pandas as pd
import hmac
import requests
from requests import Request
import streamlit as st
# FTX_API_KEY=zPHU2acrp2uZxgVxFXhgYpUy7HAHx0LftElPPPWn
# FTX_API_SECRET=XFr2Mrj-ZZJKhvtdW5ONJYZSKoYH_9iwCVCvODdU
ts = int(time.time() * 1000)
request = Request('GET', '<https://ftx.com/api/markets>')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('ZZJKhvtdW5ONJYZSKoYH_9iwCVCvODdU'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = 'zPHU2acrp2uZxgVxFXhgYpUy7HAHx0LftElPPPWn'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)


endpoint_url = 'https://ftx.com/api/markets'

# Get all market data as JSON
all_markets = requests.get(endpoint_url).json()

# Convert JSON to Pandas DataFrame
df = pd.DataFrame(all_markets['result'])
df.set_index('name', inplace = True)
st.dataframe(df)
