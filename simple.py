import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()
win.resize(250, 150)
win.setWindowTitle('Simple')
win.show()

sys.exit(app.exec_())
