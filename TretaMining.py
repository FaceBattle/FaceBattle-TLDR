from flask import Flask, render_template

'''
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
'''

#from graph_tool.all import *
from mcl_clustering import mcl
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A = np.array(
               [[1, 2, 3, 1, 0, 0],
               [2, 1, 2, 1, 1, 0],
               [3, 2, 1, 1, 0, 0],
               [1, 1, 1, 1, 0, 0],
               [0, 1, 0, 0, 1, 4],
               [0, 0, 0, 0, 4, 1]])

#M, clusters = mcl(A)
#print(clusters)

def getClusters(M):
    return mcl(M)

from networkx_viewer import Viewer

def getCircularGraph(clusters):
    G = nx.Graph()
    for node, cluster in clusters.items():
        if (len(cluster) > 1):
            G.add_node(node)
    for node, cluster in clusters.items():
        if G.has_node(node):
            for i, each_node in enumerate(cluster):
                if G.has_node(each_node):
                    if (i):
                        G.add_edge(each_node, prev)
                    else:
                        first = each_node
                    if (i == len(cluster)-1):
                        G.add_edge(each_node, first)
                    prev = each_node
    print(len(G.nodes()))
    print(len(G.edges()))
    nx.draw(G)
    plt.show()
    #app = Viewer(G)
    #app.mainloop()

def getFullGraph(clusters):
    G = nx.Graph()
    for node, cluster in clusters.items():
        if (len(cluster) > 2):
            G.add_node(node)
    for node, cluster in clusters.items():
        if G.has_node(node):
            for a in cluster:
                if G.has_node(a):
                    for b in cluster:
                        if G.has_node(b):
                            if a != b:
                                G.add_edge(a, b)
    nx.draw(G)
    print(len(G.nodes()))
    print(len(G.edges()))
    #nx.draw_random(G)
    plt.show()



# draw graph
#nx.draw(G)
#nx.draw_spring(G)
#nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)
