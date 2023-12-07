import pandas as pd
from final_project_part1 import *
from A_star import *
from math import *


def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

class TubeGraph:
    def __init__(self):
        self.edges = {}
        self.coordinates = {} 
        self.destination = None 

    def add_station(self, station_id, lat, lon):
        self.coordinates[station_id] = (lat, lon)

    def add_connection_by_distance(self, station1, station2):
        lon1, lat1 = self.coordinates[station1]
        lon2, lat2 = self.coordinates[station2]
        weight = haversine(lon1, lat1, lon2, lat2)
        self.edges.setdefault(station1, []).append((station2, weight))
        self.edges.setdefault(station2, []).append((station1, weight))

    def add_connection_by_time(self, station1, station2, time):
        self.edges.setdefault(station1, []).append((station2, time))
        self.edges.setdefault(station2, []).append((station1, time))

    def set_destination(self, destination_id):
        self.destination = destination_id

    def initialize_adjacency(self):
        self.adj = {station: set() for station in self.coordinates}
        for station, connections in self.edges.items():
            for (neighbour, _) in connections:
                self.adj[station].add(neighbour)

    def heuristic(self, node):
        if self.destination is None or node not in self.coordinates or self.destination not in self.coordinates:
            return float('inf')  # Return infinity if there is no destination or invalid nodes
        
        lon1, lat1 = self.coordinates[node]
        lon2, lat2 = self.coordinates[self.destination]
        return haversine(lon1, lat1, lon2, lat2)

    def w(self, node1, node2):
        for neighbour, weight in self.edges[node1]:
            if neighbour == node2:
                return weight
        return float('inf')  # Return infinity if there is no direct connection

stations_df = pd.read_csv('london_stations.csv')
connections_df = pd.read_csv('london_connections.csv')

tube_graph = TubeGraph()

for index, row in stations_df.iterrows():
    tube_graph.add_station(station_id=row['id'], lat=row['latitude'], lon=row['longitude'])

for index, row in connections_df.iterrows():
    tube_graph.add_connection_by_distance(station1=row['station1'], station2=row['station2'])

tube_graph.initialize_adjacency()

source_station_id = 11  
destination_station_id = 163  

tube_graph.set_destination(destination_station_id)

def heuristic_wrapper(node):
    return tube_graph.heuristic(node)

# Run the A* algorithm
predecessor, path = a_star(tube_graph, source_station_id, destination_station_id, heuristic_wrapper)

print("Shortest path from station", source_station_id, "to", destination_station_id, "is:", path)

predecessorDijk, distances = dijkstra2(tube_graph, source_station_id)

pathDijkstra = []
current = destination_station_id

while current is not None:
    pathDijkstra.insert(0, current)  
    current = predecessorDijk.get(current)

if pathDijkstra and pathDijkstra[0] == source_station_id: 
    print("Shortest path from station", source_station_id, "to", destination_station_id, "is:", pathDijkstra)
else:
    print("No path found from station", source_station_id, "to", destination_station_id)
