import sys
from PyQt4 import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    
    # create the screen object
    screen = QtGui.QDesktopWidget().screenGeometry()
    
    
    # assign height and width of desktop screen to the widget
    w = QtGui.QWidget()
    w.resize(screen.width(),screen.height())
    w.setWindowTitle('Train Traffic Simulator')

    # Time slider
    slider = QtGui.QSlider(1, w)
    slider.setRange(0, 2359)
    slider.setSingleStep(10)
    slider.resize(500, 20)
    slider.move(200, 57)

    # Start button
    sbtn = QtGui.QPushButton('Start Simulation', w)
    sbtn.setToolTip('Click to start simulation')
    sbtn.resize(sbtn.sizeHint())
    sbtn.move(50, 50)
    
    # Quit button
    qbtn = QtGui.QPushButton('Quit', w)
    qbtn.setToolTip('Quit Application')
    qbtn.resize(sbtn.sizeHint())
    qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    qbtn.move(screen.width()-170, screen.height()-70)


    
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()