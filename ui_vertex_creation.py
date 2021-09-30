# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vertex_creationyJPWNr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_vertex(object):
    def setupUi(self, vertex):
        if not vertex.objectName():
            vertex.setObjectName(u"vertex")
        vertex.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(vertex)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 90, 291, 21))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy1.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy1)
        self.checkBox_2.setChecked(False)

        self.horizontalLayout.addWidget(self.checkBox_2)


        self.retranslateUi(vertex)

        QMetaObject.connectSlotsByName(vertex)
    # setupUi

    def retranslateUi(self, vertex):
        vertex.setWindowTitle(QCoreApplication.translate("vertex", u"Create Vertex", None))
        self.label.setText(QCoreApplication.translate("vertex", u"AB", None))
        self.checkBox.setText(QCoreApplication.translate("vertex", u"A", None))
        self.checkBox_2.setText(QCoreApplication.translate("vertex", u"B", None))
    # retranslateUi

