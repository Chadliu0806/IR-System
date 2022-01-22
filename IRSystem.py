import os
from os import listdir
from os.path import isfile, isdir, join

from XMLParser import XMLParser
from JSONParser import JSONParser
from VerifyCode import GenerateChecksum
from VerifyCode import GenerateCRC32
from VerifyCode import Comparison
<<<<<<< HEAD
from NLTKParser import CBOW_model, Skipgram_model, TFIDF_Weight, edit_distance, Matching
from NLTKParser import Zipf, getQuery, getPattern, OpenTFIDFDocument, OpenInfoDocument, InitTFIDFTable, InitIndexTable, InitInfoTable
import re
=======
from NLTKParser import CBOW_model, Skipgram_model, TFIDF_Weight, Zipf_distribution, getIndex, edit_distance, Matching, listInit
from NLTKParser import getPattern, OpenDocument, InitTFIDFTable
from WebCrawler import web_crawler
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
<<<<<<< HEAD

=======
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QObject
from PySide6.QtCore import QFile
from PySide6.QtGui import QFont
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

import pandas as pd 
import seaborn as sns
from sklearn.decomposition import PCA
<<<<<<< HEAD
=======
import adjustText
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

import sys
import matplotlib.pyplot as plt

from MainWindow import Ui_Form
from sklearn.model_selection import train_test_split

search_pattern = ''

def plot_2d_representation_of_words(
    word_list, 
    word_vectors, 
    flip_x_axis = False,
    flip_y_axis = False,
    label_x_axis = "x",
    label_y_axis = "y", 
    label_label = "city"):

    pca = PCA(n_components = 2)

    word_plus_coordinates=[]

    for word in word_list: 

        current_row = []
        current_row.append(word)
        current_row.extend(word_vectors[word])
        word_plus_coordinates.append(current_row)

    word_plus_coordinates = pd.DataFrame(word_plus_coordinates)

    coordinates_2d = pca.fit_transform(
        word_plus_coordinates.iloc[:,1:300])
    coordinates_2d = pd.DataFrame(
        coordinates_2d, columns=[label_x_axis, label_y_axis])
    coordinates_2d[label_label] = word_plus_coordinates.iloc[:,0]
    if flip_x_axis:
        coordinates_2d[label_x_axis] = \
        coordinates_2d[label_x_axis] * (-1)
    if flip_y_axis:
        coordinates_2d[label_y_axis] = \
        coordinates_2d[label_y_axis] * (-1)

    plt.figure(figsize = (15,10))
    p1=sns.scatterplot(
        data=coordinates_2d, x=label_x_axis, y=label_y_axis)

    x = coordinates_2d[label_x_axis]
    y = coordinates_2d[label_y_axis]
    label = coordinates_2d[label_label]

    texts = [plt.text(x[i], y[i], label[i]) for i in range(len(x))]
    adjustText.adjust_text(texts)



if __name__ == '__main__':

    os.system("")
    
    class MainWindow(QtWidgets.QMainWindow, Ui_Form):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_Form()
            self.ui.setupUi(self)
          

<<<<<<< HEAD
            self.maxFiles = 2000
            self.bStemming = False
            self.bStopwords = True
            self.bTFIDF = False
=======
            self.maxFiles = 500
            self.bStemming = False
            self.bStopwords = True
            self.bTFIDF = False
            self.bPartial = True
            self.bIgnoreCase = False
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
            self.TFIDFMethod = 0

            # function tab
            self.ui.tabWidget.setCurrentIndex(0)
<<<<<<< HEAD
            #self.ui.tabWidget.currentChanged['int'].connect(self.onTabChanged)
=======
            self.ui.tabWidget.currentChanged['int'].connect(self.onTabChanged)
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

            # Word2Vect tab
            self.ui.Word2Vect_tabWidget.setCurrentIndex(0)
            self.ui.Word2Vect_tabWidget.currentChanged['int'].connect(self.onWord2VectChanged)
            
<<<<<<< HEAD
            # Amount of files spin control
            self.ui.file_spinBox.setValue(2000)
            self.maxFiles = 2000
=======
            # Function Combobox 
            self.ui.func_comboBox.currentIndexChanged.connect(self.comboboxchanged)
            # Amount of files spin control
            self.ui.file_spinBox.setValue(80)
            self.maxFiles = 80
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
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
<<<<<<< HEAD

                      
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
=======
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

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
<<<<<<< HEAD
            self.ui.Info_tableWidget.horizontalHeader().setFont(font)
            self.ui.Info_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Info_tableWidget.horizontalHeader().resizeSection(1,500)
            #self.ui.Info_tableWidget.cellClicked.connect(self.onInfoTablechanged)
            self.ui.Info_tableWidget.doubleClicked.connect(self.onInfoTableDoubleClicked)

            # Query Information
            self.ui.Query_pushButton.clicked.connect(self.onQueryClicked) 
            
=======
            self.ui.Match_tableWidget.horizontalHeader().setFont(font)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(0,100)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(1,100)
            self.ui.Match_tableWidget.horizontalHeader().resizeSection(2,300)

            # CBOW & Skig-gram tabel widget
            self.ui.CBOW_tableWidget.horizontalHeader().setFont(font)
            self.ui.CBOW_tableWidget.horizontalHeader().resizeSection(0,150)
            self.ui.CBOW_tableWidget.horizontalHeader().resizeSection(1,150)

            self.ui.Skipgram_tableWidget.horizontalHeader().setFont(font)
            self.ui.Skipgram_tableWidget.horizontalHeader().resizeSection(0,150)
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
            
        def onTabChanged(self, index):
            #if index == 0:  # Zipf
            #    self.ui.func_comboBox.setCurrentIndex(2)
            if index == 1: # Word2Vect
                self.ui.func_comboBox.setCurrentIndex(5)   

>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
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
<<<<<<< HEAD
=======
            
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
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

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

<<<<<<< HEAD
=======
        def onPartialCheck(self):
            self.bPartial = self.ui.Partial_checkBox.isChecked()
                
        def onIgnoreCaseCheck(self):
            self.bIgnoreCase = self.ui.IgnoreCase_checkBox.isChecked()

>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
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
<<<<<<< HEAD
=======
                        self.ui.file_label.setText(fullpath)
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
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
<<<<<<< HEAD
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
            
       
=======
            OpenDocument(self.ui, w_list)
        
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
           
            TFIDF_Weight(self.ui, w_list, self.TFIDFMethod)
       
        
        def comboboxchanged(self):
            type = self.ui.func_comboBox.currentIndex()
            if type == 2:
                self.bStemming = self.ui.Stemming_checkBox.isChecked()
                self.bStopwords = self.ui.Stopwords_checkBox.isChecked()
                listInit()

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
                            # Parameter 4: Indexing
                            Zipf_distribution(fullpath, self.ui.Traindata_lineEdit.text(), self.bStopwords, self.bStemming, True)  
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
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(window.width(), window.height())
    window.show()
    app.exec_()
    
    
<<<<<<< HEAD

=======
>>>>>>> ed31681a6c7ac452d7838273ee29617057d7a3d2

