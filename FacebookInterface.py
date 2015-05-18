__author__ = 'luizfernando2'
import Serializers
from facepy import GraphAPI


def get_fb_comments(id, token):
    graph = GraphAPI(token)
    comments_iterator = graph.get(path=id + '/comments?fields=attachment,from,id,message,like_count,likes&limit=100',
                                  page=True)
    comment_list = []

    while True:
        try:
            entries = next(comments_iterator)
            comment_list += Serializers.multiple_comment_json_serializer(entries)
        except StopIteration:
            break

    return comment_list

def get_fb_group_post(id, token):
    graph = GraphAPI(token)
    original_post_json = graph.get(path=id+'?fields=attachments,message,id,from,likes.limit(1).summary(true),comments.limit(1).summary(true)',
              page=False)
    return Serializers.post_serializer(original_post_json)


def get_fb_page_post(id, token):
    graph = GraphAPI(token)
    original_post_json = graph.get(path=id+'?fields=message,id,from,likes.limit(1).summary(true),comments.limit(1).summary(true)',
              page=False)
    return Serializers.post_serializer(original_post_json)