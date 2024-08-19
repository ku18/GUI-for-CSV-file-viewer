#!/usr/bin/env python
# coding: utf-8

# ## Eagle GUI for Machine learning and tensor flow

# In[73]:


#_____________________________________________________________________________________________________________________________#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loading the Libraries~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#_____________________________________________________________________________________________________________________________#

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext 
import csv

# filedialog Module for opening file dialogs that allow users to select files.
# messagebox: Module for displaying message boxes, useful for error or info dialogs.
# scrolledtext: Provides a text widget with a scrollbar.
# csv: Python's module for reading and writing CSV (Comma-Separated Values) files.

import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import numpy as np
import pydot
from sklearn.model_selection import train_test_split

from tkinter import *
from tkinter import messagebox
root = tk.Tk()


# title of the tk inter window
root.title("EAGLE: CSV Viwer")

# root size and bg color
root.geometry("800x400")
root.configure(bg="#2E4053")
#_____________________________________________________________________________________________________________________________#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Loading the data set~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#_____________________________________________________________________________________________________________________________#

#------------------------------------------ Selecting file from local machine ------------------------------------------------#

label1= tk.Label(root, text = 'Click to load csv file', font=("Helvetica", 14), fg="white", bg="#2E4053")
label1.grid(row=0, column=0, padx=10, pady=10)


# Creating a function named open file
# This function will be called when the user clicks the "Open CSV" button.

def open_file(): # Open a file dialog to select a CSV file. 
    
    #filedialog.askopenfilename: Opens a dialog window for selecting a file. It returns the file path of the selected file.
    #filetypes: Specifies the types of files that can be selected. In this case, it allows CSV files and all files.
    #if not file path: Checks if no file was selected (empty filepath). If true, it returns early from the function without doing anything.
    #try: Starts a block of code that might raise an exception, enabling error handling.
    
    filepath = filedialog.askopenfilename( filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    
    
    if not filepath: 
    
        return
    
    # Read the selected CSV file
    
    try:
        with open(filepath, newline='') as csvfile: # Opens the selected file in read mode.
            reader = csv.reader(csvfile) # Reads the CSV file using Python's CSV module.
            
            # Clear the text box Clears all content from the text box. '1.0' means the start of the text, and tk.END means the end of the text.
            text_box_1.delete('1.0', tk.END)
            
            # Display the content of the CSV file
            for row in reader:
                text_box_1.insert(tk.END, ', '.join(row) + '\n')
            #for row in reader:: Loops through each row in the CSV file.
            #text_box.insert(tk.END, ', '.join(row) + '\n'): Inserts each row into the text box. Rows are joined into a single string, separated by commas, and a newline is added.
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

# Create a button to open a file

open_button = tk.Button(root, text="Open CSV", command = open_file, font=("Helvetica", 14, "bold"), bg="#1ABC9C", fg="white", activebackground="#16A085", activeforeground="white", padx=20, pady=10, anchor = 'center')
open_button.grid(row=0, column=1, padx=10, pady=10, sticky = 'nsew')

# Create a scrolled text box to display the CSV content
text_box_1 = scrolledtext.ScrolledText(root, wrap=tk.NONE, height=10, width=80, font=("Courier", 12), bg="#F5F5F5", fg="#2C3E50", padx=10, pady=10, borderwidth=5, relief=tk.GROOVE)
text_box_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
#wrap=tk.NONE: Disables automatic text wrapping, allowing horizontal scrolling.
#borderwidth=5, relief=tk.GROOVE: Sets the border width to 5 pixels and gives it a grooved look.


# Configure grid layout to stretch the text box
root.grid_columnconfigure(1, weight=1)  # Makes column 1 (the column with the text box) expand to fill the available space.
#root.grid_rowconfigure(1, weight=1) # Makes row 1 (the row with the text box) expand to fill the available space.



root.mainloop() ## opens the gui window keeps in a loop until the user closes it

