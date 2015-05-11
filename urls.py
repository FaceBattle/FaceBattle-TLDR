from flask import Flask, render_template, request
from TLDR import summarize_post
import re


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
    post, summarized_post, summarized_comments, images, top_commenters = summarize_post(url.group(0), token)

    return render_template('postTLDR.html',
                           post=post,
                           summarized_comments=summarized_comments[:6],
                           summarized_post=summarized_post[0],
                           images=images[:6],
                           top_commenters=top_commenters
                           )

if __name__ == '__main__':
    app.run(host='0.0.0.0')