# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_database.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1001, 611)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);"))
        self.gridLayout_12 = QtGui.QGridLayout(Dialog)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.scrollArea_2 = QtGui.QScrollArea(Dialog)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 308, 265))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.toolButton = QtGui.QToolButton(self.scrollAreaWidgetContents_2)
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.toolButton_3 = QtGui.QToolButton(self.scrollAreaWidgetContents_2)
        self.toolButton_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.info_table = QtGui.QTableWidget(self.scrollAreaWidgetContents_2)
        self.info_table.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.info_table.setObjectName(_fromUtf8("info_table"))
        self.info_table.setColumnCount(0)
        self.info_table.setRowCount(0)
        self.gridLayout_2.addWidget(self.info_table, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_12.addWidget(self.scrollArea_2, 0, 2, 1, 1)
        self.scrollArea_3 = QtGui.QScrollArea(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 308, 264))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_11 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)
        self.peak_table = QtGui.QTableWidget(self.scrollAreaWidgetContents_3)
        self.peak_table.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.peak_table.setObjectName(_fromUtf8("peak_table"))
        self.peak_table.setColumnCount(0)
        self.peak_table.setRowCount(0)
        self.gridLayout_11.addWidget(self.peak_table, 1, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_12.addWidget(self.scrollArea_3, 1, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 539))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.molecules_table = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.molecules_table.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.molecules_table.setObjectName(_fromUtf8("molecules_table"))
        self.molecules_table.setColumnCount(0)
        self.molecules_table.setRowCount(0)
        self.gridLayout.addWidget(self.molecules_table, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_12.addWidget(self.scrollArea, 0, 1, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setMinimumSize(QtCore.QSize(100, 0))
        self.checkBox_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox_7.setStyleSheet(_fromUtf8(""))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_10.addWidget(self.checkBox_7, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setStyleSheet(_fromUtf8(""))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_10.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setStyleSheet(_fromUtf8(""))
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_10.addWidget(self.checkBox, 0, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setStyleSheet(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_10.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.gridLayout_10)
        self.label = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setMinimumSize(QtCore.QSize(100, 0))
        self.checkBox_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox_8.setStyleSheet(_fromUtf8(""))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.gridLayout_9.addWidget(self.checkBox_8, 0, 0, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_4.setStyleSheet(_fromUtf8(""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_9.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setStyleSheet(_fromUtf8(""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_9.addWidget(self.checkBox_5, 0, 1, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_6.setStyleSheet(_fromUtf8(""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_9.addWidget(self.checkBox_6, 1, 1, 1, 1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_9)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_7.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout_7.addWidget(self.radioButton_4, 0, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_7.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout_7.addWidget(self.radioButton_3, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtGui.QToolButton(self.groupBox_3)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.verticalLayout_3)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.gridLayout_8.addWidget(self.checkBox_9, 0, 0, 1, 1)
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.gridLayout_8.addWidget(self.checkBox_10, 1, 0, 1, 1)
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_8.addWidget(self.checkBox_11, 0, 1, 1, 1)
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.gridLayout_8.addWidget(self.checkBox_12, 1, 1, 1, 1)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.gridLayout_8)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayout_6.addWidget(self.checkBox_13, 0, 0, 1, 1)
        self.checkBox_14 = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.gridLayout_6.addWidget(self.checkBox_14, 1, 0, 1, 1)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.gridLayout_6)
        self.gridLayout_5.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.frame_2 = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(_fromUtf8("background-color: rgb(32, 32, 32);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.back_btn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.horizontalLayout_4.addWidget(self.back_btn)
        self.advanced_btn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advanced_btn.sizePolicy().hasHeightForWidth())
        self.advanced_btn.setSizePolicy(sizePolicy)
        self.advanced_btn.setStyleSheet(_fromUtf8("background-color: rgb(1, 133, 116);"))
        self.advanced_btn.setObjectName(_fromUtf8("advanced_btn"))
        self.horizontalLayout_4.addWidget(self.advanced_btn)
        self.gridLayout_12.addWidget(self.frame_2, 2, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_6.setText(_translate("Dialog", "Info", None))
        self.toolButton.setText(_translate("Dialog", "Edit", None))
        self.toolButton_3.setText(_translate("Dialog", "Save", None))
        self.label_11.setText(_translate("Dialog", "Peak Information", None))
        self.label_5.setText(_translate("Dialog", "Molecule Entries", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Filter", None))
        self.label_2.setText(_translate("Dialog", "Category", None))
        self.checkBox_7.setText(_translate("Dialog", "All", None))
        self.checkBox_3.setText(_translate("Dialog", "Experiment", None))
        self.checkBox.setText(_translate("Dialog", "Known", None))
        self.checkBox_2.setText(_translate("Dialog", "Artifact", None))
        self.label.setText(_translate("Dialog", "Frequency", None))
        self.checkBox_8.setText(_translate("Dialog", "All", None))
        self.checkBox_4.setText(_translate("Dialog", "MHz", None))
        self.checkBox_5.setText(_translate("Dialog", "GHz", None))
        self.checkBox_6.setText(_translate("Dialog", "cm -1", None))
        self.label_3.setText(_translate("Dialog", "Temperature", None))
        self.groupBox.setTitle(_translate("Dialog", "Min", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Max", None))
        self.label_7.setText(_translate("Dialog", "Composition", None))
        self.radioButton_2.setText(_translate("Dialog", "Is exactly", None))
        self.radioButton_4.setText(_translate("Dialog", "All", None))
        self.radioButton.setText(_translate("Dialog", "Has", None))
        self.radioButton_3.setText(_translate("Dialog", "Does not have", None))
        self.lineEdit_2.setText(_translate("Dialog", "--", None))
        self.toolButton_2.setText(_translate("Dialog", "...", None))
        self.label_9.setText(_translate("Dialog", "Experiment Type", None))
        self.checkBox_9.setText(_translate("Dialog", "Discharge", None))
        self.checkBox_10.setText(_translate("Dialog", "Stable", None))
        self.checkBox_11.setText(_translate("Dialog", "Heated Nozzle", None))
        self.checkBox_12.setText(_translate("Dialog", "Laser Ablation", None))
        self.label_10.setText(_translate("Dialog", "Other", None))
        self.checkBox_13.setText(_translate("Dialog", "isotopes", None))
        self.checkBox_14.setText(_translate("Dialog", "vibrational", None))
        self.back_btn.setText(_translate("Dialog", "Back to Main Menu", None))
        self.advanced_btn.setText(_translate("Dialog", "Advanced ...", None))

