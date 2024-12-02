import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlTableModel

from main_window_ui import Ui_MainWindow
from transaction_ui import Ui_tr_dialog
from connection import Data
from category_ui import Ui_category_dialog
from new_category_ui import Ui_new_category_dialog


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.initUI()

    def initUI(self):
        self.view_data()
        self.reload_data()
        self.ui.btn_new_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delete_transaction.clicked.connect(self.delete_current_transaction)
        self.ui.category_btn.clicked.connect(self.categories)

    def reload_data(self):
        self.ui.current_balance.setText(self.conn.total_balance())
        self.ui.income_balance.setText(self.conn.total_income())
        self.ui.outcome_balance.setText(self.conn.total_outcome())
        categories = self.conn.get_categories(True)
        icons = self.conn.get_categories_icons()
        self.ui.first_name.setText(categories[0])
        self.ui.second_name.setText(categories[1])
        self.ui.third_name.setText(categories[2])
        self.ui.fourth_name.setText(categories[3])
        self.ui.first_icon.setPixmap(QPixmap(':/icons/icons/' + icons[0]))
        self.ui.second_icon.setPixmap(QPixmap(':/icons/icons/' + icons[1]))
        self.ui.third_icon.setPixmap(QPixmap(':/icons/icons/' + icons[2]))
        self.ui.fourth_icon.setPixmap(QPixmap(':/icons/icons/' + icons[3]))
        self.ui.first_total.setText(self.conn.total_for_category(categories[0]))
        self.ui.second_total.setText(self.conn.total_for_category(categories[1]))
        self.ui.third_total.setText(self.conn.total_for_category(categories[2]))
        self.ui.fourth_total.setText(self.conn.total_for_category(categories[3]))

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.model.select()

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_tr_dialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.cb_choose_category.setPlaceholderText("Выберите категорию")
        self.ui_window.cb_choose_category.addItems(self.conn.get_categories())
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Новая транзакция":
            self.ui_window.btn_new_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.tr_lbl.setText('Редактировать транзакцию')
            self.ui_window.btn_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_items_to_cb(self):
        items = self.conn.get_categories()
        for item in items:
            self.ui_window.cb_choose_category.addItem(item)

    def add_new_transaction(self):
        try:
            date = self.ui_window.dateEdit.text()
            category = self.ui_window.cb_choose_category.currentText()
            description = self.ui_window.le_description.text()
            balance = self.ui_window.le_balance.text()
            status = 'Доход' if self.ui_window.rb_income.isChecked() else 'Расход'
            if balance.isdigit() or (balance[:-1].isdigit() and balance[-1] == '₽'):
                if status == 'Расход' and balance[0] != '-':
                    balance = '-' + balance
                self.conn.add_new_transaction_query(date, category, description, balance, status)
                self.view_data()
                self.reload_data()
                self.new_window.close()
        except IndexError:
            pass

    def edit_current_transaction(self):
        try:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))
            date = self.ui_window.dateEdit.text()
            category = self.ui_window.cb_choose_category.currentText()
            description = self.ui_window.le_description.text()
            balance = self.ui_window.le_balance.text()
            status = 'Доход' if self.ui_window.rb_income.isChecked() else 'Расход'
            if status == 'Расход' and balance[0] != '-':
                balance = '-' + balance
            self.conn.update_transaction_query(date, category, description, balance, status, id)
            self.view_data()
            self.reload_data()
            self.new_window.close()
        except IndexError:
            pass

    def delete_current_transaction(self):
        try:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))
            self.conn.delete_transaction_query(id)
            self.view_data()
            self.reload_data()
        except IndexError:
            pass

    def categories(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_category_dialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.remove_categories_cmb_box.setPlaceholderText('Выбрать категорию')
        self.ui_window.add_categories_cmb_box.setPlaceholderText('Заменить на')
        self.ui_window.remove_categories_cmb_box.addItems(self.conn.get_categories(True))
        self.ui_window.add_categories_cmb_box.addItems(self.conn.get_categories(False))
        self.ui_window.save_btn.clicked.connect(self.replace_category)
        self.ui_window.new_category_btn.clicked.connect(self.new_category)
        self.new_window.show()

    def replace_category(self):
        category_r = self.ui_window.remove_categories_cmb_box.currentText()
        category_n = self.ui_window.add_categories_cmb_box.currentText()
        if category_r and category_n:
            self.conn.update_categories(category_r, category_n)
            self.reload_data()
            self.new_window.close()

    def new_category(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_new_category_dialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.choose_icon_cb.setPlaceholderText('Выбрать иконку')
        self.ui_window.category_save_btn.clicked.connect(self.add_new_category)
        self.new_window.show()

    def add_new_category(self):
        lst = ['add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'bookmark_check_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'category_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'celebration_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'dangerous_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'database_upload_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'delete_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'directions_car_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'edit_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'file_export_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg', 'flower.svg',
               'fork_spoon_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'grocery_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg', 'human.svg',
               'monitoring_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'other_admission_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'palette_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'search_insights_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg', 'settings.svg',
               'settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'shopping_cart_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'target_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'trending_down_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'trending_up_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg',
               'wifi_add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg', 'work_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg']
        name = self.ui_window.category_name_edit.text()
        icon = lst[self.ui_window.choose_icon_cb.currentIndex()]
        self.conn.add_new_category(name, icon)
        self.new_window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
