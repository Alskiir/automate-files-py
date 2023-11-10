import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    """
    A class that handles file system events, such as file creation, and moves .unitypackage files to a specified folder.
    """
    def __init__(self, destination_folder):
        self.destination_folder = destination_folder

    def on_created(self, event):
        if not event.is_directory:  # Check if the event is not a directory (i.e., a file)
            file_path = event.src_path
            if file_path.endswith(".unitypackage"):  # Search for .unitypackage files
                self.move_file(file_path, self.destination_folder)

    # Move the file from the source to the destination folder
    def move_file(self, source):
        try:
            shutil.move(source, self.destination_folder)
            print(f"Moved file from {source} to {self.destination_folder}")
        except Exception as e:
            print(f"Error moving file: {e}")

def main(folder_to_watch="C:/Users/dough/Downloads"):
    event_handler = FileHandler("C:/Users/dough/Documents/Unity Packages")
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()

    try:
        # Run the observer loop indefinitely
        while True:  
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if the user interrupts the script
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()