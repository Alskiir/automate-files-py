import shutil
import sys
from PyQt5 import QtWidgets, QtGui
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from plyer import notification
from pathlib import Path

# Define the paths for the files to watch and their destinations
FOLDER_TO_WATCH = Path("C:/Users/dough/Downloads")
DESTINATIONS = {
    ".unitypackage": {
        "Nardo": "C:/Users/dough/Documents/Unity Packages/Nardo",
        "": "C:/Users/dough/Documents/Unity Packages/",
    },
    ".txt": {
        "word1": "C:/Users/dough/Documents/Text Files/word1",
        "word2": "C:/Users/dough/Documents/Text Files/word2",
    },
}

# Define the path for the icon
ICON_PATH = "icon.png"


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super().__init__(icon, parent)
        menu = QtWidgets.QMenu(parent)
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(sys.exit)
        self.setContextMenu(menu)


class FileHandler(PatternMatchingEventHandler):
    """
    A class that handles file system events, such as file creation,
    and moves files to specified folders based on their extensions and/or names.
    """

    def __init__(self, destinations):
        super().__init__(patterns=["*"], ignore_directories=True)
        self.destinations = destinations

    def on_created(self, event):
        # Check if the event is not a directory (i.e., a file)
        if not event.is_directory:
            # Convert to Path object
            file_path = Path(event.src_path)
            # Convert file name to lowercase
            file_name = file_path.name.lower()
            # Get file extension
            file_extension = file_path.suffix

            # Check if file extension is in destinations dictionary
            if file_extension in self.destinations:
                # Check if file name is empty or contains certain words
                for word, destination in self.destinations[file_extension].items():
                    if not file_name or word.lower() in file_name:
                        self.move_file(file_path, Path(destination))
                        # Stop checking words once a match is found
                        break

    def notifError(
        self, source, destination
    ):  # Display notification if file move fails
        self.notify("File Error", f"Error moving file from {source} to {destination}")

    def notifSuccess(
        self, source, destination
    ):  # Display notification if file move succeeds
        self.notify(
            "File Success", f"Successfully moved file from {source} to {destination}"
        )

    def notify(self, title, message):
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="File Organizer",
                app_icon=ICON_PATH,
            )
        except Exception as e:
            print(f"Error displaying notification: {e}")

    def move_file(self, source, destination):
        try:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            self.notifSuccess(source, destination)
        except Exception as e:
            self.notifError(source, destination)
            print(f"Error moving file: {e}")


def create_observer(event_handler, folder_to_watch):
    """Create and start an Observer."""
    observer = Observer()
    observer.schedule(event_handler, str(folder_to_watch), recursive=False)
    observer.start()
    return observer


def create_tray_icon(icon_path, parent_widget):
    """Create and show a SystemTrayIcon."""
    tray_icon = SystemTrayIcon(QtGui.QIcon(icon_path), parent_widget)
    tray_icon.show()
    return tray_icon


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    tray_icon = create_tray_icon(ICON_PATH, w)

    event_handler = FileHandler(DESTINATIONS)
    observer = create_observer(event_handler, FOLDER_TO_WATCH)

    try:
        sys.exit(app.exec_())
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()