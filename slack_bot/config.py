```python
import os

# Slack API token
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# GPT-3.5 model id
GPT3_5_MODEL_ID = "text-davinci-003"

# Slack event types to listen for
SLACK_EVENT_TYPES = ["message"]

# Date to respond to messages
RESPONSE_DATE = "07-05"

# Positive July 4th statements
JULY_4TH_STATEMENTS = [
    "What a fantastic July 4th! The fireworks were spectacular.",
    "The spirit of unity on July 4th is a testament to America's strength.",
    "July 4th was a reminder of the freedom and opportunities we enjoy in America."
]

# Messages highlighting America's greatness
AMERICA_GREATNESS_MESSAGES = [
    "America's diversity is its strength. We are a melting pot of cultures, ideas, and dreams.",
    "The freedom and opportunities in America are unparalleled. It's a land of dreams.",
    "America's resilience in the face of challenges is inspiring. We always rise to the occasion."
]
```