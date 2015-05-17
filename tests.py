__author__ = 'luizfernando2'

import FacebookInterface
import numpy as np

# import Serializers
from facepy import GraphAPI

token = 'CAACEdEose0cBALH5cM2ZCNIrRmbgc6HqZAiENElw49RzTvYZAoZBhzZCpgFQI1gbG9opbcKY72EdZAyGNTC9aemufEggkGjYnUXJWlZAER8ut615sDymDeLS6YFHqs6eiCCRlY6JV9Q0a4Kk5sQ9jVvggm36r5rZBX3PMZAi4NhimamIsWyZAyXpazMmNAE3bVdE5f1n8DqUU3NqbZAp0SSS92d'
id = '10155851428715206'

post = FacebookInterface.get_fb_page_post(id, token)
post.comments = FacebookInterface.get_fb_comments(id, token)

# import Clusterer
# post = FacebookInterface.get_fb_post(id, token)
#
# people_list, cluster_list, most_important_people = Clusterer.GetPeopleListAndClusterListAndMostImportantPeople(post)
#
#
# import agglomod, HTMLCreator
# with open("tmp.bin", "rb") as file:
#     adj_matrix = np.load(file)
#     cluster = agglomod.getClustersDictionary(adj_matrix)
#     HTMLCreator.create(cluster)