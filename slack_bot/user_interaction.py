```python
import datetime
from slack_sdk import WebClient
from .config import SLACK_API_TOKEN
from .gpt3_5_integration import generate_response
from .slack_integration import respond_to_message

# Initialize a Web API client
slack_web_client = WebClient(token=SLACK_API_TOKEN)

def handle_user_interaction(event_data):
    """
    Function to handle user interaction on Slack.
    """
    slack_event = event_data.get("event", {})

    # Check if the event has text and is not from a bot
    if "text" in slack_event and not "bot_id" in slack_event:

        # Get the user's message from the event data
        slack_message = slack_event["text"]

        # Get the channel ID to send the message to
        slack_channel_id = slack_event["channel"]

        # Check if the current date is July 5th
        if datetime.datetime.now().date() == datetime.date(datetime.datetime.now().year, 7, 5):

            # Generate a response using GPT-3.5
            gpt3_5_response = generate_response(slack_message)

            # Respond to the user's message
            respond_to_message(slack_web_client, slack_channel_id, gpt3_5_response)
```
