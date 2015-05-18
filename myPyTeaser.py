# coding=utf-8
# based on https://github.com/xiaoxu193/PyTeaser

from stop_words import get_stop_words
from re import split as regex_split, sub as regex_sub, UNICODE as REGEX_UNICODE
import numpy as np
from collections import Counter
from math import fabs

stopWords = get_stop_words('portuguese', cache=True)

ideal = 20.0
number_of_comments = 10


def SummarizeComments(main_post, comments):
    comment_likes = [comment.like_count for comment in comments]
    comment_message_list = [comment.message for comment in comments]

    summaries = []
    weights = []
    split_comments = []
    keys = {}
    comment_likes_normed = [1.0*(x - min(comment_likes))/
                            (max(comment_likes) - min(comment_likes)) for x in comment_likes]
    comment_sizes = [len(comment) for comment in comment_message_list]
    comment_sizes_normed = [1.0*(x - min(comment_sizes))/
                            (max(comment_sizes) - min(comment_sizes)) for x in comment_sizes]
    for i, text in enumerate(comment_message_list):
        # cur_sentences = split_sentences(text)
        cur_sentences = [text]
        weights += [(2*comment_likes_normed[i] + comment_sizes_normed[i])/3]*len(cur_sentences)
        split_comments += cur_sentences
        keys.update(keywords(text))

    title_words = split_words(main_post)
    if len(split_comments) <= number_of_comments:
        return split_comments, keys

    #score sentences, and use the top 10 sentences
    best = scoreComments(split_comments, title_words, keys, weights)

    # summaries = comments[best]
    for index in list(best):
        summaries.append(comments[index])

    return summaries, keys


def scoreComments(comments, titleWords, keywords, weights):
    #score sentences based on different features
    scores = []
    sentences = []
    for i, s in enumerate(comments):
        sentence = split_words(s)
        titleFeature = title_score(titleWords, sentence)
        sentenceLength = length_score(sentence)
        sbsFeature = sbs(sentence, keywords)
        dbsFeature = dbs(sentence, keywords)
        frequency = (sbsFeature + dbsFeature) / 2.0 * 10.0

        #weighted average of scores from four categories
        totalScore = (titleFeature*1.0 + frequency*2.0 +
                      sentenceLength*1.0 + weights[i]*3.0) / 6.0

        scores.append(totalScore)

    indices = np.argpartition(np.array(scores), -number_of_comments)[-number_of_comments:]
    indices.sort()
    return indices


def Summarize(title, text):
    summaries = []
    sentences = split_sentences(text)
    keys = keywords(text)
    titleWords = split_words(title)

    if len(sentences) <= 5:
        return sentences

    #score setences, and use the top 5 sentences
    ranks = score(sentences, titleWords, keys).most_common(5)
    for rank in ranks:
        summaries.append(rank[0])

    return summaries


def score(sentences, titleWords, keywords):
    #score sentences based on different features

    senSize = len(sentences)
    ranks = Counter()
    for i, s in enumerate(sentences):
        sentence = split_words(s)
        titleFeature = title_score(titleWords, sentence)
        sentenceLength = length_score(sentence)
        sentencePosition = sentence_position(i+1, senSize)
        sbsFeature = sbs(sentence, keywords)
        dbsFeature = dbs(sentence, keywords)
        frequency = (sbsFeature + dbsFeature) / 2.0 * 10.0

        #weighted average of scores from four categories
        totalScore = (titleFeature*1.5 + frequency*2.0 +
                      sentenceLength*1.0 + sentencePosition*1.0) / 4.0
        ranks[s] = totalScore
    return ranks


def sbs(words, keywords):
    score = 0.0
    if len(words) == 0:
        return 0
    for word in words:
        if word in keywords:
            score += keywords[word]
    return (1.0 / fabs(len(words)) * score)/10.0


def dbs(words, keywords):
    if (len(words) == 0):
        return 0

    summ = 0
    first = []
    second = []

    for i, word in enumerate(words):
        if word in keywords:
            score = keywords[word]
            if first == []:
                first = [i, score]
            else:
                second = first
                first = [i, score]
                dif = first[0] - second[0]
                summ += (first[1]*second[1]) / (dif ** 2)

    # number of intersections
    k = len(set(keywords.keys()).intersection(set(words))) + 1
    return (1/(k*(k+1.0))*summ)


def split_words(text):
    #split a string into array of words
    try:
        text = regex_sub(r'[^\w ]', '', text, flags=REGEX_UNICODE)  # strip special chars
        return [x.strip('.').lower() for x in text.split()]
    except TypeError:
        print ("Error while splitting characters")
        return None


def keywords(text):
    """get the top 10 keywords and their frequency scores
    ignores blacklisted words in stopWords,
    counts the number of occurrences of each word
    """
    text = split_words(text)
    numWords = len(text)  # of words before removing blacklist words
    freq = Counter(x for x in text if x not in stopWords and len(x) > 3)

    minSize = min(10, len(freq))  # get first 10
    keywords = {x: y for x, y in freq.most_common(minSize)}  # recreate a dict

    for k in keywords:
        articleScore = keywords[k]*1.0 / numWords
        keywords[k] = articleScore * 1.5 + 1

    return keywords


def split_sentences(text):
    '''
    The regular expression matches all sentence ending punctuation and splits the string at those points.
    At this point in the code, the list looks like this ["Hello, world", "!" ... ]. The punctuation and all quotation marks
    are separated from the actual text. The first s_iter line turns each group of two items in the list into a tuple,
    excluding the last item in the list (the last item in the list does not need to have this performed on it). Then,
    the second s_iter line combines each tuple in the list into a single item and removes any whitespace at the beginning
    of the line. Now, the s_iter list is formatted correctly but it is missing the last item of the sentences list. The
    second to last line adds this item to the s_iter list and the last line returns the full list.
    '''

    sentences = regex_split(u'(?<![A-ZА-ЯЁ])([.!?]"?)(?=\s+\"?[A-ZА-ЯЁ])', text, flags=REGEX_UNICODE)
    s_iter = zip(*[iter(sentences[:-1])] * 2)
    s_iter = [''.join(y).lstrip() for y in s_iter]
    s_iter.append(sentences[-1])
    return s_iter



def length_score(sentence):
    return 1 - fabs(ideal - len(sentence)) / ideal


def title_score(title, sentence):
    title = [x for x in title if x not in stopWords]
    count = 0.0
    for word in sentence:
        if (word not in stopWords and word in title):
            count += 1.0

    if len(title) == 0:
        return 0.0

    return count/len(title)


def sentence_position(i, size):
    """different sentence positions indicate different
    probability of being an important sentence"""

    normalized = i*1.0 / size
    if 0 < normalized <= 0.1:
        return 0.17
    elif 0.1 < normalized <= 0.2:
        return 0.23
    elif 0.2 < normalized <= 0.3:
        return 0.14
    elif 0.3 < normalized <= 0.4:
        return 0.08
    elif 0.4 < normalized <= 0.5:
        return 0.05
    elif 0.5 < normalized <= 0.6:
        return 0.04
    elif 0.6 < normalized <= 0.7:
        return 0.06
    elif 0.7 < normalized <= 0.8:
        return 0.04
    elif 0.8 < normalized <= 0.9:
        return 0.04
    elif 0.9 < normalized <= 1.0:
        return 0.15
    else:
        return 0
