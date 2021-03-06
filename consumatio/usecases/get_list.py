from consumatio.usecases.get_movie import *
from consumatio.usecases.get_tv import *
from consumatio.external.db.models import MediaData, User


def get_list(tmdb: object, external_id: str, type: str, watchStatus: str,
             favorite: bool, db: object) -> list:
    """
    Get list from database with respect to the values of watchStatus and favorite
    :param tmdb: <object> Tmdb object 
    :param external_id: <str> External ID provided by OAuth
    :param type: <str> Type of the media to query
    :param watchStatus: <str> watchStatus of the media to be contained in the list
    :param favorite: <bool> True if the media in the list should contain only favorites
    :param db: <object> Database object
    :return: <list> List of the media requested with respect to the values of watchStatus and favorite
    """
    watch_list = []
    results = []

    if watchStatus == None and favorite != None:
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.favorite_content == favorite,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    elif watchStatus == None and favorite == None:
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    elif watchStatus != None and favorite != None:
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.watch_status_content == watchStatus,
            MediaData.favorite_content == favorite,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    else:
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.watch_status_content == watchStatus,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    for result in results:
        if type == "Movie":
            dict = get_movie(external_id, tmdb, result.media_id_content, db)
            dict["__typename"] = "Movie"
            watch_list.append(dict)
        elif type == "TV":
            dict = get_tv(external_id, tmdb, result.media_id_content, db)
            dict["__typename"] = "TV"
            watch_list.append(dict)

    return watch_list
