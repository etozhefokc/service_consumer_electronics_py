import xml.etree.ElementTree as xml

import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QDialog, QMessageBox, QFileDialog

import sys

from PyQt5.uic.uiparser import QtCore


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Login")
        self.setFixedSize(300, 400)

        self.m_text = QtWidgets.QLabel(self)
        self.m_text.setText("Авторизация")
        self.m_text.move(10, 5)

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Логин")
        self.m_text2.move(10, 35)

        self.n_text = QtWidgets.QLineEdit(self)
        self.n_text.setFixedWidth(280)
        self.n_text.setPlaceholderText("Введите логин")
        self.n_text.move(10, 65)

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Пароль")
        self.m_text3.move(10, 95)

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите пароль")
        self.n_text2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.n_text2.move(10, 125)

        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.move(10, 165)
        self.btn_l.setText("Войти")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.login)

    def login(self):
        cursor = dbs.cursor()
        query = "SELECT * FROM `performers` WHERE `username` = '" + self.n_text.text() + \
                "' AND `password` = '" + self.n_text2.text() + "'"
        cursor.execute(query)
        for r in cursor:
            print(r)

        if cursor.execute(query) == 1:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Неправильный логин или пароль')


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Софт-Мастер")
        self.setFixedSize(1090, 500)

        self.centralwidget = QtWidgets.QWidget()
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.blayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.h1layout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.h2layout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)

        self.tablechoose = QtWidgets.QComboBox(self.verticalLayoutWidget)

        self.tablechoose.setFixedWidth(200)
        self.tablechoose.addItem("Заявки")
        self.tablechoose.addItem("Специалисты")
        self.tablechoose.addItem("Клиенты")
        self.tablechoose.currentTextChanged.connect(self.on_currentIndexChanged)
        self.tablechoose.currentTextChanged.connect(self.updatetable)
        self.tablechoose.currentTextChanged.connect(self.updatetable)

        self.updatebtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.updatebtn.setText("Обновить")
        self.updatebtn.setFixedWidth(150)
        self.updatebtn.clicked.connect(self.updatetable)

        self.updbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.updbtn.setText("Редактировать заявку")
        self.updbtn.setFixedWidth(150)
        self.updbtn.clicked.connect(self.updtablewindow)

        self.insertbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.insertbtn.setText("Добавить заявку")
        self.insertbtn.setFixedWidth(150)
        self.insertbtn.clicked.connect(self.inserttablewindow)

        self.deletebtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deletebtn.setText("Удалить заявку")
        self.deletebtn.setFixedWidth(150)
        self.deletebtn.clicked.connect(self.deletewindow)

        self.savebtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.savebtn.setText("Отчет по заявкам")
        self.savebtn.setFixedWidth(150)
        self.savebtn.clicked.connect(self.savewindow)

        self.printbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.printbtn.setText("Печать заявок")
        self.printbtn.setFixedWidth(150)

        self.printbtn.clicked.connect(self.printwindow)

        self.sortbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sortbtn.setText("Отсортировать заявки")
        self.sortbtn.setFixedWidth(150)

        self.exitbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitbtn.setText("Выход")
        self.exitbtn.setFixedWidth(150)

        self.exitbtn.clicked.connect(self.close)

        self.table1 = QtWidgets.QTableWidget()
        self.table1.setRowCount(10)
        self.table1.setColumnCount(4)

        self.table1.setFixedWidth(917)
        self.table1.setFixedHeight(400)

        self.table1.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table1.selectionModel().selectionChanged.connect(self.on_selection)

        self.h1layout.addWidget(self.tablechoose)
        self.h1layout.addSpacing(1075)

        self.blayout.addWidget(self.updatebtn)
        self.blayout.addWidget(self.updbtn)
        self.blayout.addWidget(self.insertbtn)
        self.blayout.addWidget(self.deletebtn)
        self.blayout.addWidget(self.sortbtn)
        self.blayout.addWidget(self.savebtn)
        self.blayout.addWidget(self.printbtn)
        self.blayout.addWidget(self.exitbtn)
        self.blayout.addSpacing(170)

        self.h2layout.addLayout(self.blayout)
        self.h2layout.addWidget(self.table1)
        self.h2layout.addSpacing(200)

        self.vlayout.addLayout(self.h1layout)
        self.vlayout.addLayout(self.h2layout)

        self.setCentralWidget(self.centralwidget)
        self.on_currentIndexChanged(1)
        self.updatetable()
        self.updatetable()

        self.updtablewindow_inst0 = UpdWindow0(self)
        self.updtablewindow_inst1 = UpdWindow1(self)
        self.updtablewindow_inst2 = UpdWindow2(self)
        self.insertwindow_inst0 = InsertWindow0(self)
        self.insertwindow_inst1 = InsertWindow1(self)
        self.insertwindow_inst2 = InsertWindow2(self)
        self.deletewindow_inst = DeleteWindow(self)

    def updtablewindow(self):
        if self.on_currentIndexChanged(0) == 0:
            self.updtablewindow_inst0.setModal(True)
            self.updtablewindow_inst0.exec()
        if self.on_currentIndexChanged(0) == 1:
            self.updtablewindow_inst1.setModal(True)
            self.updtablewindow_inst1.exec()
        if self.on_currentIndexChanged(0) == 2:
            self.updtablewindow_inst2.setModal(True)
            self.updtablewindow_inst2.exec()

    def deletewindow(self):
        self.deletewindow_inst.setModal(True)
        self.deletewindow_inst.exec()

    def inserttablewindow(self):
        if self.on_currentIndexChanged(0) == 0:
            self.insertwindow_inst0.setModal(True)
            self.insertwindow_inst0.exec()
        elif self.on_currentIndexChanged(0) == 1:
            self.insertwindow_inst1.setModal(True)
            self.insertwindow_inst1.exec()
        elif self.on_currentIndexChanged(0) == 2:
            self.insertwindow_inst2.setModal(True)
            self.insertwindow_inst2.exec()

    def printwindow(self, limit):
        sql_connect(host, port, user, passwd, database)
        cursor = dbs.cursor()
        if self.on_currentIndexChanged(0) == 0:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='things'"
        if self.on_currentIndexChanged(0) == 1:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='performers'"
        if self.on_currentIndexChanged(0) == 2:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='clients'"
        limit = cursor.execute(query)
        s1 = ""
        l = 1
        for r in cursor:
            if l != limit:
                s1 += '"' + str(r[0]) + '",'
                l += 1
            else:
                s1 += '"' + str(r[0]) + '"'
            print(r)
        limit = self.table1.rowCount()
        if self.on_currentIndexChanged(0) == 1 or self.on_currentIndexChanged(0) == 2:
            for i in range(0, limit):
                pole0 = str(self.table1.model().index(i, 0).data())
                pole1 = str(self.table1.model().index(i, 1).data())
                pole2 = str(self.table1.model().index(i, 2).data())
                pole3 = str(self.table1.model().index(i, 3).data())
                s1 += "\n" + '"' + pole0 + '","' + pole1 + '","' + pole2 + '","' + pole3 + '"'
        if self.on_currentIndexChanged(0) == 0:
            for i in range(0, limit):
                pole0 = str(self.table1.model().index(i, 0).data())
                pole1 = str(self.table1.model().index(i, 1).data())
                pole2 = str(self.table1.model().index(i, 2).data())
                pole3 = str(self.table1.model().index(i, 3).data())
                pole4 = str(self.table1.model().index(i, 4).data())
                pole5 = str(self.table1.model().index(i, 5).data())
                pole6 = str(self.table1.model().index(i, 6).data())
                pole7 = str(self.table1.model().index(i, 7).data())
                pole8 = str(self.table1.model().index(i, 8).data())
                s1 += "\n" + '"' + pole0 + '","' + pole1 + '","' + pole2 + '","' + pole3 + '","' + pole4 + '","' + pole5 + '","' + pole6 + '","' + pole7 + '","' + pole8 + '"'
        print(s1)
        editor = QtWidgets.QTextEdit(self)
        editor.setPlainText(s1)
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            editor.document().print_(dialog.printer())

    def savewindow(self, limit):
        sql_connect(host, port, user, passwd, database)
        cursor = dbs.cursor()
        if self.on_currentIndexChanged(0) == 0:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='things'"
        if self.on_currentIndexChanged(0) == 1:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='performers'"
        if self.on_currentIndexChanged(0) == 2:
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='clients'"
        limit = cursor.execute(query)
        s1 = ""
        l = 1
        for r in cursor:
            if l != limit:
                s1 += '"' + str(r[0]) + '",'
                l += 1
            else:
                s1 += '"' + str(r[0]) + '"'
            print(r)
        limit = self.table1.rowCount()
        if self.on_currentIndexChanged(0) == 1 or self.on_currentIndexChanged(0) == 2:
            for i in range(0, limit):
                pole0 = str(self.table1.model().index(i, 0).data())
                pole1 = str(self.table1.model().index(i, 1).data())
                pole2 = str(self.table1.model().index(i, 2).data())
                pole3 = str(self.table1.model().index(i, 3).data())
                s1 += "\n" + '"' + pole0 + '","' + pole1 + '","' + pole2 + '","' + pole3 + '"'
        if self.on_currentIndexChanged(0) == 0:
            for i in range(0, limit):
                pole0 = str(self.table1.model().index(i, 0).data())
                pole1 = str(self.table1.model().index(i, 1).data())
                pole2 = str(self.table1.model().index(i, 2).data())
                pole3 = str(self.table1.model().index(i, 3).data())
                pole4 = str(self.table1.model().index(i, 4).data())
                pole5 = str(self.table1.model().index(i, 5).data())
                pole6 = str(self.table1.model().index(i, 6).data())
                pole7 = str(self.table1.model().index(i, 7).data())
                pole8 = str(self.table1.model().index(i, 8).data())
                s1 += "\n" + '"' + pole0 + '","' + pole1 + '","' + pole2 + '","' + pole3 + '","' + pole4 + '","' + pole5 + '","' + pole6 + '","' + pole7 + '","' + pole8 + '"'
        print(s1)
        name = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить отчет", "", "Файлы CSV (*.csv);;Все файлы (*)")
        if name:
            print(name)
            if name[0] != '':
                file = open(name[0], 'w')
                text = s1
                file.write(text)
                file.close()
            else:
                pass

    def updatetable(self):
        if self.on_currentIndexChanged(0) == 0:
            sql_connect(host, port, user, passwd, database)
            cursor = dbs.cursor()
            query = "SELECT * FROM `things`"
            cursor.execute(query)
            limit = cursor.execute(query)
            tableindex = 0
            self.table1.setColumnCount(9)
            for r in cursor:
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(r[0])))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(str(r[1])))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(r[2])))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(r[3])))
                self.table1.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(str(r[4])))
                self.table1.setItem(tableindex, 5, QtWidgets.QTableWidgetItem(str(r[5])))
                self.table1.setItem(tableindex, 6, QtWidgets.QTableWidgetItem(str(r[6])))
                self.table1.setItem(tableindex, 7, QtWidgets.QTableWidgetItem(str(r[7])))
                self.table1.setItem(tableindex, 8, QtWidgets.QTableWidgetItem(str(r[8])))

                self.table1.setRowHeight(tableindex, 10)
                tableindex += 1
                print(r)
            self.table1.setRowCount(limit)
            self.table1.setCurrentCell(0, 0)
            for tableindex in range(tableindex, 30):
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 5, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 6, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 7, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 8, QtWidgets.QTableWidgetItem(""))

            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='things'"
            limit = cursor.execute(query)
            s1 = ""
            l = 0
            for r in cursor:
                self.table1.setHorizontalHeaderItem(l, QtWidgets.QTableWidgetItem(str(r[0])))
                l += 1

        if self.on_currentIndexChanged(0) == 1:
            sql_connect(host, port, user, passwd, database)
            cursor = dbs.cursor()
            query = "SELECT * FROM `performers`"
            cursor.execute(query)
            limit = cursor.execute(query)
            tableindex = 0
            self.table1.setColumnCount(4)
            for r in cursor:
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(r[0])))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(r[1]))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(r[2]))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(r[3])))

                self.table1.setRowHeight(tableindex, 10)
                tableindex += 1
                print(r)
            self.table1.setRowCount(limit)
            self.table1.setCurrentCell(0, 0)
            for tableindex in range(tableindex, 30):
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(""))

            cursor1 = dbs.cursor()
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='performers'"
            limit = cursor1.execute(query)
            s1 = ""
            l = 0
            for r in cursor1:
                self.table1.setHorizontalHeaderItem(l, QtWidgets.QTableWidgetItem(str(r[0])))
                l += 1
        if self.on_currentIndexChanged(0) == 2:
            sql_connect(host, port, user, passwd, database)
            cursor = dbs.cursor()
            query = "SELECT * FROM `clients`"
            cursor.execute(query)
            limit = cursor.execute(query)
            tableindex = 0
            self.table1.setColumnCount(4)
            for r in cursor:
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(r[0])))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(r[1]))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(r[2]))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(r[3])))

                self.table1.setRowHeight(tableindex, 10)
                tableindex += 1
                print(r)
            self.table1.setRowCount(limit)
            self.table1.setCurrentCell(0, 0)
            for tableindex in range(tableindex, 30):
                self.table1.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(""))
                self.table1.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(""))

            cursor1 = dbs.cursor()
            query = "select `COLUMNS`.`COLUMN_NAME` from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='clients'"
            limit = cursor1.execute(query)
            s1 = ""
            l = 0
            for r in cursor1:
                self.table1.setHorizontalHeaderItem(l, QtWidgets.QTableWidgetItem(str(r[0])))
                l += 1
        return limit

    def on_selection(self, selected):
        global s_row
        for ix in selected.indexes():
            if ix.column() == 0:
                s_row = ix.row()
        return s_row

    def on_currentIndexChanged(self, index):
        if index == "Заявки":
            self.tablechoose.setCurrentIndex(0)
        elif index == "Специалисты":
            self.tablechoose.setCurrentIndex(1)
        elif index == "Клиенты":
            self.tablechoose.setCurrentIndex(2)
        print(self.tablechoose.currentIndex())
        return self.tablechoose.currentIndex()


class UpdWindow0(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 480)

        self.m_text0 = QtWidgets.QLabel(self)
        self.m_text0.setText("Id")
        self.n_text0 = QtWidgets.QLineEdit(self)
        self.n_text0.setFixedWidth(280)
        self.n_text0.setPlaceholderText("Введите Id")

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.m_text1 = QtWidgets.QLabel(self)

        self.m_text1.setText("Назавание")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите назавание")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Важность")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите важность")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Дата получения ГГГГ-ММ-ДД")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Введите дату получения")

        self.m_text4 = QtWidgets.QLabel(self)
        self.m_text4.setText("Дата выдачи ГГГГ-ММ-ДД")

        self.n_text4 = QtWidgets.QLineEdit(self)
        self.n_text4.setFixedWidth(280)
        self.n_text4.setPlaceholderText("Введите дату выдачи")

        self.m_text5 = QtWidgets.QLabel(self)
        self.m_text5.setText("Статус")

        self.n_text5 = QtWidgets.QLineEdit(self)
        self.n_text5.setFixedWidth(280)
        self.n_text5.setPlaceholderText("Статус")

        self.m_text6 = QtWidgets.QLabel(self)
        self.m_text6.setText("Тип")

        self.n_text6 = QtWidgets.QLineEdit(self)
        self.n_text6.setFixedWidth(280)
        self.n_text6.setPlaceholderText("Введите тип")

        self.m_text7 = QtWidgets.QLabel(self)
        self.m_text7.setText("ID специалиста")

        self.n_text7 = QtWidgets.QLineEdit(self)
        self.n_text7.setFixedWidth(280)
        self.n_text7.setPlaceholderText("Введите ID специалиста")

        self.m_text8 = QtWidgets.QLabel(self)
        self.m_text8.setText("ID клиента")

        self.n_text8 = QtWidgets.QLineEdit(self)
        self.n_text8.setFixedWidth(280)
        self.n_text8.setPlaceholderText("ID клиента")

        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.setText("Добавить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.upd_in_db)

        self.vlayout.addWidget(self.m_text0)
        self.vlayout.addWidget(self.n_text0)
        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)
        self.vlayout.addWidget(self.m_text4)
        self.vlayout.addWidget(self.n_text4)
        self.vlayout.addWidget(self.m_text5)
        self.vlayout.addWidget(self.n_text5)
        self.vlayout.addWidget(self.m_text6)
        self.vlayout.addWidget(self.n_text6)
        self.vlayout.addWidget(self.m_text7)
        self.vlayout.addWidget(self.n_text7)
        self.vlayout.addWidget(self.m_text8)
        self.vlayout.addWidget(self.n_text8)

        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(50)
        self.setLayout(self.vlayout)

    def upd_in_db(self):
        print(s_row)
        print(self.main.table1.model().index(s_row, 0).data())

        pole0 = str(self.main.table1.model().index(s_row, 0).data())
        pole1 = str(self.main.table1.model().index(s_row, 1).data())
        pole2 = str(self.main.table1.model().index(s_row, 2).data())
        pole3 = str(self.main.table1.model().index(s_row, 3).data())
        pole4 = str(self.main.table1.model().index(s_row, 4).data())
        pole5 = str(self.main.table1.model().index(s_row, 5).data())
        pole6 = str(self.main.table1.model().index(s_row, 6).data())
        pole7 = str(self.main.table1.model().index(s_row, 7).data())
        pole8 = str(self.main.table1.model().index(s_row, 8).data())

        idt = str(self.n_text0.text())
        nam = str(self.n_text1.text())
        imp = str(self.n_text2.text())
        col = str(self.n_text3.text())
        rel = str(self.n_text4.text())
        sta = str(self.n_text5.text())
        typ = str(self.n_text6.text())
        pid = str(self.n_text7.text())
        cid = str(self.n_text8.text())
        if idt == "":
            idt = pole0
        if nam == "":
            nam = pole1
        if imp == "":
            imp = pole2
        if col == "":
            col = pole3
        if rel == "":
            rel = pole4
        if sta == "":
            sta = pole5
        if typ == "":
            typ = pole6
        if pid == "":
            pid = pole7
        if cid == "":
            cid = pole8

        cursor = dbs.cursor()
        query1 = "UPDATE `things` SET `id`='" + idt + "',`name`='" + nam + "',`importance`='" + imp + "',`сollect_date`='" + col + "',`realize_date`='" + rel + "',`status`='" + sta + "',`type`='" + typ + "',`performer_id`='" + pid + "',`client_id`='" + cid + "'" \
                "WHERE `id`='" + pole0 + "' AND `name`='" + pole1 + "' AND `importance`='" + pole2 + "' AND `сollect_date`='" + pole3 + "' AND `realize_date`='" + pole4 + "' AND `status`='" + pole5 + "' AND `type`='" + pole6 + "' AND `performer_id`='" + pole7 + "' AND `client_id`='" + pole8 + "'"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.close()
        print(cursor.execute(query1))


class UpdWindow1(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 400)

        self.vlayout = QtWidgets.QVBoxLayout(self)

        self.m_text0 = QtWidgets.QLabel(self)
        self.m_text0.setText("Id")

        self.n_text0 = QtWidgets.QLineEdit(self)
        self.n_text0.setFixedWidth(280)
        self.n_text0.setPlaceholderText("Введите Id")

        self.m_text1 = QtWidgets.QLabel(self)
        self.m_text1.setText("ФИО")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите ФИО")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Username")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите Username")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Password")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Введите Password")

        self.btn_l = QtWidgets.QPushButton(self)

        self.btn_l.setText("Изменить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.upd_in_db)

        self.vlayout.addWidget(self.m_text0)
        self.vlayout.addWidget(self.n_text0)
        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)
        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(500)
        self.setLayout(self.vlayout)

    def upd_in_db(self):
        print(s_row)
        print(self.main.table1.model().index(s_row, 0).data())

        pole0 = str(self.main.table1.model().index(s_row, 0).data())
        pole1 = str(self.main.table1.model().index(s_row, 1).data())
        pole2 = str(self.main.table1.model().index(s_row, 2).data())
        pole3 = str(self.main.table1.model().index(s_row, 3).data())
        idt = str(self.n_text0.text())
        fio = str(self.n_text1.text())
        usr = str(self.n_text2.text())
        pas = str(self.n_text3.text())
        if idt == "":
            idt = pole0
        if fio == "":
            fio = pole1
        if usr == "":
            usr = pole2
        if pas == "":
            pas = pole3
        cursor = dbs.cursor()
        query1 = "UPDATE `performers` SET `id`='" + idt + "',`performer`='" + fio + "',`username`='" + usr + "'," \
                                                                                                             "`password`='" + pas + "' WHERE `id`= '" + pole0 + "' AND `performer`= '" + pole1 + "' AND `username` ='" + pole2 + "' AND `password`='" + pole3 + "'"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.close()
        print(cursor.execute(query1))


class UpdWindow2(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 400)

        self.vlayout = QtWidgets.QVBoxLayout(self)

        self.m_text0 = QtWidgets.QLabel(self)
        self.m_text0.setText("Id")

        self.n_text0 = QtWidgets.QLineEdit(self)
        self.n_text0.setFixedWidth(280)
        self.n_text0.setPlaceholderText("Введите Id")

        self.m_text1 = QtWidgets.QLabel(self)
        self.m_text1.setText("ФИО")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите ФИО")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Адрес")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите адрес")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Телефон")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Введите телефон")

        self.btn_l = QtWidgets.QPushButton(self)

        self.btn_l.setText("Изменить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.upd_in_db)

        self.vlayout.addWidget(self.m_text0)
        self.vlayout.addWidget(self.n_text0)
        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)
        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(500)
        self.setLayout(self.vlayout)

    def upd_in_db(self):
        print(s_row)
        print(self.main.table1.model().index(s_row, 0).data())

        pole0 = str(self.main.table1.model().index(s_row, 0).data())
        pole1 = str(self.main.table1.model().index(s_row, 1).data())
        pole2 = str(self.main.table1.model().index(s_row, 2).data())
        pole3 = str(self.main.table1.model().index(s_row, 3).data())
        idt = str(self.n_text0.text())
        fio = str(self.n_text1.text())
        usr = str(self.n_text2.text())
        pas = str(self.n_text3.text())
        if idt == "":
            idt = pole0
        if fio == "":
            fio = pole1
        if usr == "":
            usr = pole2
        if pas == "":
            pas = pole3
        cursor = dbs.cursor()
        query1 = "UPDATE `clients` SET `id`='" + idt + "',`client`='" + fio + "',`address`='" + usr + "'," \
                                                                                                             "`contact`='" + pas + "' WHERE `id`= '" + pole0 + "' AND `client`= '" + pole1 + "' AND `address` ='" + pole2 + "' AND `contact`='" + pole3 + "'"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.close()
        print(cursor.execute(query1))


class InsertWindow0(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 450)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.m_text1 = QtWidgets.QLabel(self)

        self.m_text1.setText("Назавание")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите назавание")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Важность")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите важность")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Дата получения ГГГГ-ММ-ДД")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Введите дату получения")

        self.m_text4 = QtWidgets.QLabel(self)
        self.m_text4.setText("Дата выдачи ГГГГ-ММ-ДД")

        self.n_text4 = QtWidgets.QLineEdit(self)
        self.n_text4.setFixedWidth(280)
        self.n_text4.setPlaceholderText("Введите дату выдачи")

        self.m_text5 = QtWidgets.QLabel(self)
        self.m_text5.setText("Статус")

        self.n_text5 = QtWidgets.QLineEdit(self)
        self.n_text5.setFixedWidth(280)
        self.n_text5.setPlaceholderText("Статус")

        self.m_text6 = QtWidgets.QLabel(self)
        self.m_text6.setText("Тип")

        self.n_text6 = QtWidgets.QLineEdit(self)
        self.n_text6.setFixedWidth(280)
        self.n_text6.setPlaceholderText("Введите тип")

        self.m_text7 = QtWidgets.QLabel(self)
        self.m_text7.setText("ID специалиста")

        self.n_text7 = QtWidgets.QLineEdit(self)
        self.n_text7.setFixedWidth(280)
        self.n_text7.setPlaceholderText("Введите ID специалиста")

        self.m_text8 = QtWidgets.QLabel(self)
        self.m_text8.setText("ID клиента")

        self.n_text8 = QtWidgets.QLineEdit(self)
        self.n_text8.setFixedWidth(280)
        self.n_text8.setPlaceholderText("ID клиента")

        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.setText("Добавить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.insert_in_db)

        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)

        self.vlayout.addWidget(self.m_text4)
        self.vlayout.addWidget(self.n_text4)
        self.vlayout.addWidget(self.m_text5)
        self.vlayout.addWidget(self.n_text5)
        self.vlayout.addWidget(self.m_text6)
        self.vlayout.addWidget(self.n_text6)
        self.vlayout.addWidget(self.m_text7)
        self.vlayout.addWidget(self.n_text7)
        self.vlayout.addWidget(self.m_text8)
        self.vlayout.addWidget(self.n_text8)

        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(500)
        self.setLayout(self.vlayout)

    def insert_in_db(self):
        sql_connect(host, port, user, passwd, database)
        cursor = dbs.cursor()
        query = "SELECT MAX(`id`) FROM `things`"
        cursor.execute(query)
        nam = str(self.n_text1.text())
        imp = str(self.n_text2.text())
        col = str(self.n_text3.text())
        rel = str(self.n_text4.text())
        sta = str(self.n_text5.text())
        typ = str(self.n_text6.text())
        pid = str(self.n_text7.text())
        cid = str(self.n_text8.text())
        for r in cursor:
            nid = str(r[0] + 1)
        print(nid)
        query1 = "INSERT INTO `things` (`id`, `name`, `importance`, `сollect_date`, `realize_date`, `status`, `type`, `performer_id`, `client_id`)" \
                 " VALUES ('" + nid + "', '" + nam + "', '" + imp + "', '" + col + "', '" + rel + "', '" + sta + "', '" + typ + "', '" + pid + "', '" + cid + "')"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.main.updatetable()


class InsertWindow1(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 400)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.m_text1 = QtWidgets.QLabel(self)
        self.m_text1.setText("Username")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите Username")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("ФИО")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Введите ФИО")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Password")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Введите Password")

        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.setText("Добавить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.insert_in_db)

        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)
        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(500)
        self.setLayout(self.vlayout)

    def insert_in_db(self):
        sql_connect(host, port, user, passwd, database)
        cursor = dbs.cursor()
        query = "SELECT MAX(`id`) FROM `performers`"
        cursor.execute(query)
        usr = str(self.n_text1.text())
        fio = str(self.n_text2.text())
        pas = str(self.n_text3.text())
        for r in cursor:
            nid = str(r[0] + 1)
        print(nid)
        query1 = "INSERT INTO `performers` (`id`, `performer`, `username`, `password`) VALUES ('" + nid + "', '" + fio + "', '" + usr + "', '" + pas + "')"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.main.updatetable()


class InsertWindow2(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Изменение поля")
        self.setFixedSize(300, 400)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.m_text1 = QtWidgets.QLabel(self)
        self.m_text1.setText("ФИО")

        self.n_text1 = QtWidgets.QLineEdit(self)
        self.n_text1.setFixedWidth(280)
        self.n_text1.setPlaceholderText("Введите ФИО")

        self.m_text2 = QtWidgets.QLabel(self)
        self.m_text2.setText("Введите адрес")

        self.n_text2 = QtWidgets.QLineEdit(self)
        self.n_text2.setFixedWidth(280)
        self.n_text2.setPlaceholderText("Адрес")

        self.m_text3 = QtWidgets.QLabel(self)
        self.m_text3.setText("Введите телефон")

        self.n_text3 = QtWidgets.QLineEdit(self)
        self.n_text3.setFixedWidth(280)
        self.n_text3.setPlaceholderText("Телефон")

        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.setText("Добавить")
        self.btn_l.setFixedWidth(280)
        self.btn_l.clicked.connect(self.insert_in_db)

        self.vlayout.addWidget(self.m_text1)
        self.vlayout.addWidget(self.n_text1)
        self.vlayout.addWidget(self.m_text2)
        self.vlayout.addWidget(self.n_text2)
        self.vlayout.addWidget(self.m_text3)
        self.vlayout.addWidget(self.n_text3)
        self.vlayout.addWidget(self.btn_l)
        self.vlayout.addSpacing(500)
        self.setLayout(self.vlayout)

    def insert_in_db(self):
        sql_connect(host, port, user, passwd, database)
        cursor = dbs.cursor()
        query = "SELECT MAX(`id`) FROM `clients`"
        cursor.execute(query)
        usr = str(self.n_text1.text())
        fio = str(self.n_text2.text())
        pas = str(self.n_text3.text())
        for r in cursor:
            nid = str(r[0] + 1)
        print(nid)
        query1 = "INSERT INTO `clients` (`id`, `client`, `address`, `contact`) VALUES ('" + nid + "', '" + usr + "', '" + fio + "', '" + pas + "')"
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.main.updatetable()


class DeleteWindow(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setWindowTitle("Удалить")
        self.setFixedSize(250, 100)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.hlayout = QtWidgets.QHBoxLayout(self)

        self.m_text1 = QtWidgets.QLabel(self)
        self.m_text1.setText("Вы действительно хотите удалить строку?")

        self.btn_d = QtWidgets.QPushButton(self)
        self.btn_d.setText("Да")
        self.btn_d.setFixedWidth(75)
        self.btn_d.clicked.connect(self.delete_in_db)

        self.btn_n = QtWidgets.QPushButton(self)
        self.btn_n.setText("Нет")
        self.btn_n.setFixedWidth(75)
        self.btn_n.clicked.connect(self.close)

        self.vlayout.addWidget(self.m_text1)
        self.hlayout.addSpacing(75)
        self.hlayout.addWidget(self.btn_d)
        self.hlayout.addWidget(self.btn_n)
        self.vlayout.addSpacing(500)
        self.vlayout.addLayout(self.hlayout)
        self.setLayout(self.vlayout)

    def delete_in_db(self):
        print(s_row)
        print(self.main.table1.model().index(s_row, 0).data())
        pole0 = str(self.main.table1.model().index(s_row, 0).data())
        cursor = dbs.cursor()
        if self.main.on_currentIndexChanged(0) == 0:
            query1 = "DELETE FROM `things` WHERE `id` =" + pole0
        elif self.main.on_currentIndexChanged(0) == 1:
            query1 = "DELETE FROM `performers` WHERE `id` =" + pole0
        elif self.main.on_currentIndexChanged(0) == 2:
            query1 = "DELETE FROM `clients` WHERE `id` =" + pole0
        print(query1)
        cursor.execute(query1)
        dbs.commit()
        self.main.updatetable()
        self.close()
        print(cursor.execute(query1))


class XML:
    fileName: str

    def __init__(self, fileName):
        self.fileName = fileName + ".xml"
        self.openFile()

    def openFile(self):
        try:
            file = open(self.fileName, "r")
        except FileNotFoundError:
            self.createFile()

    def createFile(self):
        rootXML = xml.Element("settings")

        text = xml.Element("text")
        text.text = "Text"
        rootXML.append(text)

        file = open(self.fileName, "w")
        file.write(xml.tostring(rootXML, encoding="utf-8", method="xml").decode(encoding="utf-8"))
        file.close()

    def editFile(self, element, value):
        tree = xml.ElementTree(file=self.fileName)
        rootXML = tree.getroot()
        for elem in rootXML.iter(element):
            elem.text = str(value)

        tree = xml.ElementTree(rootXML)
        tree.write(self.fileName)

    def parsingFile(self, elements, text=True):
        tree = xml.ElementTree(file=self.fileName)
        rootXML = tree.getroot()
        for element in rootXML.iter(elements):
            if (text):
                return element.text
            return element


def sql_connect(host, port, user, passwd, database):
    global dbs
    dbs = pymysql.connect(host=host, user=user, passwd=passwd, port=port, database=database)


def sql_connect_chek(host, port, user, passwd, database):
    try:
        if pymysql.connect(host=host, user=user, passwd=passwd, port=port, database=database) is None:
            global dbs
            dbs = pymysql.connect(host=host, user=user, passwd=passwd, port=port, database=database)
    except pymysql.MySQLError as e:
        app = QtWidgets.QApplication(sys.argv)
        err = QMessageBox()
        err.setIcon(QMessageBox.Critical)
        err.setText("Ошибка в соединении с базой данных")
        err.setWindowTitle("Ошибка")
        err.setStandardButtons(QMessageBox.Ok)
        err.show()
        sys.exit(app.exec_())


def application():
    app = QtWidgets.QApplication(sys.argv)
    #login = Login()
    #if login.exec_() == QtWidgets.QDialog.Accepted:
    window = Window()
    window.show()
    sys.exit(app.exec_())


dbxml = XML("config")
host = dbxml.parsingFile("host", True)
user = dbxml.parsingFile("user", True)
passwd = dbxml.parsingFile("passwd", True)
port = int(dbxml.parsingFile("port", True))
database = dbxml.parsingFile("database", True)

sql_connect_chek(host, port, user, passwd, database)

sql_connect(host, port, user, passwd, database)
application()
