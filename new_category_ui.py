# Form implementation generated from reading ui file 'new_category_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_new_category_dialog(object):
    def setupUi(self, new_category_dialog):
        new_category_dialog.setObjectName("new_category_dialog")
        new_category_dialog.resize(328, 248)
        new_category_dialog.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.767363, y2:0.937, stop:0.590909 rgba(56, 166, 123, 255), stop:0.846591 rgba(0, 0, 0, 236));\n"
"font: Noto Sans;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(new_category_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tr_frame = QtWidgets.QFrame(parent=new_category_dialog)
        self.tr_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.tr_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tr_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tr_frame.setObjectName("tr_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tr_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.tr_frame)
        self.label.setStyleSheet("color: white;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.category_name_edit = QtWidgets.QLineEdit(parent=self.tr_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_name_edit.sizePolicy().hasHeightForWidth())
        self.category_name_edit.setSizePolicy(sizePolicy)
        self.category_name_edit.setStyleSheet("font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.category_name_edit.setObjectName("category_name_edit")
        self.verticalLayout.addWidget(self.category_name_edit)
        self.choose_icon_cb = QtWidgets.QComboBox(parent=self.tr_frame)
        self.choose_icon_cb.setStyleSheet("QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QComboBox QListView {\n"
"font-size: 16px;\n"
"background-color: gray;\n"
"color: white;\n"
"}")
        self.choose_icon_cb.setCurrentText("")
        self.choose_icon_cb.setIconSize(QtCore.QSize(40, 30))
        self.choose_icon_cb.setFrame(True)
        self.choose_icon_cb.setObjectName("choose_icon_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/bookmark_check_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon1, "")
        self.choose_icon_cb.setItemText(1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/category_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon2, "")
        self.choose_icon_cb.setItemText(2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/celebration_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon3, "")
        self.choose_icon_cb.setItemText(3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/dangerous_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon4, "")
        self.choose_icon_cb.setItemText(4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/database_upload_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon5, "")
        self.choose_icon_cb.setItemText(5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/delete_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon6, "")
        self.choose_icon_cb.setItemText(6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icons/directions_car_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon7, "")
        self.choose_icon_cb.setItemText(7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icons/edit_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon8, "")
        self.choose_icon_cb.setItemText(8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icons/file_export_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon9, "")
        self.choose_icon_cb.setItemText(9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icons/flower.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon10, "")
        self.choose_icon_cb.setItemText(10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icons/fork_spoon_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon11, "")
        self.choose_icon_cb.setItemText(11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/icons/grocery_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon12, "")
        self.choose_icon_cb.setItemText(12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/icons/human.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon13, "")
        self.choose_icon_cb.setItemText(13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/icons/monitoring_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon14, "")
        self.choose_icon_cb.setItemText(14, "")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icon/icons/other_admission_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon15, "")
        self.choose_icon_cb.setItemText(15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icon/icons/palette_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon16, "")
        self.choose_icon_cb.setItemText(16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icon/icons/search_insights_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon17, "")
        self.choose_icon_cb.setItemText(17, "")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icon/icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon18, "")
        self.choose_icon_cb.setItemText(18, "")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icon/icons/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon19, "")
        self.choose_icon_cb.setItemText(19, "")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icon/icons/shopping_cart_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon20, "")
        self.choose_icon_cb.setItemText(20, "")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icon/icons/target_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon21, "")
        self.choose_icon_cb.setItemText(21, "")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icon/icons/trending_down_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon22, "")
        self.choose_icon_cb.setItemText(22, "")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icon/icons/trending_up_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon23, "")
        self.choose_icon_cb.setItemText(23, "")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icon/icons/wifi_add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon24, "")
        self.choose_icon_cb.setItemText(24, "")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icon/icons/work_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.choose_icon_cb.addItem(icon25, "")
        self.choose_icon_cb.setItemText(25, "")
        self.verticalLayout.addWidget(self.choose_icon_cb)
        self.category_save_btn = QtWidgets.QPushButton(parent=self.tr_frame)
        self.category_save_btn.setStyleSheet("QPushButton {\n"
"color: white;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: 1px solid white;\n"
"border-top-left-radius: 7px;\n"
"height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 30)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70)\n"
"}")
        self.category_save_btn.setIcon(icon)
        self.category_save_btn.setIconSize(QtCore.QSize(25, 25))
        self.category_save_btn.setObjectName("category_save_btn")
        self.verticalLayout.addWidget(self.category_save_btn)
        self.verticalLayout_2.addWidget(self.tr_frame)

        self.retranslateUi(new_category_dialog)
        self.choose_icon_cb.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(new_category_dialog)

    def retranslateUi(self, new_category_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_category_dialog.setWindowTitle(_translate("new_category_dialog", "NewCategory"))
        self.label.setText(_translate("new_category_dialog", "Новая категория"))
        self.category_name_edit.setPlaceholderText(_translate("new_category_dialog", "Название категории"))
        self.choose_icon_cb.setItemText(0, _translate("new_category_dialog", ""))
        self.category_save_btn.setText(_translate("new_category_dialog", "Сохранить категорию"))