# -*- coding: utf-8 -*-

import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import csv

def get_pos(lat, lng):
    return lat, lng

m = fl.Map([60.5, 25.5], zoom_start=7)
#m.add_child(fl.LatLngPopup())
m.add_child(fl.ClickForMarker())
map = st_folium(m, height=600, width=1200)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    la, lo = data

with open("data.csv", "a", newline='') as f:
    if data is not None:
        st.write(data) # Writes to the app
        print(la, lo, sep = ',') # Writes to terminal
        writer = csv.writer(f)
        writer.writerow(data)
