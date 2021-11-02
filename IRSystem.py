import os
from os import listdir
from os.path import isfile, isdir, join
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk

from nltk.featstruct import find_variables
from XMLParser import XMLParser
from JSONParser import JSONParser
from VerifyCode import GenerateChecksum
from VerifyCode import GenerateCRC32
from VerifyCode import Comparison
from NLTKParser import CSVJoin, Zipf_distribution, getIndex, edit_distance, Matching, listInit

import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
from MainWindow import Ui_Form

search_pattern = ''

if __name__ == '__main__':

    os.system("")
   
    class MainWindow(QtWidgets.QMainWindow, Ui_Form):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_Form()
            self.ui.setupUi(self)

            self.maxFiles = 25
            self.bStemming = False
            self.bStopwords = True
            self.bPartial = True
            self.bIgnoreCase = False

            # Function Combobox 
            self.ui.func_comboBox.currentIndexChanged.connect(self.comboboxchanged)
            # Amount of files spin control
            self.ui.file_spinBox.valueChanged.connect(self.spinchanged)
            self.ui.file_label.setText('No File')
            # progress bar
            self.ui.file_progressBar.setValue(0)
            self.ui.file_progressBar.setRange(0, self.maxFiles)
            # perform button
            self.ui.perform_pushButton.clicked.connect(self.onPerformClicked)
            # search button
            self.ui.search_pushButton.clicked.connect(self.onSearchClicked)

            # Stemming & Stopwords check box
            self.ui.Stemming_checkBox.clicked.connect(self.onStemmingCheck)
            self.ui.Stopwords_checkBox.clicked.connect(self.onStopwordsCheck)

            # Index table
            self.ui.Index_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.Index_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.Index_tableWidget.verticalHeader().setVisible(False)
            font = self.ui.Index_tableWidget.horizontalHeader().font()
            font.setBold(True)
            self.ui.Index_tableWidget.horizontalHeader().setFont(font)
            self.ui.Index_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Index_tableWidget.horizontalHeader().resizeSection(1,100)
            self.ui.Index_tableWidget.horizontalHeader().resizeSection(2,300)

            # Partial checkbox
            self.ui.Partial_checkBox.clicked.connect(self.onPartialCheck)
            # Ignore case checkbox
            self.ui.IgnoreCase_checkBox.clicked.connect(self.onIgnoreCaseCheck)


            # Matching table
            self.ui.Match_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.Match_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.Match_tableWidget.verticalHeader().setVisible(False)
            font = self.ui.Match_tableWidget.horizontalHeader().font()
            font.setBold(True)
            self.ui.Match_tableWidget.horizontalHeader().setFont(font)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(1,100)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(2,300)

        def onPerformClicked(self):
            self.ui.Index_tableWidget.clearContents()
            self.ui.Index_tableWidget.setRowCount(0)
            self.ui.Index_tableWidget.setColumnCount(3)
            self.ui.Index_tableWidget.setHorizontalHeaderLabels(['Word', 'Document', 'Rows'])
            self.ui.func_comboBox.setCurrentIndex(0)
            self.ui.func_comboBox.setCurrentIndex(2)

        def onSearchClicked(self):
            self.ui.Match_tableWidget.clearContents()
            self.ui.Match_tableWidget.setRowCount(0)
            self.ui.Match_tableWidget.setColumnCount(3)
            self.ui.Match_tableWidget.setHorizontalHeaderLabels(['Word', 'Document', 'Rows'])
            self.ui.func_comboBox.setCurrentIndex(0)
            self.ui.func_comboBox.setCurrentIndex(3)

        def spinchanged(self):
            value = self.ui.file_spinBox.value()
            self.ui.file_progressBar.setRange(1, value)
            self.maxFiles = value

        def onStemmingCheck(self):
            self.bStemming = self.ui.Stemming_checkBox.isChecked()
                
        def onStopwordsCheck(self):
            self.bStopwords = self.ui.Stopwords_checkBox.isChecked()

        def onPartialCheck(self):
            self.bPartial = self.ui.Partial_checkBox.isChecked()
                
        def onIgnoreCaseCheck(self):
            self.bIgnoreCase = self.ui.IgnoreCase_checkBox.isChecked()

        def comboboxchanged(self):
            type = self.ui.func_comboBox.currentIndex()
            if type == 2:
                self.bStemming = self.ui.Stemming_checkBox.isChecked()
                self.bStopwords = self.ui.Stopwords_checkBox.isChecked()
                listInit()

                # Get all files and directories
                path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                files = listdir(path)
                i = 0
                for f in files:
                # Get full path
                    fullpath = join(path, f)
                    if isfile(fullpath):    # Is file ?
                        ext = os.path.splitext(fullpath)[1]
                        if (ext == '.csv'): # only process CSV file
                            # Paramerer 1: file path name
                            # Paramerer 2: stop words
                            # Paramerer 3: stemming flag
                            # Parameter 4: Indexing
                            Zipf_distribution(fullpath, self.bStopwords, self.bStemming, True)  
                            i += 1
                            if i > self.maxFiles:
                                break
                            self.ui.file_label.setText(fullpath)
                            self.ui.file_progressBar.setValue(i)
                        elif isdir(fullpath):   #  Is directory ?
                            print("Folder :", f)
        
                getIndex(self.ui)
            elif type == 3:
                filename = QFileDialog.getOpenFileName(self, 'Select Index file', 'D:\\', 'CSV File(*.CSV);;All files(*)')
                Matching(self.ui, filename[0], self.ui.Match_lineEdit.text(), self.bPartial, self.bIgnoreCase)
            elif type == 4:
                filename = QFileDialog.getOpenFileName(self, 'Select CSV file', 'D:\\', 'CSV File(*.CSV);;All files(*)')
                edit_distance(filename[0])
    

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(window.width(), window.height())
    window.show()
    app.exec_()
    
    """
    type = int(input("1. Information Retrieval\n2. Contents Compare.\n3. Zipf Distribution\n4. Matching\n5. Edit Distance\nPlease select the above of the functions : "))
  
    if (type == 3):
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askdirectory()
        # Get all files and directories
      
        files = listdir(path)
        for f in files:
            # Get full path
            fullpath = join(path, f)
            if isfile(fullpath):    # Is file ?
                ext = os.path.splitext(fullpath)[1]
                if (ext == '.csv'): # only process CSV file
                    # Paramerer 1: file path name
                    # Paramerer 2: stop words
                    # Paramerer 3: stemming flag
                    # Parameter 4: Indexing
                    Zipf_distribution(fullpath, True, False, True)  
            elif isdir(fullpath):   #  Is directory ?
                print("Folder :", f)
        
        getIndex()
    elif (type == 4):
        Matching('d:\\Index_Result.csv', 'COVID-19')
    elif (type == 5):
        edit_distance('d:\\Edit_Dist.csv')
    elif (type == 1):
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
    

    #sys.exit(app.exec())
    """

