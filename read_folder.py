from os import listdir
from check_image import is_image_extension

def to_raw_str(string:str):
    return fr"{string}"

def get_images(folder:str = "./"):
    images = list()
    for filename in listdir(folder):
        if is_image_extension(filename):
            img = open(f"{folder}\\{filename}","rb")
            images.append(img)
    return images
        


if __name__ == "__main__":
    import to_pdf as a
    testpath = r"C:\Users\gabri\Pictures\Bento\\"
    print(listdir(testpath))

    img = a.sort_images(get_images(testpath))
    a.save_images_to_pdf(img,"bentinho") 
