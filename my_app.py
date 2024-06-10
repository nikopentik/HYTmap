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
m.add_child(fl.ClickForMarker())

# Lisää olemassa olevat markkerit CSV-tiedostosta
try:
    data_df = pd.read_csv("data.csv")
    if not data_df.empty and 'lat' in data_df.columns and 'lng' in data_df.columns:
        for idx, row in data_df.iterrows():
            fl.Marker([row['lat'], row['lng']], popup=f"Point {idx+1}").add_to(m)
except FileNotFoundError:
    st.write("CSV file not found. A new file will be created when you add a marker.")
except pd.errors.EmptyDataError:
    st.write("CSV file is empty. Add a marker to start logging data.")
except KeyError:
    st.write("CSV file does not contain the required columns. A new file will be created.")

# Näytä kartta Streamlitissa
map = st_folium(m, height=600, width=1200)

# Määrittele get_pos-funktio
def get_pos(lat, lng):
    return lat, lng

# Hanki koordinaatit karttaklikkauksesta
data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    la, lo = data

    # Lisää uudet koordinaatit CSV-tiedostoon
    with open("data.csv", "a", newline='') as f:
        if data is not None:
            st.write(data)  # Kirjoittaa sovellukseen
            print(la, lo, sep=',')  # Kirjoittaa terminaaliin
            writer = csv.DictWriter(f, fieldnames=["target_group", "lat", "lng"])
            if f.tell() == 0:  # Tarkistaa, onko tiedosto tyhjä, ja lisää otsikot
                writer.writeheader()
            writer.writerow({"target_group": tg, "lat": la, "lng": lo})

    # Lisää uusi markkeri kartalle
    fl.Marker([la, lo], popup="New Point").add_to(m)

# Päivitä kartta uusilla markkereilla
map = st_folium(m, height=600, width=1200)

# Lopeta-painike
if st.button('Stop and exit'):
    st.write('Stopping... You can close the window')
    st.stop()
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
