import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplicat: ion,
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def _init_ (self):
    super()._init_ ()
    uic.loadUi("UI.ui', self)
    self.paint = False
    self.pushButton.clicked.connect(self.draw_circle)


  def draw_circle(self):
    self.paint = True
    self.update()


  def paintEvent(self, event):
    if self paint:
      qp= QPainter(self)
      qp.begin(self)
      self.draw_random_circle(qp)
      qp.end()

  
  def draw_random circle(self, qp):
    qp.setBrush(QColor(255, 255, 0))
    diameter = random.randint(20, 100)
    x = random.randint(0, self.width() - diameter)
    y = random.randint(0, self.width() - diameter)
    qp.drawEllips(x, y, dameter, diameter)

    if __name__ == '__main__':
    app = QApplication(sys.argv)
    wt = WordTrick()
    wt.show()
    sys.exit(app.exec())

