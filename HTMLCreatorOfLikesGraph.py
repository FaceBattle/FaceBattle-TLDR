__author__ = 'gbuenoandrade'
import os

def getPointString(x, y, groupNum):
    return "{x: " + str(x) + ", y: " + str(y) + ", group: " + str(groupNum) + "}"

def create(data):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_HTML = os.path.join(APP_ROOT, 'htmlPartsOfLikesGraph')
    file1 = os.path.join(APP_HTML, "p1.txt")
    file2 = os.path.join(APP_HTML, "p2.txt")

    p1 = open(file1, "r").read()
    p2 = open(file2, "r").read()

    dataString = ""
    migue = 0
    for x, vec in data.items():
        migue += 1
        if migue%4 == 0:
            for j in range(0,3):
                if len(dataString) > 0:
                    dataString += "\n,"
                dataString += getPointString(x,vec[j], j)
    ret = ""
    ret = p1 + dataString + p2

    return ret
    # file3 = os.path.join(APP_ROOT, 'graphOfLikes.html')
    # with open(file3, "w") as file:
    #     file.write(p1)
    #     file.write(dataString)
    #     file.write(p2)