This is a file renamer python script that renames files in a specified folder based on a specific naming convention. It extracts information such as date and name from the original file names and creates a new standardized file name.

## Features

- Supports renaming files with date and name information.
- Converts both abbreviated and full month names to the numeric format.
- Creates a new folder ("Renamed Folder") inside the specified folder and copies the renamed files into it.

## Usage

1. Run the script by executing the `FileRenamer.py` file.
2. A file dialog will appear, prompting you to select the folder containing the files you want to rename.
3. The script will create a new folder named "Renamed Folder" inside the selected folder and copy the renamed files into it.

## Example

Original file name: `21 Feb 2019 - Shihab Hashib.xlsx`

Renamed file name: `21-02-2019-Shihab-Hashib.xlsx`

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python installations)

## How to Run

1. Install Python from [python.org](https://www.python.org/).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script with the command: `python FileRenamer.py`

## License

This project is licensed under the MIT License.
