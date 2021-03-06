from consumatio.usecases.get_season import *


def get_tv_seasons(external_id: str, tmdb: object, code: int,
                   db: object) -> list:
    """
    Get a list of all seasons of a TV show
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object 
    :param code: <int> Id of the TV show
    :param db: <object> Database object
    :return: <list> List of Seasons
    """
    tv_details = tmdb.get_tv_details(external_id, code)

    number_of_seasons = tv_details.get("number_of_seasons")

    result = []
    for i in range(1, number_of_seasons + 1):
        season = get_season(external_id, tmdb, code, i, db)
        result.append(season)

    return result