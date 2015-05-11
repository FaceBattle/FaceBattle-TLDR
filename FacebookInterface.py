__author__ = 'luizfernando2'
import Serializers
from facepy import GraphAPI


def get_fb_comments(id, token):
    graph = GraphAPI(token)
    comments_iterator = graph.get(path=id + '/comments?fields=attachment,from,id,message,like_count&limit=100', page=True)
    comment_list = []

    while True:
        try:
            entries = next(comments_iterator)
            comment_list += Serializers.multiple_comment_json_serializer(entries)
        except StopIteration:
            break
    return comment_list


def get_fb_post (id, token):
    graph = GraphAPI(token)
    return graph.get(path=id+'?fields=attachments,message,id,from,likes.limit(1).summary(true),comments.limit(1).summary(true)',
              page=False)