from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        lay = QtWidgets.QVBoxLayout(self)
        tree = QtWidgets.QTreeWidget()
        tree.setColumnCount(2)
        lay.addWidget(tree)

        for i in range(4):
            parent_it = QtWidgets.QTreeWidgetItem(["{}-{}".format(i, l) for l in range(2)])
            tree.addTopLevelItem(parent_it)
            for j in range(5):
                it = QtWidgets.QTreeWidgetItem(["{}-{}-{}".format(i, j, l) for l in range(2)])
                parent_it.addChild(it)
        tree.expandAll()

        tree.itemClicked.connect(self.onItemClicked)

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def onItemClicked(self, it, col):
        print(it, col, it.text(col))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
