__author__ = 'danielpazinato'

import pickle
import unicodedata
import string
import operator
import unicodedata
import re
import codecs
from stop_words import get_stop_words
from wordcloud import WordCloud
from os import path
import matplotlib.pyplot as plt


def remove_accents(line):
    no_accent = ''.join((c for c in unicodedata.normalize('NFD', line) if unicodedata.category(c) != 'Mn')).lower()
    return re.sub(r'[^a-zA-Z0-9 ]', '', no_accent)
    #return no_accent

def save_dict(file_name):
    total_freq = 59384218 #total number of frequecies

    dict_freq = {}
    fobj = codecs.open(file_name, mode = 'r', encoding = 'utf-8')
    for line in fobj:
        value = line.split()
        if len(value) == 2:
            dict_freq[remove_accents(value[1])] = int(value[0])/total_freq

    pickle.dump(dict_freq, open(file_name +".p", "wb" ))


def frequency(word):
    file_name = "texts_files/freq_portugues"
    dict_freq = pickle.load( open(file_name +".p", "rb" ) )

    if word in dict_freq:
        return dict_freq[remove_accents(word)]
    else:
        print("word not in the dictionary")

#receive a string with all comments
#return a image with the worldCloud
def freq_comment(all_comments, _width = 1200, _height = 1000):

    file_name = "texts_files/freq_portugues"
    dict_freq = pickle.load( open(file_name +".p", "rb" ) )
    web_stopWords = ["q","vc","vcs","tipo","ta","pra","pq","ne","sobre"]

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
    stopWords += web_stopWords

    #remove stop words
    for word in stopWords:
        dict_tokens.pop(remove_accents(word), None);

    #sorted by frequency
    sorted_tokens = sorted(dict_tokens.items(), key=operator.itemgetter(1),reverse=True)
    num_tokens = int(min(len(sorted_tokens)/2, 1000))

    sorted_tokens = sorted_tokens[0:num_tokens]

    #normalize by frequency
    standart_frequency = dict_freq["acelga"]
    for i in range(len(sorted_tokens)):
        (token,value) = sorted_tokens[i]
        if token in dict_freq:
            sorted_tokens[i] = (token,value/dict_freq[token])
        else:
            sorted_tokens[i] = (token,value/standart_frequency)

    sorted_tokens_after = sorted(sorted_tokens,key=operator.itemgetter(1), reverse=True)

    #print(sorted_tokens)
    #wordcloud = WordCloud(font_path="~/Library/Fonts/Arial.ttf")
    #wordcloud.generate("eu sou legal mas eu tambem sou mais sou bom e e aa a a")

    #print(sorted_tokens_after)

    wordcloud = WordCloud(width= _width,height= _height,font_path="~/Library/Fonts/Arial.ttf").generate_from_frequencies(sorted_tokens_after)
    # Open a plot of the generated image.
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    return wordcloud


file_name = "texts_files/freq_portugues"
save_dict(file_name)


file = codecs.open("texts_files/comment1", mode = 'r', encoding = 'utf-8')

#put all comments in a line
all_comments = ""
for line in file:
    all_comments += str(line)
freq_comment(all_comments)


print(frequency("gestao"))
print(frequency("legal"))
