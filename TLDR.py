__author__ = 'luizfernando2'

import myPyTeaser
import FacebookInterface
import  Clusterer as cl
from collections import Counter
from text_analise import freq_comment

def summarize_post(id, token):
    # post = FacebookInterface.get_fb_post(id, token)
    post = FacebookInterface.get_fb_page_post(id, token)

    #this may take a while
    post.comments = FacebookInterface.get_fb_comments(post.id, token)

    image_comment_list = []
    text_comment_list = []
    commenter_counter = Counter()

    for comment in post.comments:
        commenter_counter[comment.owner] += 1
        if comment.image_URL is None:
            text_comment_list.append(comment)
        else:
            image_comment_list.append(comment)

    image_comment_list.sort(reverse=True, key=lambda x: x.like_count)


    summarized_post = myPyTeaser.Summarize('', post.message) if post.message is not None else None

    summarized_comments, keywords = myPyTeaser.SummarizeComments(post.message if post.message is not None else '', post.comments)

    top3_commenters = commenter_counter.most_common(3)
    # return summarized_post, summarized_comments
    return post, summarized_post, summarized_comments, image_comment_list, top3_commenters




def people_grouping(post):
    max_clusters = 3
    person_per_cluster = 3

    people_list, clusters, most_important_people = cl.GetPeopleListAndClusterListAndMostImportantPeople(post)

    new_group_list = []
    new_most_important_people = []

    for i in range(max_clusters):
        new_most_important_people.append([])

    for cluster_number, cluster in enumerate(clusters[:max_clusters]):
        my_cluster_list = []
        for person_adj_id in cluster:
            people_list[person_adj_id].group_number = cluster_number
            my_cluster_list.append(people_list[person_adj_id])
        new_group_list.append(my_cluster_list)

    for person_id in most_important_people:
        group = (people_list[person_id]).group_number

        if (group is not None and len(new_most_important_people[group]) < person_per_cluster):
            new_most_important_people[group].append(people_list[person_id])


    return new_group_list, new_most_important_people

def GetTopPostsFromTopGroups(group_list, comments):
    v = [0, 0, 0]
    a = comments
    a.sort(reverse=True, key = lambda x : x.like_count)
    ans = []
    ans.append([])
    ans.append([])
    ans.append([])
    for comment in a:
        if comment.owner in group_list[0] and v[0] < 2:
            v[0] += 1
            ans[0].append(comment)
        if comment.owner in group_list[1] and v[1] < 2:
            v[1] += 1
            ans[1].append(comment)
        if comment.owner in group_list[2] and v[2] < 2:
            v[2] += 1
            ans[2].append(comment)
    return ans

def GetTopImagesFromTopGroups(group_list, comments):
    v = [0, 0, 0]
    a = comments
    a.sort(reverse=True, key = lambda x : x.like_count)
    ans = []
    ans.append([])
    ans.append([])
    ans.append([])
    for comment in a:
        if comment.image_URL is not None:
            if comment.owner in group_list[0] and v[0] < 2:
                v[0] += 1
                ans[0].append(comment)
            if comment.owner in group_list[1] and v[1] < 2:
                v[1] += 1
                ans[1].append(comment)
            if comment.owner in group_list[2] and v[2] < 2:
                v[2] += 1
                ans[2].append(comment)
    return ans


def MakeWordCloudFromTopGroups(group_list, comments, post_id):
    a = comments
    a.sort(reverse=True, key = lambda x : x.like_count)
    ans = []
    ans.append('')
    ans.append('')
    ans.append('')
    for comment in a:
        if comment.owner in group_list[0]:
            ans[0] += '. ' + comment.message
        elif comment.owner in group_list[1]:
            ans[1] += '. ' + comment.message
        elif comment.owner in group_list[2]:
            ans[2] += '. ' + comment.message

    freq_comment(ans[0], _width=400, _height=400, save_file_name=post_id+'_0')
    freq_comment(ans[1], _width=400, _height=400, save_file_name=post_id+'_1')
    freq_comment(ans[2], _width=400, _height=400, save_file_name=post_id+'_2')

    return ans


def GetLikesInTimeFromTopGroups(comments, group_list):
    dict = {}
    likes = [[], [], []]
    v = [0, 0, 0]
    for i, comment in enumerate(comments):
        if comment.owner in group_list[0]:
            v[0] += 1
        if comment.owner in group_list[1]:
            v[1] += 1
        if comment.owner in group_list[2]:
            v[2] += 1
        dict[i] = v[0], v[1], v[2]
        likes[0].append(v[0])
        likes[1].append(v[1])
        likes[2].append(v[2])
    return dict