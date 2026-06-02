from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

class Database:

    def __init__(self, config):
        df = config.host()             
        self.engine = create_engine(
            f"postgresql+psycopg2://"
            f"{df['user']}:{df['password']}@"
            f"{df['host']}:{df['port']}/"
            f"{df['database']}"
        )

        self.Session = sessionmaker(
            bind=self.engine
        )

    def create_tables(self):

        Base.metadata.create_all(
            self.engine
        )

    def get_session(self):

        return self.Session()

