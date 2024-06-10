# -*- coding: utf-8 -*-

import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import csv
import pandas as pd

# Otsikko
st.title('Workshop 1C – Mapping the HRS locations')

# Radiopainikkeet kohderyhmän valintaa varten
groups = ('Hauling and logistic companies, public transportation operators, vehicle manufacturers',
          'HRS operators, infrastructure designers and owners, public authorities')
group = st.radio("First select your target group", groups)
try:
    tg = groups.index(group)
except:
    tg = 0

# Alateksti ennen karttaa
st.subheader('Map: Zoom, pan and click to select locations')

# Luo folium-kartta
m = fl.Map([60.5, 25.5], zoom_start=7)
m.a