# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from pickle import FALSE

from PyQt6 import QtCore, QtGui, QtWidgets
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 643)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.591227, y2:0.727, stop:0.75 rgba(56, 166, 123, 255), stop:1 rgba(0, 0, 0, 236));\n"
"font: \"Noto Sans\";")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.categories_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.categories_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.categories_frame.setObjectName("categories_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.category_btn = QtWidgets.QPushButton(parent=self.categories_frame)
        self.category_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 3px solid rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"     border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"")
        self.category_btn.setObjectName("category_btn")
        self.verticalLayout_2.addWidget(self.category_btn)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.first_icon = QtWidgets.QLabel(parent=self.categories_frame)
        self.first_icon.setMinimumSize(QtCore.QSize(0, 0))
        self.first_icon.setMaximumSize(QtCore.QSize(24, 16777215))
        self.first_icon.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.first_icon.setText("")
        self.first_icon.setPixmap(QtGui.QPixmap(":/icons/icons/grocery_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.first_icon.setObjectName("first_icon")
        self.horizontalLayout_3.addWidget(self.first_icon)
        self.first_name = QtWidgets.QLabel(parent=self.categories_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_name.sizePolicy().hasHeightForWidth())
        self.first_name.setSizePolicy(sizePolicy)
        self.first_name.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.first_name.setObjectName("first_name")
        self.horizontalLayout_3.addWidget(self.first_name)
        self.first_total = QtWidgets.QLabel(parent=self.categories_frame)
        self.first_total.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.first_total.setObjectName("first_total")
        self.horizontalLayout_3.addWidget(self.first_total)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.second_icon = QtWidgets.QLabel(parent=self.categories_frame)
        self.second_icon.setMaximumSize(QtCore.QSize(24, 16777215))
        self.second_icon.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.second_icon.setText("")
        self.second_icon.setPixmap(QtGui.QPixmap(":/icons/icons/fork_spoon_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.second_icon.setObjectName("second_icon")
        self.horizontalLayout_4.addWidget(self.second_icon)
        self.second_name = QtWidgets.QLabel(parent=self.categories_frame)
        self.second_name.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.second_name.setObjectName("second_name")
        self.horizontalLayout_4.addWidget(self.second_name)
        self.second_total = QtWidgets.QLabel(parent=self.categories_frame)
        self.second_total.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.second_total.setObjectName("second_total")
        self.horizontalLayout_4.addWidget(self.second_total)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.third_icon = QtWidgets.QLabel(parent=self.categories_frame)
        self.third_icon.setMaximumSize(QtCore.QSize(24, 16777215))
        self.third_icon.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.third_icon.setText("")
        self.third_icon.setPixmap(QtGui.QPixmap(":/icons/icons/work_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.third_icon.setObjectName("third_icon")
        self.horizontalLayout_5.addWidget(self.third_icon)
        self.third_name = QtWidgets.QLabel(parent=self.categories_frame)
        self.third_name.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.third_name.setObjectName("third_name")
        self.horizontalLayout_5.addWidget(self.third_name)
        self.third_total = QtWidgets.QLabel(parent=self.categories_frame)
        self.third_total.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.third_total.setObjectName("third_total")
        self.horizontalLayout_5.addWidget(self.third_total)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fourth_icon = QtWidgets.QLabel(parent=self.categories_frame)
        self.fourth_icon.setMaximumSize(QtCore.QSize(24, 16777215))
        self.fourth_icon.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.fourth_icon.setText("")
        self.fourth_icon.setPixmap(QtGui.QPixmap(":/icons/icons/other_admission_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.fourth_icon.setObjectName("fourth_icon")
        self.horizontalLayout_6.addWidget(self.fourth_icon)
        self.fourth_name = QtWidgets.QLabel(parent=self.categories_frame)
        self.fourth_name.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.fourth_name.setObjectName("fourth_name")
        self.horizontalLayout_6.addWidget(self.fourth_name)
        self.fourth_total = QtWidgets.QLabel(parent=self.categories_frame)
        self.fourth_total.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.fourth_total.setObjectName("fourth_total")
        self.horizontalLayout_6.addWidget(self.fourth_total)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout.addWidget(self.categories_frame, 0, 1, 1, 1)
        self.balance_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.balance_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.balance_frame.setObjectName("balance_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.balance_frame)
        self.verticalLayout.setContentsMargins(12, 12, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.balance_frame)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 25pt;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.current_balance = QtWidgets.QLabel(parent=self.balance_frame)
        self.current_balance.setStyleSheet("color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.current_balance.setObjectName("current_balance")
        self.verticalLayout.addWidget(self.current_balance)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.balance_frame)
        self.label_3.setMaximumSize(QtCore.QSize(24, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none;\n"
"padding-top: 10px;\n"
"border: none;\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/trending_up_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.balance_frame)
        self.label_4.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.income_balance = QtWidgets.QLabel(parent=self.balance_frame)
        self.income_balance.setStyleSheet("color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.income_balance.setObjectName("income_balance")
        self.verticalLayout.addWidget(self.income_balance)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.balance_frame)
        self.label_6.setMaximumSize(QtCore.QSize(24, 16777215))
        self.label_6.setStyleSheet("background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icons/trending_down_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.balance_frame)
        self.label_7.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.outcome_balance = QtWidgets.QLabel(parent=self.balance_frame)
        self.outcome_balance.setStyleSheet("color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.outcome_balance.setObjectName("outcome_balance")
        self.verticalLayout.addWidget(self.outcome_balance)
        self.gridLayout.addWidget(self.balance_frame, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_new_transaction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_new_transaction.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 2px solid rgb(255,255,255);\n"
"font-size: 13pt;\n"
"     border-top-left-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QtCore.QSize(25, 25))
        self.btn_new_transaction.setObjectName("btn_new_transaction")
        self.horizontalLayout_8.addWidget(self.btn_new_transaction)
        self.btn_edit_transaction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_edit_transaction.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"    border: 2px solid rgb(255,255,255);\n"
"font-size: 13pt;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/edit_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QtCore.QSize(24, 20))
        self.btn_edit_transaction.setObjectName("btn_edit_transaction")
        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)
        self.btn_delete_transaction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_transaction.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"    border: 2px solid rgb(255,255,255);\n"
"font-size: 13pt;\n"
"     border-top-right-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/delete_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_delete_transaction.setIcon(icon2)
        self.btn_delete_transaction.setIconSize(QtCore.QSize(20, 20))
        self.btn_delete_transaction.setObjectName("btn_delete_transaction")
        self.horizontalLayout_8.addWidget(self.btn_delete_transaction)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setStyleSheet("QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
" border: 2px solid rgb(255,255,255);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setObjectName("tableView")
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 2)

        self.logo_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.logo_frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.logo_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 7px;")
        self.logo_frame.setObjectName("logo_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.logo_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.logo_frame)
        self.label.setMaximumSize(QtCore.QSize(350, 350))
        self.label.setStyleSheet("border: 10px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.gridLayout.addWidget(self.logo_frame, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.verticalLayout_6.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExpenseTracker"))
        self.category_btn.setText(_translate("MainWindow", "Категории"))
        self.first_name.setText(_translate("MainWindow", "Продукты"))
        self.first_total.setText(_translate("MainWindow", "0₽"))
        self.second_name.setText(_translate("MainWindow", "Рестораны и кафе"))
        self.second_total.setText(_translate("MainWindow", "0₽"))
        self.third_name.setText(_translate("MainWindow", "Бизнес"))
        self.third_total.setText(_translate("MainWindow", "0₽"))
        self.fourth_name.setText(_translate("MainWindow", "Прочее"))
        self.fourth_total.setText(_translate("MainWindow", "0₽"))
        self.label_2.setText(_translate("MainWindow", "Баланс"))
        self.current_balance.setText(_translate("MainWindow", "0₽"))
        self.label_4.setText(_translate("MainWindow", "Доход"))
        self.income_balance.setText(_translate("MainWindow", "0₽"))
        self.label_7.setText(_translate("MainWindow", "Расход"))
        self.outcome_balance.setText(_translate("MainWindow", "0₽"))
        self.btn_new_transaction.setText(_translate("MainWindow", "Новая транзакция"))
        self.btn_edit_transaction.setText(_translate("MainWindow", "Редактировать транзакцию"))
        self.btn_delete_transaction.setText(_translate("MainWindow", "Удалить транзакцию"))
