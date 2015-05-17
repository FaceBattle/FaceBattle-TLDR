__author__ = 'danielpazinato'

import FacebookInterface
import numpy as np
import text_analise
import pickle
import os.path

# import Serializers
from facepy import GraphAPI

token = 'CAAGjwjYj5jQBALb8iRZAd2Ty8dYIL1yb6KIuXShxFAgrcImYx4WcMTNpPx72VoMeKrZApsoF21zMpoqOFZA8qSCiZCmsnC1MN8pIAeIFzZAZBkAWzvSkCK0HZCZAKnckFI4Mn6I3wL8EB7pyAd8ZCHuKCAAUJYiiMxdi9vZA0NUHuvkWZCeFaelFqf8Aq0C8ZCM93vITlvguQHdUMAY1yOx0Pog4'
id = '10153217214370446'



all_comments = ""


file_name = "texts_files/" + id + ".p";



if os.path.exists(os.getcwd()+"/"+file_name):
    all_comments = pickle.load( open(file_name, "rb" ) )
else:
    post = FacebookInterface.get_fb_post(id, token)
    post.comments = FacebookInterface.get_fb_comments(id, token)
    for comment in post.comments:
        all_comments = all_comments + " " + comment.message
    pickle.dump(all_comments, open(file_name, "wb" ))

text_analise.freq_comment(all_comments)



