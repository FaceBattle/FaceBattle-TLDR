__author__ = 'luizfernando2'
import Serializers
import myPyTeaser
import FacebookInterface
from facepy import GraphAPI
from collections import Counter


def summarize_post(id, token):
    graph = GraphAPI(token)
    original_post_json = graph.get(path=id+'?fields=attachments,message,id,from,likes.limit(1).summary(true),comments.limit(1).summary(true)', page=False)

    #this may take a while
    post = Serializers.post_serializer(original_post_json)
    post.comments = FacebookInterface.get_fb_comments(post.id, graph)

    image_comment_list = []
    text_comment_list = []

    commenter_counter = Counter()

    comment_list = [comment.message for comment in post.comments]


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