from os import path as ospath
import interface as gui
import read_folder as rf
import read_zip as rz
import to_pdf

_in_file_path:str = str()
_in_folder_path:str = str()

def on_radiobox(event):
    global _in_file_path
    global _in_folder_path
    evtobj = event.GetEventObject()
    assert evtobj == frame.components[0]

    if evtobj.GetSelection():
        _in_folder_path = frame.components[1].GetValue() 
        frame.components[1].SetValue(_in_file_path)
    else:
        in_file_path = frame.components[1].GetValue()
        frame.components[1].SetValue(_in_folder_path)
        

def on_button(event):
    #Only way I managed to this to work
    evtobj = event.GetEventObject()
    if evtobj == frame.components[2]:
        path = zip_folder_switcher()
        frame.components[1].SetValue(path)
        
        return
    if evtobj == frame.components[5]:
        npath = frame.show_picker(save_box)
        if npath != "":
            path = npath
            frame.components[4].SetValue(path)
        
        return
    if evtobj == frame.components[6]:
        #DO convertion stuffs
        convert()
        return

def get_dir_path(path:str):
    folder = f'{ospath.dirname(path)}\\'
    print(folder)
    return folder

def zip_folder_switcher():
    choice = frame.components[0].GetSelection()
    path = frame.components[1].GetValue()
    if choice:
        npath = frame.show_picker(fol_box)
        if npath != "":
            path = npath
    else:
       npath = frame.show_picker(f_box)
       if npath != "":
        path = npath
    return path

def convert():
    zip_folder:int = frame.components[0].GetSelection()
    inpath:str= frame.components[1].GetValue()
    outpath:str= frame.components[4].GetValue()
    filename:str = frame.components[3].GetValue()

    if inpath == "":
        raise Exception("No File Selected")
        
    
    imgs= list()
    if zip_folder:
        imgs = rf.get_images(inpath)
        if len(imgs) == 0:
            raise Exception("Folder has no images")
    else:
        zip = rz.read_zip_file(inpath)
        imgs = rz.get_images(zip)
        if len(imgs) == 0:
            raise Exception("ZipFile has no images")
    
    imgs = to_pdf.sort_images(imgs)
    

    if filename == "":
        if zip_folder:
            filename = "output"
        else:
            filename = ospath.basename(ospath.splitext(inpath)[0])

    if outpath == "":
        if zip_folder:
            outpath = f'{inpath}\\'
        else:
            outpath = get_dir_path(inpath)
    else:
        outpath = f'{outpath}\\'
    
    counter:int = 0

    while ospath.isfile(outpath+filename+'.pdf'):
        counter+=1
        filename= filename.rpartition('_',)[0]
        filename = f'{filename}_{counter:03}'
    
    to_pdf.save_images_to_pdf(imgs,file_name=filename,path=outpath)



if __name__ == "__main__":

    app = gui.wx.App()
    frame = gui.app_frame(None, title = 'ZIP/Folder to PDF Converter-Inator 9000',size = (410,220))


    f_box = frame.create_file_box("Pick the Zip File")
    fol_box = frame.create_folder_box("Pick the Folder with the images")
    save_box = frame.create_folder_box("Pick a Folder to Save to")

    frame.components[0].Bind(gui.wx.EVT_RADIOBOX,on_radiobox)
    frame.components[2].Bind(gui.wx.EVT_BUTTON,on_button)
    frame.components[5].Bind(gui.wx.EVT_BUTTON,on_button)
    frame.components[6].Bind(gui.wx.EVT_BUTTON,on_button)

    app.MainLoop()
