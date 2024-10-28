import pandas as pd
import folium as fl
from streamlit_folium import st_folium
import streamlit as st
#import csv

def get_pos(lat, lng):
    return lat, lng

st.set_page_config(layout="wide")
col1, col2 = st.columns([2,8])
with col1:
    st.title('Mapping the HRS locations')
    groups = ('Hauling and logistic companies, public transportation operators, vehicle manufacturers','HRS operators, infrastructure designers and owners, public authorities, research & academia')
    group = st.radio("First select your target group", groups)
try:
    tg = groups.index(group)
except:
    tg = 0

with col2:
    st.subheader('Map: Zoom, pan and click to select locations')
    m = fl.Map([62.5, 25.5], zoom_start=7)
    m.add_child(fl.ClickForMarker())
    map = st_folium(m, height=800, width=1000)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    la, lo = data
    df_new = pd.DataFrame({"type": [tg], "lat": [la], "lng": [lo]})
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['type', 'lat', 'lng'])
    st.session_state.df = pd.concat([st.session_state.df, df_new], ignore_index=True)

if data is not None:
    with col1:
        st.write(st.session_state.df.drop_duplicates()) # Writes to the app
    print(tg, la, lo, sep = ',') # Writes to terminal
