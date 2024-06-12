import pandas as pd

# Lue nykyinen data
try:
    data_df = pd.read_csv('data.csv')
except FileNotFoundError:
    data_df = pd.DataFrame(columns=["target_group", "lat", "lng"])

# Lisää uusi data
new_data = {
    'target_group': [1],  # Vaihda tarvittaessa oikeisiin arvoihin
    'lat': [60.169158],   # Vaihda tarvittaessa oikeisiin arvoihin
    'lng': [24.940228]    # Vaihda tarvittaessa oikeisiin arvoihin
}

new_data_df = pd.DataFrame(new_data)

# Päivitä data.csv
data_df = pd.concat([data_df, new_data_df], ignore_index=True)
data_df.to_csv('data.csv', index=False)

