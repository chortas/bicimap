from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx
import folium

useful_tags = ox.settings.useful_tags_way + ['cycleway'] + ['bicycle'] + ["oneway:bicycle"]
ox.utils.config(use_cache=True, log_console=True, useful_tags_way=useful_tags)

# location where you want to find your route
place     = 'Autonomous City of Buenos Aires, Argentina'

# find shortest route based on the mode of travel
mode      = 'bike'        # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'length'        # 'length','time'

# create graph from OSM within the boundaries of some 
# geocodable place(s)
# cf1 = '["bicycle"]'
#graph = ox.graph_from_place(place, custom_filter=cf1, retain_all=True)
#graph = nx.compose(G1, G2)

cf = '["bicycle"]'

locator = Nominatim(user_agent = "myapp")
start_location = locator.geocode("Julian Alvarez, 400, Buenos Aires")
start_location_latlng = (start_location.latitude, start_location.longitude)

end_location = locator.geocode("Julian Alvarez, 800, Buenos Aires")
end_location_latlng = (end_location.latitude, end_location.longitude)

graph = ox.graph.graph_from_place(place, network_type='bike', simplify=False, custom_filter=cf, retain_all=True)

edges_to_add = []
for u,v,k,d in graph.edges(keys=True, data=True):
    bi = False
    if d.get('bicycle')=='designated' and d.get('oneway:bicycle')=='no':
      d['oneway'] = False
      edges_to_add.append((v, u, k, d))

graph.add_edges_from(edges_to_add)

'''for u,v,k,d in graph.edges(keys=True, data=True):
  print(f"u: {u}, v: {v}, k: {k}, d: {d}")'''

fig, ax = ox.plot.plot_graph(graph, bgcolor='#c0c2c2', node_color='#f0ede6', node_size=5,edge_color='#0cc7b4', edge_linewidth=1,save=True)

# find the nearest node to the start location
orig_node = ox.get_nearest_node(graph, start_location_latlng)
print(f"orig_node: {orig_node}")

# find the nearest node to the end location
dest_node = ox.get_nearest_node(graph, end_location_latlng)
print(f"dest_node: {dest_node}")

#  find the shortest path
shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)

route1_length = int(sum(ox.utils_graph.get_route_edge_attributes(graph, shortest_route, "length")))
print("Route is", route1_length, "meters and should be 200 meters")

shortest_route_map = ox.plot_route_folium(graph, shortest_route)

shortest_route_map.save("map.html")
