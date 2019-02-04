import os
import pwd

from PyQt5 import QtCore, QtGui, QtWidgets

import gui
import main

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]


def helloworld():
    print ('Hello World')

def load_project_structure(startpath, tree):
    from PyQt5.QtWidgets import QTreeWidgetItem
    from PyQt5.QtGui import QIcon
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
        out =  "../content/" + out
    return out;


def onItemClicked(it, col):
    # print(it, col, it.text(col))
    print(getItemFullPath(it))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    dir_path = os.path.split(os.path.abspath(os.path.dirname(os.path.realpath(__file__))))[0]
    load_project_structure(
        dir_path + '/content'
        ,ui.treeWidget)
    ui.statusbar.showMessage(get_username() + ': ' + dir_path)
    ui.treeWidget.itemClicked.connect(onItemClicked)
    ui.actionBuild.triggered.connect(main.Run)
    
    MainWindow.show()
    sys.exit(app.exec_())