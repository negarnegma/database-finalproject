import psycopg2
from functools import partial
from PyQt5 import QtWidgets
import grafic
id1 = 8
# con = psycopg2.connect(
#     host = "",
#     database = "company",
#     user = "postgres",
#     password = 36016778
# )
con = psycopg2.connect(database="projV0", user="postgres", password="12", host="127.0.0.1", port="5432")

#cursor
cur = con.cursor();

def connect_to_db(ui,input):
    input = input+1
    name_in = ui.name_in2.toPlainText()
    family_in = ui.family_in2.toPlainText()
    ssn_in = ui.ssn_in2.toPlainText()
    email_in = ui.email_in2.toPlainText()
    password_in = ui.password_in2.toPlainText()
    cur.execute("insert into sabtenam (id,first_name,family_name,ssn,email_address,password) values (%s,%s,%s,%s,%s,%s)", (input, name_in,family_in,ssn_in,email_in,password_in))
    cur.execute("select id,first_name,family_name,ssn,email_address,password from sabtenam")
    rows = cur.fetchall()
    for r in rows:
      print(f"id : {r[0]} , first_name : {r[1]} , family_name : {r[2]} , ssn : {r[3]} , email_address : {r[4]} , password : {r[5]}")
    con.commit()
    cur.close()
    con.close()
    sabtenam_btn_clicked2(ui)

def check_valid_login(ui):

    con.commit()
    name_in = ui.name_in1.toPlainText()
    password_in = ui.password_in1.toPlainText()
    sql = "select * from sabtenam where first_name = %s and Password = %s"
    val = (name_in,password_in)
    res = cur.execute(sql, val)
    sql = "select first_name from sabtenam where first_name = %s and password = %s"
    res1=cur.execute(sql,(name_in,password_in))
    print(res1)
    #print(res)
    #if result == 0:
        #print("id or password is not correct !")
    #else:
        #login_btn_clicked(ui)
    #cur.execute("select first_name,password from sabtenam s1 where exist (select * from sabtenam where first_name = s1.first_name and password = s1.password)")
    #results = cur.fetchall()
    #for r in results:
        #print(f"id : {r[0]} , first_name : {r[1]}")
        #if {r[0]} == name_in and {r[1]} == password_in:
            #print("wellcom")
    #print("error! you dont sabtenam.")



    cur.close()
    con.close()
    #login_btn_clicked(ui)
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

def back_to_list_gozaresh(ui):
    ui.stackedWidget.setCurrentIndex(8)

def login_btn_clicked(ui):
       ui.stackedWidget.setCurrentIndex(2)

def sabtenam_btn_clicked1(ui):
        ui.stackedWidget.setCurrentIndex(1)

def sabtenam_btn_clicked2(ui):
        ui.stackedWidget.setCurrentIndex(2)

if __name__ == "__main__":
    import sys
   # cur.execute("select id,first_name,family_name,ssn,email_address,password from sabtenam")
    #rows = cur.fetchall()
   # for r in rows:
       # print(f"id : {r[0]} , first_name : {r[1]} , family_name : {r[2]} , ssn : {r[3]} , email_address : {r[4]} , password : {r[5]}")
    input =8
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = grafic.Ui_t()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.stackedWidget.setCurrentIndex(0)

    #connect login button
    ui.login_btn1.clicked.connect(partial(login_btn_clicked, ui))
    ui.login_btn4.clicked.connect(partial(back_to_login, ui))
    ui.login_btn3.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_16.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_15.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_7.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_8.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_9.clicked.connect(partial(back_to_login, ui))
    ui.login_btn2_14.clicked.connect(partial(back_to_login, ui))

    #connect sabtenam button
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

    #connect wallet buttons
    ui.wallet_btn1.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn2.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_12.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_11.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_7.clicked.connect(partial(back_to_wallet, ui))
    ui.wallet_btn_8.clicked.connect(partial(back_to_wallet, ui))
    ui.pushButton_65.clicked.connect(partial(back_to_wallet, ui))

    #connect ijad button
    ui.ijad_btn1.clicked.connect(partial(back_to_ijadm,ui))
    ui.ijad_btn2.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_79.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_73.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_50.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_59.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_61.clicked.connect(partial(back_to_ijadm,ui))
    ui.pushButton_70.clicked.connect(partial(back_to_ijadm,ui))

    #connect taghir button
    ui.taghir_btn1.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.taghir_btn2.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_84.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_74.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_49.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_58.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_69.clicked.connect(partial(back_to_taghir_moshakhasat,ui))
    ui.pushButton_67.clicked.connect(partial(back_to_taghir_moshakhasat,ui))

    #connect price button
    ui.price_btn1.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.price_btn2.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_82.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_76.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_53.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_60.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_66.clicked.connect(partial(back_to_moshahede_gheimat,ui))
    ui.pushButton_68.clicked.connect(partial(back_to_moshahede_gheimat,ui))

    #connect snapshot button
    ui.snap_btn1.clicked.connect(partial(back_to_snapshot,ui))
    ui.snap_btn2.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_84.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_58.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_78.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_52.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_55.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_64.clicked.connect(partial(back_to_snapshot,ui))
    ui.pushButton_71.clicked.connect(partial(back_to_snapshot,ui))

    #connect ticket button
    ui.ticket_btn1.clicked.connect(partial(back_to_send_ticket,ui))
    ui.ticket_btn2.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_81.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_75.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_51.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_57.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_64.clicked.connect(partial(back_to_send_ticket,ui))
    ui.pushButton_72.clicked.connect(partial(back_to_send_ticket,ui))

    #connect gozaresh button
    ui.gozaresh_btn1.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.gozaresh_btn2.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_83.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_77.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_54.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_56.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_65.clicked.connect(partial(back_to_list_gozaresh,ui))
    ui.pushButton_69.clicked.connect(partial(back_to_list_gozaresh,ui))

    #connect()

    sys.exit(app.exec_())