```python
import unittest
from unittest.mock import patch
from slack_bot import gpt3_5_integration

class TestGpt3_5Integration(unittest.TestCase):

    @patch('slack_bot.gpt3_5_integration.openai')
    def test_generate_response(self, mock_openai):
        # Mock the OpenAI API response
        mock_openai.ChatCompletion.create.return_value = {
            'choices': [{'message': {'content': 'Happy July 5th!'}}]
        }

        # Test the generate_response function
        response = gpt3_5_integration.generate_response('Hello bot')
        self.assertEqual(response, 'Happy July 5th!')

    @patch('slack_bot.gpt3_5_integration.openai')
    def test_generate_response_error(self, mock_openai):
        # Mock the OpenAI API to raise an exception
        mock_openai.ChatCompletion.create.side_effect = Exception('API error')

        # Test the generate_response function with error handling
        with self.assertRaises(Exception):
            gpt3_5_integration.generate_response('Hello bot')

if __name__ == '__main__':
    unittest.main()
```