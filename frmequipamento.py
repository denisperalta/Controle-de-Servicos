# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmequipamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmequip(object):
    def setupUi(self, frmequip):
        frmequip.setObjectName("frmequip")
        frmequip.resize(900, 319)
        frmequip.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.groupBox = QtWidgets.QGroupBox(frmequip)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.txtnom = QtWidgets.QLineEdit(self.groupBox)
        self.txtnom.setGeometry(QtCore.QRect(160, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtnom.setFont(font)
        self.txtnom.setMaxLength(40)
        self.txtnom.setObjectName("txtnom")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnnovo = QtWidgets.QPushButton(self.groupBox)
        self.btnnovo.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.btnnovo.setObjectName("btnnovo")
        self.btneditar = QtWidgets.QPushButton(self.groupBox)
        self.btneditar.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.btneditar.setObjectName("btneditar")
        self.btncancelar = QtWidgets.QPushButton(self.groupBox)
        self.btncancelar.setGeometry(QtCore.QRect(200, 260, 75, 23))
        self.btncancelar.setObjectName("btncancelar")
        self.btneliminar = QtWidgets.QPushButton(self.groupBox)
        self.btneliminar.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.btneliminar.setObjectName("btneliminar")
        self.btnsalvar = QtWidgets.QPushButton(self.groupBox)
        self.btnsalvar.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.btnsalvar.setObjectName("btnsalvar")
        self.txtcod = QtWidgets.QLineEdit(self.groupBox)
        self.txtcod.setEnabled(False)
        self.txtcod.setGeometry(QtCore.QRect(160, 10, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcod.setFont(font)
        self.txtcod.setObjectName("txtcod")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.codmarca = QtWidgets.QLineEdit(self.groupBox)
        self.codmarca.setEnabled(False)
        self.codmarca.setGeometry(QtCore.QRect(160, 80, 31, 31))
        self.codmarca.setObjectName("codmarca")
        self.txtmarca = QtWidgets.QLineEdit(self.groupBox)
        self.txtmarca.setEnabled(False)
        self.txtmarca.setGeometry(QtCore.QRect(190, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtmarca.setFont(font)
        self.txtmarca.setMaxLength(40)
        self.txtmarca.setObjectName("txtmarca")
        self.btnmarca = QtWidgets.QPushButton(self.groupBox)
        self.btnmarca.setGeometry(QtCore.QRect(350, 80, 31, 31))
        self.btnmarca.setObjectName("btnmarca")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 119, 371, 31))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radnd1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radnd1.setGeometry(QtCore.QRect(100, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radnd1.setFont(font)
        self.radnd1.setChecked(True)
        self.radnd1.setObjectName("radnd1")
        self.radmono = QtWidgets.QRadioButton(self.groupBox_3)
        self.radmono.setGeometry(QtCore.QRect(210, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radmono.setFont(font)
        self.radmono.setObjectName("radmono")
        self.radtri = QtWidgets.QRadioButton(self.groupBox_3)
        self.radtri.setGeometry(QtCore.QRect(300, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radtri.setFont(font)
        self.radtri.setObjectName("radtri")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 371, 31))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.rad60 = QtWidgets.QRadioButton(self.groupBox_4)
        self.rad60.setGeometry(QtCore.QRect(300, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad60.setFont(font)
        self.rad60.setObjectName("rad60")
        self.radnd2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radnd2.setGeometry(QtCore.QRect(100, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radnd2.setFont(font)
        self.radnd2.setChecked(True)
        self.radnd2.setObjectName("radnd2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.rad50 = QtWidgets.QRadioButton(self.groupBox_4)
        self.rad50.setGeometry(QtCore.QRect(210, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad50.setFont(font)
        self.rad50.setObjectName("rad50")
        self.groupBox_2 = QtWidgets.QGroupBox(frmequip)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 10, 481, 301))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabla = QtWidgets.QTableWidget(self.groupBox_2)
        self.tabla.setEnabled(True)
        self.tabla.setGeometry(QtCore.QRect(10, 40, 461, 251))
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setHighlightSections(False)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.verticalHeader().setHighlightSections(False)
        self.lblsinreg = QtWidgets.QLabel(self.groupBox_2)
        self.lblsinreg.setGeometry(QtCore.QRect(200, 160, 71, 21))
        self.lblsinreg.setObjectName("lblsinreg")
        self.lblindice = QtWidgets.QLabel(self.groupBox_2)
        self.lblindice.setGeometry(QtCore.QRect(340, 0, 46, 13))
        self.lblindice.setObjectName("lblindice")
        self.txtbuscar = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtbuscar.setGeometry(QtCore.QRect(60, 10, 171, 20))
        self.txtbuscar.setObjectName("txtbuscar")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(frmequip)
        self.tabla.cellClicked['int','int'].connect(self.lblindice.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(frmequip)
        frmequip.setTabOrder(self.txtcod, self.txtbuscar)
        frmequip.setTabOrder(self.txtbuscar, self.txtnom)
        frmequip.setTabOrder(self.txtnom, self.codmarca)
        frmequip.setTabOrder(self.codmarca, self.txtmarca)
        frmequip.setTabOrder(self.txtmarca, self.btnmarca)
        frmequip.setTabOrder(self.btnmarca, self.radnd1)
        frmequip.setTabOrder(self.radnd1, self.radmono)
        frmequip.setTabOrder(self.radmono, self.radtri)
        frmequip.setTabOrder(self.radtri, self.radnd2)
        frmequip.setTabOrder(self.radnd2, self.rad50)
        frmequip.setTabOrder(self.rad50, self.rad60)
        frmequip.setTabOrder(self.rad60, self.btnnovo)
        frmequip.setTabOrder(self.btnnovo, self.btnsalvar)
        frmequip.setTabOrder(self.btnsalvar, self.btneditar)
        frmequip.setTabOrder(self.btneditar, self.btncancelar)
        frmequip.setTabOrder(self.btncancelar, self.btneliminar)
        frmequip.setTabOrder(self.btneliminar, self.tabla)

    def retranslateUi(self, frmequip):
        _translate = QtCore.QCoreApplication.translate
        frmequip.setWindowTitle(_translate("frmequip", "Registro de Equipamento"))
        self.label.setText(_translate("frmequip", "Nome do Equipamento:"))
        self.btnnovo.setText(_translate("frmequip", "Novo"))
        self.btneditar.setText(_translate("frmequip", "Editar"))
        self.btncancelar.setText(_translate("frmequip", "Cancelar"))
        self.btneliminar.setText(_translate("frmequip", "Eliminar"))
        self.btnsalvar.setText(_translate("frmequip", "Salvar"))
        self.label_7.setText(_translate("frmequip", "Código:"))
        self.label_6.setText(_translate("frmequip", "Marca:"))
        self.btnmarca.setText(_translate("frmequip", "..."))
        self.label_9.setText(_translate("frmequip", "Modelo:"))
        self.radnd1.setText(_translate("frmequip", "Não Disponível"))
        self.radmono.setText(_translate("frmequip", "Monofásico"))
        self.radtri.setText(_translate("frmequip", "Trifásico"))
        self.rad60.setText(_translate("frmequip", "60Hz"))
        self.radnd2.setText(_translate("frmequip", "Não Disponível"))
        self.label_5.setText(_translate("frmequip", "Ciclagem:"))
        self.rad50.setText(_translate("frmequip", "50Hz"))
        self.lblsinreg.setText(_translate("frmequip", "Sem Registros"))
        self.lblindice.setText(_translate("frmequip", "TextLabel"))
        self.label_8.setText(_translate("frmequip", "Buscar:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmequip = QtWidgets.QWidget()
    ui = Ui_frmequip()
    ui.setupUi(frmequip)
    frmequip.show()
    sys.exit(app.exec_())