from graphene import ObjectType, String, Schema, Decimal, Int, List, Field, Boolean, Float
from flask import Flask, request
import json
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
import dataclasses

app = Flask(__name__)

class Movie(ObjectType):
    code = Int()
    title = String()
    genres = List(String)
    overview = String()
    popularity = Float()
    vote_average = Float()
    release_date = String()
    runtime = Int()
    status = String()
    backdrops = List(String)
    posters = List(String)
    providers = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class TV(ObjectType):
    code = Int()
    name = String()
    genres = List(String)
    overview = String()
    popularity = Float()
    vote_average = Float()
    first_air_date = String()
    last_air_date = String()
    status = String()
    backdrops = List(String)
    posters = List(String)
    providers = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class Season(ObjectType):
    code = Int()
    tv_code = Int()
    season_number = Int()
    name = String()
    overview = String()
    posters = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class Query(ObjectType):
    movie_details = Field(Movie, code=Decimal(), country=String())
    tv_details = Field(TV, code=Decimal(), country=String())
    season_details = Field(Season, code=Decimal(), season_number=Decimal())

    def resolve_movie_details(root, info, code, country):
        tmdb = Tmdb()
        return Movie.from_dict(movie_details(tmdb, code, country))

    def resolve_tv_details(root, info, code, country):
        tmdb = Tmdb()
        return TV.from_dict(tv_details(tmdb, code, country))

    def resolve_season_details(root, info, code, season_number):
        tmdb = Tmdb()
        return Season.from_dict(season_details(tmdb, code, season_number))

schema = Schema(query=Query)

@app.route('/graphql', methods=['GET'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)