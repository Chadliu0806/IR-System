import os
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from XMLParser import XMLParser
from JSONParser import JSONParser
from VerifyCode import GenerateChecksum
from VerifyCode import GenerateCRC32
from VerifyCode import Comparison

search_pattern = ''

if __name__ == '__main__':

    
    type = int(input("1. Information Retrieval\n2. Contents Compare.\nPlease select the above of the functions : "))

    if (type == 1):
        # Step1. Input search string
        app = tk.Tk()
        app.geometry("400x80")

        def getTextInput():
            global search_pattern
            search_pattern = edit.get(1.0, tk.END+"-1c")    # erase \n character
        
        edit=tk.Text(app, height=2)
        edit.pack()
        btnInput=tk.Button(app, height=1, width=20, text="Input search text", command=getTextInput)
        btnInput.pack()
        app.mainloop()
 

        # Step2. Select parser file 
        file_path = filedialog.askopenfilename(initialdir='C:\\Users\\chad.liu\Desktop\\Demo',title = "Select Parse File",
                                            filetypes = (("All","*.XML *.JSON"),("XML files","*.xml"),("JSON files","*.json")))
        
        sz = os.path.splitext(file_path)
        ext = sz[len(sz) - 1]

        print(search_pattern)
        if (ext == '.xml'):
            XMLParser(file_path, search_pattern)
        elif (ext == '.json'):
            JSONParser(file_path, search_pattern)
    elif (type == 2):        

        mode = int(input("1. MD5 Checksum\n2. CRC32.\n3. 1:1 character compare\nPlease select the above of the algorithms : ")) 
    
    
    
        file_path = filedialog.askopenfilename(initialdir='D:\\',title = "Select 1st File for Compare",
                                            filetypes = (("XML files","*.xml"),("All","*.*")))
        
        sz = os.path.splitext(file_path)
        source_name = sz[0] + sz[1]

        file_path = filedialog.askopenfilename(initialdir='D:\\',title = "Select 2nd File for Compare",
                                            filetypes = (("XML files","*.xml"),("All","*.*")))
        sz = os.path.splitext(file_path)
        target_name = sz[0] + sz[1]

        if (mode == 1):
            # Checksum
            checksum1 = GenerateChecksum(XMLParser(source_name, ''))
            checksum2 = GenerateChecksum(XMLParser(target_name, ''))
            if (checksum1 == checksum2):
                print('\nEqual')
            else:
                print('\nDifferent')
        elif (mode == 2):
            # CRC32
            CRC32_1 = GenerateCRC32(XMLParser(source_name, ''))
            CRC32_2 = GenerateCRC32(XMLParser(target_name, ''))
            if (CRC32_1 == CRC32_2):
                print('\nEqual')
            else:
                print('\nDifferent')
        elif (mode == 3):
            # 1:1 Compare
            if (Comparison(XMLParser(source_name, ''), XMLParser(target_name, '')) == True):
                print('\nEqual')
            else:
                print('\nDifferent')
                XMLParser(source_name, '')
                XMLParser(target_name, '')
    
