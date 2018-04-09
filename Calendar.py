"другий коммит"
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget, QLabel
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.label = QLabel()
        self.initUI()

    def initUI(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.setFirstDayOfWeek(QtCore.Qt.Monday)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        self.label = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
#вывод текущей даты
        self.lbl.move(450, 100)
        self.label.setText('Заходи у місті Вінниця')
        self.setFont(QFont('Comic Sans MS', 10))

# вывод окна
        self.setGeometry(300, 300, 580, 400)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.toString())



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()