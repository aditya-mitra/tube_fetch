from urllib3 import PoolManager
from datetime import datetime
from json import loads as json_loads
from django.db.models import QuerySet

from results.models import YTResult

http = PoolManager()

API_KEY = "AIzaSyApDC4cW478g8MDsSLizst-6Vh_OlV3-DQ"

BASE_URL = "https://www.googleapis.com/youtube/v3/search"

DEFAULT_QUERY = {
    "key": API_KEY,
    "q": "football",
    "safeSearch": "moderate",
    "publishedAfter": datetime(2010, 1, 1).isoformat() + "Z",
    "order": "date",
    "maxResults": "50",
    "part": "snippet",
    "pageToken": "",
}


def store_results(items: list) -> int:
    fault_limit = 0
    items_inserted = 0

    for yt_result in items:

        if yt_result["id"]["kind"] != "youtube#video":
            continue

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

    print("The number of items inserted were ", items_inserted)

    return fault_limit


def start_scheduler():
    query = DEFAULT_QUERY.copy()

    print("Fetching and Storing Results")
    fault_limit = 0

    for i in range(1, 10):
        print("Getting results for page", i, "with page token", query["pageToken"])

        r = http.request("GET", BASE_URL, fields=query)
        yt_results = json_loads(r.data.decode("utf-8"))
        fault_limit += store_results(yt_results["items"])
        query["pageToken"] = yt_results["nextPageToken"]

        if fault_limit > 5:
            break
