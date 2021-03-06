# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_file_verification.ui'
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
        Dialog.resize(985, 684)
        Dialog.setMinimumSize(QtCore.QSize(0, 9))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777214))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(48, 48, 48);\n"
"gridline-color: rgb(195, 195, 195);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.index_lbl = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.index_lbl.setFont(font)
        self.index_lbl.setObjectName(_fromUtf8("index_lbl"))
        self.gridLayout_2.addWidget(self.index_lbl, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 3, 2, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.file_name_lbl = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.file_name_lbl.setFont(font)
        self.file_name_lbl.setObjectName(_fromUtf8("file_name_lbl"))
        self.gridLayout_2.addWidget(self.file_name_lbl, 4, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 8, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancel_btn = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.ok_btn = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet(_fromUtf8("background-color: rgba(0, 128, 128, 154);"))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout.addWidget(self.ok_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.units_combobx = QtGui.QComboBox(Dialog)
        self.units_combobx.setEnabled(True)
        self.units_combobx.setObjectName(_fromUtf8("units_combobx"))
        self.gridLayout.addWidget(self.units_combobx, 3, 2, 1, 1)
        self.notes_lbl = QtGui.QLabel(Dialog)
        self.notes_lbl.setObjectName(_fromUtf8("notes_lbl"))
        self.gridLayout.addWidget(self.notes_lbl, 14, 0, 1, 1)
        self.category_lbl = QtGui.QLabel(Dialog)
        self.category_lbl.setObjectName(_fromUtf8("category_lbl"))
        self.gridLayout.addWidget(self.category_lbl, 2, 0, 1, 1)
        self.compostition_lbl = QtGui.QLabel(Dialog)
        self.compostition_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.compostition_lbl.setObjectName(_fromUtf8("compostition_lbl"))
        self.gridLayout.addWidget(self.compostition_lbl, 4, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.artifact_rdio = QtGui.QRadioButton(Dialog)
        self.artifact_rdio.setObjectName(_fromUtf8("artifact_rdio"))
        self.verticalLayout_2.addWidget(self.artifact_rdio)
        self.known_rdio = QtGui.QRadioButton(Dialog)
        self.known_rdio.setObjectName(_fromUtf8("known_rdio"))
        self.verticalLayout_2.addWidget(self.known_rdio)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 1)
        self.units_lbl = QtGui.QLabel(Dialog)
        self.units_lbl.setObjectName(_fromUtf8("units_lbl"))
        self.gridLayout.addWidget(self.units_lbl, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.temperature_spinbx = QtGui.QDoubleSpinBox(Dialog)
        self.temperature_spinbx.setObjectName(_fromUtf8("temperature_spinbx"))
        self.horizontalLayout_2.addWidget(self.temperature_spinbx)
        self.temperature_units_chkbx = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature_units_chkbx.sizePolicy().hasHeightForWidth())
        self.temperature_units_chkbx.setSizePolicy(sizePolicy)
        self.temperature_units_chkbx.setMaximumSize(QtCore.QSize(50, 16777215))
        self.temperature_units_chkbx.setObjectName(_fromUtf8("temperature_units_chkbx"))
        self.horizontalLayout_2.addWidget(self.temperature_units_chkbx)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.vibrational_chkbx = QtGui.QCheckBox(Dialog)
        self.vibrational_chkbx.setObjectName(_fromUtf8("vibrational_chkbx"))
        self.verticalLayout.addWidget(self.vibrational_chkbx)
        self.gridLayout.addLayout(self.verticalLayout, 7, 2, 1, 1)
        self.other_lbl = QtGui.QLabel(Dialog)
        self.other_lbl.setObjectName(_fromUtf8("other_lbl"))
        self.gridLayout.addWidget(self.other_lbl, 7, 0, 1, 1)
        self.isotope_chkbx = QtGui.QCheckBox(Dialog)
        self.isotope_chkbx.setObjectName(_fromUtf8("isotope_chkbx"))
        self.gridLayout.addWidget(self.isotope_chkbx, 8, 2, 1, 1)
        self.name_lbl = QtGui.QLabel(Dialog)
        self.name_lbl.setObjectName(_fromUtf8("name_lbl"))
        self.gridLayout.addWidget(self.name_lbl, 1, 0, 1, 1)
        self.temperature_lbl = QtGui.QLabel(Dialog)
        self.temperature_lbl.setObjectName(_fromUtf8("temperature_lbl"))
        self.gridLayout.addWidget(self.temperature_lbl, 6, 0, 1, 1)
        self.name_txt = QtGui.QLineEdit(Dialog)
        self.name_txt.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(25, 25, 25);"))
        self.name_txt.setObjectName(_fromUtf8("name_txt"))
        self.gridLayout.addWidget(self.name_txt, 1, 2, 1, 1)
        self.notes_txt = QtGui.QLineEdit(Dialog)
        self.notes_txt.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(25, 25, 25);"))
        self.notes_txt.setObjectName(_fromUtf8("notes_txt"))
        self.gridLayout.addWidget(self.notes_txt, 14, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.composition_txt = QtGui.QLineEdit(Dialog)
        self.composition_txt.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(25, 25, 25);"))
        self.composition_txt.setObjectName(_fromUtf8("composition_txt"))
        self.horizontalLayout_3.addWidget(self.composition_txt)
        self.compostion_btn = QtGui.QToolButton(Dialog)
        self.compostion_btn.setObjectName(_fromUtf8("compostion_btn"))
        self.horizontalLayout_3.addWidget(self.compostion_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.index_lbl.setText(_translate("Dialog", "(1/1)", None))
        self.label_7.setText(_translate("Dialog", "Enter Data for the Following:", None))
        self.file_name_lbl.setText(_translate("Dialog", "File Name", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))
        self.ok_btn.setText(_translate("Dialog", "OK", None))
        self.notes_lbl.setText(_translate("Dialog", "Notes: ", None))
        self.category_lbl.setText(_translate("Dialog", "*Category:", None))
        self.compostition_lbl.setText(_translate("Dialog", "*Composition: ", None))
        self.artifact_rdio.setText(_translate("Dialog", "Artifact", None))
        self.known_rdio.setText(_translate("Dialog", "Known", None))
        self.units_lbl.setText(_translate("Dialog", "*Units", None))
        self.vibrational_chkbx.setText(_translate("Dialog", "Vibrational", None))
        self.other_lbl.setText(_translate("Dialog", "Other", None))
        self.isotope_chkbx.setText(_translate("Dialog", "Isotope", None))
        self.name_lbl.setText(_translate("Dialog", "*Name of Entry:", None))
        self.temperature_lbl.setText(_translate("Dialog", "Temperature: ", None))
        self.compostion_btn.setText(_translate("Dialog", "...", None))

