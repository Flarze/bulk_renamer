# rename filename stem and leave extension untouched
# duplicate handleing
# handle empty strings and invalid filename characters
# Recursive descending into subfolders


import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("folder", type=Path)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--extension")
group.add_argument("--pattern")
parser.add_argument("--replacement", required=True)
parser.add_argument("--recursive", action="store_true")


parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
path = args.folder


def search_folder(folder: Path):
    for file in folder.iterdir():
        if file.is_file() and args.extension:
            print(file.stem + file.suffix)
        elif file.is_dir() and args.recursive:
            search_folder(file)


def replace():
    pass


def main():
    # check every file in folder
    search_folder(path)
    # if recursive check every file in folders in folder

    # check if pattern or extension
    # if pattern replace based on regex
    # if extension replace based on extension

    #


if __name__ == "__main__":
    main()
