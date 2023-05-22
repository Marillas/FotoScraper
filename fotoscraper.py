# Bibliotecas que he usado

# Esta se encarga de hacer el layout
from PyQt6 import QtCore, QtGui, QtWidgets
from selenium.webdriver.common.keys import Keys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
# Esto es un bot que se encarga de recoger datos de un html
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# Esta me sirve para hacer numeros aleatorios
import random
# Esta me sirve para poner delays en el bot
import time
# Con esta me encargo de hacer una tabla para luego pasarla al Excel
import pandas as pd
# Esto es otro bot que se encarga de simular que es un humano
import undetected_chromedriver as uc
# Estas bibliotecas me permiten conectar con firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Esta biblioteca se encarga de pasar un texto al portapales
import pyperclip


# Importo las credenciales y me conecto a mi base de datos
cred = credentials.Certificate("clave_privada.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://idealscraper-default-rtdb.firebaseio.com/'
})

# Ventana del programa
class Ui_FotoScraperFiltros(object):
    def setupUi(self, FotoScraperFiltros):
        self.comprar = ''
        self.habitacion_min = ''
        self.habitacion_max = ''
        self.banos_min = ''
        self.banos_max = ''
        # Para hacer esta ventana he usado QT Designer que es un GUI genial para hacer ventanas en python
        # Creacion y personalizacion de ventana
        FotoScraperFiltros.setObjectName("FotoScraperFiltros")
        FotoScraperFiltros.resize(1000, 698)
        FotoScraperFiltros.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.frame_morado_barra = QtWidgets.QFrame(parent=FotoScraperFiltros)
        self.frame_morado_barra.setGeometry(QtCore.QRect(0, 0, 1001, 701))
        self.frame_morado_barra.setStyleSheet("QFrame{\n"
"background-color: rgb(48, 58, 178);\n"
"}\n"
"")
        self.frame_morado_barra.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_morado_barra.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_morado_barra.setObjectName("frame_morado_barra")
        self.logo_fotoscraper = QtWidgets.QPushButton(parent=self.frame_morado_barra)
        self.logo_fotoscraper.setGeometry(QtCore.QRect(250, 10, 501, 201))
        self.logo_fotoscraper.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 58, 178);\n"
"    border: 0px\n"
"}\n"
"\n"
"")
        self.logo_fotoscraper.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fotoscraper.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logo_fotoscraper.setIcon(icon)
        self.logo_fotoscraper.setIconSize(QtCore.QSize(200, 400))
        self.logo_fotoscraper.setObjectName("logo_fotoscraper")
        self.frame_fondo = QtWidgets.QFrame(parent=self.frame_morado_barra)
        self.frame_fondo.setGeometry(QtCore.QRect(75, 260, 851, 361))
        self.frame_fondo.setStyleSheet("background-color: #F4F4FB;")
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.label_tiempo = QtWidgets.QLabel(parent=self.frame_fondo)
        self.label_tiempo.setGeometry(QtCore.QRect(40, 40, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(20)
        self.label_tiempo.setFont(font)
        self.label_tiempo.setObjectName("label_tiempo")
        self.boton_volver_filtros = QtWidgets.QPushButton(parent=self.frame_fondo)
        self.boton_volver_filtros.setGeometry(QtCore.QRect(90, 190, 291, 141))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(69)
        self.boton_volver_filtros.setFont(font)
        self.boton_volver_filtros.setStyleSheet("QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.boton_volver_filtros.setObjectName("boton_volver_filtros")
        self.label_inmuebles = QtWidgets.QLabel(parent=self.frame_fondo)
        self.label_inmuebles.setGeometry(QtCore.QRect(40, 90, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(20)
        self.label_inmuebles.setFont(font)
        self.label_inmuebles.setObjectName("label_inmuebles")
        self.boton_progreso_scrapear = QtWidgets.QPushButton(parent=self.frame_fondo)
        self.boton_progreso_scrapear.setGeometry(QtCore.QRect(510, 190, 291, 141))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(69)
        self.boton_progreso_scrapear.setFont(font)
        self.boton_progreso_scrapear.setStyleSheet("QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.boton_progreso_scrapear.setObjectName("boton_progreso_scrapear")
        self.label_error = QtWidgets.QLabel(parent=self.frame_fondo)
        self.label_error.setGeometry(QtCore.QRect(40, 140, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(20)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color:red\n"
"")
        self.label_error.setObjectName("label_error")
        self.frame_blanco = QtWidgets.QFrame(parent=self.frame_morado_barra)
        self.frame_blanco.setGeometry(QtCore.QRect(500, 0, 501, 701))
        self.frame_blanco.setStyleSheet("background-color: #F4F4FB;")
        self.frame_blanco.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_blanco.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_blanco.setObjectName("frame_blanco")
        self.lineEdit_provincia_2 = QtWidgets.QLineEdit(parent=self.frame_blanco)
        self.lineEdit_provincia_2.setGeometry(QtCore.QRect(30, 70, 391, 21))
        self.lineEdit_provincia_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_provincia_2.setObjectName("lineEdit_provincia_2")
        self.label_provincia_2 = QtWidgets.QLabel(parent=self.frame_blanco)
        self.label_provincia_2.setGeometry(QtCore.QRect(30, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.label_provincia_2.setFont(font)
        self.label_provincia_2.setObjectName("label_provincia_2")
        self.groupBox_comprar_alquilar = QtWidgets.QGroupBox(parent=self.frame_blanco)
        self.groupBox_comprar_alquilar.setGeometry(QtCore.QRect(30, 110, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.groupBox_comprar_alquilar.setFont(font)
        self.groupBox_comprar_alquilar.setStyleSheet("background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.groupBox_comprar_alquilar.setObjectName("groupBox_comprar_alquilar")
        self.radioButton_comprar_2 = QtWidgets.QRadioButton(parent=self.groupBox_comprar_alquilar)
        self.radioButton_comprar_2.setGeometry(QtCore.QRect(60, 30, 89, 20))
        self.radioButton_comprar_2.setObjectName("radioButton_comprar_2")
        self.radioButton_alquilar_2 = QtWidgets.QRadioButton(parent=self.groupBox_comprar_alquilar)
        self.radioButton_alquilar_2.setGeometry(QtCore.QRect(230, 30, 89, 20))
        self.radioButton_alquilar_2.setObjectName("radioButton_alquilar_2")
        self.groupBox_banos = QtWidgets.QGroupBox(parent=self.frame_blanco)
        self.groupBox_banos.setGeometry(QtCore.QRect(30, 370, 401, 111))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.groupBox_banos.setFont(font)
        self.groupBox_banos.setStyleSheet("background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.groupBox_banos.setObjectName("groupBox_banos")
        self.radioButton_banos_2 = QtWidgets.QRadioButton(parent=self.groupBox_banos)
        self.radioButton_banos_2.setGeometry(QtCore.QRect(230, 30, 89, 20))
        self.radioButton_banos_2.setObjectName("radioButton_banos_2")
        self.radioButton_banos_1 = QtWidgets.QRadioButton(parent=self.groupBox_banos)
        self.radioButton_banos_1.setGeometry(QtCore.QRect(60, 30, 111, 20))
        self.radioButton_banos_1.setObjectName("radioButton_banos_1")
        self.radioButton_banos_3 = QtWidgets.QRadioButton(parent=self.groupBox_banos)
        self.radioButton_banos_3.setGeometry(QtCore.QRect(60, 70, 111, 20))
        self.radioButton_banos_3.setObjectName("radioButton_banos_3")
        self.groupBox_habitacion = QtWidgets.QGroupBox(parent=self.frame_blanco)
        self.groupBox_habitacion.setGeometry(QtCore.QRect(30, 230, 401, 111))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.groupBox_habitacion.setFont(font)
        self.groupBox_habitacion.setStyleSheet("background-color: #FFFFFF;\n"
"border-color: #A3A3A0;")
        self.groupBox_habitacion.setObjectName("groupBox_habitacion")
        self.radioButton_habitaciones_3 = QtWidgets.QRadioButton(parent=self.groupBox_habitacion)
        self.radioButton_habitaciones_3.setGeometry(QtCore.QRect(60, 70, 89, 20))
        self.radioButton_habitaciones_3.setObjectName("radioButton_habitaciones_3")
        self.radioButton_habitaciones_2 = QtWidgets.QRadioButton(parent=self.groupBox_habitacion)
        self.radioButton_habitaciones_2.setGeometry(QtCore.QRect(230, 30, 89, 20))
        self.radioButton_habitaciones_2.setObjectName("radioButton_habitaciones_2")
        self.radioButton_habitaciones_4 = QtWidgets.QRadioButton(parent=self.groupBox_habitacion)
        self.radioButton_habitaciones_4.setGeometry(QtCore.QRect(230, 70, 89, 20))
        self.radioButton_habitaciones_4.setObjectName("radioButton_habitaciones_4")
        self.radioButton_habitaciones_1 = QtWidgets.QRadioButton(parent=self.groupBox_habitacion)
        self.radioButton_habitaciones_1.setGeometry(QtCore.QRect(60, 30, 89, 20))
        self.radioButton_habitaciones_1.setObjectName("radioButton_habitaciones_1")
        self.boton_soporte = QtWidgets.QPushButton(parent=self.frame_blanco)
        self.boton_soporte.setGeometry(QtCore.QRect(30, 490, 401, 141))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(69)
        self.boton_soporte.setFont(font)
        self.boton_soporte.setStyleSheet("QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.boton_soporte.setObjectName("boton_soporte")
        self.label_portapapeles = QtWidgets.QLabel(parent=self.frame_blanco)
        self.label_portapapeles.setGeometry(QtCore.QRect(40, 650, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.label_portapapeles.setFont(font)
        self.label_portapapeles.setStyleSheet("color: black")
        self.label_portapapeles.setObjectName("label_portapapeles")
        self.frame_morado = QtWidgets.QFrame(parent=self.frame_morado_barra)
        self.frame_morado.setGeometry(QtCore.QRect(0, 0, 501, 701))
        self.frame_morado.setStyleSheet("QFrame{\n"
"background-color: rgb(48, 58, 178);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_morado.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_morado.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_morado.setObjectName("frame_morado")
        self.boton_fotosraper = QtWidgets.QPushButton(parent=self.frame_morado)
        self.boton_fotosraper.setGeometry(QtCore.QRect(0, 0, 501, 201))
        self.boton_fotosraper.setStyleSheet("QPushButton {\n"
"    background-color: rgb(48, 58, 178);\n"
"    border: 0px\n"
"}\n"
"\n"
"\n"
"")
        self.boton_fotosraper.setText("")
        self.boton_fotosraper.setIcon(icon)
        self.boton_fotosraper.setIconSize(QtCore.QSize(200, 400))
        self.boton_fotosraper.setObjectName("boton_fotosraper")
        self.label_csv = QtWidgets.QLabel(parent=self.frame_morado)
        self.label_csv.setGeometry(QtCore.QRect(50, 420, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.label_csv.setFont(font)
        self.label_csv.setStyleSheet("color: white")
        self.label_csv.setObjectName("label_csv")
        self.lineEdit_csv = QtWidgets.QLineEdit(parent=self.frame_morado)
        self.lineEdit_csv.setGeometry(QtCore.QRect(50, 460, 391, 21))
        self.lineEdit_csv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_csv.setObjectName("lineEdit_csv")
        self.boton_scrapear = QtWidgets.QPushButton(parent=self.frame_morado)
        self.boton_scrapear.setGeometry(QtCore.QRect(50, 490, 391, 141))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(69)
        self.boton_scrapear.setFont(font)
        self.boton_scrapear.setStyleSheet("QPushButton{\n"
"background-color: #E5E6E1;\n"
"border-color: #A3A3A0;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #666664;\n"
"  font-weight: 700;\n"
"  color: rgb(255,255,255)\n"
"}")
        self.boton_scrapear.setObjectName("boton_scrapear")
        self.frame_fondo.raise_()
        self.logo_fotoscraper.raise_()
        self.frame_blanco.raise_()
        self.frame_morado.raise_()

        self.retranslateUi(FotoScraperFiltros)
        QtCore.QMetaObject.connectSlotsByName(FotoScraperFiltros)

    def retranslateUi(self, FotoScraperFiltros):
        _translate = QtCore.QCoreApplication.translate
        FotoScraperFiltros.setWindowTitle(_translate("FotoScraperFiltros", "Form"))
        self.label_tiempo.setText(_translate("FotoScraperFiltros", "TIEMPO ESTIMADO DE ESPERA:"))
        self.boton_volver_filtros.setText(_translate("FotoScraperFiltros", "VOLVER"))
        self.label_inmuebles.setText(_translate("FotoScraperFiltros", "INMUEBLES ENCONTRADOS:"))
        self.boton_progreso_scrapear.setText(_translate("FotoScraperFiltros", "SCRAPEAR"))
        self.label_error.setText(_translate("FotoScraperFiltros", "NO SE HA ENCONTRADO NINGUN INMUBLE CON ESAS CARACTERISTICAS"))
        self.label_provincia_2.setText(_translate("FotoScraperFiltros", "Provincia"))
        self.groupBox_comprar_alquilar.setTitle(_translate("FotoScraperFiltros", "¿Qué quieres hacer?"))
        self.radioButton_comprar_2.setText(_translate("FotoScraperFiltros", "Comprar"))
        self.radioButton_alquilar_2.setText(_translate("FotoScraperFiltros", "Alquilar"))
        self.groupBox_banos.setTitle(_translate("FotoScraperFiltros", "Baños"))
        self.radioButton_banos_2.setText(_translate("FotoScraperFiltros", "2"))
        self.radioButton_banos_1.setText(_translate("FotoScraperFiltros", "1"))
        self.radioButton_banos_3.setText(_translate("FotoScraperFiltros", "3"))
        self.groupBox_habitacion.setTitle(_translate("FotoScraperFiltros", "Habitaciones"))
        self.radioButton_habitaciones_3.setText(_translate("FotoScraperFiltros", "3"))
        self.radioButton_habitaciones_2.setText(_translate("FotoScraperFiltros", "2"))
        self.radioButton_habitaciones_4.setText(_translate("FotoScraperFiltros", "4"))
        self.radioButton_habitaciones_1.setText(_translate("FotoScraperFiltros", "1"))
        self.boton_soporte.setText(_translate("FotoScraperFiltros", "SOPORTE"))
        self.label_portapapeles.setText(_translate("FotoScraperFiltros", "Se ha copiado al portapapeles nuestro correo"))
        self.label_csv.setText(_translate("FotoScraperFiltros", "Nombre del archivo CSV"))
        self.boton_scrapear.setText(_translate("FotoScraperFiltros", "SCRAPEAR"))
        # Oculto lo que no quiero que se vea
        self.label_portapapeles.setHidden(True)
        self.label_error.setHidden(True)

        # Conecto todos los botones a los metodos correspondientes
        self.boton_scrapear.pressed.connect(self.comprobacion)
        self.boton_volver_filtros.pressed.connect(self.volver)
        self.boton_soporte.pressed.connect(self.portapapeles)
        self.boton_progreso_scrapear.pressed.connect(self.scrapeo)


    # Este es el metodo que se ejecuta cuando haces clic en el boton de Scrapear en la ventana secundaria
    def scrapeo(self):
        # Cambio de ventana ocultando lo que se ve delante para que se vea lo que hay detras
        self.frame_blanco.setHidden(False)
        self.frame_morado.setHidden(False)

        # Compruebo que radiobuttons estan presionados
        if self.radioButton_comprar_2.isChecked():
            self.comprar = 'comprar' 
        if self.radioButton_alquilar_2.isChecked():
            self.comprar = 'alquiler'
        if self.radioButton_banos_1.isChecked():
                self.banos_min = '&minBathrooms=1'
                self.banos_max = '?maxBathrooms=1'
        if self.radioButton_banos_2.isChecked():
                self.banos_min = '&minBathrooms=2'
                self.banos_max = '?maxBathrooms=2'
        if self.radioButton_banos_3.isChecked():
                self.banos_min = '&minBathrooms=3'
                self.banos_max = '?maxBathrooms=3'
        if self.radioButton_habitaciones_1.isChecked():
                self.habitacion_min = '&minRooms=1'
                self.habitacion_max = '&maxRooms=1'
        if self.radioButton_habitaciones_2.isChecked():
                self.habitacion_min = '&minRooms=2'
                self.habitacion_max = '&maxRooms=2'
        if self.radioButton_habitaciones_3.isChecked():
                self.habitacion_min = '&minRooms=3'
                self.habitacion_max = '&maxRooms=3'
        if self.radioButton_habitaciones_4.isChecked():
                self.habitacion_min = '&minRooms=4'
                self.habitacion_max = '&maxRooms=4'



        # LLamo al bot
        browser = uc.Chrome()
        # Este es el encabezado que tiene el excel
        encabezado_datos = ["Título", "Precio", "Metros","Inmueble","Hab",'Baños',"Antiguedad","Consumo",'Energia',"Otros","Detalles", "Comentarios", "URL"]
        # Esta es la pagina
        pag = 0
        # Hago una lista donde voy a guardar todos los datos que scrapee
        datos = []
        contador = -1
        # Paso a minusculas todo el texto que estaba en el lineEdit de escribir la provincia
        provincia = self.lineEdit_provincia_2.text().lower() + '-provincia'
        while True:
            pag += 1
            # Creo la URL que va a cargar el bot a traves de los radiobuttons presionados
            url = f'https://www.fotocasa.es/es/{self.comprar}/viviendas/{provincia}/todas-las-zonas/l/{pag}{self.banos_max}{self.habitacion_max}{self.banos_min}{self.habitacion_min}'
            browser.get(url)
            # Meto un delay de 10 a 12 segundos
            time.sleep(random.randint(10,12))
            # Descargo el html de la pagina
            html = browser.page_source
            soup = bs(html, 'lxml')

            # Recojo el numero todos los locales 
            locales_totales = int(soup.find('h2', {'class': 're-SearchPage-counterTitle'}).text.split()[0].replace('.', ''))
            # El bot se mete en el primer anuncio
            try:
                articles = browser.find_element(By.CLASS_NAME, 're-CardPackPremium')
                articles.click()
            except:
                try:
                    articles = browser.find_element(By.CLASS_NAME, 're-CardPackBasic') 
                    articles.click()
                except:
                    articles = browser.find_element(By.CLASS_NAME, 're-CardPackMinimal')
                    articles.click()
            time.sleep(2)
            url_inmueble = ''
            # Recorro 30 inmuebles
            for i in range(0, 29):
                contador = contador + 1
                print(f'{contador} / {locales_totales} / pagina: {pag}')
                time.sleep(2)
                # Me descargo el HTML de cada inmueble
                html_vivienda = browser.page_source
                soup_vivienda = bs(html_vivienda, 'lxml')

                # Paso de inmueble en inmueble
                try:
                    siguiente = browser.find_element("xpath",'//*[@class="sui-AtomButton sui-AtomButton--primary sui-AtomButton--flat sui-AtomButton--center sui-AtomButton--small sui-AtomButton--fullWidth sui-AtomButton--link re-DetailPagination-action re-DetailPagination-action--next"]').click()
                except: 
                    print("No quedan mas inmuebles")
                    break

                # Recojo el titulo
                titulo = ''
                try:
                    titulo = soup_vivienda.find('h1',{'class':'re-DetailHeader-propertyTitle'}).text
                except:
                    titulo = ''

                # Recojo el precio
                precio = ''
                try:
                    precio = soup_vivienda.find('span',{'class':'re-DetailHeader-price'}).text.replace('.', '')
                except:
                    precio = ''

                # Recojo todos los iconos que aparecen debajo del precio, si contienen m² lo recojo
                metros = ''
                try:
                    m2 = soup_vivienda.find('ul', {'class': 're-DetailHeader-features'})
                    metros_li = m2.find_all('li')
                    for li in metros_li:
                        if 'm²' in li.text:
                            metros = li.text.strip()
                            break
                except:
                    metros = ''

                # Recojo todos los iconos que aparecen debajo del precio, si contienen  habs lo recojo
                habitacion = ''
                bano = ''
                try:
                    habs = soup_vivienda.find('ul', {'class': 're-DetailHeader-features'})
                    habs_li = habs.find_all('li')
                    for li2 in habs_li:
                        try: 
                            if 'habs' in li2.text:
                                habitacion = li2.text.strip()
                        except:
                            pass
                        try:
                            if 'baños' in li2.text:
                                bano = li2.text.strip()
                            if 'baño'in li2.text:
                                bano = li2.text.strip()
                        except:
                            pass

                except:
                    habs = ''
                # Recojo todos los iconos que aparecen debajo del precio
                otras_caracteristicas = [] 
                try:
                    otros = soup_vivienda.find('ul', {'class': 're-DetailHeader-features'})
                    otros_li = otros.find_all('li')
                    for li3 in otros_li:
                        otras_caracteristicas.append(li3.text)  # Agregar cada característica a la lista
                except:
                    otras_caracteristicas = ''

                # Recojo el comentario
                comentario = ''
                try:
                    comentario = soup_vivienda.find('p',{'class':'fc-DetailDescription'}).text
                except:
                    comentario = ''

                # Recojo el tipo de inmueble
                inmueble = '' 
                try:
                    caracteristicas_extras = soup_vivienda.find_all('p', {'class': 're-DetailFeaturesList-featureValue'})
                    antiguedad = ''
                    consumo = ''
                    for caracteristica in caracteristicas_extras:
                        try:
                            if "Casa" in caracteristica.text:
                                inmueble = caracteristica.text.strip()
                            if "Piso" in caracteristica.text:
                                inmueble = caracteristica.text.strip()
                        except:
                            inmueble = ''
                        try:
                            if 'años' in caracteristica.text:
                                antiguedad = caracteristica.text.strip()
                        except:
                            antiguedad = ''
                except:
                    caracteristicas_extras = ''

                # Recojo el consumo y la energia
                consumo = ''
                try:
                    consumo = soup_vivienda.find_all('div',{'class':'re-DetailEnergyCertificate-itemUnits'})[1].text
                except:
                    consumo = ''
                energia = ''
                try:
                    energia = soup_vivienda.find_all('div',{'class':'re-DetailEnergyCertificate-itemUnits'})[0].text
                except:
                    energia = ''

                # Recojo todas las caracteristicas
                try:
                    caracteristicas_div = soup_vivienda.find('div', {'class': 're-DetailFeaturesList'})
                    caracteristicas = ''
                    for div in caracteristicas_div.find_all('div', {'class': 're-DetailFeaturesList-featureContent'}):
                        caracteristicas += div.text.strip() + ' '
                except:
                    caracteristicas = ''

                # Meto todos los datos a la lista que he creado antes
                datos.append([titulo, precio, metros, inmueble,habitacion, bano, antiguedad, consumo, energia, otras_caracteristicas, caracteristicas, comentario, url_inmueble])
                url_inmueble = browser.current_url

                # Creo una lista nueva para subir a firebase con un titulo
                datos_firebase = {
                    'titulo': titulo,
                    'precio': precio,
                    'metros': metros,
                    'inmueble': inmueble,
                    'habitacion': habitacion,
                    'bano': bano,
                    'antiguedad': antiguedad,
                    'consumo': consumo,
                    'energia': energia,
                    'otras_caracteristicas': otras_caracteristicas,
                    'caracteristicas': caracteristicas,
                    'comentario': comentario,
                    'url_inmueble': url_inmueble
                }

                time.sleep(random.randint(1, 2))
                # Recojo el nombre del csv del lineedit
                nombre_csv = self.lineEdit_csv.text()

                # Subo a firebase los datos
                ref = db.reference(f'{nombre_csv}')
                ref.push().set(datos_firebase)

                # Lo paso a excel
                df_idealista = pd.DataFrame(datos, columns=encabezado_datos)
                df_idealista.to_csv(f'{nombre_csv}.csv', index=False)

                if(contador == locales_totales):
                    browser.quit()
                    break
    # Este metodo hace que copie el correo al portapapeles  
    def portapapeles(self):
        self.label_portapapeles.setHidden(False)
        correo = "idealscraper@gmail.com"
        pyperclip.copy(correo)
    # Este metodo vuelve a la ventana inicial
    def volver(self):
                self.frame_blanco.setHidden(False)
                self.frame_morado.setHidden(False)
    # Este es el metodo que comprueba si existen resultados con tu busqueda
    def comprobacion(self):
        # Intento mostrar el boton de scrapear
        try:
             self.boton_progreso_scrapear.setHidden(False)
        except:
             pass
        # Intento ocultar el label de error
        try:
             self.label_error.setHidden(True)
        except:
             pass
        # Cambio de ventana
        self.frame_blanco.setHidden(True)
        self.frame_morado.setHidden(True)
        # No muestro el mensaje del portapapeles si es posible
        try:
                self.label_portapapeles.setHidden(True)
        except:
                pass
        # Compruebo que radiobuttons estan presionados
        if self.radioButton_comprar_2.isChecked():
                self.comprar = 'comprar' 
        if self.radioButton_alquilar_2.isChecked():
                self.comprar = 'alquiler'
        if self.radioButton_banos_1.isChecked():
                self.banos_min = '&minBathrooms=1'
                self.banos_max = '?maxBathrooms=1'
        if self.radioButton_banos_2.isChecked():
                self.banos_min = '&minBathrooms=2'
                self.banos_max = '?maxBathrooms=2'
        if self.radioButton_banos_3.isChecked():
                self.banos_min = '&minBathrooms=3'
                self.banos_max = '?maxBathrooms=3'
        if self.radioButton_habitaciones_1.isChecked():
                self.habitacion_min = '&minRooms=1'
                self.habitacion_max = '&maxRooms=1'
        if self.radioButton_habitaciones_2.isChecked():
                self.habitacion_min = '&minRooms=2'
                self.habitacion_max = '&maxRooms=2'
        if self.radioButton_habitaciones_3.isChecked():
                self.habitacion_min = '&minRooms=3'
                self.habitacion_max = '&maxRooms=3'
        if self.radioButton_habitaciones_4.isChecked():
                self.habitacion_min = '&minRooms=4'
                self.habitacion_max = '&maxRooms=4'
        
        # Llamo al bot
        browser = uc.Chrome()
        pag = 0

        # Construyo la URL
        provincia = self.lineEdit_provincia_2.text().lower() + '-provincia'
        pag += 1
        url = f'https://www.fotocasa.es/es/{self.comprar}/viviendas/{provincia}/todas-las-zonas/l/{pag}{self.banos_max}{self.habitacion_max}{self.banos_min}{self.habitacion_min}'
        browser.get(url)
        try:
                # Intento recoger el numero de inmuebles
                time.sleep(random.randint(3,5))
                html = browser.page_source
                soup = bs(html, 'lxml')
                locales_totales = int(soup.find('h2', {'class': 're-SearchPage-counterTitle'}).text.split()[0].replace('.', ''))
        except:
                # Si no lo recojo salta el mensaje de error
                self.label_error.setHidden(False)
        # Se cierra el bot
        browser.close()

        # Intento mostrar el numero de locales y el tiempo aproximado
        try:
                self.label_inmuebles.setText(f"INMUEBLES ENCONTRADOS: {locales_totales}")
                self.label_tiempo.setText(f"TIEMPO ESTIMADO DE ESPERA: {locales_totales * 3 / 60} minutos")
        except:
                # Si no puedo mostrar el numero de locales el boton de scrapear se oculta
                self.boton_progreso_scrapear.setHidden(True)
                pass
        
# Bucle para que se muestre la ventana
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FotoScraperFiltros = QtWidgets.QWidget()
    ui = Ui_FotoScraperFiltros()
    ui.setupUi(FotoScraperFiltros)
    FotoScraperFiltros.show()
    sys.exit(app.exec())