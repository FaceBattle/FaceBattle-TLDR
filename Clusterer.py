
import numpy as np
import TretaMining as TM
from mcl_clustering import mcl

the_adj_matrix = []

def GetAdjMatrixAndPeopleList(post): #post.comments
    people_list = list(post.unique_people_set())
    people_dict = {}
    for i, person in enumerate(people_list):
        people_dict[str(person.id)] = i
    adj_matrix = np.zeros((len(people_list), len(people_list)))
    for comment in post.comments:
        i_pos = people_dict[str(comment.owner.id)]
        for person in comment.likes:
            j_pos = people_dict[str(person.id)]
            adj_matrix[i_pos, j_pos] += 1
            adj_matrix[j_pos, i_pos] += 1
    for i in range(0, len(adj_matrix[3])):
        adj_matrix[i, i] = 1
    the_adj_matrix = adj_matrix
    return adj_matrix, people_list


def GetClusters(adj_matrix):

    M, cluster = mcl(adj_matrix, expand_factor=5, inflate_factor=3)

    TM.getFullGraph(cluster)
    cluster_list = []
    for a in cluster.values():
        if a not in cluster_list:
            cluster_list.append(a)
    cluster_list.sort(reverse=True)
    return cluster_list

def GetPeopleListAndClusterList(post): #post
    adj_matrix, people_list = GetAdjMatrixAndPeopleList(post)
    cluster_list = GetClusters(adj_matrix)
    return people_list, cluster_list

def GetMostImportantPeople():
    people = []
    for i, people in enumerate(the_adj_matrix):
        people.append(0)
        for j, other_people in enumerate(the_adj_matrix[i]):
            people[i] += the_adj_matrix[i][j]
    people.sort(reverse=True)
    return people
