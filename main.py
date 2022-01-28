import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class addEditCoffeeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.connection = sqlite3.connect("coffee.sqlite")
        self.modified = {}
        self.titles = None

        self.pushButtonEdit.clicked.connect(self.start_edit)
        self.pushButtonAdd.clicked.connect(self.add_row)
        self.pushButtonSave.clicked.connect(self.save_row)
        self.tableWidget.itemChanged.connect(self.item_changed)

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_row(self):
        if self.modified:
            cur = self.connection.cursor()
            que = "UPDATE coffee SET\n"
            que += ", ".join([f"\'{key}\'='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += " WHERE ID=?"
            print(que)
            cur.execute(que, (self.spinBox.text(), ))
            self.connection.commit()
            self.modified.clear()

    def add_row(self):
        pass

    def start_edit(self):
        cur = self.connection.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM coffee WHERE ID=?",
                             (item_id := self.spinBox.text(), )).fetchall()

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        if not result:
            self.label_info.setText('Ничего не нашлось')
            return
        else:
            self.label_info.setText(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.connection = sqlite3.connect("coffee.sqlite")

        self.pushButton.clicked.connect(self.select_data)

        self.textEdit.setPlainText("SELECT * FROM coffee")

        self.select_data()

        self.pushButtonEdit.clicked.connect(self.addEdit)

        self.addEditCoffee = addEditCoffeeForm()

    def addEdit(self):
        self.addEditCoffee.show()

    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        query = self.textEdit.toPlainText()
        res = self.connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())