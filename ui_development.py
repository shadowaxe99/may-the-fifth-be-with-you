import tkinter as tk
from tkinter import messagebox
from src import ai_agent


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Agent Scheduler")
        self.root.geometry("500x500")

        self.schedule_view = tk.Label(self.root, text="Schedule View")
        self.schedule_view.pack()

        self.appointment_form = tk.Entry(self.root)
        self.appointment_form.pack()

        self.preferences_form = tk.Entry(self.root)
        self.preferences_form.pack()

        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        user_input = self.appointment_form.get()
        preferences = self.preferences_form.get()

        parsed_input = ai_agent.parse_user_input(user_input)
        ai_agent.select_features(preferences)

        ai_agent.generate_schedule(parsed_input)
        ai_agent.sync_calendar()

        self.update_UI()

    def update_UI(self):
        schedule = ai_agent.user_schedule
        self.schedule_view.config(text=schedule)

        messagebox.showinfo("Update", "Schedule updated successfully")


if __name__ == "__main__":
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()
