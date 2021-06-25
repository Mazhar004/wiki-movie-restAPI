import sys

# Custom
from parsing import *
from server import *
from database import *


if __name__ == "__main__":
    if sys.argv[1].lower() == 'parse':
        data_parsing = Parsing()
        data_parsing.parse_movie_list()

        movie_database = Database()
        movie_database.collection.drop()
        movie_database.collection.insert_many(data_parsing.all_movie_data)

    elif sys.argv[1].lower() == 'server':
        app.run(debug=False)