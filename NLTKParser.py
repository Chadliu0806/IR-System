import os
from os import listdir
from os.path import isfile, isdir, join
import csv
import pandas as pd
import nltk

#nltk.download('stopwords')
#nltk.download('punkt')

import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from LinkList import LinkedList

from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import *


list = LinkedList()
All_tokens = []
encode = 'ascii'


def CSVJoin(path):

    with open('d:\\CSV_All.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        files = listdir(path)
        for f in files:
            #Get full path
            fullpath = join(path, f)
            if isfile(fullpath):    # Is file ?
                ext = os.path.splitext(fullpath)[1]
                if ext == '.csv': # only process CSV file
                    head, tail = os.path.split(fullpath)    
                    print(fullpath)
                    with open(fullpath, newline='', encoding='utf_8_sig') as csvfile:
                        source_rows = csv.reader(csvfile, delimiter=',')
                        i = 0
                        for row in source_rows:
                            if i == 0:   #row[1] != 'title' and row[2] != 'abstract':
                                Line = ['', tail]
                                writer.writerow(Line)
                            else:
                                Line = [row[1], row[2]]
                                writer.writerow(Line)
                            i += 1
def listInit():

    global list
    global All_tokens
    list.deleteAll()
    list = LinkedList()
    All_tokens = []


def Indexing(filename):
    
    global list
    global All_tokens

    sr = set(stopwords.words('english'))
    stemmer = PorterStemmer()   # Porter 法去除字尾 Stemming
   
    with open(filename, newline='', encoding='UTF8') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in rows:
            if row[0] == '' and row[1] != '':   
                tail = row[1]
                i = 1
                print(tail)
            else:
                Line = row[0]
                if row[1] != '':
                    Line = Line + ' ' + row[1]
                    
                transTable = Line.maketrans("(),.", "    ", "\":")            
                Line = Line.translate(transTable)
                
                # Porter 法去除字尾 Stemming
                Line = stemmer.stem(Line)  

                tokens = Line.encode(encoding=encode, errors='ignore').split()
                clean_tokens = tokens[:]

                  
                for token in tokens:    # 移除停用詞Stop Words
                    sz = token.decode(encode)
                    #sz = token
                    if sz in sr:
                        clean_tokens.remove(token)
                    else:
                        list.add(sz, tail, i)   
                    
                All_tokens = All_tokens + clean_tokens
            i += 1                                    

def edit_distance(filename):

    sr = set(stopwords.words('english'))
    stemmer = PorterStemmer()   # Porter 法去除字尾 Stemming
   
    before = ''
    after = ''
   
    with open(filename, newline='', encoding='ascii') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in rows:
            if i != 0:   
                Line = row[1]
                if row[2] != '':
                    Line = Line + ' ' + row[2]
                
                tokens = Line.encode(encoding=encode, errors='ignore').split()
                # Porter 法去除字尾 Stemming
                for token in tokens:
                   sz = token.decode(encode)
                   sz_Stemming = stemmer.stem(sz)
                   before = before + ' ' + sz
                   after = after + ' ' + sz_Stemming
            i += 1
    distance = nltk.edit_distance(before, after)
    message = before +' \n vs \n' + after + '\n\nDistance:' + str(distance)
    #print(message)

    msgBox = QMessageBox() 

    msgBox.setIcon(QMessageBox.Information) # add "information" icon
    msgBox.setWindowTitle('Edit Distance')
    msgBox.setText(message) # Add message
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()
   

    
def Zipf_distribution(filename, stopword=False, stemming=False, Indexing=False):
    
    global list
    global All_tokens
  
    sr = set(stopwords.words('english'))
    head, tail = os.path.split(filename)

    stemmer = PorterStemmer()   # Porter 法去除字尾 Stemming
    print(tail)

    with open(filename, newline='', encoding='utf_8_sig') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in rows:
            if i != 0:  
                Line = row[1]
                if row[2] != '':
                    Line = Line + ' ' + row[2]
                    
                transTable = Line.maketrans("(),.", "    ", "\":")            
                Line = Line.translate(transTable)
  
                # Porter 法去除字尾 Stemming
                if stemming == True:
                    Line = stemmer.stem(Line)  

                tokens = Line.encode(encoding=encode, errors='ignore').split()
                clean_tokens = tokens[:]

                if stopword == False:
                    for token in tokens:    # 不移除停用詞但要處理 Indexing
                        sz = token.decode(encode)
                        list.add(sz, tail, i+1)   
                else:
                    for token in tokens:    # 移除停用詞Stop Words
                        sz = token.decode(encode)
                        if sz in sr:
                            clean_tokens.remove(token)
                        else:
                            list.add(sz, tail, i+1)   

                All_tokens = All_tokens + clean_tokens
            i += 1
    

def getIndex(ui):
    
    global All_tokens

   # if All_tokens.amount() != 0:
    tokenlist = [ch.decode('utf_8_sig') for ch in All_tokens]

    freq = FreqDist(tokenlist)
    fdist = freq.most_common(50)

    with open('d:\\Index_Result.csv', 'w', encoding=encode, newline='') as f:
        writer = csv.writer(f)
        for item in fdist:
            word_string = item[0]
            subject = list.getNodedata(word_string)
            if subject != None:
                for key, val in subject.items():
                    data = [word_string, key, val]
                    writer.writerow(data)
                    #out_sz = 'Word:['+word_string+'], '+'Doc:['+key+'], '+'Row:'+str(val) 
                    row = ui.Index_tableWidget.rowCount()
                    ui.Index_tableWidget.insertRow(row)
                    ui.Index_tableWidget.setItem(row, 0, QTableWidgetItem(word_string))
                    item = QTableWidgetItem(key)
                    item.setForeground(QBrush(QColor(128, 0, 0)))
                    ui.Index_tableWidget.setItem(row, 1, item)
                    item = QTableWidgetItem(str(val))
                    item.setForeground(QBrush(QColor(0, 0, 128)))
                    ui.Index_tableWidget.setItem(row, 2, item)

    fig = plt.figure(figsize = (10,5))
    plt.gcf().subplots_adjust(bottom=0.35) # to avoid x-ticks cut-off    
     
    plt.ion()
    freq.plot(50, title='Top 50 Most Common Words in Corpus') #cumulative=False)
    plt.savefig('d:\\img_top50_common.png')
    plt.ioff()
    plt.show()

def Matching(ui, filename, word, bPartial, bIgnoreCase):

    with open(filename, newline='', encoding=encode) as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            bMatch = False
            src_str = word
            dst_str = row[0]
            if bIgnoreCase == True:
                src_str = src_str.lower()
                dst_str = dst_str.lower()

            if dst_str == src_str:
                bMatch = True
            if bPartial == True and src_str in dst_str:  
                bMatch = True
            
            if bMatch == True:
               print ('This \'' + word +  '\' is in rows ' + '\033[1;34m' + row[2] + '\033[0m'+ ' of this file: ' + '\033[1;33m' + row[1] + '\033[0m')
               match_row = ui.Match_tableWidget.rowCount()
               ui.Match_tableWidget.insertRow(match_row)
             
               ui.Match_tableWidget.setItem(match_row, 0, QTableWidgetItem(row[0]))
               item = QTableWidgetItem(row[1])
               item.setForeground(QBrush(QColor(128, 128, 0)))
               ui.Match_tableWidget.setItem(match_row, 1, item)
               
               item = QTableWidgetItem(str(row[2]))
               item.setForeground(QBrush(QColor(0, 0, 128)))
               ui.Match_tableWidget.setItem(match_row, 2, item)
               
            