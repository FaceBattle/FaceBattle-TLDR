__author__ = 'luizfernando2'

import FacebookInterface
import numpy as np

# import Serializers
from facepy import GraphAPI

token = 'CAAGjwjYj5jQBAAsnRasZBwRsZCoJ9bLdBH607YghIGAypOfnoMYu8gEEktUXxa61p3y3jZCZCM8vXVIoqwZA6VZCbGb1IZBWjm9fxaNDgv8Yru5VYtjWv64CAGCZByT6BDgduQN3i2m9UkFuVMiqw5avklIzLZBYQtycaPORVn0UZAqEECtJ9dSSOOiP2LnyolmylLHAyJAtGIWVmrOGrTeEBp'
id = '10153217214370446'

post = FacebookInterface.get_fb_post(id, token)
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