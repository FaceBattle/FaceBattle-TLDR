from flask import Flask, render_template

'''
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
'''


from mcl_clustering import mcl
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from networkx_viewer import Viewer

def getCircularGraph(clusters):
    G = nx.Graph()
    for node, cluster in clusters.items():
        if len(cluster) > 2:
            for i, each_node in enumerate(cluster):
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

def getFullGraph(clusters):
    G = nx.Graph()
    for id, cluster in clusters.items():
        #if len(cluster) > 2:
            for a in cluster:
                    for b in cluster:
                            if a != b:
                                G.add_edge(a, b)
    nx.draw(G)
    print(len(G.nodes()))
    print(len(G.edges()))
    plt.show()

