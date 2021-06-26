from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
from decouple import config
import copy

# Custom
from rating import *


def get_update_rating(movie):
    movie_name = movie["Film"].lower()
    year = movie["Year"]
    rating_val, rating_givers = rating_obj.get_rating_data(
        movie_name, year)
    if rating_val:
        old_movie = copy.deepcopy(movie)
        rating_val = round(rating_val, 2)
        movie["Rating"] = rating_val
        movie["Rating Givers"] = int(rating_givers)

        new_values = {"$set": movie}
        mongo.db.wiki_movie.update_one(
            old_movie, new_values)
    return movie


class MovieKey(Resource):
    @staticmethod
    def get(movie_id):
        movie = mongo.db.wiki_movie.find_one({"_id": movie_id})
        if movie:
            try:
                movie["Rating"]
            except:
                movie = get_update_rating(movie)

            movie = jsonify(movie)
            return movie
        message = {"message": "Not Found", "status": 404}
        return jsonify(message)


class MoviePage(Resource):
    @staticmethod
    def get():
        count = int(request.args["count"])
        page = int(request.args["page"])

        start = count * (page - 1) + 1
        end = count * page

        temp = []
        for i in range(start, end + 1):
            temp.append(i)

        all_movie_data = mongo.db.wiki_movie.find({"_id": {"$in": temp}})
        if all_movie_data.count():
            process_all_movie_data = []
            for i in all_movie_data:
                try:
                    i["Rating"]
                except:
                    i = get_update_rating(i)
                process_all_movie_data.append(i)
            process_all_movie_data = jsonify(process_all_movie_data)
            return process_all_movie_data

        message = {"message": "Not Found", "status": 404}
        return jsonify(message)


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://{}:{}/{}".format(
    config("MONGODB_HOST"), config("MONGODB_PORT"), config("DB_NAME"))
api = Api(app)
mongo = PyMongo(app)
api.add_resource(MovieKey, "/movie/<int:movie_id>")
api.add_resource(MoviePage, "/movie")
rating_obj = MovieRating()
