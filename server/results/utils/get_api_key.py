from datetime import datetime, timedelta
from django.db.models import QuerySet
from urllib3 import PoolManager

from results.models import YoutubeAPIKey


http = PoolManager()


def store_default_api_key():
    """
    store a default api key for fetching
    """

    API_KEY_1 = "AIzaSyCJYk3M5a_1dWpznea7ogcfiKt3fdhFyPo"
    API_KEY_2 = "AIzaSyBgyvoscfG9yyj9nG6LZOt99sQs7osvvEM"
    API_KEY_3 = "AIzaSyApDC4cW478g8MDsSLizst-6Vh_OlV3-DQ"

    QuerySet(YoutubeAPIKey).all().delete()

    QuerySet(YoutubeAPIKey).create(name="default api key 1", api_key=API_KEY_1)
    QuerySet(YoutubeAPIKey).create(name="default api key 2", api_key=API_KEY_2)
    QuerySet(YoutubeAPIKey).create(name="default api key 3", api_key=API_KEY_3)



def check_key_if_valid(key: str) -> bool:
    BASE_URL = "https://www.googleapis.com/youtube/v3/search"
    r = http.request("GET", BASE_URL, fields={"key": key})

    if r.status == 200:
        return True

    tomorrow = datetime.now() + timedelta(days=1)
    QuerySet(YoutubeAPIKey).filter(api_key=key).update(available=tomorrow)
    return False


def get_working_api_key():
    found_key = None
    while found_key is None:
        ytkey = (
            QuerySet(YoutubeAPIKey).filter(available__lte=datetime.now().date()).first()
        )

        if ytkey is None:
            break

        if check_key_if_valid(ytkey.api_key) == True:
            found_key = ytkey.api_key

    return found_key
