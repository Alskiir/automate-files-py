# Automated File Handler

This Python script automatically moves `.unitypackage` files from a specified source directory to a destination directory. It uses the `watchdog` library to monitor the source directory for any new files.

## Dependencies

- Python 3
- watchdog

You can install the dependencies with pip:

```bash
pip install watchdog
```

## Usage

By default, the script watches the `C:/Users/dough/Downloads` directory and moves any new `.unitypackage` files to `C:/Users/dough/Documents/Unity Packages`.

You can change these directories by modifying the main function in the script:
```bash
def main(folder_to_watch="your/source/directory"):
    event_handler = FileHandler("your/destination/directory")
    ...
```

To run the script, use the following command:

```bash
python automate-files.py
```

The script will run indefinitely until you stop it with `Ctrl+C`