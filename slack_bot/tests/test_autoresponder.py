```python
import unittest
from unittest.mock import patch
from datetime import datetime
from slack_bot import autoresponder, config

class TestAutoresponder(unittest.TestCase):

    @patch('slack_bot.autoresponder.datetime')
    def test_respond_on_july_5th(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 7, 5)
        self.assertTrue(autoresponder.should_respond())

    @patch('slack_bot.autoresponder.datetime')
    def test_no_respond_on_other_days(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 7, 6)
        self.assertFalse(autoresponder.should_respond())

    @patch('slack_bot.autoresponder.generate_response')
    def test_generate_positive_response(self, mock_generate_response):
        mock_generate_response.return_value = "Happy July 4th! America is great!"
        response = autoresponder.generate_response("How was your July 4th?")
        self.assertIn("Happy July 4th", response)
        self.assertIn("America is great", response)

    @patch('slack_bot.autoresponder.respond_to_message')
    def test_respond_to_message(self, mock_respond_to_message):
        mock_respond_to_message.return_value = True
        response = autoresponder.respond_to_message("slack_channel_id", "slack_message")
        self.assertTrue(response)

    @patch('slack_bot.autoresponder.customize_response')
    def test_customize_response(self, mock_customize_response):
        mock_customize_response.return_value = "Customized response"
        response = autoresponder.customize_response("slack_message", "slack_user_id")
        self.assertEqual(response, "Customized response")

if __name__ == '__main__':
    unittest.main()
```