from consumatio.constants import TMDB_FRONTEND_PREFIX


def popular_movies_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    result_list = []
    total_pages = 0

    if "results" in data and len(data["results"]) > 0:
        results = data["results"]
        total_pages = data["total_pages"]

        for result in results:

            dict = {
                "__typename": "Movie",
                "code": result.get("id"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "rating_count": result.get("vote_count"),
                "release_date": result.get("release_date"),
                "runtime": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "cast": None,
                "directors": None,
                "tmdb_url": f'{TMDB_FRONTEND_PREFIX}/movie/{result.get("id")}',
            }

            result_list.append(dict)

    return {"total_pages": total_pages, "results": result_list}
