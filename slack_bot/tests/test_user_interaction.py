```python
import unittest
from unittest.mock import patch
from datetime import datetime
from slack_bot import user_interaction

class TestUserInteraction(unittest.TestCase):

    @patch('slack_bot.user_interaction.datetime')
    def test_should_respond(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime(2022, 7, 5)
        self.assertTrue(user_interaction.should_respond())

        mock_datetime.date.today.return_value = datetime(2022, 7, 4)
        self.assertFalse(user_interaction.should_respond())

    @patch('slack_bot.user_interaction.respond_to_message')
    @patch('slack_bot.user_interaction.generate_response')
    def test_handle_message(self, mock_generate_response, mock_respond_to_message):
        mock_generate_response.return_value = "Happy July 5th!"
        user_interaction.handle_message("Hello bot!", "U12345", "C12345")
        mock_respond_to_message.assert_called_once_with("Happy July 5th!", "C12345")

    @patch('slack_bot.user_interaction.respond_to_message')
    @patch('slack_bot.user_interaction.generate_response')
    def test_handle_message_no_response(self, mock_generate_response, mock_respond_to_message):
        mock_generate_response.return_value = None
        user_interaction.handle_message("Hello bot!", "U12345", "C12345")
        mock_respond_to_message.assert_not_called()

if __name__ == '__main__':
    unittest.main()
```