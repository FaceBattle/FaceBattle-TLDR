import numpy as np
import agglomod

def GetAdjMatrixAndPeopleList(post): #post.comments
    people_list = list(post.unique_people_set())
    people_dict = {}

    #Dicionario : {"facebookid": "indice na matrix"}
    for i, person in enumerate(people_list):
        people_dict[str(person.id)] = i

    #Constroi matriz de adjacencia
    adj_matrix = np.zeros((len(people_list), len(people_list)))

    for comment in post.comments:
        i_pos = people_dict[str(comment.owner.id)]
        for person in comment.likes:
            j_pos = people_dict[str(person.id)]
            adj_matrix[i_pos, j_pos] += 1
            adj_matrix[j_pos, i_pos] += 1

    for i in range(0, len(adj_matrix[0])):
        adj_matrix[i, i] = 1

    return adj_matrix, people_list

def GetClustersOp2(adjMatrix):
    cluster = agglomod.getClustersDictionary(adjMatrix)
    cluster_list = []
    for a in cluster.values():
        if a not in cluster_list:
            cluster_list.append(a)
    cluster_list.sort(key=len, reverse=True)
    return cluster_list

def GetPeopleListAndClusterListAndMostImportantPeople(post): #post
    adj_matrix, people_list = GetAdjMatrixAndPeopleList(post)
    cluster_list = GetClustersOp2(adj_matrix)
    most_important_people, blah = GetMostImportantPeople(adj_matrix)

    return people_list, cluster_list, most_important_people


def GetMostImportantPeople(the_adj_matrix):
    #Soma linha (total de likes) para cada pessoa
    people_list_importance = []
    for i, people in enumerate(the_adj_matrix):
        people_list_importance.append(0)
        for j, other_people in enumerate(the_adj_matrix[i]):
            people_list_importance[i] += the_adj_matrix[i][j]
    # people_list_importance.sort(reverse=True)

    #Retorna lista decrescente com ids dos mais importantes
    people_list_id = argsort(people_list_importance)

    #Faz lista decrescente do peso de cada pessoa
    people_list_values = []
    for id in people_list_id:
        people_list_values.append(people_list_importance[id])

    # print('peoplr list ids')
    # print(people_list_id)
    # print('people list values')
    # print(people_list_values)

    return people_list_id, people_list_values


def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key = seq.__getitem__, reverse=True)