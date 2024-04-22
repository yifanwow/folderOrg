import os
import shutil


def copy_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through all the directories and files in the input folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            # Get the full path of the current file
            file_path = os.path.join(root, file)

            # Copy the file to the output folder
            shutil.copy2(file_path, output_folder)
            print(f"Copied {file_path} to {output_folder}")


if __name__ == "__main__":
    # Get input and output folder paths from user
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")

    # Copy files
    copy_files(input_folder, output_folder)
