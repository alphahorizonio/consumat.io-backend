import json

import requests
from consumatio.constants import TMDB_API_PREFIX
from consumatio.external.db.db import Database
from consumatio.external.logger import get_logger_instance
from consumatio.gateways.episode_gateways.episode_details_to_dict import *
from consumatio.gateways.episode_gateways.episode_images_to_dict import *
from consumatio.gateways.movie_gateways.movie_credits_to_dict import *
from consumatio.gateways.movie_gateways.movie_details_to_dict import *
from consumatio.gateways.movie_gateways.movie_images_to_dict import *
from consumatio.gateways.movie_gateways.movie_providers_to_dict import *
from consumatio.gateways.popular_gateways.popular_movies_to_dict import *
from consumatio.gateways.popular_gateways.popular_tv_to_dict import *
from consumatio.gateways.search_gateways.search_result_to_dict import *
from consumatio.gateways.season_gateways.season_details_to_dict import *
from consumatio.gateways.season_gateways.season_images_to_dict import *
from consumatio.gateways.tv_gateways.tv_credits_to_dict import *
from consumatio.gateways.tv_gateways.tv_details_to_dict import *
from consumatio.gateways.tv_gateways.tv_images_to_dict import *
from consumatio.gateways.tv_gateways.tv_providers_to_dict import *

logger = get_logger_instance()


class Tmdb():
    def __init__(self: object, tmdb_key: str, db: object):
        self.db = Database(db)
        self.api_key = tmdb_key

    def get_movie_details(self: object, user: str, movie_id: int) -> dict:
        """
        Fetch tmdb movie details endpoint
        :param movie_id: <int> Id of the movie to fetch details for
        :return: <dict> Movie details
        """
        logger.info("Fetch 'movie_details' from tmdb")
        query = f'{TMDB_API_PREFIX}/movie/{movie_id}?api_key={self.api_key}&language={self.get_language(user)}'
        data = self.get_data(query, self.db)
        return movie_details_to_dict(data)

    def get_movie_providers(
        self: object,
        user: str,
        movie_id: int,
    ) -> dict:
        """
        Fetch tmdb movie providers endpoint
        :param user: External representation of user
        :param movie_id: <int> Id of the movie to fetch details for
        :return: <dict> Movie providers
        """
        logger.info("Fetch 'movie_providers' from tmdb")
        query = f'{TMDB_API_PREFIX}/movie/{movie_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_providers_to_dict(data, self.get_country(user))

    def get_movie_images(self: object, movie_id: int) -> dict:
        """
        Fetch tmdb movie images endpoint
        :param movie_id: <int> Id of the movie to fetch providers images for
        :return: <dict> Movie images
        """
        logger.info("Fetch 'movie_images' from tmdb")
        query = f'{TMDB_API_PREFIX}/movie/{movie_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_images_to_dict(data)

    def get_movie_credits(self: object, movie_id: int) -> dict:
        """
        Fetch tmdb movie credits endpoint
        :param movie_id: <int> Id of the movie to fetch credits for
        :return: <dict> Movie credits
        """
        logger.info("Fetch 'movie_credits' from tmdb")
        query = f'{TMDB_API_PREFIX}/movie/{movie_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_credits_to_dict(data)

    def get_tv_details(self: object, user: str, tv_id: int) -> dict:
        """
        Fetch tmdb tv details endpoint
        :param user: External representation of user
        :param tv_id: <int> Id of the tv show to fetch details for
        :return: <dict> TV show details
        """
        logger.info("Fetch 'tv_details' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}?api_key={self.api_key}&language={self.get_language(user)}'
        data = self.get_data(query, self.db)
        return tv_details_to_dict(data)

    def get_tv_providers(self: object, user: str, tv_id: int) -> dict:
        """
        Fetch tmdb tv providers endpoint
        :param user: External representation of user
        :param tv_id: <int> Id of the tv show to fetch providers for
        :return: <dict> TV show providers
        """
        logger.info("Fetch'tv_providers' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_providers_to_dict(data, self.get_country(user))

    def get_tv_images(self: object, tv_id: int) -> dict:
        """
        Fetch tmdb tv images endpoint
        :param tv_id: <int> Id of the tv show to fetch images for
        :return: <dict> TV show images
        """
        logger.info("Fetch 'tv_images' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_images_to_dict(data)

    def get_tv_credits(self: object, tv_id: int) -> dict:
        """
        Fetch tmdb tv credits endpoint
        :param tv_id: <int> Id of the tv show to fetch credits for
        :return: <dict> TV show credits 
        """
        logger.info("Fetch 'tv_credits' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_credits_to_dict(data)

    def get_season_details(self: object, user: str, tv_id: int,
                           season_number: int) -> dict:
        """
        Fetch tmdb season details endpoint
        :param tv_id: <int> Id of the tv show to fetch season details for
        :param season_number: <int> Number of the season to get details for
        :return: <dict> Season details
        """
        logger.info("Fetch 'season_details' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/season/{season_number}?api_key={self.api_key}&language={self.get_language(user)}'
        data = self.get_data(query, self.db)
        return season_details_to_dict(data, tv_id)

    def get_season_images(self: object, tv_id: int,
                          season_number: int) -> dict:
        """
        Fetch tmdb season images endpoint
        :param tv_id: <int> Id of the tv show to fetch season images for
        :param season_number: <int> Number of the season to get images for
        :return: <dict> Season images
        """
        logger.info("Fetch 'season_images' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/season/{season_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return season_images_to_dict(data)

    def get_episode_details(self: object, user: str, tv_id: int,
                            season_number: int, episode_number: int) -> dict:
        """
        Fetch tmdb episode details endpoint
        :param tv_id: <int> Id of the tv show to fetch episode details for
        :param season_number: <int> Number of the season which contains the searched episode
        :param episode_number: <int> Number of the searched episode in the corresponding season
        :return: <dict> Episode details
        """
        logger.info("Fetch 'episode_details' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={self.api_key}&language={self.get_language(user)}'
        data = self.get_data(query, self.db)
        return episode_details_to_dict(data)

    def get_episode_images(self: object, tv_id: dict, season_number: int,
                           episode_number: int) -> dict:
        """
        Fetch tmdb episode images endpoint
        :param tv_id: <int> Id of the tv show to fetch episode images for
        :param season_number: <int> Number of the season which contains the searched episode
        :param episode_number: <int> Number of the searched episode in the corresponding season
        :return: <dict> Episode images 
        """
        logger.info("Fetch 'episode_images' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return episode_images_to_dict(data)

    def get_search_result(self: object, user: str, keyword: str,
                          page: int) -> dict:
        """
        Fetch tmdb search endpoint
        :param user: External representation of user
        :param keyword: <str> Search string
        :return: <dict> Search results
        """
        logger.info("Fetch 'search' from tmdb")
        query = f'{TMDB_API_PREFIX}/search/multi?api_key={self.api_key}&language={self.get_language(user)}&query={keyword}&page={page}&include_adult=false&region={self.get_country(user)}'
        data = self.get_data(query, self.db)
        return search_result_to_dict(data)

    def get_popular_movies(self: object, user: str, page: int) -> dict:
        """
        Fetch tmdb popular movies endpoint
        :param user: <str> External representation of the user
        :param page: <int> Search page (minimum:1 maximum:1000) 
        :return: <dict> Movie results
        """
        logger.info("Fetch 'popular_movies' from tmdb")
        query = f'{TMDB_API_PREFIX}/movie/popular?api_key={self.api_key}&language={self.get_language(user)}&region={self.get_country(user)}&page={page}&include_adult=false'
        data = self.get_data(query, self.db)
        return popular_movies_to_dict(data)

    def get_popular_tv(self: object, user: str, page: int) -> dict:
        """
        Fetch tmdb popular TV shows endpoint
        :param user: <str> External representation of the user
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> TV results
        """
        logger.info("Fetch 'popular_tv' from tmdb")
        query = f'{TMDB_API_PREFIX}/tv/popular?api_key={self.api_key}&language={self.get_language(user)}&page={page}&include_adult=false'
        data = self.get_data(query, self.db)
        return popular_tv_to_dict(data)

    def get_movies_by_rating(self: object, user: str, vote_avg: float,
                             votes: int, released_from: str,
                             page: int) -> dict:
        """
        Fetch movies by tmdb ratings (in descending order)
        :param user: <str> External representation of the user
        :param vote_avg: <float> Filter media with average rating greater than set value
        :param votes: <int>Filter results by minimum amount of votes
        :param released_from: <str> Search for media released after specified date (YYYY-MM-DD)
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Results of either TV shows or movies filtered by ratings
        """
        logger.info("Fetch 'movies_by_rating' from tmdb")
        query = f'{TMDB_API_PREFIX}/discover/movie?api_key={self.api_key}&language={self.get_language(user)}&region={self.get_country(user)}&sort_by=vote_average.desc&include_adult=false&include_video=false&page={page}&primary_release_date.gte={released_from}&vote_count.gte={votes}&vote_average.gte={vote_avg}'
        data = self.get_data(query, self.db)
        return popular_movies_to_dict(data)

    def get_tv_by_rating(self: object, user: str, vote_avg: float, votes: int,
                         released_from: str, page: int) -> dict:
        """
        Fetch TV shows by tmdb ratings (in descending order)
        :param user: <str> External representation of the user
        :param vote_avg: <float> Filter media with average rating greater than set value
        :param votes: <int>Filter results by minimum amount of votes
        :param released_from: <str> Search for media released after specified date (YYYY-MM-DD)
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Results of either TV shows or movies filtered by ratings
        """
        logger.info("Fetch 'tv_by_rating' from tmdb")
        query = f'{TMDB_API_PREFIX}/discover/tv?api_key={self.api_key}&language={self.get_language(user)}&sort_by=vote_average.desc&include_adult=false&include_video=false&page={page}&first_air_date.gte={released_from}&vote_count.gte={votes}&vote_average.gte={vote_avg}&watch_region={self.get_country(user)}'
        data = self.get_data(query, self.db)
        return popular_tv_to_dict(data)

    def get_recommended_movies(self: object, user: str, code: int,
                               page: int) -> dict:
        """
        Fetch tmdb movie recommendations similar to a specific movie 
        :param user: External representation of user
        :param code: <int> Id of the movie to fetch recommended items for
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Recommended movie results
        """
        logger.info("Fetch 'recommended_movies' from tmdb")
        query = f'https://api.themoviedb.org/3/movie/{code}/recommendations?api_key={self.api_key}&language={self.get_language(user)}&page={page}'
        data = self.get_data(query, self.db)
        return popular_movies_to_dict(data)

    def get_movies_with(self: object, user: str, code: int, page: int) -> dict:
        """
        Fetch movies with a specific cast/production member
        :param user: External representation of user
        :param code: <int> Id of the person to look for in movies
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Movie results
        """
        logger.info("Fetch 'movies_with' from tmdb")
        query = f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&language={self.get_language(user)}&sort_by=primary_release_date.desc&include_adult=false&include_video=false&page={page}&with_people={code}&watch_region={self.get_country(user)}'
        data = self.get_data(query, self.db)
        return popular_movies_to_dict(data)

    def get_recommended_tv(self: object, user: str, code: int,
                           page: int) -> dict:
        """
        Fetch tmdb TV recommendations similar to a specific show 
        :param user: External representation of user
        :param code: <int> Id of the TV show to fetch recommended items for
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Recommended TV show results
        """
        logger.info("Fetch 'recommended_tv' from tmdb")
        query = f'https://api.themoviedb.org/3/tv/{code}/recommendations?api_key={self.api_key}&language={self.get_language(user)}&page={page}'
        data = self.get_data(query, self.db)
        return popular_tv_to_dict(data)

    def get_data(self: object, query: str, db: object) -> dict:
        """
        Gets API response from cache or makes new API request
        :param query: <str> API query
        :param db: <object> Database object
        :return: <dict> Return response of the query
        """
        if (db.is_cached(query)):
            data = json.loads(db.get_from_cache(query))
        else:
            data = requests.get(query).json()
            db.cache(query, json.dumps(data))
        return data

    def get_country(self: object, external_id: str) -> str:
        """
        Gets specified user's country preference
        :param external_id: External representation of user
        :return: <str> Returns ISO 3166-1 alpha-2 country code (e.g. 'DE' or 'US')
        """
        user = self.db.get_user(external_id)

        return user.country

    def get_language(self: object, external_id: str) -> str:
        """
        Gets specified user's language preference
        :param external_id: External representation of user
        :return: <str> Returns RFC 5646 BCP language tag (e.g. 'de-DE' or 'en-US')
        """
        user = self.db.get_user(external_id)

        return user.language
