# -*- coding: utf-8 -*-
import os
import csv
import shutil

workDir = os.path.dirname(os.path.abspath(__file__))
filter_path = os.path.join(workDir, "AV.csv")
folder_in = os.path.join(r"input")


def filter_folders():
    filter = get_filter()
    for dir in os.scandir(folder_in):
        if(dir.name in filter):
            print(f"Exists {dir.name}")
        else:
            shutil.copy(os.path.join(workDir, folder_in, dir.name),
                        os.path.join(workDir, "Filtered", dir.name))
            print(f"Filtered {dir.name}")

def show_folder_files():
    file_path = os.path.join(workDir, "Parts.csv")
    csv = open(file_path, "w", encoding='utf8')
    # csv.write(f"sep=;\nPN;From;To\n")
    extensions = [".pdf",".dxf",".x_t",".step"]
    folders_filter = ["old","arch", "ללקוח", "קודם"]
    parts = get_filter()
    for dirname, dirnames, filenames in os.walk(folder_in):
        # print path to all filenames.
        if any(dir in dirname.lower() for dir in folders_filter ):
            continue

        cDir = dirname.replace(folder_in+'\\', "")
        part_id = extract_first_folder(cDir)
        if(part_id not in parts):
            continue
        for filename in filenames:
            try:
                if any(ext in filename.lower() for ext in extensions ):
                    cFile = os.path.join(dirname, filename)
                    new_file = os.path.join(workDir, "Parts" ,part_id,filename)
                    print(f"{cFile} => {new_file}")
                    csv.write(f"{part_id};{cFile};{new_file}\n")
            except Exception as e:
                # print("Error:"+cDir)
                print(f"Error:{cFile}. {e}")
    csv.close()

def get_filter():
    with open(filter_path, newline='', encoding='utf8') as f:
        reader = csv.reader(f)
        out = list(reader)
    return [item for sublist in out for item in sublist]


def extract_first_folder(text):
    return text.split("\\")[0]


print(f'Program Start in {workDir} folder')
# print('CC0097' in filter)
# print(filter_folders())
show_folder_files()
print(f'Program end.')
