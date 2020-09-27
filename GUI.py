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

filename = ""
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

    file_location.configure(text="File Opened: "+ filename )
    path = filename

def copyToProject(path):
    # print('Path: {}\nNew path: {}\n'.format( path, os.path.join(pathlib.Path().absolute(), "plate_copies") ))
    # print('END PATH: {}'.format('./' + os.path.join(os.path.basename(path), '')))
    shutil.copy(path, 'plate_copies')
    
    return './' + os.path.basename(path)

def sendPlate(filename):
    copyToProject(filename)
    imgurpush.pushImage(copyToProject(filename))


    
       
# window = tk.ThemedTk() 
# window.get_themes()
# window.set_theme("plastik")

window = Tk()
window['bg']='black'
window.title('AutoLicense')
window.geometry("500x400") 

window.columnconfigure(0, weight=1)   # Set weight to row and 
window.rowconfigure(0, weight=1)

# T1 = tk.Text(window) 
# T1.tag_configure("center", justify='center') 
# T1.insert("1.0", "text") 
# T1.tag_add("center", "1.0", "end") 
# T1.pack()

container = Frame(window, bg='black')   # bg color to show extent
container.grid(row=0, column=0)

myFont = font.Font(size=30)



#File Explorer
file_location = Label(container,  
                      text = "File Explorer using Tkinter",  
                      fg = "blue",
                      anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont', padx=10, pady=10) 
   
       
button_explore = Button(container,  
                        text = "Browse Files", 
                        command= browseFiles,
                        anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont')  
   
button_exit = Button(container,  
                     text = "Exit", 
                     command = exit,
                     anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont')  

button_sendPlate = Button(container,  
                        text = "Send", 
                        command=lambda :sendPlate(filename),
                        anchor = CENTER, highlightbackground = "white", bg='black', foreground='white', font='myFont')  
   
   



file_location.grid(column = 0, row = 0)

   
button_explore.grid(column = 0, row = 1, padx=10, pady=10) 
   
button_exit.grid(column = 0,row = 2, padx=10, pady=10) 

button_sendPlate.grid(column = 0,row = 3, padx=10, pady=10)

   
window.mainloop() 