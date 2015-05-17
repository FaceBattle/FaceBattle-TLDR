import pickle

import operator
import unicodedata
import re
from stop_words import get_stop_words
from wordcloud import WordCloud
import os
import math

def remove_accents(line):
    no_accent = ''.join((c for c in unicodedata.normalize('NFD', line) if unicodedata.category(c) != 'Mn')).lower()
    return re.sub(r'[^a-zA-Z0-9 ]', '', no_accent)
    #return no_accent

# def save_dict(file_name):
#     total_freq = 59384218 #total number of frequecies
#
#     dict_freq = {}
#     fobj = codecs.open(file_name, mode = 'r', encoding = 'utf-8')
#     for line in fobj:
#         value = line.split()
#         if len(value) == 2:
#             dict_freq[remove_accents(value[1])] = int(value[0])/total_freq
#
#     pickle.dump(dict_freq, open(file_name +".p", "wb" ))


def frequency(word):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')
    file_name = os.path.join(APP_STATIC, 'freq_portugues.p')
    dict_freq = pickle.load(open(file_name, "rb" ) )

    if word in dict_freq:
        return dict_freq[remove_accents(word)]
    else:
        print("word not in the dictionary")

#receive a string with all comments
#return a image with the worldCloud
def freq_comment(all_comments, _width = 200, _height = 100, save_file_name= 'tmp'):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')
    file_name = os.path.join(APP_STATIC, 'freq_portugues.p')
    dict_freq = pickle.load(open(file_name, "rb" ) )

    web_stopWords = ["q","vc","vcs","tipo","ta","pra","pq","ne","sobre","ser","cara","la"]

    all_comments = remove_accents(all_comments)
    tokens = all_comments.split()

    #build token dictionary
    dict_tokens = {}
    for token in tokens:
        if token in dict_tokens:
            dict_tokens[token] += 1
        else:
            dict_tokens[token] = 1

    #remove stop words
    stopWords = get_stop_words('portuguese', cache=True)
    stopWords += get_stop_words('english', cache=True)
    stopWords += web_stopWords

    #remove stop words
    for word in stopWords:
        dict_tokens.pop(remove_accents(word), None)

    #for word in dict_tokens:
    #    print(dict_tokens[token])
    #    dict_tokens[token] = 1+math.log(dict_tokens[token])

    #sorted by frequency
    sorted_tokens = sorted(dict_tokens.items(), key=operator.itemgetter(1),reverse=True)
    num_tokens = int(min(len(sorted_tokens)/2, 1000))

    sorted_tokens = sorted_tokens[0:num_tokens]

    #normalize by frequency
    standart_frequency = dict_freq["acelga"]
    for i in range(len(sorted_tokens)):
        (token,value) = sorted_tokens[i]
        if token in dict_freq:
            sorted_tokens[i] = (token, math.log(value/dict_freq[token]))
        else:
            sorted_tokens[i] = (token,math.log(value/standart_frequency))

    sorted_tokens_after = sorted(sorted_tokens,key=operator.itemgetter(1), reverse=True)
    max_num_words = 100
    sorted_tokens_after = sorted_tokens_after[0:max_num_words]

    print("COMECANDO A PLOTAR WORDCLOUD")

    arial_path = os.path.join(APP_ROOT,"Arial.ttf")
    wordcloud = WordCloud(width= _width,height= _height,font_path=arial_path).generate_from_frequencies(sorted_tokens_after)

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'tmp')
    save_file_name = os.path.join(APP_STATIC, save_file_name + '.png')

    wordcloud.to_file(save_file_name)
    print("WORDCLOUD TERMINADO")

    return sorted_tokens_after


#file_name = "texts_files/freq_portugues"
#save_dict(file_name)


# file = codecs.open("texts_files/comment1", mode = 'r', encoding = 'utf-8')
# #put all comments in a line
# all_comments = ""
# for line in file:
#     all_comments += str(line)
# freq_comment(all_comments)


def get_most_freq(all_comments):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')
    file_name = os.path.join(APP_STATIC, 'freq_portugues.p')
    dict_freq = pickle.load(open(file_name, "rb" ) )

    web_stopWords = ["q","vc","vcs","tipo","ta","pra","pq","ne","sobre","ser","cara","la"]

    all_comments = remove_accents(all_comments)
    tokens = all_comments.split()

    #build token dictionary
    dict_tokens = {}
    for token in tokens:
        if token in dict_tokens:
            dict_tokens[token] += 1
        else:
            dict_tokens[token] = 1

    #remove stop words
    stopWords = get_stop_words('portuguese', cache=True)
    stopWords += get_stop_words('english', cache=True)
    stopWords += web_stopWords

    #remove stop words
    for word in stopWords:
        dict_tokens.pop(remove_accents(word), None)

    #for word in dict_tokens:
    #    print(dict_tokens[token])
    #    dict_tokens[token] = 1+math.log(dict_tokens[token])

    #sorted by frequency
    sorted_tokens = sorted(dict_tokens.items(), key=operator.itemgetter(1),reverse=True)
    num_tokens = int(min(len(sorted_tokens)/2, 1000))

    sorted_tokens = sorted_tokens[0:num_tokens]

    #normalize by frequency
    standart_frequency = dict_freq["acelga"]
    for i in range(len(sorted_tokens)):
        (token,value) = sorted_tokens[i]
        if token in dict_freq:
            sorted_tokens[i] = (token, math.log(value/dict_freq[token]))
        else:
            sorted_tokens[i] = (token,math.log(value/standart_frequency))

    sorted_tokens_after = sorted(sorted_tokens,key=operator.itemgetter(1), reverse=True)
    max_num_words = 100
    sorted_tokens_after = sorted_tokens_after[0:max_num_words]

    return sorted_tokens_after
