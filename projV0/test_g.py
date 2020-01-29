import psycopg2
import hashlib
import uuid
from ticket import ticket_crud
from functools import partial
from PyQt5 import QtWidgets
import tm
from user import user_crud


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = tm.Ui_Form()
    ui.setupUi(Form)
    ui.label.setText("123")
    ui.textEdit.insertPlainText("salam")
    Form.show()
    #text = ui.textEdit.toPlainText()
    listWidget = QtWidgets.QListWidget()

    listWidget.addItem('test')
   # listWidget.addItem(text)
    listWidget.show()
    sys.exit(app.exec_())
    #ui.listWidget.addItem("salam")
    #ui.pushButton.clicked.connect(partial(show_text_in_list,ui))
