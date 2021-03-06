from consumatio.entities.season import Season
from consumatio.external.db.models import MediaData, User


def get_season(external_id: str, tmdb: object, code: int, season_number: int,
               db: object) -> dict:
    """
    Make all relevant API requests for this usecase (details) and assemble a Season
    :param external_id: <str> External ID provided by OAuth 
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the tv_show to get season details for
    :param season_number: <int> Number of season to get details for
    :param db: <object> Database object
    :return: <dict> Season details
    """
    dict_season_details = tmdb.get_season_details(external_id, code,
                                                  season_number)

    result = db.session.query(MediaData).join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == 'Season',
        User.external_id_content == external_id,
        MediaData.media_id_content == dict_season_details.get("code")).first()

    favorite = False
    number_of_watched_episodes = 0
    if result != None:
        number_of_watched_episodes = result.number_of_watched_episodes
        favorite = result.favorite_content

    dict = {
        "code": dict_season_details.get("code"),
        "tv_code": code,
        "season_number": dict_season_details.get("season_number"),
        "title": dict_season_details.get("title"),
        "overview": dict_season_details.get("overview"),
        "poster_path": dict_season_details.get("poster_path"),
        "favorite": favorite,
        "number_of_episodes": dict_season_details.get("number_of_episodes"),
        "air_date": dict_season_details.get("air_date"),
        "number_of_watched_episodes": number_of_watched_episodes
    }

    season = Season.from_dict(dict)

    return season.to_dict()
