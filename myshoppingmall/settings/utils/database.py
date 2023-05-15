class Postgres:
    def __init__(
        self,
        host,
        port="5432",
        name="postgres",
        user="postgres",
        password="postgres",
        conn_max_age=60,
    ):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        self.conn_max_age = conn_max_age

    @property
    def database(self):
        return {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": self.host,
            "PORT": self.port,
            "NAME": self.name,
            "USER": self.user,
            "PASSWORD": self.password,
            "CONN_MAX_AGE": self.conn_max_age,
        }