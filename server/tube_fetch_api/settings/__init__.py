from dotenv import load_dotenv

load_dotenv()

from os import getenv

IS_PRODUCTION = (
    getenv("IS_PRODUCTION") is not None and getenv("IS_PRODUCTION").upper() == "TRUE"
)

if IS_PRODUCTION:
    print("The production server is running 🎉")
    from .production import *
else:
    from .dev import *

from .base import *
