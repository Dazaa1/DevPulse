def estimated_readtime(articles, id):
    article = articles[id]
    split_article = article["content"].split(" ")
    return len(split_article)