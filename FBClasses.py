

class Post:
    def __init__(self, message, id, like_count, comment_count, owner, image_url):
        self.message = message
        self.id = id
        self.like_count = like_count
        #likes = set of Person
        self.likes = set()
        self.comment_count = comment_count
        #comments = array of Comment
        self.comments = []
        self.owner = owner
        self.image_url = image_url

    def __str__(self):
        return "ID: {0} \n Likes: {1} \n Comments: {2}".format(self.id, self.like_count, self.comment_count)

    def unique_people_set(self):
        people_set = set()
        for comment in self.comments:
            people_set.add(comment.owner)

            people_set.update(comment.likes)

        return people_set



class Comment:
    def __init__(self, message, id, like_count, owner, image_url, like_set):
        self.message = message
        self.id = id
        self.like_count = like_count
        self.likes = like_set
        self.owner = owner
        self.image_URL = image_url

    def __str__(self):
        return self.message


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)