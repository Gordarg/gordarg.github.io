import os
import os.path
import pwd

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem, QInputDialog, QLineEdit, QApplication
from PyQt5.QtGui import QIcon

import gui
import main

dir_path = os.path.split(os.path.abspath(os.path.dirname(os.path.realpath(__file__))))[0] + '/content'
_translate = QtCore.QCoreApplication.translate
current_dir = current_selected = dir_path

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]


def helloworld():
    print ('Hello World')

def load_project_structure(startpath, tree):
    for element in os.listdir(startpath):
        path_info = startpath + "/" + element
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        if os.path.isdir(path_info):
            load_project_structure(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon('folder.png'))
        else:
            parent_itm.setIcon(0, QIcon('file.png'))

def getItemFullPath(item):
    out = item.text(0)

    if item.parent():
        out = getItemFullPath(item.parent()) + "/" + out
    else:
        out =  dir_path + "/" + out
    return out

def newFolder():
    name = QInputDialog.getText(None,"New Folder","Enter the name")
    print ('new folder: ' + current_dir + "/" + name[0] + ".md")
    os.mkdir(current_dir + "/" + name[0])
    load_project_structure(dir_path,ui.treeWidget)

def newFile():
    name = QInputDialog.getText(None,"New File","Enter the name")
    print('new file: ' + current_dir + "/" + name[0] + ".md")
    open(current_dir + "/" + name[0] + ".md", 'a').close()
    load_project_structure(dir_path,ui.treeWidget)

def onItemClicked(it, col):
    # print(it, col, it.text(col))
    current_dir = current_selected = getItemFullPath(it)
    if os.path.isfile(current_selected):
        current_dir = os.path.dirname(current_selected)
    print(current_dir)
    ui.statusbar.showMessage(get_username() + ': ' + current_selected)
    if os.path.isfile(current_selected):
        with open(current_selected) as f:
            ui.plainTextEdit.setPlainText(_translate("MainWindow", ''.join(f.readlines())))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    load_project_structure(
        dir_path
        ,ui.treeWidget)
    ui.treeWidget.itemClicked.connect(onItemClicked)
    ui.actionBuild.triggered.connect(main.Run)
    ui.actionFile.triggered.connect(newFile)
    ui.actionFolder.triggered.connect(newFolder)

    MainWindow.show()
    sys.exit(app.exec_())