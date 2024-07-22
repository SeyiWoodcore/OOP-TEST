        
from sqlalchemy import create_engine
from env import Secrets
from sqlalchemy.pool import QueuePool
import logging

logging.basicConfig(level=logging.INFO)



            #Create a class for your database connection
class Database:
        def __init__(self,db):
                    self.db = db
                    pass

        def connection(db):
            try:
                getdatabaseConnection = create_engine(
                        f"mysql+pymysql://{Secrets.DB_USER}:{Secrets.DB_USER_PASSWD}@{Secrets.DB_HOST}:{Secrets.DB_PORT}/{db}?charset=utf8mb4",
                            pool_recycle=300,
                        )
                conn = getdatabaseConnection.connect().execution_options(
                            stream_results=True
                        )
                return conn
            except Exception as e:
                 logging.info(f"An exception occurred while running report sql {e}")
                 print("An exception occurred while running report sql", e)
