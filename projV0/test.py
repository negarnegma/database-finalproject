from random import randint

import psycopg2
import hashlib
import uuid
from resources.SSH import SSH
from PyQt5.QtWidgets import QMessageBox
from resources.Offered import Offered
from ticket import ticket_crud
from resources import resources_crud
from functools import partial
from PyQt5 import QtWidgets, QtGui
import grafic12
import hg
from tkinter import *

from user import user_crud
from resources import snapshot_crud, resources_crud, Ordered
import database.database as db

id1 = 8
con = psycopg2.connect(database="projV0", user="postgres", password="12", host="127.0.0.1", port="5432")
# cursor
cur = con.cursor()

current_user_id = 0

chosen_config = 0

offered_configs = [
    Offered(0, "FreeBSD", "2", "3", "6", "20", "4"),
    Offered(0, "FreeBSD", "10", "4", "8", "25", "9"),
    Offered(0, "win7", "4", "2", "5", "10", "6"),
    Offered(0, "win7", "16", "2", "5", "30", "7"),
    Offered(0, "Ubuntu", "8", "3", "6", "15", "7"),
    Offered(0, "Ubuntu", "12", "2", "7", "35", "12")
]


def set_labels(ui):
    global offered_configs
    db.insert_primery_data_offered_config(offered_configs)
    # resource 1
    ui.label_239.setText(offered_configs[0].os)
    ui.label_241.setText(offered_configs[0].ram)
    ui.label_238.setText(offered_configs[0].cores)
    ui.label_240.setText(offered_configs[0].cpu_freq)
    ui.label_242.setText(offered_configs[0].disk)
    ui.label_243.setText(offered_configs[0].bound_rate)

    # resource 2
    ui.label_246.setText(offered_configs[1].os)
    ui.label_247.setText(offered_configs[1].ram)
    ui.label_244.setText(offered_configs[1].cores)
    ui.label_248.setText(offered_configs[1].cpu_freq)
    ui.label_245.setText(offered_configs[1].disk)
    ui.label_249.setText(offered_configs[1].bound_rate)

    # resource 3
    ui.label_258.setText(offered_configs[2].os)
    ui.label_259.setText(offered_configs[2].ram)
    ui.label_256.setText(offered_configs[2].cores)
    ui.label_260.setText(offered_configs[2].cpu_freq)
    ui.label_257.setText(offered_configs[2].disk)
    ui.label_261.setText(offered_configs[2].bound_rate)

    # resource 4
    ui.label_252.setText(offered_configs[3].os)
    ui.label_253.setText(offered_configs[3].ram)
    ui.label_250.setText(offered_configs[3].cores)
    ui.label_254.setText(offered_configs[3].cpu_freq)
    ui.label_251.setText(offered_configs[3].disk)
    ui.label_255.setText(offered_configs[3].bound_rate)

    # resource 5
    ui.label_264.setText(offered_configs[4].os)
    ui.label_265.setText(offered_configs[4].ram)
    ui.label_262.setText(offered_configs[4].cores)
    ui.label_266.setText(offered_configs[4].cpu_freq)
    ui.label_263.setText(offered_configs[4].disk)
    ui.label_267.setText(offered_configs[4].bound_rate)

    # resource 6
    ui.label_270.setText(offered_configs[5].os)
    ui.label_271.setText(offered_configs[5].ram)
    ui.label_268.setText(offered_configs[5].cores)
    ui.label_272.setText(offered_configs[5].cpu_freq)
    ui.label_269.setText(offered_configs[5].disk)
    ui.label_273.setText(offered_configs[5].bound_rate)

    ui.label_22.setText("0")
    ui.label_23.setText("0")


def send_ssh(ui):
    user_id = ui.name_in1.toPlainText()
    ssh_name = ui.textEdit_7.toPlainText()
    ssh_content = ui.textEdit_8.toPlainText()
    ssh = SSH(0,ssh_name,ssh_content)
    resources_crud.add_ssh(user_id,ssh)

def print_all_user_ssh(ui):
    user_id = ui.name_in1.toPlainText()
    resources_crud.get_all_ssh(ui,user_id)

def back_to_login(ui):
    ui.stackedWidget.setCurrentIndex(0)


def back_to_sabtenam(ui):
    ui.stackedWidget.setCurrentIndex(1)


def back_to_wallet(ui):
    ui.stackedWidget.setCurrentIndex(2)


def back_to_ijadm(ui):
    ui.stackedWidget.setCurrentIndex(3)
    ui.checkBox.setChecked(False)
    ui.checkBox_2.setChecked(False)
    ui.checkBox_3.setChecked(False)
    ui.checkBox_4.setChecked(False)
    ui.checkBox_5.setChecked(False)
    ui.checkBox_6.setChecked(False)


def back_to_ijadm2(ui):
    try:
        ui.stackedWidget.setCurrentIndex(4)
        global chosen_config
        if ui.checkBox.isChecked():
            chosen_config = 1
        if ui.checkBox_2.isChecked():
            chosen_config = 2
        if ui.checkBox_3.isChecked():
            chosen_config = 3
        if ui.checkBox_4.isChecked():
            chosen_config = 4
        if ui.checkBox_5.isChecked():
            chosen_config = 5
        if ui.checkBox_6.isChecked():
            chosen_config = 6
        print(chosen_config)

        ui.os_in2_2.setText(offered_configs[chosen_config - 1].os)
        ui.core_in2_2.setText(offered_configs[chosen_config - 1].cores)
        ui.storage_in2_2.setText(offered_configs[chosen_config - 1].disk)
        ui.frequency_in2_2.setText(offered_configs[chosen_config - 1].cpu_freq)
        ui.bandwidth_in2_2.setText(offered_configs[chosen_config - 1].bound_rate)
        ui.ram_in2_2.setText(offered_configs[chosen_config - 1].ram)

        sshHa = resources_crud.get_all_ssh(current_user_id)
        ui.create_u_c_ssh.clear()
        ui.create_u_c_ssh.addItem('None')
        for c in sshHa:
            ui.create_u_c_ssh.addItem(str(c.ssh_id))
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def back_to_taghir_moshakhasat(ui):
    try:
        global current_user_id
        ui.stackedWidget.setCurrentIndex(5)
        confs = resources_crud.get_user_resources(current_user_id)
        ui.manbaIds.clear()
        for c in confs:
            ui.manbaIds.addItem(str(c.ordered_id))
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def back_to_moshahede_gheimat(ui):
    ui.stackedWidget.setCurrentIndex(6)


def back_to_snapshot(ui):
    ui.stackedWidget.setCurrentIndex(7)


def back_to_send_ticket(ui):
    ui.stackedWidget.setCurrentIndex(8)


def back_to_ticket_answer(ui):
    ui.stackedWidget.setCurrentIndex(9)


def back_to_list_gozaresh(ui):
    ui.stackedWidget.setCurrentIndex(10)


def list_of_gozaresh(ui):
    ui.stackedWidget.setCurrentIndex(11)


def add_balance(ui):
    global current_user_id
    user_crud.add_balance(current_user_id, ui.amount.toPlainText())
    get_balance(ui)


def get_balance(ui):
    global current_user_id
    balance = user_crud.get_balance(current_user_id)
    ui.label_22.setText(str(balance))


def get_all_user_tickets(ui):
    try:
        global current_user_id
        ticket_crud.get_all_user_tickets(ui, current_user_id)
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def get_all_answers_for_a_ticket(ui):
    try:
        global current_user_id
        ticket_crud.get_all_answers_for_a_ticket(ui, current_user_id, ui.textEdit_6.toPlainText())
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def add_ticket(ui):
    try:
        global current_user_id
        ticket_crud.add_ticket(current_user_id, ui.textEdit.toPlainText())
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def answer_ticket(ui):
    try:
        global current_user_id
        ticket_crud.answer_ticket(current_user_id, ui.answer_text.toPlainText(), ui.textEdit_6.toPlainText())
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def add_snapshot(ui):
    try:
        global current_user_id
        size = randint(1, 300)
        ui.snapshot_size.setText(str(size))
        snapshot_crud.add_snapshot(current_user_id, ui.userconfigId.toPlainText(), size)
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def get_snapshots(ui):
    try:
        global current_user_id
        snpshots = snapshot_crud.get_snapshots(ui.userconfigId.toPlainText())

        ui.snapshots.setText("")
        ui.snapshots.insertPlainText("date                     size")
        for snpshot in snpshots:
            ui.snapshots.insertPlainText("\n%21.21s %s" %
                                         (snpshot.create_date, snpshot.size))
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def get_user_conf_info(ui):
    try:
        global current_user_id
        u_conf = resources_crud.get_user_resource_info(current_user_id, ui.manbaIds.currentText())

        ui.os_in2.setText(u_conf.os)
        ui.core_in2.setText(str(u_conf.cores))
        ui.storage_in2.setText(str(u_conf.disk))
        ui.frequency_in2.setText(str(u_conf.cpu_freq))
        ui.bandwidth_in2.setText(str(u_conf.bound_rate))
        ui.ram_in2.setText(str(u_conf.ram))
        ui.update_ssh.setText(str(u_conf.ssh_id))
        ui.offeredId_in2_2.setText(str(u_conf.offered_config_id))

    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def update_user_conf_info(ui):
    try:
        global current_user_id
        resources_crud.update_user_resource(current_user_id, ui.manbaIds.currentText(), Ordered.Ordered(
            ui.manbaIds.currentText(),
            ui.os_in2.toPlainText(),
            float(ui.ram_in2.toPlainText()),
            float(ui.core_in2.toPlainText()),
            float(ui.storage_in2.toPlainText()),
            float(ui.frequency_in2.toPlainText()),
            float(ui.bandwidth_in2.toPlainText()),
            ui.update_ssh.toPlainText(),
            float(current_user_id),
            0,
            int(ui.offeredId_in2_2.toPlainText())
        ))

    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Err..")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def create_u_conf(ui):
    try:
        global current_user_id
        global offered_configs
        global chosen_config
        resources_crud.add_user_resource(current_user_id, Ordered.Ordered(
            0, offered_configs[chosen_config - 1].os,
            offered_configs[chosen_config - 1].ram,
            offered_configs[chosen_config - 1].cores,
            offered_configs[chosen_config - 1].disk,
            offered_configs[chosen_config - 1].cpu_freq,
            offered_configs[chosen_config - 1].bound_rate,
            ui.create_u_c_ssh.currentText(),
            current_user_id, 0,
            offered_configs[chosen_config - 1].offered_id
        ))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("منبع ایجاد شد!")
        msg.setWindowTitle("موفقیت")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.exec_()

    except Exception as e:
        ui.bandwidth_in2_2.setText(str(e))


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
    ui = grafic12.Ui_t()
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

    ui.checkBox.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.checkBox_2.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.checkBox_3.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.checkBox_4.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.checkBox_5.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.checkBox_6.stateChanged.connect(partial(back_to_ijadm2, ui))
    ui.back_to_manba.clicked.connect(partial(back_to_ijadm, ui))
    ui.create_u_conf.clicked.connect(partial(create_u_conf, ui))

    # connect taghir button
    ui.taghir_btn1.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.taghir_btn2.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_84.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_74.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_49.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_58.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_69.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.pushButton_67.clicked.connect(partial(back_to_taghir_moshakhasat, ui))
    ui.manbaIds.currentTextChanged.connect(partial(get_user_conf_info, ui))
    ui.pushButton_3.clicked.connect(partial(update_user_conf_info, ui))

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
    ui.pushButton.clicked.connect(partial(send_ssh, ui))
    ui.pushButton_4.clicked.connect(partial(print_all_user_ssh, ui))

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
    ui.addsnapshot.clicked.connect(partial(add_snapshot, ui))
    ui.getsnapshots.clicked.connect(partial(get_snapshots, ui))

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
    ui.answer.clicked.connect(partial(answer_ticket, ui))  # send ticket
    ui.pushButton_7.clicked.connect(partial(back_to_ticket_answer, ui))  # go to answer ticket page

    sys.exit(app.exec_())
