from operator import indexOf

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import plotly.express as px
#
df = pd.read_excel("pogoda_rozszerzona.xlsx")
#
df["timestamp_dt"] = pd.to_datetime(
    df["timestamp"],
    format="%H:%M:%S %d-%m-%Y"
)
# # sortowanie po tomestamp
df = df.sort_values("timestamp_dt")
#
# plt.figure()
# plt.scatter(df["temp"], df["humidity"])
# plt.title("Temp. vs wilgotność")
# plt.xlabel("Temp. w st.C")
#
# # plt.show()
# # Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
#
# plt.show()
#
# #Wykres pudełkowy
top_cities = df["place"].value_counts().head(5).index
subset = df[df["place"].isin(top_cities)]
# print(subset.loc[:,"place"])

data_for_box = [
    subset[subset["place"] == city]["temp"]
    for city in top_cities
    ]
plt.figure()
plt.boxplot(data_for_box, tick_labels = top_cities)
plt.show()
# Temperatura i temp. odczuwalna, w czasie dla jednego miasta
city = "Lisbon"
city_df = df[df["place"] == city]

plt.figure()
plt.plot(city_df["timestamp_dt"], city_df["temp"], label="Temperatura")
plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label="Odczuwalna")

plt.legend()

plt.title(f"Temperatura w czasie - {city}")

plt.show()

# Średnia temperatura w miastach - wykres słupkowy

mean_temp = df.groupby("place")["temp"].mean().sort_values()

plt.figure()
plt.bar(mean_temp.index, mean_temp.values)
plt.ylim(-20,50)

plt.show()

# Średnia wilgotność w miastach - wykres słupkowy

mean_humid = df.groupby("place")["humidity"].mean().sort_values()

plt.figure()
plt.bar(mean_humid.index, mean_humid.values)
plt.ylim(0,100)

plt.show()

# Prędkość wiatru w Toroncie
city = "Toronto"
city_df = df[df["place"] == city]

plt.figure()
plt.plot(city_df["timestamp_dt"], city_df["wind"], label="Wiatr")

plt.legend()

plt.title(f"Wiatr  - {city}")

plt.show()


# PLOTLY

#Wykres kołowy
fig = px.pie(
    data_frame = df,
    names= "description",
    title="udział typów pogody"
)
fig.show()

#Wykres słupkowy
fig = px.bar(
data_frame = df,
x= "place",
title="Liczba obserwacji w miastach"
)
fig.update_layout()
xaxis_title="Miasto"
yaxis_title=
fig.show()