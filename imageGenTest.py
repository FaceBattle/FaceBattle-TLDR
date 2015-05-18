import os

def genImage(file_name):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'tmp')
    file_name = os.path.join(APP_STATIC, file_name + '.png')

    image = open(file_name, 'rb')
    return image