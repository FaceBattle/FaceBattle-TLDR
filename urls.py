from flask import Flask, render_template, request, send_file
from TLDR import summarize_post, people_grouping, GetLikesInTimeFromTopGroups
import re
from imageGenTest import genImage
import HTMLCreatorOfLikesGraph
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/tldr/', methods=['POST'])
def make_tldr():
    url = request.form['posturl']
    url = re.search('(\d)+', url)
    token = request.form['authtoken']
    id = url.group(0)
    post, summarized_post, summarized_comments, images, top_commenters = summarize_post(id, token)
    grouped_list, most_important_people = people_grouping(post)
    dict = GetLikesInTimeFromTopGroups(post.comments, grouped_list)
    print "opaaaa"
    HTMLCreatorOfLikesGraph.create(dict)

    # for people_list in grouped_list:
    #     for person in people_list:
    #         print(person.name)
    #     print("***cluster done***")

    if summarized_post is not None:
        summarized_post = summarized_post[0]

    return render_template('postTLDR.html',
                           post=post,
                           summarized_comments=summarized_comments[:6],
                           summarized_post=summarized_post,
                           images=images[:6],
                           top_commenters=top_commenters,
                           most_important_people = most_important_people
                           )

@app.route('/fig/<int:post_id>/<int:group_number>')
def fig(post_id, group_number):
    img = genImage()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0')