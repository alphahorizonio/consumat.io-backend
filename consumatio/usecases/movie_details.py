from consumatio.entities.movie import Movie

def movie_details(tmdb, code, country):
    dict_movie_details = tmdb.get_movie_details(code)
    dict_movie_images = tmdb.get_movie_images(code)
    dict_movie_providers = tmdb.get_movie_providers(code, country)

    providers = []
    for provider in range(len(dict_movie_providers.get("providers").get("flatrate"))):
        providers.append(dict_movie_providers.get("providers").get("flatrate")[provider].get("provider_name"))

    dict = {
        "code": dict_movie_details.get("code"),
        "title": dict_movie_details.get("title"),
        "genres": dict_movie_details.get("genres"),
        "overview": dict_movie_details.get("overview"),
        "popularity": dict_movie_details.get("popularity"),
        "vote_average": dict_movie_details.get("vote_average"),
        "release_date": dict_movie_details.get("release_date"),
        "runtime": dict_movie_details.get("runtime"),
        "status": dict_movie_details.get("status"),
        "backdrops": dict_movie_images.get("backdrops"),
        "posters": dict_movie_images.get("posters"),
        "providers": providers,
        "watch_status": None,
        "rating": None,
        "favorite": None
    }

    print(dict.get("release_date"))
    movie = Movie.from_dict(dict)

    return movie.to_dict()