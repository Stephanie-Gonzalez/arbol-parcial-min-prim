# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Lectura del archivo y construcción del grafo
graph = nx.Graph()
with open('graph.txt') as f:
    for line in f:
        frm, to, cost = line.strip().split()
        graph.add_edge(frm, to, weight=int(cost))


def prim(graph, start):
    
# Inicialización
    mst = []
    visited = set([start])
    edges = [(data['weight'], start, to) for to, data in graph[start].items()]
    heapq.heapify(edges)
    
# Bucle hasta que todas las aristas estén en el árbol
    while edges:
      
        
# Encuentra la arista con el costo mínimo que conecta un vértice visitado con uno no visitado
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            
# Agrega las aristas del vértice recién visitado al heap
         for to_next, data in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (data['weight'], to, to_next))
   
    
# Construye el árbol parcial mínimo
    mst_graph = nx.Graph()
    for frm, to, cost in mst:
        mst_graph.add_edge(frm, to, weight=cost)
    
    return mst_graph

# Construcción del árbol parcial mínimo y visualización
mst = prim(graph, 'A')
pos = nx.spring_layout(mst)
nx.draw_networkx_nodes(mst, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_labels(mst, pos, font_size=20, font_family='sans-serif')
nx.draw_networkx_edges(mst, pos, edgelist=mst.edges(), width=2, edge_color='black')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst, 'weight'), font_size=15, font_family='sans-serif')
plt.axis('off')
plt.show()
