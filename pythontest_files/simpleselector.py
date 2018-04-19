import sip
sip.setapi('QString', 2)
from PyQt4 import QtCore, QtGui, QtWebKit
from ui_window import Ui_Window
class SimpleSelector(QtGui.QWidget, Ui_Window):
    def __init__(self, parent=None):
        super(SimpleSelector, self).__init__(parent)
        self.setupUi(self)
        self._lastElements = []
    def on_elementLineEdit_returnPressed(self):
        frame = self.webView.page().mainFrame()
        document = frame.documentElement()
        elements = document.findAll(self.elementLineEdit.text())
        for element in self._lastElements:
            element.removeAttribute('style')
        for element in elements:
            element.setAttribute('style', 'background-color: #f0f090')
        self._lastElements = elements
    def on_highlightButton_clicked(self):
        self.on_elementLineEdit_returnPressed()
    def setUrl(self, url):
        self.webView.setUrl(url)
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = SimpleSelector()
    win.setUrl(QtCore.QUrl('http://opencircuitdesign.com/qflow/'))
    win.show()
    sys.exit(app.exec_())
