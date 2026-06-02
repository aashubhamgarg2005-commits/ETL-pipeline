from configparser import ConfigParser

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)

    @property
    def path(self):
        return self.config.get("DATASOURCE", "path")

    def host(self):
        return { "host": self.config.get("DATABASE", "host"),
            "port": self.config.get("DATABASE", "port"),
            "user": self.config.get("DATABASE", "user"),
            "password": self.config.get("DATABASE", "password"),
            "database": self.config.get("DATABASE", "dbname") }
