# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmregistro.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmregistro(object):
    def setupUi(self, frmregistro):
        frmregistro.setObjectName("frmregistro")
        frmregistro.resize(1021, 697)
        frmregistro.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(frmregistro)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1001, 681))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.btnproveedor = QtWidgets.QPushButton(self.groupBox)
        self.btnproveedor.setGeometry(QtCore.QRect(260, 20, 71, 31))
        self.btnproveedor.setObjectName("btnproveedor")
        self.txtcod = QtWidgets.QLineEdit(self.groupBox)
        self.txtcod.setEnabled(False)
        self.txtcod.setGeometry(QtCore.QRect(140, 20, 121, 30))
        self.txtcod.setObjectName("txtcod")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.label_4.setObjectName("label_4")
        self.txtnum = QtWidgets.QLineEdit(self.groupBox)
        self.txtnum.setGeometry(QtCore.QRect(470, 20, 121, 30))
        self.txtnum.setObjectName("txtnum")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 20, 111, 31))
        self.label_5.setObjectName("label_5")
        self.btnfuncio = QtWidgets.QPushButton(self.groupBox)
        self.btnfuncio.setGeometry(QtCore.QRect(260, 60, 71, 31))
        self.btnfuncio.setObjectName("btnfuncio")
        self.txtcodfuncio = QtWidgets.QLineEdit(self.groupBox)
        self.txtcodfuncio.setEnabled(True)
        self.txtcodfuncio.setGeometry(QtCore.QRect(110, 60, 31, 30))
        self.txtcodfuncio.setObjectName("txtcodfuncio")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.label_6.setObjectName("label_6")
        self.txtnomfuncio = QtWidgets.QLineEdit(self.groupBox)
        self.txtnomfuncio.setEnabled(False)
        self.txtnomfuncio.setGeometry(QtCore.QRect(140, 60, 121, 30))
        self.txtnomfuncio.setObjectName("txtnomfuncio")
        self.txtnomequip = QtWidgets.QLineEdit(self.groupBox)
        self.txtnomequip.setEnabled(False)
        self.txtnomequip.setGeometry(QtCore.QRect(140, 100, 121, 30))
        self.txtnomequip.setObjectName("txtnomequip")
        self.txtcodequip = QtWidgets.QLineEdit(self.groupBox)
        self.txtcodequip.setEnabled(True)
        self.txtcodequip.setGeometry(QtCore.QRect(110, 100, 31, 30))
        self.txtcodequip.setObjectName("txtcodequip")
        self.btnequip = QtWidgets.QPushButton(self.groupBox)
        self.btnequip.setGeometry(QtCore.QRect(260, 100, 71, 31))
        self.btnequip.setObjectName("btnequip")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 61, 31))
        self.label_8.setObjectName("label_8")
        self.radabierto = QtWidgets.QRadioButton(self.groupBox)
        self.radabierto.setGeometry(QtCore.QRect(80, 220, 111, 31))
        self.radabierto.setObjectName("radabierto")
        self.radproceso = QtWidgets.QRadioButton(self.groupBox)
        self.radproceso.setGeometry(QtCore.QRect(180, 220, 111, 31))
        self.radproceso.setObjectName("radproceso")
        self.radconcluido = QtWidgets.QRadioButton(self.groupBox)
        self.radconcluido.setGeometry(QtCore.QRect(290, 220, 111, 31))
        self.radconcluido.setObjectName("radconcluido")
        self.txtobs = QtWidgets.QTextEdit(self.groupBox)
        self.txtobs.setGeometry(QtCore.QRect(110, 140, 251, 71))
        self.txtobs.setObjectName("txtobs")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 91, 31))
        self.label_9.setObjectName("label_9")
        self.txtnomcliente = QtWidgets.QLineEdit(self.groupBox)
        self.txtnomcliente.setEnabled(False)
        self.txtnomcliente.setGeometry(QtCore.QRect(500, 60, 121, 30))
        self.txtnomcliente.setObjectName("txtnomcliente")
        self.txtcodcliente = QtWidgets.QLineEdit(self.groupBox)
        self.txtcodcliente.setEnabled(True)
        self.txtcodcliente.setGeometry(QtCore.QRect(470, 60, 31, 30))
        self.txtcodcliente.setObjectName("txtcodcliente")
        self.btncliente = QtWidgets.QPushButton(self.groupBox)
        self.btncliente.setGeometry(QtCore.QRect(620, 60, 71, 31))
        self.btncliente.setObjectName("btncliente")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(360, 60, 61, 31))
        self.label_10.setObjectName("label_10")
        self.txtnum_2 = QtWidgets.QLineEdit(self.groupBox)
        self.txtnum_2.setGeometry(QtCore.QRect(490, 140, 121, 30))
        self.txtnum_2.setObjectName("txtnum_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(380, 140, 111, 31))
        self.label_11.setObjectName("label_11")
        self.txtnum_3 = QtWidgets.QLineEdit(self.groupBox)
        self.txtnum_3.setGeometry(QtCore.QRect(490, 180, 121, 30))
        self.txtnum_3.setObjectName("txtnum_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(380, 180, 111, 31))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(frmregistro)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 260, 981, 421))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabla = QtWidgets.QTableWidget(self.groupBox_2)
        self.tabla.setGeometry(QtCore.QRect(10, 10, 961, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tabla.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabla.setFont(font)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setHighlightSections(False)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.verticalHeader().setHighlightSections(False)
        self.txtcodprod = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtcodprod.setGeometry(QtCore.QRect(10, 340, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtcodprod.setFont(font)
        self.txtcodprod.setFrame(True)
        self.txtcodprod.setObjectName("txtcodprod")
        self.txtnomprod = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtnomprod.setEnabled(False)
        self.txtnomprod.setGeometry(QtCore.QRect(189, 340, 631, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtnomprod.setFont(font)
        self.txtnomprod.setFrame(True)
        self.txtnomprod.setObjectName("txtnomprod")
        self.txtcantidad = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtcantidad.setGeometry(QtCore.QRect(820, 340, 150, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.txtcantidad.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtcantidad.setFont(font)
        self.txtcantidad.setFrame(True)
        self.txtcantidad.setObjectName("txtcantidad")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(130, 210, 2, 2))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblindice = QtWidgets.QLabel(self.groupBox_2)
        self.lblindice.setGeometry(QtCore.QRect(910, 10, 53, 16))
        self.lblindice.setObjectName("lblindice")
        self.lblitems = QtWidgets.QLabel(self.groupBox_2)
        self.lblitems.setGeometry(QtCore.QRect(910, 380, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblitems.setFont(font)
        self.lblitems.setObjectName("lblitems")
        self.lblfocus = QtWidgets.QLabel(self.groupBox_2)
        self.lblfocus.setGeometry(QtCore.QRect(840, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblfocus.setFont(font)
        self.lblfocus.setObjectName("lblfocus")
        self.btncancel = QtWidgets.QPushButton(self.groupBox_2)
        self.btncancel.setEnabled(True)
        self.btncancel.setGeometry(QtCore.QRect(280, 380, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btncancel.setFont(font)
        self.btncancel.setObjectName("btncancel")
        self.btnlimpiar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnlimpiar.setEnabled(False)
        self.btnlimpiar.setGeometry(QtCore.QRect(190, 380, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnlimpiar.setFont(font)
        self.btnlimpiar.setObjectName("btnlimpiar")
        self.btngrabar = QtWidgets.QPushButton(self.groupBox_2)
        self.btngrabar.setEnabled(False)
        self.btngrabar.setGeometry(QtCore.QRect(100, 380, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btngrabar.setFont(font)
        self.btngrabar.setObjectName("btngrabar")
        self.btneditar = QtWidgets.QPushButton(self.groupBox_2)
        self.btneditar.setGeometry(QtCore.QRect(100, 380, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btneditar.setFont(font)
        self.btneditar.setObjectName("btneditar")
        self.btnbuscar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnbuscar.setGeometry(QtCore.QRect(160, 340, 31, 31))
        self.btnbuscar.setObjectName("btnbuscar")
        self.btnnovo = QtWidgets.QPushButton(self.groupBox_2)
        self.btnnovo.setGeometry(QtCore.QRect(10, 380, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnnovo.setFont(font)
        self.btnnovo.setObjectName("btnnovo")
        self.txtcodprod.raise_()
        self.txtnomprod.raise_()
        self.txtcantidad.raise_()
        self.tabla.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.lblindice.raise_()
        self.lblitems.raise_()
        self.lblfocus.raise_()
        self.btncancel.raise_()
        self.btnlimpiar.raise_()
        self.btngrabar.raise_()
        self.btneditar.raise_()
        self.btnbuscar.raise_()
        self.btnnovo.raise_()

        self.retranslateUi(frmregistro)
        self.tabla.cellActivated['int','int'].connect(self.lblindice.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(frmregistro)
        frmregistro.setTabOrder(self.txtcod, self.btnproveedor)
        frmregistro.setTabOrder(self.btnproveedor, self.txtcantidad)
        frmregistro.setTabOrder(self.txtcantidad, self.txtcodprod)
        frmregistro.setTabOrder(self.txtcodprod, self.btngrabar)
        frmregistro.setTabOrder(self.btngrabar, self.btnlimpiar)
        frmregistro.setTabOrder(self.btnlimpiar, self.btncancel)
        frmregistro.setTabOrder(self.btncancel, self.txtnomprod)
        frmregistro.setTabOrder(self.txtnomprod, self.tabla)

    def retranslateUi(self, frmregistro):
        _translate = QtCore.QCoreApplication.translate
        frmregistro.setWindowTitle(_translate("frmregistro", "Registro de Serviço"))
        self.groupBox.setTitle(_translate("frmregistro", "Entrada"))
        self.btnproveedor.setText(_translate("frmregistro", "Consultar"))
        self.label_4.setText(_translate("frmregistro", "Código:"))
        self.label_5.setText(_translate("frmregistro", "Nro. Orçamento:"))
        self.btnfuncio.setText(_translate("frmregistro", "Consultar"))
        self.label_6.setText(_translate("frmregistro", "Funcionário:"))
        self.btnequip.setText(_translate("frmregistro", "Consultar"))
        self.label_7.setText(_translate("frmregistro", "Equipamento:"))
        self.label_8.setText(_translate("frmregistro", "Estado:"))
        self.radabierto.setText(_translate("frmregistro", "Em aberto"))
        self.radproceso.setText(_translate("frmregistro", "Em processo"))
        self.radconcluido.setText(_translate("frmregistro", "Concluído"))
        self.label_9.setText(_translate("frmregistro", "Observação:"))
        self.btncliente.setText(_translate("frmregistro", "Consultar"))
        self.label_10.setText(_translate("frmregistro", "Cliente:"))
        self.label_11.setText(_translate("frmregistro", "Subtotal"))
        self.label_12.setText(_translate("frmregistro", "Total Cobrado:"))
        self.lblindice.setText(_translate("frmregistro", "TextLabel"))
        self.lblitems.setText(_translate("frmregistro", "0"))
        self.lblfocus.setText(_translate("frmregistro", "Items:"))
        self.btncancel.setText(_translate("frmregistro", "Cancelar"))
        self.btnlimpiar.setText(_translate("frmregistro", "Limpiar"))
        self.btngrabar.setText(_translate("frmregistro", "Grabar"))
        self.btneditar.setText(_translate("frmregistro", "Editar"))
        self.btnbuscar.setText(_translate("frmregistro", "..."))
        self.btnnovo.setText(_translate("frmregistro", "Novo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmregistro = QtWidgets.QWidget()
    ui = Ui_frmregistro()
    ui.setupUi(frmregistro)
    frmregistro.show()
    sys.exit(app.exec_())