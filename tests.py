__author__ = 'luizfernando2'

import FacebookInterface
import numpy as np

# import Serializers
from facepy import GraphAPI

token = 'CAAWvbeaxw2gBAGYeqrc0c37iQHZBpzDLUvZCiadwsL3CAs98uUTUx45PrgFg43N9sixc1wvjs7Doq7il8hZCBpjuWxgGh5MjECfELRSJWsxLePdMeAWjZAdeOHAPRqx9OlF68c0YaykFESjLrndZAw7OZBSj84LDHhTGa2FXkyBUSeZBHZANifjvZBczXTWpsSg8ZD'
id = '10153217214370446'
#
# post = FacebookInterface.get_fb_post(id, token)
# post.comments = FacebookInterface.get_fb_comments(id, token)
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
# with open("tmp.bin", "wb") as file:
#     np.save(file,adj_matrix)
#

import Clusterer
post = FacebookInterface.get_fb_post(id, token)

people_list, cluster_list, most_important_people = Clusterer.GetPeopleListAndClusterListAndMostImportantPeople(post)


import agglomod, HTMLCreator
with open("tmp.bin", "rb") as file:
    adj_matrix = np.load(file)
    cluster = agglomod.getClustersDictionary(adj_matrix)
    HTMLCreator.create(cluster)