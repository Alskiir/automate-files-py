# Automated File Handler

This Python script automatically moves files from a specified source directory to different destination directories based on their file extensions. It uses the `watchdog` library to monitor the source directory for any new files.

## Dependencies

- Python 3
- watchdog

You can install the dependencies with pip:

```bash
pip install watchdog
```

## Usage

By default, the script watches the `C:/Users/dough/Downloads` directory and moves any new `.unitypackage` files to `C:/Users/dough/Documents/Unity Packages` and `.txt` files to `C:/Users/dough/Documents/Text Files`.

You can change these directories by modifying the main function in the script:
```bash
destinations = {
    ".unitypackage": "your/destination/directory/for/unitypackage/files",
    ".txt": "your/destination/directory/for/txt/files",
    # Add more file extensions and destinations as needed
}
```

To run the script, use the following command:

```bash
python automate-files.py
```

## Additional Notes

- The script will run indefinitely until you stop it with `Ctrl+C`.
- If a destination directory does not exist, the script will create it.