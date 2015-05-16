import matplotlib.pyplot as plt
import io
#define some data

def genImage():
    x = [1,2,3,4]
    y = [20, 21, 20.5, 20.8]

    #plot data
    plt.plot(x, y)
    fig = plt.gcf()
    imgdata = io.BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    return imgdata