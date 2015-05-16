
import numpy as np
import TretaMining as TM

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


def GetClusters(adj_matrix):
    M, cluster = TM.mcl(adj_matrix, expand_factor=5, inflate_factor=3)
    print(cluster)
    TM.getFullGraph(cluster)
    cluster_list = []
    for a in cluster.values():
        if a not in cluster_list:
            cluster_list.append(a)
    sorted(cluster_list)
    cluster_list = list(reversed(cluster_list))
    for a in cluster_list:
        print(a)
    return cluster_list

def GetPeopleListAndClusterList(post): #post
    adj_matrix, people_list = GetAdjMatrixAndPeopleList(post)
    cluster_list = GetClusters(adj_matrix)
    return people_list, cluster_list


