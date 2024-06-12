# -*- coding: utf-8 -*-

import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import csv

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
m = fl.Map(location=[60.5, 25.5], zoom_start=7)
m.add_child(fl.ClickForMarker())

# Näytä kartta Streamlitissa ja kerää klikkauksen tiedot
map_data = st_folium(m, height=600, width=1200)

# Määrittele get_pos-funktio
def get_pos(lat, lng):
    return lat, lng

# Hanki koordinaatit karttaklikkauksesta
if map_data.get("last_clicked"):
    la, lo = get_pos(map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"])
    
    # Lisää uudet koordinaatit CSV-tiedostoon
    with open("data.csv", "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["target_group", "lat", "lng"])
        if f.tell() == 0:  # Tarkistaa, onko tiedosto tyhjä, ja lisää otsikot
            writer.writeheader()
        writer.writerow({"target_group": tg, "lat": la, "lng": lo})
    
    # Lisää uusi markkeri kartalle ja näytä koordinaatit popupissa
    fl.Marker([la, lo], popup=f"Coordinates: ({la}, {lo})").add_to(m)

# Näytä päivitetty kartta
st_folium(m, height=600, width=1200)

# Lopeta-painike
if st.button('Stop and exit'):
    st.write('Stopping... You can close the window')
    st.stop()

