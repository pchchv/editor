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
