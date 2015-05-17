__author__ = 'luizfernando2'

import FacebookInterface
import numpy as np

# import Serializers
from facepy import GraphAPI

token = 'CAACEdEose0cBALH5cM2ZCNIrRmbgc6HqZAiENElw49RzTvYZAoZBhzZCpgFQI1gbG9opbcKY72EdZAyGNTC9aemufEggkGjYnUXJWlZAER8ut615sDymDeLS6YFHqs6eiCCRlY6JV9Q0a4Kk5sQ9jVvggm36r5rZBX3PMZAi4NhimamIsWyZAyXpazMmNAE3bVdE5f1n8DqUU3NqbZAp0SSS92d'
id = '10155851428715206'

post = FacebookInterface.get_fb_page_post(id, token)
post.comments = FacebookInterface.get_fb_comments(id, token)

#
# people_set = post.unique_people_set()
#
# people_list = list(people_set)
#
# people_dict = {}
# for i, person in enumerate(people_list):
#     people_dict[str(person.id)] = i
#
# adj_matrix = np.zeros((len(people_list), len(people_list)))
#
# for comment in post.comments:
#     i_pos = people_dict[str(comment.owner.id)]
#     for person in comment.likes:
#         j_pos = people_dict[str(person.id)]
#         adj_matrix[i_pos, j_pos] += 1
#         adj_matrix[j_pos, i_pos] += 1
#

#

#
# with open("tmp.bin", "rb") as file:
#     adj_matrix = np.load(file)
#     import TretaMining as TM
#     for i in range(0, len(adj_matrix[3])):
#         adj_matrix[i, i] = 1
#     M, cluster = TM.getClusters(adj_matrix)
#     print(cluster)
#     #TM.getFullGraph(cluster)
#     TM.getCircularGraph(cluster)

# with open("tmp.bin", "wb") as file:
#     np.save(file,adj_matrix)

#with open("tmp.bin", "rb") as file:
#    adj_matrix = np.load(file)