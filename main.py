import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Circles(QWidget):
    def __init__(self):
        super(Circles, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    @staticmethod
    def draw_circle(qp):
        diam = random.randrange(1, 361)
        x = random.randrange(1, 512 - diam)
        y = random.randrange(1, 361 - diam)
        qp.setBrush(QColor('yellow'))
        qp.setPen(QColor('yellow'))
        qp.drawEllipse(x, y, diam, diam)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Circles()
    wnd.show()
    sys.exit(app.exec())





