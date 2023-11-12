# File Automation Script

This script automatically moves files from a specified source directory to destination directories based on their file extensions and names. It uses the `watchdog` library to monitor the source directory for changes and the `PyQt5` library to display a system tray icon.

## Requirements

- Python 3
- PyQt5
- watchdog

You can install the required Python libraries with pip:

```bash
pip install PyQt5 watchdog
```

## Usage

By default, the script watches the `C:/Users/dough/Downloads` directory and moves any new `.unitypackage` files to `C:/Users/dough/Documents/Unity Packages` and `.txt` files to `C:/Users/dough/Documents/Text Files`.

Update the `FOLDER_TO_WATCH` and `DESTINATIONS` variables `config.json` to match your source and destination directories.
```bash
"FOLDER_TO_WATCH": "C:/Users/dough/Downloads",
"DESTINATIONS": {
    ".unitypackage": {
        "word": "your/destination/directory/for/unitypackage/files",
       "": "your/destination/directory/for/unitypackagefiles"
    },
    ".txt": {
        "word1": "your/destination/directory/for/text/files",
        "": "your/destination/directory/for/textfiles"
    }
    # Add more file extensions and destinations as needed
}
```

To run the script, use the following command:

```bash
python main.py
```

## Additional Notes

- The script will appear in the `hidden icons` section in the taskbar.
- To close the application, right click the icon and press `Exit`.
- If a destination directory does not exist, the script will create it.