import os
from datetime import datetime


def files_scan_1(path):
    data = os.listdir(path)
    for file in data:
        a = file
    #     if os.path.isfile(os.path.join(path, file)):
    #         yield file


def files_scan_2(path):
    data = os.scandir(path)
    with data as listOfEntries:
        for entry in listOfEntries:
            if not entry.is_file():
                print(entry.name)


files_scan_2("/home/kretowicz/Projects/learnPython/scanner/abcd")
