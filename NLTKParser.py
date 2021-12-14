import os
from os import listdir
from os.path import isfile, isdir, join
import csv
from gensim.models import keyedvectors
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

from PySide6 import QtCore
from PySide6.QtGui import QColor, QBrush, QPixmap
from PySide6.QtWidgets import *

from gensim.models.keyedvectors import KeyedVectors
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import multiprocessing
import timeit
import math
import re
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

_list = LinkedList()
All_tokens = []
encode = 'ascii'
docs_list = []
original_docs_list = []

def listInit():

    global list
    global All_tokens
    #list.deleteAll()
    _list = LinkedList()
    All_tokens = []


def Indexing(filename):
    
    global _list
    global All_tokens

    sr = set(stopwords.words('english'))
    sr.add('also')
    sr.add('this')
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
                        _list.add(sz, tail, i)   
                    
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
   
def Stemming(line):

    stemmer = PorterStemmer()   # Porter 法去除字尾 Stemming
    
    stemming_string = ''

   # tokens = line.encode(encoding=encode, errors='ignore').split()
    tokens = word_tokenize(line)
    # Porter 法去除字尾 Stemming
    for token in tokens:
       # sz = token.decode(encode)
        sz = token
        sz_result = stemmer.stem(sz)
        stemming_string = stemming_string + ' ' + sz_result
    return stemming_string

def Zipf_distribution(source, target=None, stopword=False, stemming=False, Indexing=False):
    
    global _list
    global All_tokens

    global docs_list
    global original_docs_list
    string_list = ''
    original_string_list = ''
    
    sr = set(stopwords.words('english'))
    
    new_stopwords = ['?', '$', '%', '\'s', 'would', 'n\'t',
                     'about', 'again', 'al.', 'all', 'almost', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'are', 'as', 'at',
                     'be', 'because', 'been', 'before', 'being', 'between', 'both', 'but', 'by',
                     'can', 'could', 
                     'did', 'do', 'does', 'done', 'due', 'during',
                     'e.g.', 'each', 'eight', 'either', 'enough', 'especially', 'et.', 'et al.', 'etc',
                     'five', 'for', 'found', 'four', 'from', 'further',
                     'had', 'has', 'have', 'having', 'here', 'how', 'however', 'hi',
                     'i', 'i.e.', 'if', 'in', 'into', 'is', 'it', 'its', 'itself',
                     'just',
                     'kg', 'km',
                     'made', 'mainly', 'make', 'may', 'mg', 'might', 'ml', 'mm', 'most', 'mostly', 'must',
                     'nearly', 'neither', 'nine', 'no', 'nor', 'not',
                     'obtained', 'of', 'often', 'on', 'one', 'or', 'our', 'overall',
                     'perhaps',
                     'quite',
                     'rather', 'really', 'regarding',
                     'seem', 'seen', 'seven', 'several', 'should', 'show', 'showed', 'shown', 'shows', 'significantly', 'since', 'six', 'so', 'some', 'such',
                     'ten', 'than', 'that', 'the', 'their', 'theirs', 'them', 'then', 'there', 'therefore', 'these', 'they', 'this', 'those', 'three', 'through', 'thus', 'to', 'two',
                     'upon', 'use', 'used', 'using',
                     'various', 'very',
                     'was', 'we', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'why', 'with', 'within', 'without'
                    ]
    sr = sr.union(new_stopwords)
    head, tail = os.path.split(source)

    print(tail)
    with open(source, newline='', encoding='utf_8_sig') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in rows:
            if i != 0:  
                Line = row[1]
                if row[2] != '':
                    Line = Line + ' ' + row[2]
                
                original_string_list += Line
                transTable = Line.maketrans("(),.?", "     ", "\":")            
                Line = Line.translate(transTable)
  
                # Porter 法去除字尾 Stemming

                if stemming == True:
                    Line = Stemming(Line)  

                #tokens = Line.encode(encoding=encode, errors='ignore').split()
                # tokens = Line
                tokens = Line.encode(encoding=encode, errors='ignore').split() 
                clean_tokens = tokens[:]

                sz = ''
                if stopword == False:
                    for token in tokens:    # 不移除停用詞但要處理 Indexing
                        #sz = token
                        sz = token.decode(encode)
                        if not sz.isdigit() and len(sz) >= 2:  # ignore digital number
                            _list.add(sz, tail, i+1)   
                            string_list += sz
                            string_list += ' '
                else:
                    for token in tokens:    # 移除停用詞Stop Words
                        #sz = token
                        sz = token.decode(encode)
                        if sz in sr:
                            clean_tokens.remove(token)
                        else:
                            if not sz.isdigit() and len(sz) >= 2:  # ignore digital number
                                _list.add(sz, tail, i+1)   
                                string_list += sz
                                string_list += ' '
                            else:
                                clean_tokens.remove(token)
                All_tokens = All_tokens + clean_tokens
            i += 1

    string_list += '\n'
    docs_list.append(string_list)
    original_docs_list.append(original_string_list)
    f = open(target, "a")
    f.write(string_list)
    f.close()


def getIndex(ui):
    
    global All_tokens

   # if All_tokens.amount() != 0:
    tokenlist = [ch.decode('utf_8_sig') for ch in All_tokens]

    freq = FreqDist(tokenlist)
    fdist = freq.most_common(50)

    if 0:
        w_list = []
        w_list.append('omicron')
        w_list.append('market')
        w_list.append('travel')
        w_list.append('variant')
        w_list.append('covid')
        w_list.append('restrict')
    
        for item in fdist:
            word_string = item[0]
            row = ui.Index_tableWidget.rowCount()
            ui.Index_tableWidget.insertRow(row)
            item = QTableWidgetItem(word_string)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        
            if word_string in w_list:
                item.setCheckState(QtCore.Qt.Checked)    
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            ui.Index_tableWidget.setItem(row, 0, item)
    else:
        w_list = []
        w_list.append('oil')
        w_list.append('covid')
        w_list.append('omicron')
        w_list.append('variant')
        w_list.append('concern')
        w_list.append('stock')

        for word_string in w_list:
            row = ui.Index_tableWidget.rowCount()
            ui.Index_tableWidget.insertRow(row)
            item = QTableWidgetItem(word_string)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)   
            ui.Index_tableWidget.setItem(row, 0, item) 

    """
    with open('d:\\Index_Result.csv', 'w', encoding=encode, newline='') as f:
        writer = csv.writer(f)
        for item in fdist:
            word_string = item[0]
            
            subject = _list.getNodedata(word_string)
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
    """                
    #plt.clf()
    
    
    fig = plt.figure(figsize = (10,5))
    plt.gcf().subplots_adjust(bottom=0.35) # to avoid x-ticks cut-off    
    plt.ion()
   
    freq.plot(50, title='Top 50 Most Common Words in Corpus') #cumulative=False)
    plt.ioff() 
    plt.savefig('d:\\img_top50_common.png')
    
    pixmap = QPixmap('d:\\img_top50_common.png')
    ui.Zipf_label.setPixmap(pixmap)
    ui.Zipf_label.setScaledContents(True)
    
    

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

def InitTFIDFTable(ui):
    ui.TFIDF_tableWidget.clearContents()
    ui.TFIDF_tableWidget.setRowCount(0)
    ui.TFIDF_tableWidget.setColumnCount(ui.file_spinBox.value()+1)
    
    header_labels = []
    header_labels.append('Word')
    for i in range(ui.file_spinBox.value()):
        label = 'Doc' + str(i+1)
        header_labels.append(label)
    ui.TFIDF_tableWidget.setHorizontalHeaderLabels(header_labels)
  
    
def CBOW_model(ui):

    if ui.TrainCBOWModel_comBox.currentText() == '':
        msgBox = QMessageBox() 
        msgBox.setIcon(QMessageBox.Warning) # add "Warning" icon
        msgBox.setWindowTitle('CBOW model')
        msgBox.setText('Please Input file name for CBOW model') # Add message
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        return

    fullpath = os.getcwd() + '\\' + ui.TrainCBOWModel_comBox.currentText()
    

    start = timeit.default_timer()

    sentences = LineSentence(ui.Traindata_lineEdit.text())
    if not os.path.isfile(fullpath):
        model = Word2Vec(sentences, vector_size=250, window=10, min_count=3,workers=multiprocessing.cpu_count(), sg=0, negative=20)
        model.save(fullpath)
        print('\ndone')
    else:
        model = Word2Vec.load(fullpath)

    stop = timeit.default_timer()
    ui.CostTime_Label.setText('Elapsed time : ' + str(round(stop - start, 6)) + ' ms')

    sz = ui.SimilarWord_comboBox.currentText()
    similar_list = model.wv.most_similar(sz, topn=20)
    
    w_list = []
    v_list = []
    
    w_list.append(sz)
    v_list.append(model.wv.get_vector(sz)) 
    
    ui.CBOW_tableWidget.clearContents()
    ui.CBOW_tableWidget.setRowCount(0)
    ui.CBOW_tableWidget.setColumnCount(2)
    ui.CBOW_tableWidget.setHorizontalHeaderLabels(['Similarity word', 'Score'])
            

    row = ui.CBOW_tableWidget.rowCount()
    ui.CBOW_tableWidget.insertRow(row)
    ui.CBOW_tableWidget.setItem(row, 0, QTableWidgetItem(sz))
    item = QTableWidgetItem(str(model.wv.similarity(sz, sz)))
    item.setForeground(QBrush(QColor(128, 0, 0)))
    ui.CBOW_tableWidget.setItem(row, 1, item)
         
    for word_string, val in similar_list:
        row = ui.CBOW_tableWidget.rowCount()
        ui.CBOW_tableWidget.insertRow(row)
        ui.CBOW_tableWidget.setItem(row, 0, QTableWidgetItem(word_string))
        item = QTableWidgetItem(str(val))
        item.setForeground(QBrush(QColor(128, 0, 0)))
        ui.CBOW_tableWidget.setItem(row, 1, item)

        w_list.append(word_string)
        v_list.append(model.wv.get_vector(word_string))

    pca = PCA(n_components=2)
    result = pca.fit_transform(v_list)
    # Visual display
    plt.clf()
    plt.scatter(result[:, 0], result[:, 1])
    plt.ioff()
   
    for i, word in enumerate(w_list):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.savefig('d:\\Word2Vec_CBOW.png')
    pixmap = QPixmap('d:\\Word2Vec_CBOW.png')
    ui.CBOWImage_label.setPixmap(pixmap)
    ui.CBOWImage_label.setScaledContents(True)
    plt.ion()
    #plt.show()
   

def Skipgram_model(ui):

    if ui.TrainSkipgramModel_comboBox.currentText() == '':
        msgBox = QMessageBox() 
        msgBox.setIcon(QMessageBox.Warning) # add "Warning" icon
        msgBox.setWindowTitle('Skip-gram model')
        msgBox.setText('Please Input file name for Skip-gram model') # Add message
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        return

    fullpath = os.getcwd() + '\\' + ui.TrainSkipgramModel_comboBox.currentText()
    
    start = timeit.default_timer()
    
    if not os.path.isfile(fullpath):
        sentences = LineSentence(ui.Traindata_lineEdit.text())
        model = Word2Vec(sentences, vector_size=250, window=10, min_count=3,workers=multiprocessing.cpu_count(), sg=1, negative=20)
        model.save(fullpath)
        print('\ndone')
    else:
        model = Word2Vec.load(fullpath)
    
    stop = timeit.default_timer()
    ui.CostTime_Label.setText('Elapsed time : ' + str(round(stop - start, 6)) + ' ms')
            
    sz = ui.SimilarWord_comboBox.currentText()
    similar_list = model.wv.most_similar(sz, topn=20)
    
    w_list = []
    v_list = []

    w_list.append(sz)
    v_list.append(model.wv.get_vector(sz)) 

    ui.Skipgram_tableWidget.clearContents()
    ui.Skipgram_tableWidget.setRowCount(0)
    ui.Skipgram_tableWidget.setColumnCount(2)
    ui.Skipgram_tableWidget.setHorizontalHeaderLabels(['Similarity word', 'Score'])
    

    row = ui.Skipgram_tableWidget.rowCount()
    ui.Skipgram_tableWidget.insertRow(row)
    ui.Skipgram_tableWidget.setItem(row, 0, QTableWidgetItem(sz))
    item = QTableWidgetItem(str(model.wv.similarity(sz, sz)))
    item.setForeground(QBrush(QColor(128, 0, 0)))
    ui.Skipgram_tableWidget.setItem(row, 1, item)
         
    for word_string, val in similar_list:
        row = ui.Skipgram_tableWidget.rowCount()
        ui.Skipgram_tableWidget.insertRow(row)
        ui.Skipgram_tableWidget.setItem(row, 0, QTableWidgetItem(word_string))
        item = QTableWidgetItem(str(val))
        item.setForeground(QBrush(QColor(128, 0, 0)))
        ui.Skipgram_tableWidget.setItem(row, 1, item)

        w_list.append(word_string)
        v_list.append(model.wv.get_vector(word_string))
        
        
    pca = PCA(n_components=2)
    result = pca.fit_transform(v_list)
    # Visual display
           
    plt.ioff()
    plt.clf()
    plt.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(w_list):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
            
    plt.savefig('d:\\Word2Vec_Skipgram.png')
    pixmap = QPixmap('d:\\Word2Vec_Skipgram.png')
    ui.SkipgramImage_label.setPixmap(pixmap)
    ui.SkipgramImage_label.setScaledContents(True)
    plt.ion()
    
    #plt.show()

def OpenDocument(ui, w_list):
    
    global original_docs_list
    text = str(ui.TFIDF_Doc_comboBox.currentText())
    if text != '':
        doc_index = int(text)
        szSentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', original_docs_list[doc_index-1])

        html_string = ''
        for n in range(len(szSentences)):
            word_rank = 0
            for i in range(len(w_list)):
                temp = Stemming(szSentences[n].lower())
                if w_list[i] in temp:
                    word_rank += 1

            if word_rank >= ui.TFIDF_Rank_spinBox.value():
                html_string = html_string + '<font color=\"red\">' + szSentences[n] + '</font>'
            else:
                temp = Stemming(szSentences[n].lower())
                word_all = temp.split()
                #word_all = szSentences[n].split()
                for word in word_all:
                    if word in w_list:
                        html_string = html_string + '<font color=\"blue\">' + ' ' + str(word) + ' ' + '</font>'     
                    else:
                        html_string = html_string + '<font color=\"black\">' + ' ' + str(word) + ' ' + '</font>'      
        ui.TFIDF_textEdit.setHtml(html_string)        


def getPattern(source, target, stopword=False, stemming=False):       

    global _list
    global docs_list
    global original_docs_list
    string_list = ""
    original_string_list = ""
    
    
    sr = set(stopwords.words('english'))
    
    new_stopwords = ['?', '$', '%', '\'s', 'would', 'n\'t',
                     'about', 'again', 'al.', 'all', 'almost', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'are', 'as', 'at',
                     'be', 'because', 'been', 'before', 'being', 'between', 'both', 'but', 'by',
                     'can', 'could', 
                     'did', 'do', 'does', 'done', 'due', 'during',
                     'e.g.', 'each', 'eight', 'either', 'enough', 'especially', 'et.', 'et al.', 'etc',
                     'five', 'for', 'found', 'four', 'from', 'further',
                     'had', 'has', 'have', 'having', 'here', 'how', 'however', 'hi',
                     'i', 'i.e.', 'if', 'in', 'into', 'is', 'it', 'its', 'itself',
                     'just',
                     'kg', 'km',
                     'made', 'mainly', 'make', 'may', 'mg', 'might', 'ml', 'mm', 'most', 'mostly', 'must',
                     'nearly', 'neither', 'nine', 'no', 'nor', 'not',
                     'obtained', 'of', 'often', 'on', 'one', 'or', 'our', 'overall',
                     'perhaps',
                     'quite',
                     'rather', 'really', 'regarding',
                     'seem', 'seen', 'seven', 'several', 'should', 'show', 'showed', 'shown', 'shows', 'significantly', 'since', 'six', 'so', 'some', 'such',
                     'ten', 'than', 'that', 'the', 'their', 'theirs', 'them', 'then', 'there', 'therefore', 'these', 'they', 'this', 'those', 'three', 'through', 'thus', 'to', 'two',
                     'upon', 'use', 'used', 'using',
                     'various', 'very',
                     'was', 'we', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'why', 'with', 'within', 'without'
                    ]
    sr = sr.union(new_stopwords)

    head, tail = os.path.split(source)

    print(tail)
    with open(source, newline='', encoding='utf_8_sig') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in rows:
            if i != 0:  
                Line = row[1]
                if row[2] != '':
                    Line = Line + ' ' + row[2]
                    
                    original_string_list += Line
                    
                    transTable = Line.maketrans("(),.?", "     ", "\":")            
                    Line = Line.translate(transTable)
  
                    # Porter 法去除字尾 Stemming
                    if stemming == True:
                        Line = Stemming(Line)  
                
                    tokens = Line.encode(encoding=encode, errors='ignore').split()
                    clean_tokens = tokens[:]

                    sz = ''
                    if stopword == False:
                        for token in tokens:    # 不移除停用詞但要處理 Indexing
                            sz = token.decode(encode)
                            if not sz.isdigit() and len(sz) >= 2:  # ignore digital number
                                string_list += sz
                                string_list += ' '
                    else:
                        for token in tokens:    # 移除停用詞Stop Words
                            sz = token.decode(encode)
                            if sz in sr:
                                clean_tokens.remove(token)
                            else:
                                if not sz.isdigit() and len(sz) >= 2:  # ignore digital number
                                    string_list += sz
                                    string_list += ' '
            i += 1
    string_list += '\n'
    docs_list.append(string_list)
    original_docs_list.append(original_string_list)
    f = open(target, "a")
    f.write(string_list)
    f.close()


def TFIDF_Weight(ui, word_list, method=0):  

    InitTFIDFTable(ui)

    global docs_list
    doc_all = [[word.lower() for word in doc.split() if len(word) >= 2] for doc in docs_list]

    if method == 0:     # Log-frequency weighting
        # TF
        tf = dict()
        for n in range(len(doc_all)):
            for word in doc_all[n]:
                if word not in tf: 
                    tf[word] = [0 for _ in doc_all]     # Initial zero
                # 詞彙在該文件中出現次數
                total_sum = 0
                for term in doc_all[n]:
                    if term == word:
                        total_sum = total_sum + 1
                tf[word][n] = total_sum 

        # weight
        sorted_word = sorted(set([word for word in tf]))
        tfidf = list()
        
        for word in sorted_word:
            value = tf[word]
            n = 0
            for v in value:
                if v > 0:
                    value[n] = 1 + math.log10(v)
                else:
                    value[n] = 0
                n = n + 1
            tfidf.append(value)
        #   tfidf = normalize(tfidf, norm='l2')
        
        """
        f = []
        tf = {}
        idf = {}
        D = len(doc_all)
        avgdl = sum([len(doc)+ 0.0 for doc in doc_all]) / D
        for doc in doc_all:
            tmp = {}
            for word in doc:
                tmp[word] = tmp.get(word, 0) + 1
            f.append(tmp)
            for k in tmp.keys():
                tf[k] = tf.get(k, 0) + 1
        for k, v in tf.items():
            idf[k] = math.log(D - v + 0.5) - math.log(v + 0.5)
        # D, avgdl
     
       """
        array = cosine_similarity(tfidf, tfidf)
        f = open('d:\\123.txt', 'a')

        for i in range(10):
            f.write(str(array[i]))
        f.close()

    else: # TF-IDF weighting
        # TF
        tf = dict()
        for n in range(len(doc_all)):
            for word in doc_all[n]:
                if word not in tf: 
                    tf[word] = [0 for _ in doc_all]     # Initial zero
                # 分子為詞彙在該文件中出現次數
                # 分母則為該文件中所有詞彙數
                total_sum = 0
                for term in doc_all[n]:
                    if term == word:
                        total_sum = total_sum + 1

                tf[word][n] = total_sum/len(doc_all[n])  
                #tf[word][n] = sum([1 for term in doc_all[n] if term == word])/len(doc_all[n])  

        # IDF
        total_D = len(doc_all)
        idf = dict()
        for doc in doc_all:
            for word in doc:
                if word not in idf:
                    # word_idf = math.log10(total_D/(sum([1 for doc in doc_all if word in doc])+1))
                    total_sum = 1
                    for doc in doc_all:
                        if word in doc:
                            total_sum = total_sum + 1
                    # 分子為所有文件數量
                    # 分母為包含該詞彙的文件數量
                    word_idf = math.log10(total_D/total_sum)    
                    idf[word] = word_idf

        # TF_IDF : Weight
        sorted_word = sorted(set([word for word in tf]))
        tfidf = list()
        
        for word in sorted_word:
            value = tf[word]
            value = [v*idf[word] for v in value]
            tfidf.append(value)
        tfidf = normalize(tfidf, norm='l2')
       
        ### cosine_similarity 餘弦相似性
        ### cosine_similarity(tfidf[i:i+1], tfidf)[0] 第i篇與全部文章比較相似性
        ### cosine_similarity(tfIdf, tfIdf) ---> 全部文章交叉比較相似性

        """
        array = cosine_similarity(tfidf, tfidf)
        f = open('d:\\123.txt', 'a')

        for i in range(10):
            f.write(str(array[i]))
        f.close()
        #print(array)
        """
        
        """
        # TF-IDF
        vectorizer = TfidfVectorizer(smooth_idf=True)
        tfidf = vectorizer.fit_transform(docs_list)
        cols = vectorizer.get_feature_names_out()
        weight = tfidf.toarray()              # tfidf array to Doc-1 ~ Doc-n
        result = pd.DataFrame(tfidf.toarray(), columns=vectorizer.get_feature_names_out())
        # print(pd.DataFrame(results).transpose())    
        #print(result)
    
        """
       

    results = dict()
    doc_rank = []    
        
    for col in range(len(tfidf[0])):
        doc_rank.append(0)
                
    for top_Word in word_list:
        row = ui.TFIDF_tableWidget.rowCount()
        ui.TFIDF_tableWidget.insertRow(row)
        item = QTableWidgetItem(top_Word)
        ui.TFIDF_tableWidget.setItem(row, 0, item)
        for n in range(len(sorted_word)):
            results[sorted_word[n]] = tfidf[n]
            if sorted_word[n] == top_Word:
                for col in range(len(tfidf[n])):
                    item = QTableWidgetItem(str(round(tfidf[n][col],5)))
                    if tfidf[n][col] > 0:
                        doc_rank[col] = doc_rank[col] + 1
                    item.setForeground(QBrush(QColor(0, 0, 128)))
                    ui.TFIDF_tableWidget.setItem(row, col+1, item)
    
    weight_count = []
    for n in range(len(sorted_word)):
        weight_count.append(0)
        weight_count[n] = 0
        for w in range(len(results[sorted_word[n]])):
            weight_count[n] = weight_count[n] + results[sorted_word[n]][w]
            
    ui.TFIDF_Doc_comboBox.clear()
    
    for n in range(len(doc_rank)):
        if doc_rank[n] >= len(word_list):
            print('Doc' + str(n+1) +  ':' + str(doc_rank[n]))
            ui.TFIDF_Doc_comboBox.addItem(str(n+1))
    
    msgBox = QMessageBox() 
    msgBox.setIcon(QMessageBox.Information) # add "information" icon
    msgBox.setWindowTitle('TF-IDF')
    msgBox.setText('TF-IDF computing complete.') # Add message
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

    
    
   
    