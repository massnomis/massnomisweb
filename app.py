import streamlit as st
from multiapp import MultiApp
from apps import midnovSUSHI,THORCHAINMIDNOV,testt,levanaspecial,MINELUNA,earlynovTHOR,minestaking,defilamatry1,aave29,beth,FlipsideValidator,flashy,aaavemidoctoberbatch,thorchain,aave_migration,bluna,compare,eth_fees,eth_matic_vol,extra,GPdata,gpusers,home,loop1,loop2,polygon_fees,steth
# import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.markdown("""
# 
""")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://app.ens.domains/name/massnomis.eth/details" target="_blank">massnomis</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/massnomis/massnomisweb" target="_blank">GitHub</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/sammycrypto4" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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

app.add_app("aaavemidoctoberbatch", aaavemidoctoberbatch.app)

app.add_app("FlipsideValidator", FlipsideValidator.app)

app.add_app("aave29", aave29.app)

app.add_app("defilamatry1", defilamatry1.app)

app.add_app("minestaking", minestaking.app)

app.add_app("MINELUNA", MINELUNA.app)

app.add_app("earlynovTHOR", earlynovTHOR.app)

app.add_app("levanaspecial", levanaspecial.app)

app.add_app("testt", testt.app)

app.add_app("THORCHAINMIDNOV", THORCHAINMIDNOV.app)

app.add_app("midnovSUSHI", midnovSUSHI.app)


# midnovSUSHI.py
# aaavemidoctoberbatch
# FlipsideValidator



# The main app
app.run()