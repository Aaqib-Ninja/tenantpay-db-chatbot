
import os
from dotenv import load_dotenv

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()


slack_token = os.getenv("SLACK_BOT_TOKEN")

class SlackUtils():
    def __init__(self):
        self.client = WebClient(token=slack_token)
        self.channel_id = os.getenv("SLACK_CHANNEL_ID")

    def post_message(self, text): 
        try:
            print("SLACK_CHANNEL_ID", self.channel_id)
            response = self.client.chat_postMessage(
                channel=self.channel_id,
                text=text #"Hello from your app! :tada:"
            )
            print(response)
            # response = {'ok': True, 'channel': 'C0872H98EPL', 'ts': '1735829427.573779', 'message': {'user': 'U086W0UJ7FG', 'type': 'message', 'ts': '1735829427.573779', 'bot_id': 'B086ZPV07LM', 'app_id': 'A0872EC6VC3', 'text': 'hello', 'team': 'TJNB6E9B9', 'bot_profile': {'id': 'B086ZPV07LM', 'app_id': 'A0872EC6VC3', 'name': 'TenantPay DB Chatbot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1735828787, 'team_id': 'TJNB6E9B9'}, 'blocks': [{'type': 'rich_text', 'block_id': 'VOhA', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'hello'}]}]}]}}
        except SlackApiError as e:
            print("Inside error")
            print(e)
            # You will get a SlackApiError if "ok" is False
            assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'


    def list_channel_members(self):
        """
        Lists all user IDs in a specific Slack channel.

        Args:
            token (str): Slack Bot Token.
            channel_id (str): ID of the Slack channel.

        Returns:
            list: List of user IDs in the channel.
        """

        response = self.client.conversations_members(channel=self.channel_id)
        # response = {'ok': True, 'members': ['U07RPH2AJNP', 'U07RS54M10U', 'U086W0UJ7FG'], 'response_metadata': {'next_cursor': ''}}
        members = response['members']
        while 'next_cursor' in response.get('response_metadata', {}) and response['response_metadata']['next_cursor'] != '':
            cursor = response['response_metadata']['next_cursor']
            response = self.client.conversations_members(channel=self.channel_id, cursor=cursor)
            members.extend(response['members'])

        return members
    

    def get_user_details(self, user_id):
        """
        Fetches details of a user by their user ID.

        Args:
            token (str): Slack Bot Token.
            user_id (str): Slack user ID.

        Returns:
            dict: Dictionary containing user's real name and display name.
        """
        user_details = {}

        try:
            # Fetch user info
            response = self.client.users_info(user=user_id)
            # response = {'ok': True, 'user': {'id': 'U07RPH2AJNP', 'team_id': 'TJNB6E9B9', 'name': 'aaqib', 'deleted': False, 'color': 'a2a5dc', 'real_name': 'Aaqib', 'tz': 'Asia/Kolkata', 'tz_label': 'India Standard Time', 'tz_offset': 19800, 'profile': {'title': 'Software Engineer', 'phone': '', 'skype': '', 'real_name': 'Aaqib', 'real_name_normalized': 'Aaqib', 'display_name': 'Aaqib', 'display_name_normalized': 'Aaqib', 'fields': None, 'status_text': '', 'status_emoji': '', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'gdbf22d05197', 'huddle_state': 'default_unset', 'huddle_state_expiration_ts': 0, 'first_name': 'Aaqib', 'last_name': '', 'image_24': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-24.png', 'image_32': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-32.png', 'image_48': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-48.png', 'image_72': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-72.png', 'image_192': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-192.png', 'image_512': 'https://secure.gravatar.com/avatar/dbf22d051978e1236f714eab86f06293.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-512.png', 'status_text_canonical': '', 'team': 'TJNB6E9B9'}, 'is_admin': False, 'is_owner': False, 'is_primary_owner': False, 'is_restricted': False, 'is_ultra_restricted': False, 'is_bot': False, 'is_app_user': False, 'updated': 1735798719, 'is_email_confirmed': True, 'who_can_share_contact_card': 'EVERYONE'}}
            user = response.get('user', {})
            user_details = {
                'real_name': user.get('real_name', 'Unknown'),
                'display_name': user.get('profile', {}).get('display_name', 'Unknown')
            }
        except SlackApiError as e:
            print(e)
            print(f"Error fetching user details for {user_id}: {e.response['error']}")

        return user_details
    
    # Get messages from a user
    def get_messages_from_user(self, user_id):

        """
        Fetches messages from a specific user in a Slack channel.

        Args:
            token (str): Slack Bot Token.
            channel_id (str): ID of the Slack channel to search in.
            user_id (str): Slack user ID of the target user.

        Returns:
            list: List of messages from the specific user.
        """
        messages = []

        try:
            # Fetch conversation history
            response = self.client.conversations_history(channel=self.channel_id)
            for message in response['messages']:
                if message.get('user') == user_id:
                    messages.append(message['text'])
        
        except SlackApiError as e:
            print(e)
            print(f"Error fetching messages: {e.response['error']}")

        return messages
