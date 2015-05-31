__author__ = 'danielpazinato'










#put in html

{% for node in nodes%}
     { id: {{ node.id }}, label: "node.name" ,shape: 'circularImage', value: {{ node.value }} , image : "node.image_url",
              group:{{ node.group }} },
{% endfor%}
#    nodes = [
#     {% for person_id in all_important_people_ids%}
#          {%if people_list[person_id].group_number != None %}
#         { id: {{ person_id|e }}, label: "{{ people_list[person_id].name|e }}" ,shape: 'circularImage', value: {{ all_important_people_weights[loop.index0]|e }} , image : "http://graph.facebook.com/{{people_list[person_id].id}}/picture?width=50&height=50",
#             group:{{ people_list[person_id].group_number|e }} },
#         {% endif %}
#     {% endfor %}
# ];
#


#egdes list a tuple
{% for a,b in nodes%}
     {from: {{ a }}, to: {{ b }} },
{% endfor%}

# // create connetions between people
# // value corresponds with the amount of contact between two people
# edges = [
#   {% for i in all_important_people_ids %}
#     {% for j in all_important_people_ids %}
#     {%if adj_matrix[i][j] > 0.01 and i < j and people_list[i].group_number != None and people_list[j].group_number != None%}
#       {from: {{ i }}, to: {{ j }} },
#     {% endif %}{% endfor %}{% endfor %}
# ];