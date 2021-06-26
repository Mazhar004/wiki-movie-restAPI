import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class MovieRating:
    def __init__(self):
        self.movies_csv = self.read_csv(
            "https://school.cefalolab.com/assignment/python/movies.csv")

        self.rating = self.read_csv(
            "https://school.cefalolab.com/assignment/python/ratings.csv")
        self.process_rating = self.rating_prepare()

    def read_csv(self, filename):
        try:
            csv = pd.read_csv(filename)
        except:
            csv = None
        return csv

    def rating_prepare(self):
        process_rating = None
        if isinstance(self.movies_csv, pd.DataFrame):
            if isinstance(self.rating, pd.DataFrame):
                average = self.rating.groupby(by=["movieId"]).mean().rating
                total = self.rating.groupby(by=["movieId"]).count().rating

                movies_csv_value = self.movies_csv.values
                temp_movie_data = []
                for i in movies_csv_value:
                    movieId, title, genres = i.tolist()
                    film, year = " ".join(title.split(
                        "(")[:-1]).strip().lower(), title.split("(")[-1].replace(")", "").strip()
                    try:
                        temp_movie_data.append(
                            [film, year, genres, average.loc[movieId], total.loc[movieId]])
                    except:
                        pass
                process_rating = pd.DataFrame(
                    temp_movie_data, columns=["film", "year", "genres", "rating", "rating_givers"])
        return process_rating

    def get_rating_data(self, movie_name, year):
        rating_val = None
        rating_givers = None
        if isinstance(self.process_rating, pd.DataFrame):
            common_name = self.process_rating[self.process_rating.film == movie_name.lower(
            )]
            if common_name.shape[0]:
                if common_name.shape[0] == 1:
                    rating_val, rating_givers = common_name.iloc[0].values[-2:]
                else:
                    common_data = common_name[common_name.year == year]
                    if common_data.shape[0]:
                        rating_val, rating_givers = common_data.values[0][-2:]

        return rating_val, rating_givers
