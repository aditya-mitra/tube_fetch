import sys
import logging
from urllib3 import PoolManager
from datetime import datetime
from json import loads as json_loads
from django.db.models import QuerySet
from apscheduler.schedulers.background import BackgroundScheduler

from results.models import YTResult
from .get_api_key import store_default_api_key, get_working_api_key

http = PoolManager()


BASE_URL = "https://www.googleapis.com/youtube/v3/search"

DEFAULT_QUERY = {
    "key": "",
    "q": "football",
    "safeSearch": "moderate",
    "publishedAfter": datetime(2021, 1, 1).isoformat() + "Z",
    "order": "date",
    "maxResults": "50",
    "part": "snippet",
    "type": "video",
    "pageToken": "",
}

logger = logging.getLogger("GET_AND_STORE_YT_RESULTS")
handler = logging.StreamHandler()
formatter = logging.Formatter("[GET_AND_STORE_YT_RESULTS] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def store_results(items: list) -> int:
    fault_limit = 0
    items_inserted = 0

    for yt_result in items:

        if (
            QuerySet(model=YTResult)
            .filter(video_id=yt_result["id"]["videoId"])
            .exists()
        ):
            fault_limit = fault_limit + 1
            continue

        QuerySet(model=YTResult).create(
            video_id=yt_result["id"]["videoId"],
            title=yt_result["snippet"]["title"],
            thumbnail_url=yt_result["snippet"]["thumbnails"]["medium"]["url"],
            description=yt_result["snippet"]["description"],
            published_date=yt_result["snippet"]["publishedAt"],
        )

        items_inserted = items_inserted + 1

    logger.info("The number of items inserted were {}".format(items_inserted))

    return fault_limit


def get_results():
    query = DEFAULT_QUERY.copy()
    working_key = get_working_api_key()
    if working_key is None:
        logger.critical("No Working API Keys found. (Please add a new one)")
        return

    logger.info("Using API Key - {}".format(working_key))

    query["key"] = working_key

    logger.info("Fetching and Storing Results")
    fault_limit = 0

    for i in range(1, 10):
        logger.info(
            "Getting results for page {} with page token {}".format(
                i, query["pageToken"]
            )
        )

        r = http.request("GET", BASE_URL, fields=query)
        yt_results = json_loads(r.data.decode("utf-8"))
        if "items" not in yt_results:
            break
        fault_limit += store_results(yt_results["items"])
        query["pageToken"] = yt_results["nextPageToken"]

        if fault_limit > 5:

            logger.warning(
                "The fault was {} (Stopping getting more results)".format(fault_limit)
            )
            break


def start_scheduler():

    if "migrate" in sys.argv or "makemigrations" in sys.argv:
        return

    store_default_api_key()
    scheduler = BackgroundScheduler()
    get_results() # intial populate
    scheduler.add_job(get_results, "interval", minutes=2)
    scheduler.start()
