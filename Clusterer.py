import numpy as np
import TretaMining as TM
from mcl_clustering import mcl
import agglomod

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
    return adj_matrix, people_list

def GetClustersOp2(adjMatrix):
    cluster = agglomod.getClustersDictionary(adjMatrix)
    TM.getFullGraph(cluster)
    cluster_list = []
    for a in cluster.values():
        if a not in cluster_list:
            cluster_list.append(a)
    cluster_list.sort(key=len, reverse=True)
    return cluster_list

def GetClusters(adj_matrix):
    M, cluster = mcl(adj_matrix, expand_factor=5, inflate_factor=3)

    TM.getFullGraph(cluster)
    cluster_list = []
    for a in cluster.values():
        if a not in cluster_list:
            cluster_list.append(a)
    cluster_list.sort(key=len, reverse=True)
    return cluster_list


def GetPeopleListAndClusterListAndMostImportantPeople(post): #post
    adj_matrix, people_list = GetAdjMatrixAndPeopleList(post)
    cluster_list = GetClustersOp2(adj_matrix)
    most_important_people = GetMostImportantPeople(adj_matrix)

    return people_list, cluster_list, most_important_people


def GetMostImportantPeople(the_adj_matrix):
    people_list = []
    for i, people in enumerate(the_adj_matrix):
        people_list.append(0)
        for j, other_people in enumerate(the_adj_matrix[i]):
            people_list[i] += the_adj_matrix[i][j]
    # people_list.sort(reverse=True)
    people_list = argsort(people_list)
    return people_list


def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key = seq.__getitem__, reverse=True)