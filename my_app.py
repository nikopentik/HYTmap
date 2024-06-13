import pandas as pd
import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import csv

def get_pos(lat, lng):
    return lat, lng

st.title('Workshop 1C – Mapping the HRS locations')

groups = {
    1: 'Hauling and logistic companies, public transportation operators, vehicle manufacturers',
    2: 'HRS operators, infrastructure designers and owners, public authorities'
}
group_labels = list(groups.values())
group = st.radio("First select your target group", group_labels)

try:
    tg = group_labels.index(group) + 1
except:
    tg = 1

st.subheader('Map: Zoom, pan and click to select locations')

m = fl.Map([60.5, 25.5], zoom_start=7)
m.add_child(fl.ClickForMarker())
map = st_folium(m, height=600, width=1200)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    la, lo = data
    df_new = pd.DataFrame({"type": [tg], "lat": [la], "lng": [lo]})
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['type', 'lat', 'lng'])
    st.session_state.df = pd.concat([st.session_state.df, df_new], ignore_index=True)

if data is not None:
    st.write(st.session_state.df.drop_duplicates()) # Writes to the app
    print(tg, la, lo, sep = ',') # Writes to terminal

    # Save to CSV
    with open("data.csv", "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["type", "lat", "lng"])
        if f.tell() == 0:  # Tarkistaa, onko tiedosto tyhjä, ja lisää otsikot
            writer.writeheader()
        writer.writerow({"type": tg, "lat": la, "lng": lo})

