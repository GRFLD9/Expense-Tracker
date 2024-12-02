from PyQt6 import QtWidgets, QtSql
import sqlite3


class Data:
    def __init__(self):
        super().__init__()
        self.cat_con = sqlite3.connect("expense_db.db")
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Дата VARCHAR(20), "
                   "Категория VARCHAR(20), Описание VARCHAR(20), Сумма REAL, Статус VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Дата, Категория, Описание, Сумма, Статус) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Дата=?, Категория=?, Описание=?, Сумма=?, Статус=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            s = str(query.value(0)) if str(query.value(0)) else '0'
            return s + '₽'

        return '0'

    def total_balance(self):
        return self.get_total(column="Сумма")

    def total_income(self):
        return self.get_total(column="Сумма", filter="Статус", value="Доход")

    def total_outcome(self):
        return self.get_total(column="Сумма", filter="Статус", value="Расход")

    def total_for_category(self, category):
        return self.get_total(column="Сумма", filter="Категория", value=category)

    def get_categories(self, active=None):
        cur = self.cat_con.cursor()
        query = "SELECT Категория FROM categories"
        if active is not None:
            if active:
                query += " WHERE Активна = 1"
            else:
                query += " WHERE Активна = 0"
        query1 = list(map(lambda x: x[0], cur.execute(query).fetchall()))
        return query1

    def get_categories_icons(self):
        cur = self.cat_con.cursor()
        return list(map(lambda x: x[0], cur.execute('SELECT Иконка FROM categories WHERE Активна = 1').fetchall()))

    def update_categories(self, category_r, category_n):
        cur = self.cat_con.cursor()
        cur.execute("UPDATE categories SET Активна = 0 WHERE Категория = ?", (category_r,))
        cur.execute("UPDATE categories SET Активна = 1 WHERE Категория = ?", (category_n,))
        self.cat_con.commit()

    def add_new_category(self, name, icon):
        cur = self.cat_con.cursor()
        cur.execute("INSERT INTO categories VALUES (NULL, ?, 0, ?)", (name, icon))
        self.cat_con.commit()

