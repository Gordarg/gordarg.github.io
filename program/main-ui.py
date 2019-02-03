from PyQt5 import QtCore, QtGui, QtWidgets
import gui

def load_project_structure(startpath, tree):
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
            load_project_structure(path_info, parent_itm)
            # parent_itm.setIcon(0, QIcon('assets/folder.ico'))
        # else:
            # parent_itm.setIcon(0, QIcon('assets/file.ico'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    load_project_structure("/var/www/html",ui.treeWidget)
    MainWindow.show()
    sys.exit(app.exec_())