import json
import sys
from pathlib import Path
from PyQt5 import QtWidgets, QtGui
from watchdog.observers import Observer

from system_tray_icon import SystemTrayIcon
from file_handler import FileHandler


def main():
    # Load configuration from JSON file
    with open("config.json", "r") as f:
        config = json.load(f)

    folder_to_watch = Path(config["FOLDER_TO_WATCH"])
    destinations = config["DESTINATIONS"]
    ICON_PATH = config["ICON_PATH"]

    app = QtWidgets.QApplication(sys.argv)

    # Create the system tray icon
    tray_icon = SystemTrayIcon(QtGui.QIcon(ICON_PATH))
    tray_icon.show()

    event_handler = FileHandler(destinations)
    observer = Observer()
    observer.schedule(event_handler, str(folder_to_watch), recursive=False)
    observer.start()

    try:
        sys.exit(app.exec_())
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()