from .base import *
from .utils.database import Postgres

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

pg = Postgres(host="localhost", port="5555", name="mocktask", user="pg", password="pg")
DATABASES = {"default": pg.database}