import os



from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import os

from dotenv import load_dotenv
load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()