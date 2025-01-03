import os
from sqlalchemy import create_engine, text
import sqlparse

class SQLUtils():
    def __init__(self):
        self.db_user = os.getenv("DB_USERNAME")
        self.db_pass = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_name = os.getenv("DB_DATABASE")
        self.engine = create_engine(f"mysql+pymysql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}")

    def execute_sql(self, processed_sql):
        try:
            with self.engine.connect() as connection:
                query = text(processed_sql)
                print("query")
                result = connection.execute(query)

                # for row in result:
                #     print(row)
                    # break
                return result
        except:
            print("Hello execute_sql Exception")

    def is_safe_select(self, sql_statement):
        if sql_statement is None or sql_statement.strip() == "":
            return False
        parsed = sqlparse.parse(sql_statement)
        if not parsed:
            return False
        statement = parsed[0]
        if statement.get_type() != "SELECT":
            return False
        # Add additional checks here for nested statements or unions
        return True

