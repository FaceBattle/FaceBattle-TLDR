__author__ = 'luizfernando2'
from FBClasses import Comment, Post, Person


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

    return Comment(message=message,
                   id=id,
                   like_count=like_count,
                   owner=person,
                   image_url=image_url
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