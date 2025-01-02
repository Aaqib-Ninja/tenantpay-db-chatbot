import os
from sqlalchemy import create_engine, text

class SQLUtils():
    def __init__(self):
        self.db_user = os.getenv("DB_USERNAME")
        self.db_pass = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_name = os.getenv("DB_DATABASE")
        self.engine = create_engine(f"mysql+pymysql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}")

    def execute_sql(self, processed_sql):
        with self.engine.connect() as connection:
            query = text(processed_sql)
            print("query")
            result = connection.execute(query)

            for row in result:
                print(row)
                # break
            return result