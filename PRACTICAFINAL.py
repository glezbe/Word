import os
import speech_recognition as sr

from PySide6.QtGui import QAction, QIcon, QKeySequence, QTextDocument, QTextCursor, QFontDatabase, QTextCharFormat, QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFontDialog,
    QApplication,
    QColorDialog,
    QComboBox,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QToolBar,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QDockWidget,
)

from contadorWidget import WordCounterWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Práctica Final")

        self.area_texto = QTextEdit()
        self.setCentralWidget(self.area_texto)

        self.barra_estado = self.statusBar()
        self.word_counter = WordCounterWidget(wpm=200, parent=self)
        self.barra_estado.addPermanentWidget(self.word_counter)

        self.area_texto.textChanged.connect(
            lambda: self.word_counter.update_from_text(self.area_texto.toPlainText())
        )
        self.word_counter.update_from_text(self.area_texto.toPlainText())

        self.fichero_actual = None

        self.fun_accionesArchivo()
        self.fun_accionesEditar()
        self.fun_accionBuscar()
        self.fun_barra_menu()
        self.fun_barra_herramientas()
        self.fun_buscador()

    def fun_accionesArchivo(self):
        icono_nuevo = os.path.join(os.path.dirname(__file__), "nuevo.png")
        self.nuevo = QAction(QIcon(icono_nuevo), "Nuevo", self)
        self.nuevo.setShortcut(QKeySequence("Ctrl+n"))
        self.nuevo.triggered.connect(self.fun_nuevo)

        icono_abrir = os.path.join(os.path.dirname(__file__), "abrir.png")
        self.abrir = QAction(QIcon(icono_abrir), "Abrir", self)
        self.abrir.setShortcut(QKeySequence("Ctrl+a"))
        self.abrir.triggered.connect(self.fun_abrir)

        icono_guardar = os.path.join(os.path.dirname(__file__), "guardar.png")
        self.guardar = QAction(QIcon(icono_guardar), "Guardar", self)
        self.guardar.setShortcut(QKeySequence("Ctrl+g"))
        self.guardar.triggered.connect(self.fun_guardar)

        icono_salir = os.path.join(os.path.dirname(__file__), "salir.png")
        self.salir = QAction(QIcon(icono_salir), "Salir", self)
        self.salir.setShortcut(QKeySequence("Ctrl+s"))
        self.salir.triggered.connect(self.fun_salir)

    def fun_accionesEditar(self):
        icono_deshacer = os.path.join(os.path.dirname(__file__), "deshacer.png")
        self.deshacer = QAction(QIcon(icono_deshacer), "Deshacer", self)
        self.deshacer.setShortcut(QKeySequence("Ctrl+d"))
        self.deshacer.triggered.connect(self.fun_deshacer)

        icono_rehacer = os.path.join(os.path.dirname(__file__), "rehacer.png")
        self.rehacer = QAction(QIcon(icono_rehacer), "Rehacer", self)
        self.rehacer.setShortcut(QKeySequence("Ctrl+r"))
        self.rehacer.triggered.connect(self.fun_rehacer)

        icono_copiar = os.path.join(os.path.dirname(__file__), "copiar.png")
        self.copiar = QAction(QIcon(icono_copiar), "Copiar", self)
        self.copiar.setShortcut(QKeySequence("Ctrl+c"))
        self.copiar.triggered.connect(self.fun_copiar)

        icono_cortar = os.path.join(os.path.dirname(__file__), "cortar.png")
        self.cortar = QAction(QIcon(icono_cortar), "Cortar", self)
        self.cortar.setShortcut(QKeySequence("Ctrl+x"))
        self.cortar.triggered.connect(self.fun_cortar)

        icono_pegar = os.path.join(os.path.dirname(__file__), "pegar.png")
        self.pegar = QAction(QIcon(icono_pegar), "Pegar", self)
        self.pegar.setShortcut(QKeySequence("Ctrl+v"))
        self.pegar.triggered.connect(self.fun_pegar)

        icono_color = os.path.join(os.path.dirname(__file__), "color.png")
        self.color = QAction(QIcon(icono_color), "Color", self)
        self.color.triggered.connect(self.fun_fondo)

        icono_fuente = os.path.join(os.path.dirname(__file__), "funete.png")
        self.fuente = QAction(QIcon(icono_fuente), "Fuente", self)
        self.fuente.triggered.connect(self.fun_dialogo_fuente)

        icono_micro = os.path.join(os.path.dirname(__file__), "microfono.png")
        self.dictado_voz = QAction(QIcon(icono_micro), "Dictado por voz", self)
        self.dictado_voz.setShortcut(QKeySequence("Ctrl+Shift+D"))
        self.dictado_voz.triggered.connect(self.dictar_por_voz)

    def fun_accionBuscar(self):
        icono_buscar = os.path.join(os.path.dirname(__file__), "buscar.png")
        self.buscarAct = QAction(QIcon(icono_buscar), "Buscar y Reemplazar", self)
        self.buscarAct.setShortcut(QKeySequence("Ctrl+f"))
        self.buscarAct.triggered.connect(self.fun_mostrar_buscador)

    def fun_barra_menu(self):
        barraM = self.menuBar()

        menuA = barraM.addMenu("Archivo")
        menuA.addActions([self.nuevo, self.abrir, self.guardar, self.salir])

        menuE = barraM.addMenu("Editar")
        menuE.addActions(
            [
                self.deshacer,
                self.rehacer,
                self.copiar,
                self.cortar,
                self.pegar,
                self.fuente,
                self.color,
                self.dictado_voz,
            ]
        )

        menuB = barraM.addMenu("Buscar")
        menuB.addAction(self.buscarAct)

    def fun_barra_herramientas(self):
        barraH = QToolBar("Herramientas")
        self.addToolBar(barraH)
        barraH.addActions(
            [
                self.nuevo,
                self.abrir,
                self.guardar,
                self.deshacer,
                self.rehacer,
                self.copiar,
                self.cortar,
                self.pegar,
                self.fuente,
                self.color,
                self.buscarAct,
                self.dictado_voz,
            ]
        )

    def fun_buscador(self):
        panel = QWidget()
        layout = QVBoxLayout()

        self.buscar = QLineEdit()
        self.buscar.setPlaceholderText("Texto a buscar...")
        self.reemplazar = QLineEdit()
        self.reemplazar.setPlaceholderText("Reemplazar con...")

        layout.addWidget(self.buscar)
        layout.addWidget(self.reemplazar)

        btns_layout = QHBoxLayout()
        self.btn_sig = QPushButton("Buscar ↓")
        self.btn_prev = QPushButton("Buscar ↑")
        self.btn_reemplazar = QPushButton("Reemplazar")
        self.btn_reemplazar_todo = QPushButton("Reemplazar todas")

        btns_layout.addWidget(self.btn_sig)
        btns_layout.addWidget(self.btn_prev)
        layout.addLayout(btns_layout)

        layout.addWidget(self.btn_reemplazar)
        layout.addWidget(self.btn_reemplazar_todo)

        self.combobox_fuentes = QComboBox()
        self.combobox_fuentes.setFixedSize(180, 26)
        self.combobox_fuentes.setPlaceholderText("Tipo de letra")

        fuentes_disponibles = QFontDatabase.families()
        self.combobox_fuentes.addItems(fuentes_disponibles)

        self.combobox_fuentes.currentTextChanged.connect(self.fun_fuente)

        layout.addWidget(self.combobox_fuentes)

        panel.setLayout(layout)

        self.btn_sig.clicked.connect(self.fun_encontrar_sig)
        self.btn_prev.clicked.connect(self.fun_encontrar_prev)
        self.btn_reemplazar.clicked.connect(self.fun_reemplazar_uno)
        self.btn_reemplazar_todo.clicked.connect(self.fun_reemplazar_todo)

        self.dock = QDockWidget("Buscar / Reemplazar", self)
        self.dock.setWidget(panel)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.dock.hide()

    def fun_abrir(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.area_texto.setPlainText(f.read())
            self.fichero_actual = path
            self.barra_estado.showMessage(f"Archivo abierto: {path}", 3000)
            self.word_counter.update_from_text(self.area_texto.toPlainText())

    def fun_nuevo(self):
        self.area_texto.clear()
        self.fichero_actual = None
        self.barra_estado.showMessage("Nuevo documento creado", 3000)
        self.word_counter.update_from_text(self.area_texto.toPlainText())

    def fun_guardar(self):
        if not self.fichero_actual:
            path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
            if not path:
                return
            self.fichero_actual = path

        with open(self.fichero_actual, "w", encoding="utf-8") as f:
            f.write(self.area_texto.toPlainText())
        self.barra_estado.showMessage("Archivo guardado con éxito", 3000)

    def fun_salir(self):
        self.close()
        self.barra_estado.showMessage("Cerrando APP", 3)

    def fun_deshacer(self):
        self.area_texto.undo()
        self.barra_estado.showMessage("Acción deshecha", 3000)

    def fun_rehacer(self):
        self.area_texto.redo()
        self.barra_estado.showMessage("Acción rehecha", 3000)

    def fun_copiar(self):
        self.area_texto.copy()
        self.barra_estado.showMessage("Sección copiada", 3000)

    def fun_cortar(self):
        self.area_texto.cut()
        self.barra_estado.showMessage("Sección cortada", 3000)

    def fun_pegar(self):
        self.area_texto.paste()
        self.barra_estado.showMessage("Sección pegada", 3000)

    def fun_fuente(self, fuente):
        cursor = self.area_texto.textCursor()
        formato = QTextCharFormat()
        formato.setFont(QFont(fuente))

        if cursor.hasSelection():
            cursor.mergeCharFormat(formato)
            self.area_texto.mergeCurrentCharFormat(formato)
        else:
            self.area_texto.setCurrentFont(QFont(fuente))

    def fun_dialogo_fuente(self):
        resultado = QFontDialog.getFont(self)
        if not isinstance(resultado, tuple) or len(resultado) < 2:
            return

        if isinstance(resultado[0], QFont):
            fuente, ok = resultado[0], bool(resultado[1])
        elif isinstance(resultado[1], QFont):
            ok, fuente = bool(resultado[0]), resultado[1]
        else:
            return

        if ok:
            cursor = self.area_texto.textCursor()
            formato = QTextCharFormat()
            formato.setFont(fuente)

            if cursor.hasSelection():
                cursor.mergeCharFormat(formato)
                self.area_texto.mergeCurrentCharFormat(formato)
            else:
                self.area_texto.setCurrentFont(fuente)

            try:
                self.combobox_fuentes.setCurrentText(fuente.family())
            except Exception:
                pass

    def fun_fondo(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.area_texto.setStyleSheet(f"background-color: {color.name()};")

    def fun_encontrar_sig(self):
        text = self.buscar.text()
        if not text:
            return

        cursor = self.area_texto.textCursor()
        document = self.area_texto.document()

        found = document.find(text, cursor)

        if found.isNull():
            inicio = QTextCursor(document)
            found = document.find(text, inicio)
            if found.isNull():
                self.barra_estado.showMessage("No se encontraron coincidencias", 3000)
                return

        self.area_texto.setTextCursor(found)

    def fun_encontrar_prev(self):
        text = self.buscar.text()
        if not text:
            return

        cursor = self.area_texto.textCursor()
        document = self.area_texto.document()

        found = document.find(text, cursor, QTextDocument.FindBackward)

        if found.isNull():
            fin = QTextCursor(document)
            fin.movePosition(QTextCursor.End)
            found = document.find(text, fin, QTextDocument.FindBackward)
            if found.isNull():
                self.barra_estado.showMessage("No se encontraron coincidencias anteriores", 3000)
                return

        self.area_texto.setTextCursor(found)

    def fun_reemplazar_uno(self):
        cursor = self.area_texto.textCursor()
        if cursor.hasSelection():
            cursor.insertText(self.reemplazar.text())
            self.barra_estado.showMessage("Reemplazo realizado", 3000)
        self.fun_encontrar_sig()

    def fun_reemplazar_todo(self):
        search_text = self.buscar.text()
        replace_text = self.reemplazar.text()
        if not search_text:
            return
        content = self.area_texto.toPlainText()
        new_content = content.replace(search_text, replace_text)
        self.area_texto.setPlainText(new_content)
        self.barra_estado.showMessage("Reemplazo de todas las coincidencias completado", 3000)
        self.word_counter.update_from_text(self.area_texto.toPlainText())

    def fun_mostrar_buscador(self):
        self.dock.show()
        self.buscar.setFocus()

    def reconocer_voz(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.6)
                recognizer.pause_threshold = 1.2
                recognizer.non_speaking_duration = 0.6
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""
        except Exception:
            return None

        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            return texto.strip()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

    def dictar_por_voz(self):
        texto = self.reconocer_voz()
        self.procesar_texto_de_voz(texto)

    def procesar_texto_de_voz(self, texto):
        if texto is None:
            return
        if texto == "":
            return
        self.area_texto.insertPlainText(texto + " ")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
