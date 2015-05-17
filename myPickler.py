__author__ = 'luizfernando2'
import pickle


def serialize_everything(post, summarized_post, summarized_comments, images,
                         top_commenters, grouped_list, most_important_people):
    f = open('post', 'w')
    pickle.dump(post, f)
    f.close()

    f = open('sum_p', 'w')
    pickle.dump(summarized_post, f)
    f.close()

    f = open('sum_com', 'w')
    pickle.dump(summarized_comments, f)
    f.close()

    f = open('images', 'w')
    pickle.dump(images, f)
    f.close()

    f = open('top_comenters', 'w')
    pickle.dump(top_commenters, f)
    f.close()

    f = open('grouped_list', 'w')
    pickle.dump(grouped_list, f)
    f.close()

    f = open('most_imp_people', 'w')
    pickle.dump(most_important_people, f)
    f.close()


def load_everything():
    f = open('post', 'r')
    post = pickle.load(f)
    f.close()

    f = open('sum_p', 'r')
    summarized_post = pickle.load(f)
    f.close()

    f = open('sum_com', 'r')
    summarized_comments = pickle.load(f)
    f.close()

    f = open('images', 'r')
    images = pickle.load(f)
    f.close()

    f = open('top_comenters', 'r')
    top_commenters = pickle.load(f)
    f.close()

    f = open('grouped_list', 'r')
    grouped_list = pickle.load(f)
    f.close()

    f = open('most_imp_people', 'r')
    most_imp_people = pickle.load(f)
    f.close()

    return post, summarized_post, summarized_comments, images, top_commenters, grouped_list, most_imp_people

