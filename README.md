#FaceBattle TLDR


##What is it?

The goal of this project is to break-down long, heated Facebook discussion posts in order to extract useful and concise information about it. Based on the comments and likes-distribution, we use a clustering algorithm to group the people who agree among themselves and provide fun, interactive ways to visualize the information.

[Click here to test it](http://polar-fortress-9545.herokuapp.com)

## How it works:
Our analysis starts from the idea that people that agree with an idea will give a like to the comments of people defending that idea. So we make a graph of who gave a like to who, where the weight of an edge is the ammount of likes given between the 2 people.

On that graph, we run a [Girvan-Newman algorithm](http://en.wikipedia.org/wiki/Girvan–Newman_algorithm) for community detection, effectively separating all the people that appeared in the discussion (either by commenting or liking) into groups.

We then provide information about each group, such as the comments with most likes, the most important words used, and the total likes evolution over time.

##Instructions:

To run it locally, you can just download the project and run the following:

(Note: the project was implemented in Python 3)

```
pip install -r requirements.txt
python urls.py
```

The website should then be accesible on `localhost:5000`

###Restrictions:
Unfortunately, due to the Graph API restrictions, we are unable to access posts within private groups or pages, so you need to test it on public posts.

And also, since this was a hackaton project, the code is still pretty messy and will fail on special ocasions (e.g: invalid links, or privacy-protected posts will result in an internal server error message), but we're working on improving the system to actually make it a fully reliable website.

##Todo:

- [ ] Fix or completely remake the word cloud generator.
- [ ] Make the system robust to errors such as invalid links.
- [ ] Add sentiment analysis to the graph creation process.
