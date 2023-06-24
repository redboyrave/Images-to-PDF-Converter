import wx

class app_frame(wx.Frame):

    components = list()

    def __init__(self, *args, **kw):
        super(app_frame,self).__init__(*args, **kw)

        #background panel, all the interface is parented to it
        bkg = wx.Panel(self)

        #No resizing!! Bad User!!
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        self.setup_interface(bkg)

        self.Show()
    
        '''
        #Interface should look kinda like this
        ____________________________________
        |FILE__HELP_________________________|
        |radial (zip or folder)             |
        |textbox(for input)         | button|  horizontal sizer w/2 vertical sizers?
        |___________________________________|
        |                                   |
        |textbox for name       |label(.pdf)|  horizontal sizer w/2 vertical sizers
        |___________________________________|
        |                                   |
        |textbox(for output)        |button||  horizontal sizer w/2 vertical sizers
        |___________________________________|
        |___________________________|button||
        '''
        

    def setup_interface(self,parent):
        hboxes = list()
        for i in range(0,5):
            hbox = wx.BoxSizer(orient= wx.HORIZONTAL)
            hboxes.append(hbox)
        #1
        rad = wx.RadioBox(parent, choices=["zip","folder"]) 
        #2
        file_label = wx.StaticText(parent,label="File: ")
        file_text = wx.TextCtrl(parent,value="") 
        file_button = wx.Button(parent,label="...") 
        #3
        name_label = wx.StaticText(parent,label="PDF Name: ")
        name_text =wx.TextCtrl(parent,value="") 
        name_format = wx.StaticText(parent,label=".pdf")
        #4
        out_label = wx.StaticText(parent,label="Save to: ")
        out_text = wx.TextCtrl(parent,value="") 
        out_button = wx.Button(parent,label="...")
        #5
        info_text1 = wx.StaticText(parent,label="Empty boxes")
        info_text2 = wx.StaticText(parent,label="will default to input file/folder")
        convert_button = wx.Button(parent,label="Start")


        gbox = wx.FlexGridSizer(rows=5,cols=3,vgap=5,hgap=5)
        # gbox = wx.GridBagSizer(rows = 5, collumns = )

        #first hbox choice is a radio box with two options
        gbox.Add(0,0,flag = wx.EXPAND)
        gbox.Add(rad,flag=wx.ALIGN_CENTER)
        gbox.Add(0,0,flag = wx.EXPAND)
        
        #second hbox is a textbox with a button on the side
        gbox.Add(file_label,flag=wx.ALIGN_RIGHT)
        gbox.Add(file_text,proportion=1,flag=wx.EXPAND)
        gbox.Add(file_button, flag=wx.ALIGN_LEFT)
        
        #third box is a text bos with the file name + a label written ".pdf"
        gbox.Add(name_label,flag=wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM)
        gbox.Add(name_text,proportion=1,flag=wx.EXPAND)
        gbox.Add(name_format, flag=wx.ALIGN_LEFT)

        #Fourth box is textbox with a button on the side
        gbox.Add(out_label,flag=wx.ALIGN_RIGHT)
        gbox.Add(out_text,proportion=1,flag=wx.EXPAND)
        gbox.Add(out_button,flag=wx.ALIGN_LEFT)

        #Fifth Box is a button to save
        gbox.Add(info_text1,0,flag = wx.ALIGN_RIGHT)
        gbox.Add(info_text2,0,flag = wx.EXPAND)
        gbox.Add(convert_button)


        gbox.AddGrowableCol(1,1)
        
        
        vbox = wx.BoxSizer(orient= wx.VERTICAL )
        vbox.Add(gbox,border=10,flag= wx.ALL & ~(wx.TOP)| wx.EXPAND)

        parent.SetSizer(vbox)
        #                   0 ,    1    ,    2      ,    3    ,    4   ,     5    ,      6
        self.components = [rad,file_text,file_button,name_text,out_text,out_button,convert_button]
        


    def create_file_box(self,message):
        out = wx.FileDialog(self,message=message,wildcard="*.zip")
        return out

    def create_folder_box(self,message:str):
        out = wx.DirDialog(self,message=message)
        return out

    def show_picker(event,dialog_box:wx.FileDialog | wx.DirDialog) -> str:
        pick = dialog_box.ShowModal()
        if pick== wx.ID_OK:
                return dialog_box.GetPath()
        else:
            return ""




#standalone test
'''
if __name__ == "__main__":

    app = wx.App(clearSigInt= True)
    frame = app_frame(None, title = 'ZIP/Folder to PDF Converter-Inator 9000',size = (410,220))

    f_box = frame.create_file_box("Pick the Zip File")
    fol_box = frame.create_folder_box("Pick the Folder with the images")
    save_box = frame.create_folder_box("Pick a Folder to Save to")

    app.MainLoop()
    # update()
    '''