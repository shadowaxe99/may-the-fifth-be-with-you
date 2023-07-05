```python
import datetime
from slack_bot import slack_integration, gpt3_5_integration, customization, user_interaction

def main():
    # Check if today's date is July 5th
    if datetime.datetime.now().date() != datetime.date(datetime.datetime.now().year, 7, 5):
        print("Today is not July 5th. The bot will not respond to messages.")
        return

    # Initialize Slack and GPT-3.5 integration
    slack_client = slack_integration.initialize_slack_client()
    gpt3_5_client = gpt3_5_integration.initialize_gpt3_5_client()

    # Listen for Slack messages
    slack_integration.listen_for_messages(slack_client, handle_message)

def handle_message(slack_message):
    # Generate a response using GPT-3.5
    gpt3_5_response = gpt3_5_integration.generate_response(gpt3_5_client, slack_message)

    # Customize the response based on user preferences
    customized_response = customization.customize_response(gpt3_5_response, slack_message)

    # Respond to the Slack message
    user_interaction.respond_to_message(slack_client, slack_message, customized_response)

if __name__ == "__main__":
    main()
```