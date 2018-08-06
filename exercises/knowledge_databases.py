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


    

def query_all_articles():
    articles = session.query(Knowledge).all()
    return articles


x= query_all_articles()
print(x)



def query_article_by_topic(chosen_topic):
    art = session.query(Knowledge).filter_by(chosen_topic=chosen_topic).first()
    return art
print(query_article_by_topic("swing dancing"))

def query_article_by_rating(rating):
    threshold= input("rating")
    rat = session.query(Knowledge).filter_by(rating<threshold).first()
    return rat


    

def delete_article_by_topic():
    pass

def delete_all_articles():
    pass

def edit_article_rating():
    pass
