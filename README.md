Temporary Files Cleanup Script
A simple Python script for deleting temporary files from specified directories. This script helps to free up disk space by removing temporary files with extensions like .tmp, .temp, .log, and .cache.

FEATURES
*Deletes temporary files in specified directories
*Supports multiple directories as input
*Logs deleted files for easy tracking
REQUIREMENTS
Python 3.x

INSTALLATION:
1.Clone the repository or download the script directly: git clone https://github.com/DmytriVasylenko959/temp-file-cleanup.git
2.Navigate to the directory:cd temp-file-cleanup

USAGE
1.Run the script: python delete_temp_files.py
2.Enter the paths of the directories you want to clean, separated by commas:Enter paths to folders (comma-separated): /path/to/folder1, /path/to/folder2
The script will scan the specified directories and delete any files with the .tmp, .temp, .log, or .cache extensions. It will print the paths of deleted files to the console.

example:python delete_temp_files.py
Output:Enter paths to folders (comma-separated): /Users/YourName/Temp, /Users/YourName/Downloads
Checking directory: /Users/YourName/Temp
Deleted file: /Users/YourName/Temp/sample.tmp
Deleted file: /Users/YourName/Temp/old.cache
Directory not found: /Users/YourName/Downloads

CUSTOMIZATION
You can modify the list of extensions for temporary files in the script by editing the temp_extensions list: temp_extensions = ['.tmp', '.temp', '.log', '.cache']
Add or remove file extensions as needed.

This README provides a clear overview and example usage to make your project user-friendly on GitHub. Let me know if you'd like to add anything specific!
