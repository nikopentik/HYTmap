import pandas as pd

# Lue nykyinen CSV-tiedosto
try:
    data_df = pd.read_csv("data.csv")
except FileNotFoundError:
    data_df = pd.DataFrame(columns=["target_group", "lat", "lng"])

# Tee muutoksia data_df:hen tarvittavalla tavalla
# Esimerkiksi lisää uusi rivi
# Huomaa, että tässä esimerkissä käytämme kiinteitä arvoja
new_data = pd.DataFrame([{"target_group": 0, "lat": 60.5, "lng": 25.5}])  # Korvaa tämä todellisilla tiedoilla
data_df = pd.concat([data_df, new_data], ignore_index=True)

# Kirjoita päivitetty CSV-tiedosto takaisin
data_df.to_csv("data.csv", index=False)


