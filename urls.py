from flask import Flask, render_template, request, send_file
from TLDR import summarize_post, people_grouping, GetTopPostsFromTopGroups, GetTopImagesFromTopGroups, \
    MakeWordCloudFromTopGroups, GetLikesInTimeFromTopGroups, GetFreqFromAllComments
import re
from imageGenTest import genImage
import HTMLCreatorOfLikesGraph
import Clusterer
from flask_sslify import SSLify


app = Flask(__name__)
app.debug = False

sslify = SSLify(app)


@sslify.app.route('/tldr/', methods=['POST'])
def make_tldr():
    url = request.form['posturl']
    url = re.findall('\/(\d+)\/', url + '/')
    token = request.form['authtoken']
    id = url[-1]

    print("COMECANDO")

    post, summarized_post, summarized_comments, images, top_commenters = summarize_post(id, token)
    grouped_list, most_important_people = people_grouping(post)

    print("TERMINOU REQUESTS")

    top_comments = GetTopPostsFromTopGroups(grouped_list, post.comments)
    # MakeWordCloudFromTopGroups(grouped_list, post.comments, post.id)
    word_array = GetFreqFromAllComments(post.comments)

    mydict = GetLikesInTimeFromTopGroups(post.comments, grouped_list)
    graphic_script = HTMLCreatorOfLikesGraph.create(mydict)

    if summarized_post is not None:
        summarized_post = summarized_post[0]


    adj_matrix, people_list = Clusterer.GetAdjMatrixAndPeopleList(post)
    most_important_people_ids, important_weights = Clusterer.GetMostImportantPeople(adj_matrix)

    max_weight = max([max(x) for x in adj_matrix])
    min_weight = min([min(x) for x in adj_matrix])

    if max_weight!=min_weight:
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] != 0:
                    adj_matrix[i][j] = (adj_matrix[i][j] - min_weight)/(max_weight - min_weight)

    n_people = min(len(adj_matrix),120)

    return render_template('postGraph.html',
                       post=post,
                       summarized_comments=summarized_comments[:6],
                       summarized_post=summarized_post,
                       images=images[:9],
                       top_commenters=top_commenters,
                       most_important_people = most_important_people,
                       adj_matrix = adj_matrix,
                       people_list = people_list,
                       all_important_people_ids  = most_important_people_ids[:n_people],
                       all_important_people_weights = important_weights[:n_people],
                       timeline_script = graphic_script,
                       top_comments=top_comments,
                       word_array=word_array
                       )
@sslify.app.route('/')
def hello_world():
    return render_template('index.html')


@sslify.app.route('/fig/<post_id>/<group_number>')
def fig(post_id, group_number):
    img = genImage(post_id + '_' + group_number)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    sslify.app.run(host='0.0.0.0')