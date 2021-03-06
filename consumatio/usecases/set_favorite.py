from consumatio.exceptions.invalid_parameter import InvalidParameter


def set_favorite(tmdb: object, database: object, external_id: str, media: str,
                 code: int, seasonNumber: int, episodeNumber: int,
                 favorite: bool) -> dict:
    """
    Set favorite for a particular Movie, TV, Season or Episode
    :param tmdb: <object> Tmdb object
    :param database: <object> Database object to access database
    :param external_id: <str> External Id provided by OAuth
    :param media: <str> Type of media to
    :param code: <int> Code of the media to favorite
    :param seasonNumber: <int> Number of season if media is season
    :param episodeNumber: <int> Number of episode if media is episode
    :param favorite: <bool> Boolean to set favorite to
    :return: <dict> Successful response
    """

    if media == "TV" and (episodeNumber != None or seasonNumber != None):
        raise InvalidParameter(
            "Please don't specify an episodeNumber or a seasonNumber when favoriting a ",
            media)

    if media == "Movie" and (episodeNumber != None or seasonNumber != None):
        raise InvalidParameter(
            "Please don't specify an episodeNumber or a seasonNumber when favoriting a ",
            media)

    if media == "Season" and (episodeNumber != None or seasonNumber == None):
        raise InvalidParameter(
            "Please specify a seasonNumber and don't specify a episodeNumber when favoriting a ",
            media)

    if media == "Episode" and (episodeNumber == None or seasonNumber == None):
        raise InvalidParameter(
            "Please specify a seasonNumber and episodeNumber when favoriting a ",
            media)

    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    tv_code = None
    if media == "Season":
        result = tmdb.get_season_details(external_id, code, seasonNumber)
        code = result.get("code")
        tv_code = result.get("tv_code")
    if media == "Episode":
        result = tmdb.get_episode_details(external_id, code, seasonNumber,
                                          episodeNumber)
        tv_code = tmdb.get_season_details(external_id, code,
                                          seasonNumber).get("tv_code")
        code = result.get("code")

    if not database.media_data_exists(user_id, media, code):
        database.media_data(user_id, media, code, tv_code)

    database.favorite(user_id, media, code, favorite)
    return {"status": True}