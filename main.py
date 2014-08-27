import sys
from PyQt4 import QtCore, QtGui

def main():
	app = QtGui.QApplication(sys.argv)
	w = QtGui.QWidget()
	screen = QtGui.QDesktopWidget().screenGeometry()
	w.resize(screen.width(),screen.height())
	w.setWindowTitle('Train Traffic Simulator')
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()