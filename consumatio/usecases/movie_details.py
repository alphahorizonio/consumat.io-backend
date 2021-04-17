from consumatio.entities.movie import Movie

def movie_details(tmdb, code, country):
    dict_movie_details = tmdb.get_movie_details(code)
    dict_movie_images = tmdb.get_movie_images(code)
    dict_movie_providers = tmdb.get_movie_providers(code, country)

    dict = {
        "code": dict_movie_details.get("code"),
        "title": dict_movie_details.get("title"),
        "genres": dict_movie_details.get("genres"),
        "overview": dict_movie_details.get("overview"),
        "popularity": dict_movie_details.get("popularity"),
        "voteAverage": dict_movie_details.get("vote_average"),
        "releaseDate": dict_movie_details.get("release_date"),
        "runtime": dict_movie_details.get("runtime"),
        "status": dict_movie_details.get("status"),
        "backdrops": dict_movie_images.get("backdrops"),
        "posters": dict_movie_images.get("posters"),
        "providers":dict_movie_providers.get("providers"), 
        "watchStatus": None,
        "rating": None,
        "favorite": None
    }

    return dict