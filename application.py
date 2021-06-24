import sys

#Custom
from parsing import *


if __name__ == "__main__":
    if sys.argv[1].lower()=='parse':
        data_parsing = Parsing()
        data_parsing.parse_movie_list()
        data_parsing.save()

