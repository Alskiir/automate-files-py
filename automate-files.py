import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    """
    A class that handles file system events, such as file creation, 
    and moves files to specified folders based on their extensions.
    """
    
    def __init__(self, destinations):
        self.destinations = destinations

    def on_created(self, event):
        # Check if the event is not a directory (i.e., a file)
        if not event.is_directory:
            file_path = event.src_path
            file_extension = os.path.splitext(file_path)[1]
            # Check if the file extension is in the destinations dictionary
            if file_extension in self.destinations:  
                self.move_file(file_path, self.destinations[file_extension])

    def move_file(self, source, destination):
        try:
            # Create the destination folder if it doesn't exist
            os.makedirs(destination, exist_ok=True)  
            # Move the file from the source to the destination folder
            shutil.move(source, destination)
            print(f"Moved file from {source} to {destination}")
        except Exception as e:
            print(f"Error moving file: {e}")

def main(folder_to_watch="C:/Users/dough/Downloads"):
    destinations = {
        ".unitypackage": "C:/Users/dough/Documents/Unity Packages",
        ".txt": "C:/Users/dough/Documents/Text Files",
        # Add more file extensions and destinations as needed
    }
    event_handler = FileHandler(destinations)
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