import os
import tkinter as tk
from tkinter import filedialog
from XMLParser import XMLParser
from JSONParser import JSONParser

search_pattern = ''

if __name__ == '__main__':

    # Step1. Input search string
    root = tk.Tk()
    root.geometry("400x80")

    def getTextInput():
        global search_pattern
        search_pattern = edit.get(1.0, tk.END+"-1c")    # erase \n character
       
    edit=tk.Text(root, height=2)
    edit.pack()
    btnInput=tk.Button(root, height=1, width=20, text="Input search text", command=getTextInput)
    btnInput.pack()
    root.mainloop()

    # Step2. Select parser file 
    file_path = filedialog.askopenfilename(initialdir='D:\\',title = "Select Packet Capture File!",
                                           filetypes = (("All","*.XML *.JSON"),("XML files","*.xml"),("JSON files","*.json")))
    
    sz = os.path.splitext(file_path)
    ext = sz[len(sz) - 1]

    print(search_pattern)
    if (ext == '.xml'):
        XMLParser(file_path, search_pattern)
    elif (ext == '.json'):
        JSONParser(file_path, search_pattern)
