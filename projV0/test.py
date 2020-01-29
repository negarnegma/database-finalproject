import psycopg2
import hashlib
import uuid
from ticket import ticket_crud
from functools import partial
from PyQt5 import QtWidgets, QtGui
import grafic7
import hg
from tkinter import *
from user import user_crud
import database as db

id1 = 8
con = psycopg2.connect(database="projV0", user="postgres", password="12", host="127.0.0.1", port="5432")
# cursor
cur = con.cursor()

current_user_id = 0


def set_labels(ui):
    # resource 1
    ui.label_239.setText("FreeBSD")
    ui.label_241.setText("2")
    ui.label_238.setText("3")
    ui.label_240.setText("6")
    ui.label_242.setText("20")
    ui.label_243.setText("4")
    ui.label_158.setText("142,000")

    # resource 2
    ui.label_246.setText("FreeBSD")
    ui.label_247.setText("10")
    ui.label_244.setText("4")
    ui.label_248.setText("8")
    ui.label_245.setText("25")
    ui.label_249.setText("9")
    ui.label_160.setText("259,000")

    # resource 3
    ui.label_258.setText("win7")
    ui.label_259.setText("4")
    ui.label_256.setText("2")
    ui.label_260.setText("5")
    ui.label_257.setText("10")
    ui.label_261.setText("6")
    ui.label_162.setText("92,000")

    # resource 4
    ui.label_252.setText("win7")
    ui.label_253.setText("16")
    ui.label_250.setText("2")
    ui.label_254.setText("5")
    ui.label_251.setText("30")
    ui.label_255.setText("7")
    ui.label_164.setText("179,000")

    # resource 5
    ui.label_264.setText("Linux")
    ui.label_265.setText("8")
    ui.label_262.setText("3")
    ui.label_266.setText("6")
    ui.label_263.setText("15")
    ui.label_267.setText("7")
    ui.label_166.setText("159,000")

    # resource 6
    ui.label_270.setText("Linux")
    ui.label_271.setText("12")
    ui.label_268.setText("2")
    ui.label_272.setText("7")
    ui.label_269.setText("35")
    ui.label_273.setText("12")
    ui.label_168.setText("200,000")

    ui.label_22.setText("0")
    ui.label_23.setText("0")


def back_to_login(ui):
    ui.stackedWidget.setCurrentIndex(0)


def back_to_sabtenam(ui):
    ui.stackedWidget.setCurrentIndex(1)


def back_to_wallet(ui):
    ui.stackedWidget.setCurrentIndex(2)


def back_to_ijadm(ui):
    ui.stackedWidget.setCurrentIndex(3)


def back_to_taghir_moshakhasat(ui):
    ui.stackedWidget.setCurrentIndex(4)


def back_to_moshahede_gheimat(ui):
    ui.stackedWidget.setCurrentIndex(5)


def back_to_snapshot(ui):
    ui.stackedWidget.setCurrentIndex(6)


def back_to_send_ticket(ui):
    ui.stackedWidget.setCurrentIndex(7)


def back_to_ticket_answer(ui):
    ui.stackedWidget.setCurrentIndex(8)


def back_to_list_gozaresh(ui):
    ui.stackedWidget.setCurrentIndex(9)


def list_of_gozaresh(ui):
    ui.stackedWidget.setCurrentIndex(10)


def add_balance(ui):
    global current_user_id
    user_crud.add_balance(current_user_id, ui.amount.toPlainText())
    get_balance(ui)


def get_balance(ui):
    global current_user_id
    balance = user_crud.get_balance(current_user_id)
    ui.label_22.setText(str(balance))


def get_all_user_tickets(ui):
    global current_user_id
    ticket_crud.get_all_user_tickets(ui, current_user_id)


def get_all_answers_for_a_ticket(ui):
    global current_user_id
    ticket_crud.get_all_answers_for_a_ticket(ui, current_user_id, ui.textEdit_6.toPlainText())


def add_ticket(ui):
    global current_user_id
    ticket_crud.add_ticket(current_user_id, ui.textEdit.toPlainText())


def answer_ticket(ui):
    global current_user_id
    ticket_crud.answer_ticket(current_user_id, "answer", 1)


def login_btn_clicked(ui):
    try:
        if user_crud.login_user(ui.name_in1.toPlainText(), ui.password_in1.toPlainText()):
            global current_user_id
            current_user_id = user_crud.get_user_id(ui.name_in1.toPlainText())
            print(current_user_id)
            ui.stackedWidget.setCurrentIndex(2)
            get_balance(ui)
        else:
            ui.name_in1.setText("wrong")
            ui.password_in1.setText("wrong")
            cursor = ui.name_in1.textCursor()
            cursor.setPosition(0)
            cursor.setPosition(5, QtGui.QTextCursor.KeepAnchor)
            ui.name_in1.setTextCursor(cursor)
    except Exception as e:
        print(e)


def sabtenam_btn_clicked1(ui):
    ui.stackedWidget.setCurrentIndex(1)


def sabtenam_btn_clicked2(ui):
    try:
        user_crud.register_user(ui.ssn_in2.toPlainText(), ui.family_in2.toPlainText(), ui.email_in2.toPlainText(),
                                ui.password_in2.toPlainText())
        ui.stackedWidget.setCurrentIndex(0)
    except Exception as e:
        ui.ssn_in2.setText("error")
        ui.family_in2.setText(e.__str__())
        ui.email_in2.setText("error")
        ui.password_in2.setText("error")


if __name__ == "__main__":
    import sys

    input = 8
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = grafic7.Ui_t()
    ui.setupUi(MainWindow)
    set_labels(ui)
    MainWindow.show()
    ui.stackedWidget.setCurrentIndex(0)

    # connect login button
    ui.login_btn1.clicked.connect(partial(login_btn_clicked, ui))
    ui.login_btn4.clicked.connect(partial(back_to_login, ui))
    ui.login_btn3.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_16.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_15.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_7.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_8.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_9.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_14.clicked.connect(partial(back_to_login, ui))

    # connect sabtenam button
    ui.sabtenam_btn1.clicked.connect(partial(sabtenam_btn_clicked1, ui))
    ui.sabtenam_btn2.clicked.connect(partial(sabtenam_btn_clicked2, ui))
    ui.sabtenam_btn3.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn4.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_12.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_11.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_7.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_8.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_9.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_10.clicked.connect(partial(back_to_sabtenam, ui))
    ui.sabtenam_btn3_13.clicked.connect(partial(back_to_sabtenam, ui))

    # connect wallet buttons
    ui.wallet_btn1.clicked.connect(partial(get_balance, ui))  # mojodi ra namayesh bede
    ui.afzayesh_mojodi_btn.clicked.connect(partial(add_balance,
                                                   ui))  # afzayesh mojodi  از این جا هیچ وقت نمایش نمیده!! چرا؟! مهم نیست حالا جای دیگه نمایش میدیم
    ui.wallet_btn2.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_12.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_11.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_7.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_8.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_13.clicked.connect(partial(back_to_wallet, ui))
    ui.pushButton_65.clicked.connect(partial(back_to_wallet, ui))

    # connect ijad button
    ui.ijad_btn1.clicked.connect(partial(back_to_ijadm, ui))
    ui.ijad_btn2.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_79.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_73.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_50.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_59.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_61.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_70.clicked.connect(partial(back_to_ijadm, ui))
    ui.pushButton_68.clicked.connect(partial(back_to_ijadm, ui))

    # connect taghir button
    ui.taghir_btn1.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.taghir_btn2.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_84.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_74.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_49.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_58.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_69.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_67.clicked.connect(partial(back_to_taghir_moshakhasat, ui))

    # connect price button
    ui.price_btn1.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.price_btn2.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_82.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_76.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_53.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_60.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_66.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_68.clicked.connect(partial(back_to_moshahede_gheimat, ui))
    ui.pushButton_89.clicked.connect(partial(back_to_moshahede_gheimat, ui))

    # connect snapshot button
    ui.snap_btn1.clicked.connect(partial(back_to_snapshot, ui))
    ui.snap_btn2.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_84.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_58.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_78.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_52.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_55.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_64.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_71.clicked.connect(partial(back_to_snapshot, ui))
    ui.pushButton_87.clicked.connect(partial(back_to_snapshot, ui))

    # connect ticket button
    ui.ticket_btn1.clicked.connect(partial(back_to_send_ticket, ui))
    ui.ticket_btn2.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_81.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_75.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_51.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_57.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_64.clicked.connect(partial(back_to_send_ticket, ui))
    ui.pushButton_72.clicked.connect(partial(back_to_send_ticket, ui))

    # connect gozaresh button
    ui.gozaresh_btn1.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.gozaresh_btn2.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_83.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_77.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_54.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_56.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_65.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_69.clicked.connect(partial(back_to_list_gozaresh, ui))
    ui.pushButton_88.clicked.connect(partial(back_to_list_gozaresh, ui))

    ui.pushButton_6.clicked.connect(
        partial(get_all_user_tickets, ui))  # moshahede all tickets
    ui.pushButton_2.clicked.connect(partial(get_all_answers_for_a_ticket,
                                            ui))  # moshahede all answers for tickets
    ui.pushButton_5.clicked.connect(partial(add_ticket, ui))  # send ticket
    ui.pushButton_7.clicked.connect(partial(back_to_ticket_answer, ui))  # go to answer ticket page

    sys.exit(app.exec_())
