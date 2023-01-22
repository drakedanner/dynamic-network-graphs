import networkx as nx
import csv

# create an empty directed graph
G = nx.DiGraph()

# read the CSV file
with open("dynamic-simple.csv") as file:
    reader = csv.reader(file)
    next(reader) # skip the header
    for row in reader:
        source, target, date = row

        # add the edge to the graph
        G.add_edge(source, target, date=date)

# create a timestamp attribute for each edge
for u, v, data in G.edges(data=True):
    data['timestamp'] = data['date']

# export the graph to a GEXF file
nx.write_gexf(G, "graph.gexf")