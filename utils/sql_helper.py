import os
from sqlalchemy import create_engine, text
import sqlparse
import pandas as pd

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
            return ""


    def execute_sql_excel(self, processed_sql):
        try:
            with self.engine.connect() as connection:
                query = text(processed_sql)
                print("query")
                result = connection.execute(query)

                # for row in result:
                #     print(row)
                    # break
                # return result

                data_rows = []
                headers = list(result.keys())

                for row in result:
                    data_rows.append(row)
                    
                return headers, data_rows
        except:
            print("Hello execute_sql Exception")
            return [], []

    def create_excel_file(self, headers, data):
        output_file = "./query_outputs.xlsx"

        table = [dict(zip(headers, row)) for row in data]

        df = pd.DataFrame(table)
        df = df.astype(str)
        df.fillna("null", inplace=True)

        df.to_excel(output_file, index=False)
        return output_file



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

