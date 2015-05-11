__author__ = 'luizfernando2'
import Serializers


def get_fb_comments(id, graph):
        comments_iterator = graph.get(path=id + '/comments?fields=attachment,from,id,message,like_count&limit=100', page=True)
        comment_list = []

        while True:
            try:
                entries = next(comments_iterator)
                comment_list += Serializers.multiple_comment_json_serializer(entries)
            except StopIteration:
                break
        return comment_list
