import zipfile
import os
import subprocess
import sys

def create_modules_zip(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


if __name__ == "__main__":
    create_modules_zip('', 'archive_student.zip')
    subprocess.run([sys.executable, 'archive_student.zip'])