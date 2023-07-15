import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


class MLModel:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=1)

    def train_model(self, user_preferences, user_schedule):
        # Convert user_preferences and user_schedule to DataFrame
        user_preferences_df = pd.DataFrame(user_preferences)
        user_schedule_df = pd.DataFrame(user_schedule)

        # Combine the DataFrames
        combined_df = pd.concat(
            [user_preferences_df, user_schedule_df], axis=1)

        # Split the data into training and validation data
        train_X, val_X, train_y, val_y = train_test_split(
            combined_df.drop('appointment', axis=1),
            combined_df['appointment'],
            random_state=1
        )

        # Fit the model with the training data
        self.model.fit(train_X, train_y)

        # Make predictions with the validation data
        val_predictions = self.model.predict(val_X)

        # Print the mean absolute error of the predictions
        print(mean_absolute_error(val_y, val_predictions))

    def generate_schedule(self, user_preferences):
        # Convert user_preferences to DataFrame
        user_preferences_df = pd.DataFrame(user_preferences)

        # Make predictions with the user_preferences
        schedule_predictions = self.model.predict(user_preferences_df)

        return schedule_predictions
