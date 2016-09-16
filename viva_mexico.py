# -*- coding: utf-8 -*-
"""
    ¡Viva México!
    Práctica de 15 de Septiembre
"""

import sys
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class VivaMexico(QWidget):
   
    def __init__(self):
        super(VivaMexico, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle('¡Viva México!')
        self.setWindowIcon(QIcon('bandera_mexico.png'))
        self.centrar()

        self.heroes()
        self.agregar_boton()
        self.show()

    def centrar(self): 
        frame = self.frameGeometry()
        escritorio = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(escritorio)
        self.move(frame.topLeft())

    def agregar_boton(self):
        self.boton = QPushButton('Aprietame', self)
        self.boton.clicked.connect(self.cambiar_boton)
        self.boton.resize(self.boton.sizeHint())
        self.boton.move(20, 200)

    def cambiar_boton(self):
        self.boton.setText(
            str(self.dias_hasta_15_sep()) + ' días faltan para el 15 de Sep'
        )
        self.boton.resize(self.boton.sizeHint())

    def heroes(self):
        self.Morelos_label = QLabel()
        self.Hidalgo_label = QLabel()
        self.Guerrero_label = QLabel()
        self.vbox = QVBoxLayout()

        self.Morelos_label.setText('Morelos')
        self.Hidalgo_label.setText('Hidalgo')
        self.Guerrero_label.setText('Guerrero')

        self.Morelos_label.setAlignment(Qt.AlignLeft)
        self.Hidalgo_label.setAlignment(Qt.AlignCenter)
        self.Guerrero_label.setAlignment(Qt.AlignRight)

        self.vbox.addWidget(self.Morelos_label)
        self.vbox.addStretch()
        self.vbox.addWidget(self.Hidalgo_label)
        self.vbox.addStretch()
        self.vbox.addWidget(self.Guerrero_label)
        self.vbox.addStretch()

        self.setLayout(self.vbox)

    def dias_hasta_15_sep(self):
        dia_actual = datetime.date.today()
        sep_15_este_anio = datetime.date(dia_actual.year, 9, 15)
        if dia_actual <= sep_15_este_anio:
            # La resta regresa un timedelta le saco los días para que me de
            # un entero
            dias = (sep_15_este_anio - dia_actual).days
        else:
            # Hace la resta del 15 de Sep del siguiente año con el día de
            # hoy
            dias = (datetime.date(dia_actual.year+1, 9, 15) - dia_actual).days
        return dias

def main():
    app = QApplication(sys.argv)
    viva_mexico = VivaMexico()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
