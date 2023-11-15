import os
import shutil
import re
from tkinter import Tk, filedialog


def renameFile(filePath):
    # Using regular expression to get date
    match = re.match(
        r"(\d{1,2}\s\w+(\s\w+)?\s\d{4})\s-\s(.+)\.(\w+)", filePath)

    if match:
        date_str, _, name, ext = match.groups()

        # Name Jan to January if your format is like that.
        months = {
            'Jan': '01', 'Feb': '02',
            'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06',
            'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10',
            'Nov': '11', 'Dec': '12'
        }
        for month_name, month_num in months.items():
            date_str = date_str.replace(month_name, month_num)

        formatted_date = '-'.join(date_str.split())

        new_file_name = f"{formatted_date}-{name.replace(' ', '-').replace('.', '')}.{ext}"

        return new_file_name
    else:
        return None


def renameFilesInFolder(inputFolder, outputFolder):
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    for filename in os.listdir(inputFolder):
        filePath = os.path.join(inputFolder, filename)

        if os.path.isfile(filePath):
            newFilename = renameFile(filename)

            if newFilename:
                new_filePath = os.path.join(outputFolder, newFilename)
                shutil.copy(filePath, new_filePath)
                print(f"Renamed and copied: {filename} to {newFilename}")


def select_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder")
    return folder_selected


if __name__ == "__main__":
    inputFolder = select_folder()

    # Make an folder inside the selected folder
    outputFolder = os.path.join(inputFolder, "Renamed Folder")

    # Rename files and copy them to the output folder
    renameFilesInFolder(inputFolder, outputFolder)
