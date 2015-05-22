import networkx as nx
import matplotlib.pyplot as plt
import io

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
    # print(len(G.nodes()))
    # print(len(G.edges()))
    # nx.draw(G)
    # plt.show()


def getFullGraph(clusters):
    G = nx.Graph()
    for id, cluster in clusters.items():
        #if len(cluster) > 2:
            for a in cluster:
                    for b in cluster:
                            if a != b:
                                G.add_edge(a, b)
    # nx.draw(G)
    # print(len(G.nodes()))
    # print(len(G.edges()))
    # plt.show()
    fig = plt.gcf()
    imgdata = io.BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    return imgdata
