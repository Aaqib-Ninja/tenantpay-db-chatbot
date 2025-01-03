
# 'bot_id': 'B086ZPV07LM', 
# 'app_id': 'A0872EC6VC3',
# 'user': 'U086W0UJ7FG', 


# import logging
# logging.basicConfig(level=logging.DEBUG)

import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from utils.chatgpt_helper import OpenAIUtils
from utils.slack_helper import SlackUtils
from utils.sql_helper import SQLUtils

from dotenv import load_dotenv
load_dotenv()


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
OPENAI_ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")
SPECIFIC_USER_IDS = ["U07RPH2AJNP"] # U07RPH2AJNP:Aaqib

openai_utils = OpenAIUtils()
sql_utils = SQLUtils()

thread = openai_utils.create_thread()
print(thread.id)


app = App(token=SLACK_BOT_TOKEN)
BOT_USER_ID = app.client.auth_test()["user_id"]

@app.event("message")
def handle_message_events(event, say):
    user_id = event.get("user")
    text = event.get("text")
    channel = event.get("channel")

    # Check if the message is from the specific user
    # if user_id in SPECIFIC_USER_IDS:
    print("text")
    print(text)
    print(BOT_USER_ID)
    print("=====")
    if BOT_USER_ID in text:
        # print(f"Message from {user_id}: {text}")
        # say(text="hello", channel=channel)  # Respond with "hello" in the same channel
        print("found")
        formatted_input = openai_utils.format_input(text, BOT_USER_ID)
        print("formatted_input:", formatted_input)

        run = openai_utils.converse(assistant_id=OPENAI_ASSISTANT_ID, thread_id=thread.id, msg=formatted_input)
        print("run")
        message = openai_utils.extract_latest_response(thread_id=thread.id)
        print("message:", message)
        processed_sql = openai_utils.extract_sql_statement(message)
        print("processed_sql:", processed_sql)
        is_safe_select = sql_utils.is_safe_select(processed_sql)
        print("is_safe_select:", is_safe_select)
        # if processed_sql == None:
        if is_safe_select is False:
            say(text=str(message), channel=channel)
            print("say complete")
        else:
            try:
                output_text=""
                query_output = sql_utils.execute_sql(processed_sql)
                print("query_output", query_output)
                if query_output == None:
                    output_text = "No data found!"
                else:
                    for idx, row in enumerate(query_output):
                        # print(row)
                        output_text+= "\n"+str(row)
                        if idx > 10:
                            break
                
            except Exception as e:
                print("Hello main Exception")
                print(e)
                output_text = "Something went wrong while executing the query. Please check"

            if type(output_text) != str:
                output_text = "Something Went wrong!"
            say(text=str(output_text), channel=channel)  # Respond in the same channel
            print("say complete")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
