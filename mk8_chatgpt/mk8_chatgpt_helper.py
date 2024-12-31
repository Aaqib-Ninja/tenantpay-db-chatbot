from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class OpenAIUtils():
    def __init__(self):
        open_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=open_api_key)


    def create_thread(self):
        thread = self.client.beta.threads.create()
        return thread

    def fetch_thread(self, thread_id):
        thread = self.client.beta.threads.retrieve(thread_id=thread_id)
        return thread

    def fetch_assistant(self, assistant_id):
        assistant = self.client.beta.assistants.retrieve(assistant_id=assistant_id)
        return assistant

    def converse(self, assistant_id, thread_id, msg):
        run = self.client.beta.threads.runs.create_and_poll(
            # thread_id=thread.id,
            # assistant_id=assistant.id,
            thread_id=thread_id,
            assistant_id=assistant_id,
            instructions=msg
        )
        return run


import re
def extract_sql_statement(text):
    pattern = r"```sql\s*(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    return None
# processed_sql = extract_sql_statement(messages.data[0].content[0].text.value)


from sqlalchemy import create_engine, text
def execute_sql(processed_sql):

    db_user = os.getenv("DB_USERNAME")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_DATABASE")
    engine_details = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
    engine = create_engine(engine_details)

    with engine.connect() as connection:
        query = text(processed_sql)
        print("query")
        result = connection.execute(query)

        for row in result:
            print(row)
            # break
        return result


# assistant_id="asst_86Ozc971ubLv1TE48XEfLwAd"
# thread_id = "thread_iRlqdnjJejbZ96CLGV5Ytx6F"
# msg = "Can you fetch the imported bank transactions for the month of October?"

# utils = OpenAIUtils()
# run = utils.converse(assistant_id=assistant_id, thread_id=thread_id, msg=msg)

# if run.status == 'completed':
#     messages = utils.client.beta.threads.messages.list(thread_id=thread_id)
#     print(messages)
# else:
#     print(run.status)
#     print("run")
