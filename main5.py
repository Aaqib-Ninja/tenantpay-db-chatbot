import os



from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import os

from dotenv import load_dotenv
load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

SPECIFIC_USER_ID = "U07RPH2AJNP" # Aaqib

@app.event("message")
def handle_message_events(event, say):
    user_id = event.get("user")
    text = event.get("text")
    channel = event.get("channel")

    # Check if the message is from the specific user
    if user_id == SPECIFIC_USER_ID:
        print(f"Message from {user_id}: {text}")
        say(text="hello", channel=channel)  # Respond with "hello" in the same channel


if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()