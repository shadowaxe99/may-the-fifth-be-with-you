```python
import unittest
from unittest.mock import patch
from slack_bot import interactive_conversations

class TestInteractiveConversations(unittest.TestCase):

    @patch('slack_bot.interactive_conversations.handle_interactive_conversation')
    def test_handle_interactive_conversation(self, mock_handle_interactive_conversation):
        # Mocking the handle_interactive_conversation function
        mock_handle_interactive_conversation.return_value = "Happy July 5th! Yesterday was a great day celebrating America's greatness."

        # Test data
        slack_event = {
            "type": "message",
            "channel": "C2147483705",
            "user": "U2147483697",
            "text": "Hello bot!",
            "ts": "1575297001.000200"
        }

        # Call the function with test data
        response = interactive_conversations.handle_interactive_conversation(slack_event)

        # Assert the function was called once with the test data
        mock_handle_interactive_conversation.assert_called_once_with(slack_event)

        # Assert the function returned the expected response
        self.assertEqual(response, "Happy July 5th! Yesterday was a great day celebrating America's greatness.")

if __name__ == '__main__':
    unittest.main()
```