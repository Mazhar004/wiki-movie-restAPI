from database import *

movie_database = Database()
all_movie_data = movie_database.collection.find()
for i in all_movie_data:
    print(i,end='\n'+45*'-'+'\n')