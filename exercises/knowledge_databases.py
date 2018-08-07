from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(chosen_topic, title, rating):
    knowledge_object = Knowledge(
        chosen_topic=chosen_topic,
        title=title,
        rating=rating)
    session.add(knowledge_object)
    session.commit()
topic1= add_article("swing dancing", "charleston", 8)
print(topic1)


    

# def query_all_articles():
#     articles = session.query(Knowledge).all()
#     return articles


# x= query_all_articles()
# print(x)



# def query_article_by_topic(chosen_topic):
#     art = session.query(Knowledge).filter_by(chosen_topic=chosen_topic).first()
#     return art
# print(query_article_by_topic("swing dancing"))

# def query_article_by_rating(rating):
    # threshold= input("rating")
    # rat = session.query(Knowledge).filter_by(rating<threshold).first()
    # return rat


    

# def delete_article_by_topic(chosen_topic):
#     dele = session.query(Knowledge).filter_by(chosen_topic=chosen_topic).delete()
#     session.commit()
# delete_article_by_topic("swing dancing")


# def delete_all_articles():
#     dele_all = session.query(Knowledge).delete()
#     session.commit()
# delete_all_articles()

def query_all_articles():
    articles = session.query(Knowledge).all()
    return articles



def edit_article_rating(title, updated_rating):
    articles = session.query(Knowledge).filter_by(title=title).all()
    for article in articles:
        article.rating = updated_rating
    session.commit()
edit_article_rating("charleston", 5)

def delete_article_by_rating(threshold):
    articles1 = session.query(Knowledge).all()
    for article in articles1:
        if article.rating<threshold:
            session.delete(article)
    session.commit()
delete_article_by_rating(6)
print(query_all_articles())





