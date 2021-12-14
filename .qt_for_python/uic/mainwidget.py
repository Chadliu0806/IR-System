# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(782, 638)
        Form.setMinimumSize(QSize(661, 601))
        icon = QIcon()
        icon.addFile(u":/IR-System/resource/IRSystem-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.func_comboBox = QComboBox(Form)
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.setObjectName(u"func_comboBox")
        self.func_comboBox.setGeometry(QRect(10, 30, 341, 21))
        self.func_comboBox.setDuplicatesEnabled(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 6, 291, 20))
        self.file_label = QLabel(Form)
        self.file_label.setObjectName(u"file_label")
        self.file_label.setGeometry(QRect(10, 60, 131, 16))
        self.file_progressBar = QProgressBar(Form)
        self.file_progressBar.setObjectName(u"file_progressBar")
        self.file_progressBar.setGeometry(QRect(10, 80, 381, 23))
        self.file_progressBar.setValue(24)
        self.file_spinBox = QSpinBox(Form)
        self.file_spinBox.setObjectName(u"file_spinBox")
        self.file_spinBox.setGeometry(QRect(560, 30, 71, 22))
        self.file_spinBox.setReadOnly(False)
        self.file_spinBox.setAccelerated(True)
        self.file_spinBox.setMinimum(1)
        self.file_spinBox.setMaximum(1000)
        self.file_spinBox.setValue(25)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 30, 90, 16))
        self.Stemming_checkBox = QCheckBox(Form)
        self.Stemming_checkBox.setObjectName(u"Stemming_checkBox")
        self.Stemming_checkBox.setGeometry(QRect(510, 80, 141, 20))
        self.Stemming_checkBox.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/IR-System/resource/Stemming-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stemming_checkBox.setIcon(icon1)
        self.Stemming_checkBox.setChecked(True)
        self.Stopwords_checkBox = QCheckBox(Form)
        self.Stopwords_checkBox.setObjectName(u"Stopwords_checkBox")
        self.Stopwords_checkBox.setGeometry(QRect(400, 80, 101, 20))
        icon2 = QIcon()
        icon2.addFile(u":/IR-System/resource/stopwords-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stopwords_checkBox.setIcon(icon2)
        self.Stopwords_checkBox.setChecked(True)
        self.file_label_2 = QLabel(Form)
        self.file_label_2.setObjectName(u"file_label_2")
        self.file_label_2.setGeometry(QRect(50, 120, 151, 16))
        self.perform_pushButton = QPushButton(Form)
        self.perform_pushButton.setObjectName(u"perform_pushButton")
        self.perform_pushButton.setGeometry(QRect(360, 30, 81, 21))
        icon3 = QIcon()
        icon3.addFile(u":/IR-System/resource/Play-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perform_pushButton.setIcon(icon3)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 150, 771, 481))
        self.tabWidget.setAutoFillBackground(False)
        self.Zipf_tab = QWidget()
        self.Zipf_tab.setObjectName(u"Zipf_tab")
        self.Index_tableWidget = QTableWidget(self.Zipf_tab)
        if (self.Index_tableWidget.columnCount() < 1):
            self.Index_tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Index_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Index_tableWidget.setObjectName(u"Index_tableWidget")
        self.Index_tableWidget.setGeometry(QRect(5, 10, 121, 291))
        self.Index_tableWidget.setFrameShadow(QFrame.Raised)
        self.IgnoreCase_checkBox = QCheckBox(self.Zipf_tab)
        self.IgnoreCase_checkBox.setObjectName(u"IgnoreCase_checkBox")
        self.IgnoreCase_checkBox.setGeometry(QRect(520, 310, 111, 20))
        self.IgnoreCase_checkBox.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/IR-System/resource/IgnoreCase-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IgnoreCase_checkBox.setIcon(icon4)
        self.IgnoreCase_checkBox.setChecked(False)
        self.file_label_3 = QLabel(self.Zipf_tab)
        self.file_label_3.setObjectName(u"file_label_3")
        self.file_label_3.setGeometry(QRect(10, 310, 61, 16))
        self.search_pushButton = QPushButton(self.Zipf_tab)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(250, 310, 71, 20))
        icon5 = QIcon()
        icon5.addFile(u":/IR-System/resource/Search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_pushButton.setIcon(icon5)
        self.Partial_checkBox = QCheckBox(self.Zipf_tab)
        self.Partial_checkBox.setObjectName(u"Partial_checkBox")
        self.Partial_checkBox.setGeometry(QRect(400, 310, 111, 20))
        icon6 = QIcon()
        icon6.addFile(u":/IR-System/resource/PartialSearch-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Partial_checkBox.setIcon(icon6)
        self.Partial_checkBox.setChecked(True)
        self.Match_lineEdit = QLineEdit(self.Zipf_tab)
        self.Match_lineEdit.setObjectName(u"Match_lineEdit")
        self.Match_lineEdit.setGeometry(QRect(80, 310, 161, 20))
        self.Match_tableWidget = QTableWidget(self.Zipf_tab)
        if (self.Match_tableWidget.columnCount() < 3):
            self.Match_tableWidget.setColumnCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        self.Match_tableWidget.setObjectName(u"Match_tableWidget")
        self.Match_tableWidget.setGeometry(QRect(10, 340, 741, 141))
        self.Match_tableWidget.setAutoFillBackground(False)
        self.Match_tableWidget.setFrameShadow(QFrame.Raised)
        self.Match_tableWidget.setGridStyle(Qt.SolidLine)
        self.Zipf_label = QLabel(self.Zipf_tab)
        self.Zipf_label.setObjectName(u"Zipf_label")
        self.Zipf_label.setGeometry(QRect(136, 10, 621, 291))
        self.tabWidget.addTab(self.Zipf_tab, "")
        self.Word2Vect_tab = QWidget()
        self.Word2Vect_tab.setObjectName(u"Word2Vect_tab")
        self.Word2Vect_tabWidget = QTabWidget(self.Word2Vect_tab)
        self.Word2Vect_tabWidget.setObjectName(u"Word2Vect_tabWidget")
        self.Word2Vect_tabWidget.setGeometry(QRect(10, 10, 751, 471))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.file_label_5 = QLabel(self.tab)
        self.file_label_5.setObjectName(u"file_label_5")
        self.file_label_5.setGeometry(QRect(10, 13, 101, 16))
        self.CBOW_tableWidget = QTableWidget(self.tab)
        if (self.CBOW_tableWidget.columnCount() < 2):
            self.CBOW_tableWidget.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.CBOW_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.CBOW_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.CBOW_tableWidget.setObjectName(u"CBOW_tableWidget")
        self.CBOW_tableWidget.setGeometry(QRect(10, 40, 351, 361))
        self.CBOW_tableWidget.setFrameShadow(QFrame.Raised)
        self.CBOWCompute_Button = QPushButton(self.tab)
        self.CBOWCompute_Button.setObjectName(u"CBOWCompute_Button")
        self.CBOWCompute_Button.setGeometry(QRect(320, 10, 91, 20))
        icon7 = QIcon()
        icon7.addFile(u":/IR-System/resource/neurone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CBOWCompute_Button.setIcon(icon7)
        self.CBOWImage_label = QLabel(self.tab)
        self.CBOWImage_label.setObjectName(u"CBOWImage_label")
        self.CBOWImage_label.setGeometry(QRect(370, 40, 361, 361))
        self.TrainCBOWModel_comBox = QComboBox(self.tab)
        self.TrainCBOWModel_comBox.setObjectName(u"TrainCBOWModel_comBox")
        self.TrainCBOWModel_comBox.setGeometry(QRect(120, 10, 191, 22))
        self.TrainCBOWModel_comBox.setEditable(True)
        self.Word2Vect_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.file_label_6 = QLabel(self.tab_2)
        self.file_label_6.setObjectName(u"file_label_6")
        self.file_label_6.setGeometry(QRect(10, 13, 101, 16))
        self.Skipgram_tableWidget = QTableWidget(self.tab_2)
        if (self.Skipgram_tableWidget.columnCount() < 2):
            self.Skipgram_tableWidget.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Skipgram_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Skipgram_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.Skipgram_tableWidget.setObjectName(u"Skipgram_tableWidget")
        self.Skipgram_tableWidget.setGeometry(QRect(10, 40, 351, 361))
        self.Skipgram_tableWidget.setFrameShadow(QFrame.Raised)
        self.SkipgramCompute_Button = QPushButton(self.tab_2)
        self.SkipgramCompute_Button.setObjectName(u"SkipgramCompute_Button")
        self.SkipgramCompute_Button.setGeometry(QRect(320, 10, 91, 20))
        self.SkipgramCompute_Button.setIcon(icon7)
        self.SkipgramImage_label = QLabel(self.tab_2)
        self.SkipgramImage_label.setObjectName(u"SkipgramImage_label")
        self.SkipgramImage_label.setGeometry(QRect(370, 40, 361, 361))
        self.TrainSkipgramModel_comboBox = QComboBox(self.tab_2)
        self.TrainSkipgramModel_comboBox.setObjectName(u"TrainSkipgramModel_comboBox")
        self.TrainSkipgramModel_comboBox.setGeometry(QRect(120, 10, 191, 22))
        self.TrainSkipgramModel_comboBox.setEditable(True)
        self.Word2Vect_tabWidget.addTab(self.tab_2, "")
        self.SkipgramImage_label.raise_()
        self.file_label_6.raise_()
        self.Skipgram_tableWidget.raise_()
        self.SkipgramCompute_Button.raise_()
        self.TrainSkipgramModel_comboBox.raise_()
        self.CostTime_Label = QLabel(self.Word2Vect_tab)
        self.CostTime_Label.setObjectName(u"CostTime_Label")
        self.CostTime_Label.setGeometry(QRect(540, 10, 201, 20))
        self.tabWidget.addTab(self.Word2Vect_tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.TFIDF_tableWidget = QTableWidget(self.tab_3)
        if (self.TFIDF_tableWidget.columnCount() < 81):
            self.TFIDF_tableWidget.setColumnCount(81)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(21, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(22, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(23, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(24, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(25, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(26, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(27, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(28, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(29, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(30, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(31, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(32, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(33, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(34, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(35, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(36, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(37, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(38, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(39, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(40, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(41, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(42, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(43, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(44, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(45, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(46, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(47, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(48, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.TFIDF_tableWidget.setHorizontalHeaderItem(49, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(50, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(51, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(52, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(53, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(54, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(55, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(56, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(57, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(58, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(59, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(60, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(61, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(62, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(63, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(64, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(65, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(66, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(67, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(68, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(69, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(70, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(71, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(72, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(73, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(74, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(75, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(76, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(77, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(78, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(79, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.TFIDF_tableWidget.setHorizontalHeaderItem(80, __qtablewidgetitem88)
        self.TFIDF_tableWidget.setObjectName(u"TFIDF_tableWidget")
        self.TFIDF_tableWidget.setGeometry(QRect(230, 40, 531, 221))
        self.TFIDF_tableWidget.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 11, 111, 16))
        self.TFIDF_Doc_comboBox = QComboBox(self.tab_3)
        self.TFIDF_Doc_comboBox.setObjectName(u"TFIDF_Doc_comboBox")
        self.TFIDF_Doc_comboBox.setGeometry(QRect(660, 9, 101, 22))
        self.TFIDF_Doc_comboBox.setEditable(False)
        self.TFIDF_Doc_comboBox.setDuplicatesEnabled(False)
        self.TFIDF_textEdit = QTextEdit(self.tab_3)
        self.TFIDF_textEdit.setObjectName(u"TFIDF_textEdit")
        self.TFIDF_textEdit.setGeometry(QRect(0, 260, 761, 191))
        self.TFIDFCompute_Button = QPushButton(self.tab_3)
        self.TFIDFCompute_Button.setObjectName(u"TFIDFCompute_Button")
        self.TFIDFCompute_Button.setGeometry(QRect(240, 10, 91, 21))
        self.TFIDFCompute_Button.setIcon(icon7)
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(7, 13, 51, 16))
        self.TFIDF_Method_comboBox = QComboBox(self.tab_3)
        self.TFIDF_Method_comboBox.addItem("")
        self.TFIDF_Method_comboBox.addItem("")
        self.TFIDF_Method_comboBox.setObjectName(u"TFIDF_Method_comboBox")
        self.TFIDF_Method_comboBox.setGeometry(QRect(64, 10, 171, 22))
        self.TFIDF_Method_comboBox.setEditable(False)
        self.TFIDF_Method_comboBox.setDuplicatesEnabled(False)
        self.TFIDF_Formula_Label = QLabel(self.tab_3)
        self.TFIDF_Formula_Label.setObjectName(u"TFIDF_Formula_Label")
        self.TFIDF_Formula_Label.setGeometry(QRect(10, 80, 211, 51))
        self.TFIDF_Formula_Label.setPixmap(QPixmap(u":/IR-System/resource/Log-frequency weighting.PNG"))
        self.TFIDF_Formula_Label.setScaledContents(True)
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 12, 31, 16))
        self.TFIDF_Rank_spinBox = QSpinBox(self.tab_3)
        self.TFIDF_Rank_spinBox.setObjectName(u"TFIDF_Rank_spinBox")
        self.TFIDF_Rank_spinBox.setGeometry(QRect(375, 9, 51, 22))
        self.TFIDF_Rank_spinBox.setReadOnly(False)
        self.TFIDF_Rank_spinBox.setAccelerated(True)
        self.TFIDF_Rank_spinBox.setMinimum(1)
        self.TFIDF_Rank_spinBox.setMaximum(10)
        self.TFIDF_Rank_spinBox.setValue(5)
        self.tabWidget.addTab(self.tab_3, "")
        self.Traindata_Button = QPushButton(Form)
        self.Traindata_Button.setObjectName(u"Traindata_Button")
        self.Traindata_Button.setGeometry(QRect(325, 115, 21, 21))
        self.Traindata_lineEdit = QLineEdit(Form)
        self.Traindata_lineEdit.setObjectName(u"Traindata_lineEdit")
        self.Traindata_lineEdit.setGeometry(QRect(130, 116, 191, 20))
        self.file_label_4 = QLabel(Form)
        self.file_label_4.setObjectName(u"file_label_4")
        self.file_label_4.setGeometry(QRect(10, 119, 101, 16))
        self.file_label_7 = QLabel(Form)
        self.file_label_7.setObjectName(u"file_label_7")
        self.file_label_7.setGeometry(QRect(362, 118, 41, 16))
        self.SimilarWord_comboBox = QComboBox(Form)
        self.SimilarWord_comboBox.addItem("")
        self.SimilarWord_comboBox.addItem("")
        self.SimilarWord_comboBox.addItem("")
        self.SimilarWord_comboBox.addItem("")
        self.SimilarWord_comboBox.addItem("")
        self.SimilarWord_comboBox.setObjectName(u"SimilarWord_comboBox")
        self.SimilarWord_comboBox.setGeometry(QRect(412, 115, 101, 22))
        self.SimilarWord_comboBox.setEditable(True)
        self.SimilarWord_comboBox.setDuplicatesEnabled(False)
        self.TFIDF_checkBox = QCheckBox(Form)
        self.TFIDF_checkBox.setObjectName(u"TFIDF_checkBox")
        self.TFIDF_checkBox.setGeometry(QRect(530, 117, 151, 20))
        self.TFIDF_checkBox.setAutoFillBackground(False)
        self.TFIDF_checkBox.setChecked(True)
        QWidget.setTabOrder(self.func_comboBox, self.file_spinBox)
        QWidget.setTabOrder(self.file_spinBox, self.Stemming_checkBox)
        QWidget.setTabOrder(self.Stemming_checkBox, self.Stopwords_checkBox)
        QWidget.setTabOrder(self.Stopwords_checkBox, self.Index_tableWidget)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)
        self.Word2Vect_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"IR-System", None))
        self.func_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Information Retrieval", None))
        self.func_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Contents Compare", None))
        self.func_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Zipf Distribution", None))
        self.func_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Matching", None))
        self.func_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Edit Distance", None))
        self.func_comboBox.setItemText(5, QCoreApplication.translate("Form", u"Word2Vect", None))

        self.func_comboBox.setCurrentText(QCoreApplication.translate("Form", u"Information Retrieval", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pelease select perform function", None))
        self.file_label.setText(QCoreApplication.translate("Form", u"Information Retrieval :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Amount of Files", None))
        self.Stemming_checkBox.setText(QCoreApplication.translate("Form", u"Porter Stemming", None))
        self.Stopwords_checkBox.setText(QCoreApplication.translate("Form", u"Stopwords", None))
        self.file_label_2.setText("")
        self.perform_pushButton.setText(QCoreApplication.translate("Form", u"Perform", None))
        ___qtablewidgetitem = self.Index_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Word", None));
        self.IgnoreCase_checkBox.setText(QCoreApplication.translate("Form", u"Ignore case", None))
        self.file_label_3.setText(QCoreApplication.translate("Form", u"Matching :", None))
        self.search_pushButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.Partial_checkBox.setText(QCoreApplication.translate("Form", u"Partial matching", None))
        self.Match_lineEdit.setText(QCoreApplication.translate("Form", u"COVID-19", None))
        ___qtablewidgetitem1 = self.Match_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Word", None));
        ___qtablewidgetitem2 = self.Match_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Document", None));
        ___qtablewidgetitem3 = self.Match_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Rows", None));
        self.Zipf_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Zipf_tab), QCoreApplication.translate("Form", u"Zipf Distribution", None))
        self.file_label_5.setText(QCoreApplication.translate("Form", u"Training model", None))
        ___qtablewidgetitem4 = self.CBOW_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Similarity word", None));
        ___qtablewidgetitem5 = self.CBOW_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Score", None));
        self.CBOWCompute_Button.setText(QCoreApplication.translate("Form", u"Execute", None))
        self.CBOWImage_label.setText("")
        self.Word2Vect_tabWidget.setTabText(self.Word2Vect_tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"CBOW Model", None))
        self.file_label_6.setText(QCoreApplication.translate("Form", u"Training model", None))
        ___qtablewidgetitem6 = self.Skipgram_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Similarity word", None));
        ___qtablewidgetitem7 = self.Skipgram_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Score", None));
        self.SkipgramCompute_Button.setText(QCoreApplication.translate("Form", u"Execute", None))
        self.SkipgramImage_label.setText("")
        self.Word2Vect_tabWidget.setTabText(self.Word2Vect_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Skip-gram Model", None))
        self.CostTime_Label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Word2Vect_tab), QCoreApplication.translate("Form", u"Word2Vec", None))
        ___qtablewidgetitem8 = self.TFIDF_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Word", None));
        ___qtablewidgetitem9 = self.TFIDF_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Doc1", None));
        ___qtablewidgetitem10 = self.TFIDF_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Doc2", None));
        ___qtablewidgetitem11 = self.TFIDF_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Doc3", None));
        ___qtablewidgetitem12 = self.TFIDF_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Doc4", None));
        ___qtablewidgetitem13 = self.TFIDF_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Doc5", None));
        ___qtablewidgetitem14 = self.TFIDF_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Doc6", None));
        ___qtablewidgetitem15 = self.TFIDF_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Doc7", None));
        ___qtablewidgetitem16 = self.TFIDF_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Doc8", None));
        ___qtablewidgetitem17 = self.TFIDF_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Doc9", None));
        ___qtablewidgetitem18 = self.TFIDF_tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Doc10", None));
        ___qtablewidgetitem19 = self.TFIDF_tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Doc11", None));
        ___qtablewidgetitem20 = self.TFIDF_tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Doc12", None));
        ___qtablewidgetitem21 = self.TFIDF_tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Doc13", None));
        ___qtablewidgetitem22 = self.TFIDF_tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Doc14", None));
        ___qtablewidgetitem23 = self.TFIDF_tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Doc15", None));
        ___qtablewidgetitem24 = self.TFIDF_tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"Doc16", None));
        ___qtablewidgetitem25 = self.TFIDF_tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Doc17", None));
        ___qtablewidgetitem26 = self.TFIDF_tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"Doc18", None));
        ___qtablewidgetitem27 = self.TFIDF_tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"Doc19", None));
        ___qtablewidgetitem28 = self.TFIDF_tableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"Doc20", None));
        ___qtablewidgetitem29 = self.TFIDF_tableWidget.horizontalHeaderItem(21)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"Doc21", None));
        ___qtablewidgetitem30 = self.TFIDF_tableWidget.horizontalHeaderItem(22)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"Doc22", None));
        ___qtablewidgetitem31 = self.TFIDF_tableWidget.horizontalHeaderItem(23)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"Doc23", None));
        ___qtablewidgetitem32 = self.TFIDF_tableWidget.horizontalHeaderItem(24)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"Doc24", None));
        ___qtablewidgetitem33 = self.TFIDF_tableWidget.horizontalHeaderItem(25)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"Doc25", None));
        ___qtablewidgetitem34 = self.TFIDF_tableWidget.horizontalHeaderItem(26)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"Doc26", None));
        ___qtablewidgetitem35 = self.TFIDF_tableWidget.horizontalHeaderItem(27)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"Doc27", None));
        ___qtablewidgetitem36 = self.TFIDF_tableWidget.horizontalHeaderItem(28)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"Doc28", None));
        ___qtablewidgetitem37 = self.TFIDF_tableWidget.horizontalHeaderItem(29)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"Doc29", None));
        ___qtablewidgetitem38 = self.TFIDF_tableWidget.horizontalHeaderItem(30)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"Doc30", None));
        ___qtablewidgetitem39 = self.TFIDF_tableWidget.horizontalHeaderItem(31)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"Doc31", None));
        ___qtablewidgetitem40 = self.TFIDF_tableWidget.horizontalHeaderItem(32)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Form", u"Doc32", None));
        ___qtablewidgetitem41 = self.TFIDF_tableWidget.horizontalHeaderItem(33)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Form", u"Doc33", None));
        ___qtablewidgetitem42 = self.TFIDF_tableWidget.horizontalHeaderItem(34)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Form", u"Doc34", None));
        ___qtablewidgetitem43 = self.TFIDF_tableWidget.horizontalHeaderItem(35)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Form", u"Doc35", None));
        ___qtablewidgetitem44 = self.TFIDF_tableWidget.horizontalHeaderItem(36)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Form", u"Doc36", None));
        ___qtablewidgetitem45 = self.TFIDF_tableWidget.horizontalHeaderItem(37)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Form", u"Doc37", None));
        ___qtablewidgetitem46 = self.TFIDF_tableWidget.horizontalHeaderItem(38)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Form", u"Doc38", None));
        ___qtablewidgetitem47 = self.TFIDF_tableWidget.horizontalHeaderItem(39)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Form", u"Doc40", None));
        ___qtablewidgetitem48 = self.TFIDF_tableWidget.horizontalHeaderItem(40)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Form", u"Doc41", None));
        ___qtablewidgetitem49 = self.TFIDF_tableWidget.horizontalHeaderItem(41)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Form", u"Doc42", None));
        ___qtablewidgetitem50 = self.TFIDF_tableWidget.horizontalHeaderItem(42)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Form", u"Doc43", None));
        ___qtablewidgetitem51 = self.TFIDF_tableWidget.horizontalHeaderItem(43)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Form", u"Doc44", None));
        ___qtablewidgetitem52 = self.TFIDF_tableWidget.horizontalHeaderItem(44)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Form", u"Doc45", None));
        ___qtablewidgetitem53 = self.TFIDF_tableWidget.horizontalHeaderItem(45)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Form", u"Doc46", None));
        ___qtablewidgetitem54 = self.TFIDF_tableWidget.horizontalHeaderItem(46)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Form", u"Doc47", None));
        ___qtablewidgetitem55 = self.TFIDF_tableWidget.horizontalHeaderItem(47)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Form", u"Doc48", None));
        ___qtablewidgetitem56 = self.TFIDF_tableWidget.horizontalHeaderItem(48)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Form", u"Doc49", None));
        ___qtablewidgetitem57 = self.TFIDF_tableWidget.horizontalHeaderItem(49)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Form", u"Doc50", None));
        ___qtablewidgetitem58 = self.TFIDF_tableWidget.horizontalHeaderItem(60)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Form", u"60", None));
        ___qtablewidgetitem59 = self.TFIDF_tableWidget.horizontalHeaderItem(70)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Form", u"70", None));
        ___qtablewidgetitem60 = self.TFIDF_tableWidget.horizontalHeaderItem(80)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Form", u"80", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"In Which Document", None))
        self.TFIDFCompute_Button.setText(QCoreApplication.translate("Form", u"Execute", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Method", None))
        self.TFIDF_Method_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Log-frequency weighting", None))
        self.TFIDF_Method_comboBox.setItemText(1, QCoreApplication.translate("Form", u"TF-IDF weighting", None))

        self.TFIDF_Formula_Label.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Rank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Weighting", None))
        self.Traindata_Button.setText(QCoreApplication.translate("Form", u"...", None))
        self.Traindata_lineEdit.setText(QCoreApplication.translate("Form", u"D:\\Training_CNBC_Data.txt", None))
        self.file_label_4.setText(QCoreApplication.translate("Form", u"Training Pattern", None))
        self.file_label_7.setText(QCoreApplication.translate("Form", u"Word : ", None))
        self.SimilarWord_comboBox.setItemText(0, QCoreApplication.translate("Form", u"omicron", None))
        self.SimilarWord_comboBox.setItemText(1, QCoreApplication.translate("Form", u"market", None))
        self.SimilarWord_comboBox.setItemText(2, QCoreApplication.translate("Form", u"travel", None))
        self.SimilarWord_comboBox.setItemText(3, QCoreApplication.translate("Form", u"variant", None))
        self.SimilarWord_comboBox.setItemText(4, QCoreApplication.translate("Form", u"covid", None))

        self.TFIDF_checkBox.setText(QCoreApplication.translate("Form", u"Weighting Computing", None))
    # retranslateUi

