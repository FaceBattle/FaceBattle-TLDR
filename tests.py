__author__ = 'luizfernando2'

import FacebookInterface
# import Serializers
from facepy import GraphAPI

token = 'CAAGjwjYj5jQBAGiZAOyqqBpU8W92SmxgzMZC97WNvfWPclPNglaHyXoZCOi8iud2LpCeXeBlbc6WKRxcbYEnpY29OTWM1ZCW7Qf2eIIqHEi9ZB99ABf8osAlUZAbRqofdTrIggh0MvGWnWPpapfjqSZBmScebXIgMFzAgzM36SfAakZB1UZBIfzoSmgvNruEnp7krhOgg4OQAgPxQjqF4AFyf'
id = '10153217214370446'
# graph = GraphAPI()
# comments_iterator = graph.get(path='10153217219485446/likes?access_token=CAAGjwjYj5jQBAKPoHhEIxoAqZBRbLgyUmeVZBdgBpyheT1STCHl3yNDTEtmeLU9GhLpI53xtqTPJH9Tcs7swcp3Fdzr1hhaGChcNHpoBJ7yqJLGKfZBXGZBcTVrczZBWE59djNAEaEAwFyIdXnxnLF5oHxcuZBcQpxG6FXv6QnMuGgzHon4jWghPZA7uwkPz9EAZC9krMbowtDNyrZASnhMqG&limit=25&after=MTAyMDAzNjMzNzAwMDQxMjM%3D',
#                       page=True)
#
# while True:
#     try:
#         entries = next(comments_iterator)
#         print(entries)
#         break
#     except StopIteration:
#             break

post = FacebookInterface.get_fb_post(id, token)
post.comments = FacebookInterface.get_fb_comments(id, token)

people_set = set()

for comment in post.comments:
    people_set.add(comment.owner)

    people_set.union(comment.likes)

for person in people_set:
    print(person.name)




