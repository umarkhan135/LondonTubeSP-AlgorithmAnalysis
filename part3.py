import pandas as pd
import numpy as np


data = pd.read_csv("london_stations.csv")

longitude = {}
latitude = {}

id_array = np.array(data["id"])


latitude_array = np.array(data["latitude"])
longitude_array = np.array(data["longitude"])

for i in range(len(id_array)):
    longitude[id_array[i]] = longitude_array[i]
    latitude[id_array[i]] = latitude_array[i]


