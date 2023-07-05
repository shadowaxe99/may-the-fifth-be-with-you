```python
import json

class UserPreferences:
    def __init__(self):
        self.preferences = {}

    def load_preferences(self, file_path="user_preferences.json"):
        try:
            with open(file_path, "r") as file:
                self.preferences = json.load(file)
        except FileNotFoundError:
            self.preferences = {}

    def save_preferences(self, file_path="user_preferences.json"):
        with open(file_path, "w") as file:
            json.dump(self.preferences, file)

    def set_user_preference(self, user_id, preference_key, preference_value):
        if user_id not in self.preferences:
            self.preferences[user_id] = {}
        self.preferences[user_id][preference_key] = preference_value
        self.save_preferences()

    def get_user_preference(self, user_id, preference_key):
        return self.preferences.get(user_id, {}).get(preference_key, None)

user_preferences = UserPreferences()
user_preferences.load_preferences()
```
