```python
import openai
from datetime import datetime
from .config import OPENAI_API_KEY, GPT3_5_MODEL_ID

openai.api_key = OPENAI_API_KEY

def generate_response(slack_message):
    if datetime.now().day == 5 and datetime.now().month == 7:
        prompt = f"{slack_message} Can you share a positive July 4th experience and promote America's greatness?"
        response = openai.Completion.create(
            engine=GPT3_5_MODEL_ID,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    else:
        return None
```