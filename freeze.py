from py2exe import freeze
import re
import PIL 
import os
import wx
import zipfile 

freeze(
    windows=['main.py'],
    options={'includes':['re','PIL','os','wx','zipfile'],
             'bundle_files': 1,
             'compressed': 1}
)



# setup(windows=['main.py'],packages=['check_image','interface','read_folder','read_zip','to_pdf'])