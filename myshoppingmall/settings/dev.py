from .base import *
from .utils.database import Postgres

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

pg = Postgres(host="localhost", port="5432", name="myshop", user="postgres", password="postgres")
DATABASES = {"default": pg.database}