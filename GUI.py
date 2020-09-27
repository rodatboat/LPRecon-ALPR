from tkinter import *
from tkinter import filedialog 
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

import shutil
import imgurpush
import os
import pathlib
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from imgurpush import license_plate_number as license_plate_number

license_image = None
filename = ""
image_path = None


       
# window = tk.ThemedTk() 
# window.get_themes()
# window.set_theme("plastik")
window = Tk()
def center_window(w=500, h=400):
    global window
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


window['bg']='black'
window.title('AutoLicense')
center_window(500, 400)

def browseFiles(): 
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("JPEG", 
                                                        "*.jpg*"),
                                                        ("PNG",
                                                        "*.png"),
                                                       ("all files", 
                                                        "*.*"))) 

    file_location.configure(text="File Opened: "+ os.path.basename(filename) )
    path = filename

def copyToProject(path):
    # print('Path: {}\nNew path: {}\n'.format( path, os.path.join(pathlib.Path().absolute(), "plate_copies") ))
    # print('END PATH: {}'.format('./' + os.path.join(os.path.basename(path), '')))
    shutil.copy(path, 'plate_copies')
    
    return os.path.basename(path)

def sendPlate(filename):
    global image_path
    global license_plate_number
    copyToProject(filename)
    path = copyToProject(filename)
    image_path = path
    
    imgurpush.pushImage(path)
    license_plate_number_label.config(text=license_plate_number)
    
    

def refresh(self):
    self.destroy()
    self.__init__()


# def viewImage():
#     global license_image
    
#     license_image = ImageTk.PhotoImage((Image.open(f'.\plate_copies\{image_path}')))
#     picture_preview.configure(image=license_image)
#     picture_preview.image = license_image



image = Image.open('background.png')

photo_image = ImageTk.PhotoImage(image)
plus_image = ImageTk.PhotoImage(Image.open('plus.png'))


window.columnconfigure(0, weight=1)   # Set weight to row and 
window.rowconfigure(0, weight=1)

# T1 = tk.Text(window) 
# T1.tag_configure("center", justify='center') 
# T1.insert("1.0", "text") 
# T1.tag_add("center", "1.0", "end") 
# T1.pack()

# container = Frame(window, bg='black')   # bg color to show extent
# container.pack()

myFont = font.Font(size=30)

background_label = Label(window, image=photo_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#File Explorer
file_location = Label(window,  
                      text = "Look up license picture!",  
                      fg = "blue",
                      anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont', padx=10, pady=20) 
   
       
button_explore = Button(window,  
                        text = "Browse Files", 
                        command= browseFiles,
                        anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont', image=plus_image)  
   

button_sendPlate = Button(window,  
                        text = "Send", 
                        command=lambda :sendPlate(filename),
                        anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont')  


license_plate_number_label = Label(window,
                        text="",
                        foreground='white',
                        bg='black',
                        font='myFont'
                        )

   



file_location.place(x=120, y=135)

   
button_explore.place(x=320, y=144)
   


button_sendPlate.place(x=258, y=210)


   
window.mainloop() 