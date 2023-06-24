import re #regular expressions
from PIL import Image



def sort_images(images:list):
    #local assist functions
    def is_int(string):
        if string.isdecimal():
            i = int(string)
            return i
        else:
            return string

    def human_sorting(file): #local function
        try:
            name = str(file.name) #from the zip file 
        except AttributeError:
            name = str(file)    #from folder
        
        bits = re.split("([0-9]+)", name)
        result = list()
        for bit in bits:
            if bit == '':
                continue
            result.append(is_int(bit))
        return result 
    #sort
    images.sort(key = human_sorting)

    return images #File-like objects from zip exporter


def save_images_to_pdf(imgs:list, file_name:str = "output", path:str = "./"):
    open_files = list()
    for img in imgs:
        i = Image.open(img)
        open_files.append(i)
    
    # print(path+file_name+".pdf")
    open_files[0].save((path+file_name+'.pdf'),save_all= True, append_images = open_files[1:] )
    print(f"Files have been converted to PDF and are saved on {path} as {file_name}.pdf")

'''
if __name__ == "__main__":
        #debugging#
    ###--from files--### will not be needed in final implementation
    import read_zip
    import read_folder

    file = read_zip.read_zip_file("./test_file.zip") #read the file, return list of files in the zip
    imgs = read_zip.get_images(file) #read the file list, returns the images inside
    imgs = sort_images(imgs)
    save_images_to_pdf(imgs) #saves to pdf, receives the img list, a name and where to save it
'''