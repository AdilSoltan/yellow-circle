import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from design import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super(Circles, self).__init__()
        self.setupUi(self)
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
        for _ in range(random.randrange(1, 10)):
            diam = random.randrange(1, 200)
            x = random.randrange(1, 512 - diam)
            y = random.randrange(1, 361 - diam)
            color = QColor(*[random.randint(0, 255) for _ in range(3)])
            qp.setBrush(color)
            qp.setPen(color)
            qp.drawEllipse(x, y, diam, diam)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Circles()
    wnd.show()
    sys.exit(app.exec())





