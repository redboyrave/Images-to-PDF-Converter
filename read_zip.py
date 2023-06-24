from zipfile import ZipFile as zip
from check_image import is_image_extension

def read_zip_file(file_path:str):
    file = zip(file_path,'r')
    return file



def get_images(file):
    file_names = zip.namelist(file) #gets the name of all the files in the zip
    images = list()

    for file_name in file_names:
        current = zip.open(file,file_name,"r")
        if is_image_extension(current.name):
            images.append(current)
    return images