from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

ox.config(log_console=True, use_cache=True)

# location where you want to find your route
place     = 'Autonomous City of Buenos Aires, Argentina'

# find shortest route based on the mode of travel
mode      = 'walk'        # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'length'        # 'length','time'

# create graph from OSM within the boundaries of some 
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode, retain_all = True)
fig, ax = ox.plot.plot_graph(graph, bgcolor='#c0c2c2', node_color='#f0ede6', node_size=5,edge_color='#0cc7b4', edge_linewidth=1,save=True)

locator = Nominatim(user_agent = "myapp")
start_location = locator.geocode("Acoyte, 275, Buenos Aires")
start_location_latlng = (start_location.latitude, start_location.longitude)

end_location = locator.geocode("Lavalleja, 844, Buenos Aires")
end_location_latlng = (end_location.latitude, end_location.longitude)

# find the nearest node to the start location
orig_node = ox.get_nearest_node(graph, start_location_latlng)

# find the nearest node to the end location
dest_node = ox.get_nearest_node(graph, end_location_latlng)

#  find the shortest path
shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)

shortest_route_map = ox.plot_route_folium(graph, shortest_route)
shortest_route_map.save("map.html")
