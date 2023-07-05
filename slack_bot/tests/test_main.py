```python
import unittest
from unittest.mock import patch
from datetime import datetime
from slack_bot import main

class TestMain(unittest.TestCase):

    @patch('slack_bot.main.datetime')
    def test_main_on_july_5th(self, mock_datetime):
        mock_datetime.datetime.now.return_value = datetime(2022, 7, 5)
        with patch('slack_bot.main.respond_to_message') as mock_respond:
            main.main()
            self.assertTrue(mock_respond.called)

    @patch('slack_bot.main.datetime')
    def test_main_not_on_july_5th(self, mock_datetime):
        mock_datetime.datetime.now.return_value = datetime(2022, 7, 6)
        with patch('slack_bot.main.respond_to_message') as mock_respond:
            main.main()
            self.assertFalse(mock_respond.called)

if __name__ == '__main__':
    unittest.main()
```