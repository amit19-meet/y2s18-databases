from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__= "Knowledge"
	student_number = Column(Integer, primary_key=True)
	chosen_topic = Column(String)
	title= Column(String)
	rating= Column(Integer)

	def __repr__(self):
       return ("Topic: {}\n"
               "The title of the article: {}\n"
               "Rating: {}\n").format(self.chosen_topic, self.title, self.rating)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

student1= Knowledge(chosen_topic= "swing dancing", title= "Charleston", rating= 8)
print("If you want to learn about"+ student1.chosen_topic()+", you should look at the Wikipedia article called rainbow.
We gave this article a rating of 9 out of 10!)
