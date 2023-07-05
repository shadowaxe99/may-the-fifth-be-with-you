```python
import unittest
from unittest.mock import patch
from datetime import datetime
from slack_bot import slack_integration

class TestSlackIntegration(unittest.TestCase):

    @patch('slack_bot.slack_integration.slack_sdk.WebClient')
    def test_respond_to_message(self, mock_slack_client):
        mock_slack_client.chat_postMessage.return_value = True
        result = slack_integration.respond_to_message("test_channel", "test_message")
        self.assertTrue(result)
        mock_slack_client.chat_postMessage.assert_called_with(channel="test_channel", text="test_message")

    @patch('slack_bot.slack_integration.datetime')
    def test_should_respond(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 7, 5)
        self.assertTrue(slack_integration.should_respond())
        mock_datetime.now.return_value = datetime(2022, 7, 4)
        self.assertFalse(slack_integration.should_respond())

    @patch('slack_bot.slack_integration.slack_sdk.WebClient')
    @patch('slack_bot.slack_integration.should_respond')
    def test_handle_slack_event(self, mock_should_respond, mock_slack_client):
        mock_should_respond.return_value = True
        mock_slack_client.chat_postMessage.return_value = True
        test_event = {
            "type": "message",
            "channel": "test_channel",
            "user": "test_user",
            "text": "test_message"
        }
        slack_integration.handle_slack_event(test_event)
        mock_slack_client.chat_postMessage.assert_called_with(channel="test_channel", text="test_message")

if __name__ == '__main__':
    unittest.main()
```