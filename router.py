from graph import *
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

graph = Graph()
graph.save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "path.html")

