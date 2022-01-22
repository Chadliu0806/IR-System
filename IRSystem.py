import os
from os import listdir
from os.path import isfile, isdir, join

from XMLParser import XMLParser
from JSONParser import JSONParser
from VerifyCode import GenerateChecksum
from VerifyCode import GenerateCRC32
from VerifyCode import Comparison
from NLTKParser import CBOW_model, Skipgram_model, TFIDF_Weight, edit_distance, Matching
from NLTKParser import Zipf, getQuery, getPattern, OpenTFIDFDocument, OpenInfoDocument, InitTFIDFTable, InitIndexTable, InitInfoTable
import re

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *


import pandas as pd 
import seaborn as sns
from sklearn.decomposition import PCA

import sys
import matplotlib.pyplot as plt

from MainWindow import Ui_Form
from sklearn.model_selection import train_test_split

search_pattern = ''

if __name__ == '__main__':

    os.system("")
    
    class MainWindow(QtWidgets.QMainWindow, Ui_Form):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_Form()
            self.ui.setupUi(self)
          

            self.maxFiles = 2000
            self.bStemming = False
            self.bStopwords = True
            self.bTFIDF = False
            self.TFIDFMethod = 0

            # function tab
            self.ui.tabWidget.setCurrentIndex(0)
            #self.ui.tabWidget.currentChanged['int'].connect(self.onTabChanged)

            # Word2Vect tab
            self.ui.Word2Vect_tabWidget.setCurrentIndex(0)
            self.ui.Word2Vect_tabWidget.currentChanged['int'].connect(self.onWord2VectChanged)
            
            # Amount of files spin control
            self.ui.file_spinBox.setValue(2000)
            self.maxFiles = 2000
            self.ui.file_spinBox.valueChanged.connect(self.spinchanged)
           
            # progress bar
            self.ui.file_progressBar.setValue(0)
            self.ui.file_progressBar.setRange(0, self.maxFiles)
            # Load button
            self.ui.Load_pushButton.clicked.connect(self.onLoadClicked)
            
            # Stemming & Stopwords check box
            self.ui.Stemming_checkBox.clicked.connect(self.onStemmingCheck)
            self.ui.Stopwords_checkBox.clicked.connect(self.onStopwordsCheck)
            
            # TF-IDF check box
            self.ui.TFIDF_checkBox.clicked.connect(self.onTFIDFCheck)

            # Index table
            self.ui.Index_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.Index_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.Index_tableWidget.verticalHeader().setVisible(False)
            font = self.ui.Index_tableWidget.horizontalHeader().font()
            font.setBold(True)
            self.ui.Index_tableWidget.horizontalHeader().setFont(font)
            self.ui.Index_tableWidget.horizontalHeader().resizeSection(0,120)

                      
            # CBOW & Skig-gram tabel widget
            self.ui.CBOW_tableWidget.horizontalHeader().setFont(font)
            self.ui.CBOW_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.CBOW_tableWidget.horizontalHeader().resizeSection(1,150)

            self.ui.Skipgram_tableWidget.horizontalHeader().setFont(font)
            self.ui.Skipgram_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Skipgram_tableWidget.horizontalHeader().resizeSection(1,150)
            
            self.ui.TFIDF_tableWidget.horizontalHeader().setFont(font)
            self.ui.TFIDF_tableWidget.horizontalHeader().resizeSection(0, 100)
            for col in range(50):
                self.ui.TFIDF_tableWidget.horizontalHeader().resizeSection(col+1, 60)
            
            self.ui.TrainCBOWModel_comBox.clear()
            curr_path = os.getcwd()
            for file in os.listdir(curr_path):
                if file.endswith('.cbow'):
                    self.ui.TrainCBOWModel_comBox.addItem(file)

            # training data button browser
            self.ui.Traindata_Button.clicked.connect(self.onTrainDataClicked) 

            # CBOW algorithm Compute push button
            self.ui.CBOWCompute_Button.clicked.connect(self.onCBOWComputeClicked) 
            # Skip-gram algorithm Compute push button
            self.ui.SkipgramCompute_Button.clicked.connect(self.onSkipgramComputeClicked) 
            
            # TFIDF Interface
            self.ui.TFIDF_Doc_comboBox.currentIndexChanged.connect(self.TFIDFDoccomboboxchanged)
            self.ui.TFIDF_Method_comboBox.currentIndexChanged.connect(self.TFIDFMethodcomboboxchanged)
            self.ui.TFIDFCompute_Button.clicked.connect(self.onTFIDFComputeClicked) 
            self.ui.TFIDF_Rank_spinBox.setValue(5)
            InitTFIDFTable(self.ui)


            self.ui.COVID19_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.DELTA_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.OMICRON_checkBox.clicked.connect(self.onQueryFilterCheck)

            self.ui.AZ_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.Pfizer_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.Moderna_checkBox.clicked.connect(self.onQueryFilterCheck)

            self.ui.UK_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.USA_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.BRAZI_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.CHINA_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.INDIA_checkBox.clicked.connect(self.onQueryFilterCheck)
            self.ui.TAIWAN_checkBox.clicked.connect(self.onQueryFilterCheck)
            
           
            # Information tab table
            self.ui.Info_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.Info_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.Info_tableWidget.verticalHeader().setVisible(False)
            font = self.ui.Info_tableWidget.horizontalHeader().font()
            font.setBold(True)
            self.ui.Info_tableWidget.horizontalHeader().setFont(font)
            self.ui.Info_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Info_tableWidget.horizontalHeader().resizeSection(1,500)
            #self.ui.Info_tableWidget.cellClicked.connect(self.onInfoTablechanged)
            self.ui.Info_tableWidget.doubleClicked.connect(self.onInfoTableDoubleClicked)

            # Query Information
            self.ui.Query_pushButton.clicked.connect(self.onQueryClicked) 
            
        def onWord2VectChanged(self, index):
            
            if index == 0: # CBOW
                print('CBOW')
                self.ui.TrainCBOWModel_comBox.clear()
                curr_path = os.getcwd()
                for file in os.listdir(curr_path):
                    if file.endswith('.cbow'):
                        print(file)
                        self.ui.TrainCBOWModel_comBox.addItem(file)
               
            elif index == 1: # Skip-gram
                print('Skip-gram')

                self.ui.TrainSkipgramModel_comboBox.clear()
                curr_path = os.getcwd()
                for file in os.listdir(curr_path):
                    if file.endswith('.skipgram'):
                        print(file)
                        self.ui.TrainSkipgramModel_comboBox.addItem(file)

        def onLoadClicked(self):
            if os.path.isfile(self.ui.Traindata_lineEdit.text()):
                os.remove(self.ui.Traindata_lineEdit.text())

            Zipf(self)   
            
        def spinchanged(self):
            value = self.ui.file_spinBox.value()
            self.ui.file_progressBar.setRange(1, value)
            self.maxFiles = value

        def onStemmingCheck(self):
            self.bStemming = self.ui.Stemming_checkBox.isChecked()
                
        def onStopwordsCheck(self):
            self.bStopwords = self.ui.Stopwords_checkBox.isChecked()
            
        def onTFIDFCheck(self):
            self.bTFIDF = self.ui.TFIDF_checkBox.isChecked()

        def onTrainDataClicked(self):
            self.bStemming = self.ui.Stemming_checkBox.isChecked()
            self.bStopwords = self.ui.Stopwords_checkBox.isChecked()
            
            if os.path.isfile(self.ui.Traindata_lineEdit.text()):
                os.remove(self.ui.Traindata_lineEdit.text())
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
                        getPattern(fullpath, self.ui.Traindata_lineEdit.text(), self.bStopwords, self.bStemming)
                        i += 1
                        if i > self.maxFiles:
                            break
                        self.ui.file_progressBar.setValue(i)
                    elif isdir(fullpath):   #  Is directory ?
                        print("Folder :", f)

        def onCBOWComputeClicked(self):
            CBOW_model(self.ui)
               
        def onSkipgramComputeClicked(self):
            Skipgram_model(self.ui)
            
        def TFIDFDoccomboboxchanged(self):
            w_list = []
            
            for i in range(self.ui.Index_tableWidget.rowCount()):
                if self.ui.Index_tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked:
                    print(self.ui.Index_tableWidget.item(i, 0).text())
                    w_list.append(self.ui.Index_tableWidget.item(i, 0).text())
            OpenTFIDFDocument(self.ui, w_list)
        
        def TFIDFMethodcomboboxchanged(self):
            self.TFIDFMethod = self.ui.TFIDF_Method_comboBox.currentIndex()
            if self.TFIDFMethod == 1:
                pixmap = QtGui.QPixmap(':/IR-System/resource/TFIDF weighting.png')
                self.ui.TFIDF_Formula_Label.setPixmap(pixmap)    
            else:
                pixmap = QtGui.QPixmap(':/IR-System/resource/Log-frequency weighting.PNG')
                self.ui.TFIDF_Formula_Label.setPixmap(pixmap)

        def onTFIDFComputeClicked(self):
            w_list = []
            
            for i in range(self.ui.Index_tableWidget.rowCount()):
                if self.ui.Index_tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked:
                    print(self.ui.Index_tableWidget.item(i, 0).text())
                    w_list.append(self.ui.Index_tableWidget.item(i, 0).text())
            self.ui.TFIDF_Rank_spinBox.setMaximum(len(w_list))
            self.ui.TFIDF_Rank_spinBox.setMinimum(1)
            self.ui.TFIDF_Rank_spinBox.setValue(len(w_list))
           
            TFIDF_Weight(self.ui, w_list, self.TFIDFMethod, True, True)

        
        def onInfoTableDoubleClicked(self):
            row = self.ui.Info_tableWidget.currentRow()
            w_list = []
            for i in range(self.ui.Index_tableWidget.rowCount()):
                if self.ui.Index_tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked:
                    w_list.append(self.ui.Index_tableWidget.item(i, 0).text())
            OpenInfoDocument(self.ui, w_list, self.ui.Info_tableWidget.item(row, 0).text())
        
        def onQueryFilterCheck(self):
            InitIndexTable(self.ui)
            InitInfoTable(self.ui)
            InitTFIDFTable(self.ui)
            getQuery(self.ui, False, False)
            
        def onQueryClicked(self):
            if not self.ui.Query_comboBox.currentText():
                msgBox = QMessageBox() 
                msgBox.setIcon(QMessageBox.Warning) # add "information" icon
                msgBox.setWindowTitle('Error')
                msgBox.setText('There are not any query string in input box.') # Add message
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                return
            InitIndexTable(self.ui)
            InitInfoTable(self.ui)
            InitTFIDFTable(self.ui)    

            self.ui.COVID19_checkBox.setChecked(False)
            self.ui.DELTA_checkBox.setChecked(False)
            self.ui.OMICRON_checkBox.setChecked(False)
            self.ui.AZ_checkBox.setChecked(False)
            self.ui.Pfizer_checkBox.setChecked(False)
            self.ui.Moderna_checkBox.setChecked(False)
            self.ui.UK_checkBox.setChecked(False)
            self.ui.USA_checkBox.setChecked(False)
            self.ui.BRAZI_checkBox.setChecked(False)
            self.ui.CHINA_checkBox.setChecked(False)
            self.ui.INDIA_checkBox.setChecked(False)
            self.ui.TAIWAN_checkBox.setChecked(False)      
            
            getQuery(self.ui, False, False)
            
       
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(window.width(), window.height())
    window.show()
    app.exec_()
    
    


