from plyer import notification
import json


class Notifier:
    def __init__(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)

    def notifierError(self, source, destination):
        # Display notification if file move fails
        self.notify(
            "File Error", f"Error moving file from {source} to {destination}"
            )

    def notifierSuccess(self, source, destination):
        # Display notification if file move succeeds
        self.notify(
            "File Success", f"Successfully moved file from {source} to {destination}"
        )

    def notify(self, title, message):
        ICON_PATH = self.config["ICON_PATH"]

        try:
            notification.notify(
                title=title,
                message=message,
                app_name="File Organizer",
                app_icon=ICON_PATH,
            )
        except Exception as e:
            print(f"Error displaying notification: {e}")