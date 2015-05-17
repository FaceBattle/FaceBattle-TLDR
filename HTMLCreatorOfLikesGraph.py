__author__ = 'gbuenoandrade'

def getPointString(x, y, groupNum):
    return "{x: " + str(x) + ", y: " + str(y) + ", group: " + str(groupNum) + "}"

def create(data):
    p1 = open("htmlPartsOfLikesGraph/p1.txt", "r").read()
    p2 = open("htmlPartsOfLikesGraph/p2.txt", "r").read()
    dataString = ""
    for x, vec in data.items():
        for j in range(0,3):
            if len(dataString) > 0:
                dataString += "\n,"
            dataString += getPointString(x,vec[j], j)
    ret = ""
    ret = p1 + dataString + p2
    with open("graphOfLikes.html", "wb") as file:
        file.write(p1)
        file.write(dataString)
        file.write(p2)