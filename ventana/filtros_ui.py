# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filtros.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_FotoScraperFiltros(object):
    def setupUi(self, FotoScraperFiltros):
        if not FotoScraperFiltros.objectName():
            FotoScraperFiltros.setObjectName(u"FotoScraperFiltros")
        FotoScraperFiltros.resize(1000, 698)
        self.frame_morado_barra = QFrame(FotoScraperFiltros)
        self.frame_morado_barra.setObjectName(u"frame_morado_barra")
        self.frame_morado_barra.setGeometry(QRect(0, 0, 1001, 701))
        self.frame_morado_barra.setStyleSheet(u"QFrame{\n"
"background-color: rgb(48, 58, 178);\n"
"}\n"
"")
        self.frame_morado_barra.setFrameShape(QFrame.StyledPanel)
        self.frame_morado_barra.setFrameShadow(QFrame.Raised)
        self.logo_fotoscraper = QPushButton(self.frame_morado_barra)
        self.logo_fotoscraper.setObjectName(u"logo_fotoscraper")
        self.logo_fotoscraper.setGeometry(QRect(250, 10, 501, 201))
        self.logo_fotoscraper.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(48, 58, 178);\n"
"	border: 0px\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../fotoscraper.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_fotoscraper.setIcon(icon)
        self.logo_fotoscraper.setIconSize(QSize(200, 400))
        self.frame_fondo = QFrame(self.frame_morado_barra)
        self.frame_fondo.setObjectName(u"frame_fondo")
        self.frame_fondo.setGeometry(QRect(75, 260, 851, 361))
        self.frame_fondo.setStyleSheet(u"background-color: #F4F4FB;")
        self.frame_fondo.setFrameShape(QFrame.StyledPanel)
        self.frame_fondo.setFrameShadow(QFrame.Raised)
        self.label_tiempo = QLabel(self.frame_fondo)
        self.label_tiempo.setObjectName(u"label_tiempo")
        self.label_tiempo.setGeometry(QRect(40, 40, 541, 31))
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(20)
        self.label_tiempo.setFont(font)
        self.boton_volver_filtros = QPushButton(self.frame_fondo)
        self.boton_volver_filtros.setObjectName(u"boton_volver_filtros")
        self.boton_volver_filtros.setGeometry(QRect(90, 190, 291, 141))
        font1 = QFont()
        font1.setFamilies([u"Fixedsys"])
        font1.setPointSize(69)
        self.boton_volver_filtros.setFont(font1)
        self.boton_volver_filtros.setStyleSheet(u"QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  text-shadow: 0 .0625rem 0 #fff;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.label_inmuebles = QLabel(self.frame_fondo)
        self.label_inmuebles.setObjectName(u"label_inmuebles")
        self.label_inmuebles.setGeometry(QRect(40, 90, 541, 31))
        self.label_inmuebles.setFont(font)
        self.boton_progreso_scrapear = QPushButton(self.frame_fondo)
        self.boton_progreso_scrapear.setObjectName(u"boton_progreso_scrapear")
        self.boton_progreso_scrapear.setGeometry(QRect(510, 190, 291, 141))
        self.boton_progreso_scrapear.setFont(font1)
        self.boton_progreso_scrapear.setStyleSheet(u"QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  text-shadow: 0 .0625rem 0 #fff;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.label_error = QLabel(self.frame_fondo)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(40, 140, 541, 31))
        self.label_error.setFont(font)
        self.label_error.setStyleSheet(u"color:red\n"
"")
        self.frame_blanco = QFrame(self.frame_morado_barra)
        self.frame_blanco.setObjectName(u"frame_blanco")
        self.frame_blanco.setGeometry(QRect(500, 0, 501, 701))
        self.frame_blanco.setStyleSheet(u"background-color: #F4F4FB;")
        self.frame_blanco.setFrameShape(QFrame.StyledPanel)
        self.frame_blanco.setFrameShadow(QFrame.Raised)
        self.lineEdit_provincia_2 = QLineEdit(self.frame_blanco)
        self.lineEdit_provincia_2.setObjectName(u"lineEdit_provincia_2")
        self.lineEdit_provincia_2.setGeometry(QRect(30, 70, 391, 21))
        self.lineEdit_provincia_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_provincia_2 = QLabel(self.frame_blanco)
        self.label_provincia_2.setObjectName(u"label_provincia_2")
        self.label_provincia_2.setGeometry(QRect(30, 30, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Fixedsys"])
        self.label_provincia_2.setFont(font2)
        self.groupBox_comprar_alquilar = QGroupBox(self.frame_blanco)
        self.groupBox_comprar_alquilar.setObjectName(u"groupBox_comprar_alquilar")
        self.groupBox_comprar_alquilar.setGeometry(QRect(30, 110, 401, 81))
        self.groupBox_comprar_alquilar.setFont(font2)
        self.groupBox_comprar_alquilar.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.radioButton_comprar_2 = QRadioButton(self.groupBox_comprar_alquilar)
        self.radioButton_comprar_2.setObjectName(u"radioButton_comprar_2")
        self.radioButton_comprar_2.setGeometry(QRect(60, 30, 89, 20))
        self.radioButton_alquilar_2 = QRadioButton(self.groupBox_comprar_alquilar)
        self.radioButton_alquilar_2.setObjectName(u"radioButton_alquilar_2")
        self.radioButton_alquilar_2.setGeometry(QRect(230, 30, 89, 20))
        self.groupBox_banos = QGroupBox(self.frame_blanco)
        self.groupBox_banos.setObjectName(u"groupBox_banos")
        self.groupBox_banos.setGeometry(QRect(30, 370, 401, 111))
        self.groupBox_banos.setFont(font2)
        self.groupBox_banos.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.radioButton_banos_2 = QRadioButton(self.groupBox_banos)
        self.radioButton_banos_2.setObjectName(u"radioButton_banos_2")
        self.radioButton_banos_2.setGeometry(QRect(230, 30, 89, 20))
        self.radioButton_banos_1 = QRadioButton(self.groupBox_banos)
        self.radioButton_banos_1.setObjectName(u"radioButton_banos_1")
        self.radioButton_banos_1.setGeometry(QRect(60, 30, 111, 20))
        self.radioButton_banos_3 = QRadioButton(self.groupBox_banos)
        self.radioButton_banos_3.setObjectName(u"radioButton_banos_3")
        self.radioButton_banos_3.setGeometry(QRect(60, 70, 111, 20))
        self.groupBox_habitacion = QGroupBox(self.frame_blanco)
        self.groupBox_habitacion.setObjectName(u"groupBox_habitacion")
        self.groupBox_habitacion.setGeometry(QRect(30, 230, 401, 111))
        self.groupBox_habitacion.setFont(font2)
        self.groupBox_habitacion.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.radioButton_habitaciones_3 = QRadioButton(self.groupBox_habitacion)
        self.radioButton_habitaciones_3.setObjectName(u"radioButton_habitaciones_3")
        self.radioButton_habitaciones_3.setGeometry(QRect(60, 70, 89, 20))
        self.radioButton_habitaciones_2 = QRadioButton(self.groupBox_habitacion)
        self.radioButton_habitaciones_2.setObjectName(u"radioButton_habitaciones_2")
        self.radioButton_habitaciones_2.setGeometry(QRect(230, 30, 89, 20))
        self.radioButton_habitaciones_4 = QRadioButton(self.groupBox_habitacion)
        self.radioButton_habitaciones_4.setObjectName(u"radioButton_habitaciones_4")
        self.radioButton_habitaciones_4.setGeometry(QRect(230, 70, 89, 20))
        self.radioButton_habitaciones_1 = QRadioButton(self.groupBox_habitacion)
        self.radioButton_habitaciones_1.setObjectName(u"radioButton_habitaciones_1")
        self.radioButton_habitaciones_1.setGeometry(QRect(60, 30, 89, 20))
        self.boton_soporte = QPushButton(self.frame_blanco)
        self.boton_soporte.setObjectName(u"boton_soporte")
        self.boton_soporte.setGeometry(QRect(30, 490, 401, 141))
        self.boton_soporte.setFont(font1)
        self.boton_soporte.setStyleSheet(u"QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  text-shadow: 0 .0625rem 0 #fff;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.label_portapapeles = QLabel(self.frame_blanco)
        self.label_portapapeles.setObjectName(u"label_portapapeles")
        self.label_portapapeles.setGeometry(QRect(40, 650, 381, 31))
        self.label_portapapeles.setFont(font2)
        self.label_portapapeles.setStyleSheet(u"color: black")
        self.frame_morado = QFrame(self.frame_morado_barra)
        self.frame_morado.setObjectName(u"frame_morado")
        self.frame_morado.setGeometry(QRect(0, 0, 501, 701))
        self.frame_morado.setStyleSheet(u"QFrame{\n"
"background-color: rgb(48, 58, 178);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_morado.setFrameShape(QFrame.StyledPanel)
        self.frame_morado.setFrameShadow(QFrame.Raised)
        self.boton_fotosraper = QPushButton(self.frame_morado)
        self.boton_fotosraper.setObjectName(u"boton_fotosraper")
        self.boton_fotosraper.setGeometry(QRect(0, 0, 501, 201))
        self.boton_fotosraper.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(48, 58, 178);\n"
"	border: 0px\n"
"}\n"
"\n"
"\n"
"")
        self.boton_fotosraper.setIcon(icon)
        self.boton_fotosraper.setIconSize(QSize(200, 400))
        self.label_csv = QLabel(self.frame_morado)
        self.label_csv.setObjectName(u"label_csv")
        self.label_csv.setGeometry(QRect(50, 420, 191, 31))
        self.label_csv.setFont(font2)
        self.label_csv.setStyleSheet(u"color: white")
        self.lineEdit_csv = QLineEdit(self.frame_morado)
        self.lineEdit_csv.setObjectName(u"lineEdit_csv")
        self.lineEdit_csv.setGeometry(QRect(50, 460, 391, 21))
        self.lineEdit_csv.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.boton_scrapear = QPushButton(self.frame_morado)
        self.boton_scrapear.setObjectName(u"boton_scrapear")
        self.boton_scrapear.setGeometry(QRect(50, 490, 391, 141))
        self.boton_scrapear.setFont(font1)
        self.boton_scrapear.setStyleSheet(u"QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  text-shadow: 0 .0625rem 0 #fff;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.frame_fondo.raise_()
        self.logo_fotoscraper.raise_()
        self.frame_blanco.raise_()
        self.frame_morado.raise_()

        self.retranslateUi(FotoScraperFiltros)

        QMetaObject.connectSlotsByName(FotoScraperFiltros)
    # setupUi

    def retranslateUi(self, FotoScraperFiltros):
        FotoScraperFiltros.setWindowTitle(QCoreApplication.translate("FotoScraperFiltros", u"Form", None))
        self.logo_fotoscraper.setText("")
        self.label_tiempo.setText(QCoreApplication.translate("FotoScraperFiltros", u"TIEMPO ESTIMADO DE ESPERA:", None))
        self.boton_volver_filtros.setText(QCoreApplication.translate("FotoScraperFiltros", u"VOLVER", None))
        self.label_inmuebles.setText(QCoreApplication.translate("FotoScraperFiltros", u"INMUEBLES ENCONTRADOS:", None))
        self.boton_progreso_scrapear.setText(QCoreApplication.translate("FotoScraperFiltros", u"SCRAPEAR", None))
        self.label_error.setText(QCoreApplication.translate("FotoScraperFiltros", u"NO SE HA ENCONTRADO NINGUN INMUBLE CON ESAS CARACTERISTICAS", None))
        self.label_provincia_2.setText(QCoreApplication.translate("FotoScraperFiltros", u"Provincia", None))
        self.groupBox_comprar_alquilar.setTitle(QCoreApplication.translate("FotoScraperFiltros", u"\u00bfQu\u00e9 quieres hacer?", None))
        self.radioButton_comprar_2.setText(QCoreApplication.translate("FotoScraperFiltros", u"Comprar", None))
        self.radioButton_alquilar_2.setText(QCoreApplication.translate("FotoScraperFiltros", u"Alquilar", None))
        self.groupBox_banos.setTitle(QCoreApplication.translate("FotoScraperFiltros", u"Ba\u00f1os", None))
        self.radioButton_banos_2.setText(QCoreApplication.translate("FotoScraperFiltros", u"2", None))
        self.radioButton_banos_1.setText(QCoreApplication.translate("FotoScraperFiltros", u"1", None))
        self.radioButton_banos_3.setText(QCoreApplication.translate("FotoScraperFiltros", u"3", None))
        self.groupBox_habitacion.setTitle(QCoreApplication.translate("FotoScraperFiltros", u"Habitaciones", None))
        self.radioButton_habitaciones_3.setText(QCoreApplication.translate("FotoScraperFiltros", u"3", None))
        self.radioButton_habitaciones_2.setText(QCoreApplication.translate("FotoScraperFiltros", u"2", None))
        self.radioButton_habitaciones_4.setText(QCoreApplication.translate("FotoScraperFiltros", u"4", None))
        self.radioButton_habitaciones_1.setText(QCoreApplication.translate("FotoScraperFiltros", u"1", None))
        self.boton_soporte.setText(QCoreApplication.translate("FotoScraperFiltros", u"SOPORTE", None))
        self.label_portapapeles.setText(QCoreApplication.translate("FotoScraperFiltros", u"Se ha copiado al portapapeles nuestro correo", None))
        self.boton_fotosraper.setText("")
        self.label_csv.setText(QCoreApplication.translate("FotoScraperFiltros", u"Nombre del archivo CSV", None))
        self.boton_scrapear.setText(QCoreApplication.translate("FotoScraperFiltros", u"SCRAPEAR", None))
    # retranslateUi

