# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 10, 481, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 10, 256, 351))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setWhatsThis("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionFolder = QtWidgets.QAction(MainWindow)
        self.actionFolder.setObjectName("actionFolder")
        self.menuNew.addAction(self.actionFile)
        self.menuNew.addAction(self.actionFolder)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def load_project_structure(self, startpath, tree):
        # cc: https://stackoverflow.com/questions/5144830
        """
        Load Project structure tree
        :param startpath: 
        :param tree: 
        :return: 
        """
        import os
        from PyQt5.QtWidgets import QTreeWidgetItem
        from PyQt5.QtGui import QIcon
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                self.load_project_structure(path_info, parent_itm)
                # parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            # else:
                # parent_itm.setIcon(0, QIcon('assets/file.ico'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open Project"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionFolder.setText(_translate("MainWindow", "Folder"))
        self.load_project_structure("/var/www/html",self.treeWidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

