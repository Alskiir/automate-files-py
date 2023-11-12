import shutil
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path

from notifications import Notifier


class FileHandler(PatternMatchingEventHandler):
    """
    A class that handles file system events, such as file creation,
    and moves files to specified folders based on their extensions and/or names.
    """

    def __init__(self, destinations):
        super().__init__(patterns=["*"], ignore_directories=True)
        self.destinations = destinations
        self.notifier = Notifier()

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

    def move_file(self, source, destination):
        try:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            print(f"Moved file from {source} to {destination}")
            # self.notifier.notifierSuccess(source, destination)
        except Exception as e:
            # self.notifier.notifierError(source, destination)
            print(f"Error moving file: {e}")
