__author__ = 'luizfernando2'
from FBClasses import Comment, Post, Person
from facepy import GraphAPI

def multiple_comment_json_serializer(entries):
    my_comment_list = []
    entries = entries['data']
    for entry in entries:
        new_comment = comment_serializer(entry)
        if len(new_comment.message.split()) > 5 or new_comment.image_URL is not None:
            my_comment_list.append(new_comment)
    return my_comment_list


def comment_serializer(comment_json):
    try:
        person_info = comment_json['from']
        person = person_serializer(person_info)
    except KeyError:
        person = None

    try:
        if comment_json['attachment']['type'] == 'photo':
            image_url = comment_json['attachment']['media']['image']['src']
        else:
            image_url = None
    except:
        image_url = None

    try:
        message = comment_json['message']
    except KeyError:
        message = None

    try:
        id = comment_json['id']
    except KeyError:
        id = None

    try:
        like_count = comment_json['like_count']
    except KeyError:
        like_count = None

    likes_set = set()
    try:
        likes_json = comment_json['likes']

        for entry in likes_json['data']:
            likes_set.add(person_serializer(entry))

        if 'paging' in likes_json:
            paging_json = likes_json['paging']
            if 'next' in paging_json:
                next_url = paging_json['next']
                next_url = next_url.replace('https://graph.facebook.com/v2.3/', '', 1)
                graph = GraphAPI()
                likes_iterator = graph.get(path=next_url, page=True)

                while True:
                    try:
                        likes_json = next(likes_iterator)
                        for entry in likes_json['data']:
                            likes_set.add(person_serializer(entry))
                    except StopIteration:
                        break

    except KeyError:
        pass


    return Comment(message=message,
                   id=id,
                   like_count=like_count,
                   owner=person,
                   image_url=image_url,
                   like_set=likes_set
                   )


def person_serializer(person_json):
    try:
        id = person_json['id']
    except KeyError:
        id = None

    try:
        name = person_json['name']
    except KeyError:
        name = None

    return Person(id=id,
                  name=name)


def post_serializer(post_json):
    try:
        person_info = post_json['from']
        person = person_serializer(person_info)
    except KeyError:
        person = None


    try:
        like_count = post_json['likes']['summary']['total_count']
    except KeyError:
        like_count = None

    try:
        if post_json['attachments']['data'][0]['type'] == 'photo':
            image_url = post_json['attachments']['data'][0]['media']['image']['src']
        else:
            image_url = None
    except:
        image_url = None

    try:
        message = post_json['message']
    except KeyError:
        message = None

    try:
        id = post_json['id']
    except KeyError:
        id = None

    try:
        comment_count = post_json['comments']['summary']['total_count']
    except KeyError:
        comment_count = None

    post = Post(message=message,
                id=id,
                like_count=like_count,
                comment_count=comment_count,
                owner=person,
                image_url=image_url
                )

    return post