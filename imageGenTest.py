import matplotlib.pyplot as plt
import io
#define some data
import os

def genImage(file_name):
    # x = [1,2,3,4]
    # y = [20, 21, 20.5, 20.8]
    #
    # #plot data
    # plt.plot(x, y)
    # fig = plt.gcf()
    # imgdata = io.BytesIO()
    # fig.savefig(imgdata, format='png')
    # imgdata.seek(0)  # rewind the data

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'tmp')
    file_name = os.path.join(APP_STATIC, file_name + '.png')

    image = open(file_name, 'rb')
    return image