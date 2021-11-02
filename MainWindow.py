# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(661, 601)
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
        self.func_comboBox.setObjectName(u"func_comboBox")
        self.func_comboBox.setGeometry(QRect(10, 40, 341, 21))
        self.func_comboBox.setDuplicatesEnabled(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 16, 291, 20))
        self.file_label = QLabel(Form)
        self.file_label.setObjectName(u"file_label")
        self.file_label.setGeometry(QRect(10, 70, 151, 16))
        self.file_progressBar = QProgressBar(Form)
        self.file_progressBar.setObjectName(u"file_progressBar")
        self.file_progressBar.setGeometry(QRect(10, 90, 381, 23))
        self.file_progressBar.setValue(24)
        self.Index_tableWidget = QTableWidget(Form)
        if (self.Index_tableWidget.columnCount() < 3):
            self.Index_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Index_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Index_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Index_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Index_tableWidget.setObjectName(u"Index_tableWidget")
        self.Index_tableWidget.setGeometry(QRect(10, 140, 641, 301))
        self.Index_tableWidget.setFrameShadow(QFrame.Sunken)
        self.file_spinBox = QSpinBox(Form)
        self.file_spinBox.setObjectName(u"file_spinBox")
        self.file_spinBox.setGeometry(QRect(560, 40, 71, 22))
        self.file_spinBox.setReadOnly(False)
        self.file_spinBox.setAccelerated(True)
        self.file_spinBox.setMinimum(1)
        self.file_spinBox.setMaximum(1000)
        self.file_spinBox.setValue(25)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 40, 90, 16))
        self.Stemming_checkBox = QCheckBox(Form)
        self.Stemming_checkBox.setObjectName(u"Stemming_checkBox")
        self.Stemming_checkBox.setGeometry(QRect(510, 90, 141, 20))
        self.Stemming_checkBox.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/IR-System/resource/Stemming-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stemming_checkBox.setIcon(icon1)
        self.Stemming_checkBox.setChecked(False)
        self.Stopwords_checkBox = QCheckBox(Form)
        self.Stopwords_checkBox.setObjectName(u"Stopwords_checkBox")
        self.Stopwords_checkBox.setGeometry(QRect(400, 90, 101, 20))
        icon2 = QIcon()
        icon2.addFile(u":/IR-System/resource/stopwords-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stopwords_checkBox.setIcon(icon2)
        self.Stopwords_checkBox.setChecked(True)
        self.file_label_2 = QLabel(Form)
        self.file_label_2.setObjectName(u"file_label_2")
        self.file_label_2.setGeometry(QRect(50, 120, 151, 16))
        self.file_label_3 = QLabel(Form)
        self.file_label_3.setObjectName(u"file_label_3")
        self.file_label_3.setGeometry(QRect(10, 450, 61, 16))
        self.Match_tableWidget = QTableWidget(Form)
        if (self.Match_tableWidget.columnCount() < 3):
            self.Match_tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Match_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.Match_tableWidget.setObjectName(u"Match_tableWidget")
        self.Match_tableWidget.setGeometry(QRect(10, 480, 641, 111))
        self.Match_tableWidget.setAutoFillBackground(False)
        self.Match_tableWidget.setFrameShadow(QFrame.Sunken)
        self.Match_lineEdit = QLineEdit(Form)
        self.Match_lineEdit.setObjectName(u"Match_lineEdit")
        self.Match_lineEdit.setGeometry(QRect(80, 450, 161, 20))
        self.search_pushButton = QPushButton(Form)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(250, 450, 71, 20))
        icon3 = QIcon()
        icon3.addFile(u":/IR-System/resource/Search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_pushButton.setIcon(icon3)
        self.perform_pushButton = QPushButton(Form)
        self.perform_pushButton.setObjectName(u"perform_pushButton")
        self.perform_pushButton.setGeometry(QRect(360, 40, 81, 21))
        icon4 = QIcon()
        icon4.addFile(u":/IR-System/resource/Play-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perform_pushButton.setIcon(icon4)
        self.Partial_checkBox = QCheckBox(Form)
        self.Partial_checkBox.setObjectName(u"Partial_checkBox")
        self.Partial_checkBox.setGeometry(QRect(400, 450, 111, 20))
        icon5 = QIcon()
        icon5.addFile(u":/IR-System/resource/PartialSearch-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Partial_checkBox.setIcon(icon5)
        self.Partial_checkBox.setChecked(True)
        self.IgnoreCase_checkBox = QCheckBox(Form)
        self.IgnoreCase_checkBox.setObjectName(u"IgnoreCase_checkBox")
        self.IgnoreCase_checkBox.setGeometry(QRect(520, 450, 111, 20))
        self.IgnoreCase_checkBox.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/IR-System/resource/IgnoreCase-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IgnoreCase_checkBox.setIcon(icon6)
        self.IgnoreCase_checkBox.setChecked(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 53, 16))
        QWidget.setTabOrder(self.func_comboBox, self.file_spinBox)
        QWidget.setTabOrder(self.file_spinBox, self.Stemming_checkBox)
        QWidget.setTabOrder(self.Stemming_checkBox, self.Stopwords_checkBox)
        QWidget.setTabOrder(self.Stopwords_checkBox, self.Index_tableWidget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"IR-System", None))
        self.func_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Information Retrieval", None))
        self.func_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Contents Compare", None))
        self.func_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Zipf Distribution", None))
        self.func_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Matching", None))
        self.func_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Edit Distance", None))

        self.func_comboBox.setCurrentText(QCoreApplication.translate("Form", u"Information Retrieval", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pelease select perform function", None))
        self.file_label.setText(QCoreApplication.translate("Form", u"Information Retrieval", None))
        ___qtablewidgetitem = self.Index_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Word", None));
        ___qtablewidgetitem1 = self.Index_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Document", None));
        ___qtablewidgetitem2 = self.Index_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Rows", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Amount of Files", None))
        self.Stemming_checkBox.setText(QCoreApplication.translate("Form", u"Porter Stemming", None))
        self.Stopwords_checkBox.setText(QCoreApplication.translate("Form", u"Stopwords", None))
        self.file_label_2.setText("")
        self.file_label_3.setText(QCoreApplication.translate("Form", u"Matching :", None))
        ___qtablewidgetitem3 = self.Match_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Word", None));
        ___qtablewidgetitem4 = self.Match_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Document", None));
        ___qtablewidgetitem5 = self.Match_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Rows", None));
        self.Match_lineEdit.setText(QCoreApplication.translate("Form", u"COVID-19", None))
        self.search_pushButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.perform_pushButton.setText(QCoreApplication.translate("Form", u"Perform", None))
        self.Partial_checkBox.setText(QCoreApplication.translate("Form", u"Partial matching", None))
        self.IgnoreCase_checkBox.setText(QCoreApplication.translate("Form", u"Ignore case", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Index", None))
    # retranslateUi

