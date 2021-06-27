import pandas as pd
import ssl
import copy

# Custom
from database import *


class MovieRating:
    ssl._create_default_https_context = ssl._create_unverified_context

    def __init__(self):
        self.db_object = Database()
        self.movies_csv = self.read_csv(
            "https://school.cefalolab.com/assignment/python/movies.csv")

        self.rating_csv = self.read_csv(
            "https://school.cefalolab.com/assignment/python/ratings.csv")
        self.process_rating = self.rating_prepare()

    @staticmethod
    def read_csv(filename):
        try:
            csv = pd.read_csv(filename)
        except:
            csv = None
        return csv

    def rating_prepare(self):
        process_rating = None
        if isinstance(self.movies_csv, pd.DataFrame) and isinstance(self.rating_csv, pd.DataFrame):
            average = self.rating_csv.groupby(by=["movieId"]).mean().rating
            total = self.rating_csv.groupby(by=["movieId"]).count().rating

            movies_csv_value = self.movies_csv.values
            temp_movie_data = []
            for i in movies_csv_value:
                movie_id, title, genres = i.tolist()
                film, year = " ".join(title.split(
                    "(")[:-1]).strip().lower(), title.split("(")[-1].replace(")", "").strip()
                try:
                    temp_movie_data.append(
                        [film, year, genres, average.loc[movie_id], total.loc[movie_id]])
                except:
                    pass
            process_rating = pd.DataFrame(
                temp_movie_data, columns=["film", "year", "genres", "rating", "rating_givers"])
        return process_rating

    def add_rating_data(self):
        if isinstance(self.process_rating, pd.DataFrame):
            values = self.process_rating.values
            for i in values:
                movie_name, year, _, rating, rating_givers = i
                movie_name = movie_name.lower()

                similar_movie = self.db_object.collection.find(
                    {'Film': movie_name, "Year": year})

                for j in similar_movie:
                    if j["Year"] == year:
                        self.rating_update(
                            j, {'rating': rating, 'rating givers': rating_givers})

    def rating_update(self, movie_data, new_data):
        old_movie = copy.deepcopy(movie_data)
        rating_val = round(new_data["rating"], 2)
        movie_data["Rating"] = rating_val
        movie_data["Rating Givers"] = int(new_data["rating givers"])

        new_values = {"$set": movie_data}
        self.db_object.collection.update_one(old_movie, new_values)


if __name__ == "__main__":
    rating_obj = MovieRating()
    rating_obj.add_rating_data()
