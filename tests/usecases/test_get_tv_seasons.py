from consumatio.external.db.models import *
from consumatio.usecases.get_tv_seasons import get_tv_seasons
from tests.utils.setup_app import setup_app


def test_get_tv_seasons():
    tmdb = setup_app()[0]

    list = [{
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        False,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        0,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }]

    assert list == get_tv_seasons("d41d8cd98@d41d8cd98.com", tmdb, 1399, db)
