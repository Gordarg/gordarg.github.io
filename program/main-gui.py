import os
import os.path
import pwd
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem, QInputDialog, QLineEdit, QApplication, QMessageBox
from PyQt5.QtGui import QIcon

import gui
import main

dir_path = os.path.split(os.path.abspath(os.path.dirname(os.path.realpath(__file__))))[0] + '/content'
_translate = QtCore.QCoreApplication.translate
current_dir = current_selected = dir_path
content = ''

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def reset_project_structure():
    ui.treeWidget.clear()

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
    reset_project_structure()
    load_project_structure(dir_path,ui.treeWidget)

def newFile():
    name = QInputDialog.getText(None,"New File","Enter the name")
    print('new file: ' + current_dir + "/" + name[0] + ".md")
    open(current_dir + "/" + name[0] + ".md", 'a').close()
    reset_project_structure()
    load_project_structure(dir_path,ui.treeWidget)

def delete():
    reply = QMessageBox.question(None, 'Delete File', 
        'Are you sure to delete following?\n' +
        current_selected
        , QMessageBox.Yes, QMessageBox.No)
    
    if reply == QMessageBox.Yes:
        if os.path.isdir(current_selected):
            shutil.rmtree(current_selected)
        else:
            os.remove(current_selected)
        
        reset_project_structure()
        load_project_structure(dir_path, ui.treeWidget)

def save():
    with open(current_selected, "w") as mdfile:
        print(ui.plainTextEdit.toPlainText(), file = mdfile)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Save file")
        msgBox.setText("Changes saved to:\n" + current_selected)
        msgBox.setInformativeText("Use button below to access previous content")
        msgBox.setDetailedText(content)
        msgBox.exec_()

def selectionChanged():
    global content
    if len(ui.treeWidget.selectedItems()) < 1:
        print ('selection cleared')
        return
    it = ui.treeWidget.selectedItems()[0]
    global current_dir
    global current_selected
    current_dir = current_selected = getItemFullPath(it)
    if os.path.isfile(current_selected):
        current_dir = os.path.dirname(current_selected)
    print('working directory: ' + current_dir)
    print('selected file/folder: ' + current_selected)
    ui.statusbar.showMessage(get_username() + ': ' + current_selected)
    if os.path.isfile(current_selected):
        with open(current_selected) as f:
            content = ''.join(f.readlines())
            ui.plainTextEdit.setPlainText(_translate("MainWindow", content))
    else:
        ui.plainTextEdit.setPlainText(_translate("MainWindow", ''))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    load_project_structure(
        dir_path
        ,ui.treeWidget)
    
    ui.treeWidget.itemSelectionChanged.connect(selectionChanged)
    ui.actionBuild.triggered.connect(main.Run)
    ui.actionFile.triggered.connect(newFile)
    ui.actionFolder.triggered.connect(newFolder)
    ui.actionDelete.triggered.connect(delete)
    ui.actionSave.triggered.connect(save)
    #TODO: Add rename

    MainWindow.show()
    sys.exit(app.exec_())