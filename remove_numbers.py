import os

def rename_files():
    file_list = os.listdir(r'/home/jeffreysbrother/Desktop/prank/')
    saved_path = os.getcwd()
    os.chdir(r'/home/jeffreysbrother/Desktop/prank/')

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()