import os
import zipfile
from gooey import Gooey, GooeyParser


@Gooey(program_description="File Extension And Compression Automator",program_name="File Automation")
def main():
    parser = GooeyParser()
    parser.add_argument("file_path",metavar="Folder Path",help="Enter Folder Path")
    parser.add_argument("zip_filename",metavar="Zip File Name",help="Enter Zip File Name")

    args = parser.parse_args()
    folder_path = args.file_path
    zip_filename = args.zip_filename

    change_extension(folder_path)
    compress_csv_files(folder_path,zip_filename)

def change_extension(folder_path:str) ->None:
    old_extension = ".txt"
    new_extension = ".csv"
    if not os.path.isdir(fr"{folder_path}"):
        raise ValueError(f"The specified path {folder_path} is not a directory or does not exist.")

    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            old_file = os.path.join(folder_path, filename)
            new_filename = filename[:-len(old_extension)] + new_extension
            new_file = os.path.join(folder_path, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")


def compress_csv_files(folder_path:str,zip_filename:str) ->None:
    filename = f"{zip_filename}.zip"
    if not os.path.isdir(folder_path):
        raise ValueError(f"The specified path {folder_path} is not a directory or does not exist.")
    zip_filepath = os.path.join(folder_path, filename)
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                zipf.write(file_path, os.path.basename(file_path))
                print(f"Compressed: {file_path}")

    print(f"All CSV files are compressed into {zip_filepath}")

main()