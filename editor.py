from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


# Defining TextEditor Class
class TextEditor:
    # Defining Constructor
    def __init__(self,root):
        # Assigning root
        self.root = root
        # Title of the window
        self.root.title("TEXT EDITOR")
        # Window Geometry
        self.root.geometry("1200x700+200+150")
        # Initializing filename
        self.filename = None
        # Declaring Title variable
        self.title = StringVar()
        # Declaring Status variable
        self.status = StringVar()
        # Creating Titlebar
        self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        # Packing Titlebar to root window
        self.titlebar.pack(side=TOP,fill=BOTH)
        # Calling Settitle Function
        self.settitle()
        # Creating Statusbar
        self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        # Packing status bar to root window
        self.statusbar.pack(side=BOTTOM,fill=BOTH)
        # Initializing Status
        self.status.set("Welcome To Text Editor")
        # Creating Menubar
        self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
        # Configuring menubar on root window
        self.root.config(menu=self.menubar)
        # Creating File Menu
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # Adding New file Command
        self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
        # Adding Open file Command
        self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
        # Adding Save File Command
        self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
        # Adding Save As file Command
        self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # Creating Edit Menu
        self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # Adding Cut text Command
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        # Adding Seprator
        self.editmenu.add_separator()
        # Adding Undo text Command
        self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        # Creating Help Menu
        self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # Adding About Command
        self.helpmenu.add_command(label="About",command=self.infoabout)
        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root,orient=VERTICAL)
        # Creating Text Area
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
        # Packing scrollbar to root window
        scrol_y.pack(side=RIGHT,fill=Y)
        # Adding Scrollbar to text area
        scrol_y.config(command=self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill=BOTH,expand=1)
        # Calling shortcuts funtion
        self.shortcuts()



# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
