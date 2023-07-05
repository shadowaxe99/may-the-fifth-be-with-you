```python
import datetime
from slack_sdk import WebClient
from .config import SLACK_API_TOKEN, MAX_MESSAGES_PER_MINUTE
from .utils import filter_inappropriate_content

class Limitations:
    def __init__(self):
        self.client = WebClient(token=SLACK_API_TOKEN)
        self.last_response_time = datetime.datetime.now()
        self.message_count = 0

    def check_date(self):
        current_date = datetime.datetime.now().date()
        if current_date.month == 7 and current_date.day == 5:
            return True
        return False

    def check_message_rate(self):
        current_time = datetime.datetime.now()
        if (current_time - self.last_response_time).seconds < 60:
            if self.message_count >= MAX_MESSAGES_PER_MINUTE:
                return False
            else:
                self.message_count += 1
        else:
            self.last_response_time = current_time
            self.message_count = 1
        return True

    def filter_content(self, message):
        return filter_inappropriate_content(message)

    def handle_limitations(self, message):
        if not self.check_date():
            return None
        if not self.check_message_rate():
            return "Sorry, I'm a bit overloaded at the moment. Please try again later."
        filtered_message = self.filter_content(message)
        if filtered_message is None:
            return "Sorry, your message contained inappropriate content."
        return filtered_message
```