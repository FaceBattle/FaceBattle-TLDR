__author__ = 'gbuenoandrade'

def getNodeString(id, group):
    return "{id: " + str(id) + ", shape: 'circularImage', image: '" + str(id) + ".png', group:" + str(group) + "}"

def getEdgeString(u, v):
    return "{from: " + str(u) + ", to:" + str(v) + "}"

def create(cluster):
    p1 = open("htmlParts/p1.txt", "r").read()
    p2 = open("htmlParts/p2.txt", "r").read()
    p3 = open("htmlParts/p3.txt", "r").read()
    nodes = ""
    edges = ""
    compNum = 0
    for comp in cluster.values():
        compNum += 1
        n = min(len(comp),5)
        for i in range(0, n):
            if len(nodes) > 0:
                nodes += ",\n"
            nodes += getNodeString(comp[i], compNum)
            for j in range(i+1,n):
                if len(edges) > 0:
                    edges += ",\n"
                edges += getEdgeString(comp[i], comp[j])


    with open("graph.html", "wb") as file:
        file.write(p1)
        file.write(nodes)
        file.write(p2)
        file.write(edges)
        file.write(p3)