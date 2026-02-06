# LibreWord
Editor de texto en PySide6

Este es un proyecto de un editor de texto hecho en Python usando
PySide6. Permite crear archivos de texto, abrirlos, guardarlos y también
buscar y reemplazar texto. También tiene un contador de palabras y
algunas opciones de edición.

Funciones principales: - Crear un archivo nuevo - Abrir archivos .txt -
Guardar - Salir del programa - Copiar, cortar y pegar - Deshacer y
rehacer - Cambiar la fuente - Cambiar el color del fondo del editor -
Buscar y reemplazar texto - Contador de palabras automático

Requisitos: Instalar PySide6: pip install PySide6 (version PySide6==6.9.2)

Los iconos deben estar en la misma carpeta que el archivo del programa.

Cómo ejecutar: python main.py

Estructura básica: main.py nuevo.png abrir.png guardar.png salir.png
deshacer.png rehacer.png copiar.png cortar.png pegar.png color.png
funete.png buscar.png README.md

<img width="1919" height="991" alt="image" src="https://github.com/user-attachments/assets/2c96293c-ba7c-4f66-8c88-0b638eb493a7" />

He firmado el .exe
<img width="1428" height="286" alt="image" src="https://github.com/user-attachments/assets/6ca8e2be-559d-4829-bc35-d06cbd00d64b" />
<img width="1896" height="99" alt="image" src="https://github.com/user-attachments/assets/2dcdf662-940e-4f2c-95ed-dacb48dfb8b1" />
<img width="1443" height="704" alt="image" src="https://github.com/user-attachments/assets/08742f81-790c-4f80-b15a-3544e3299fe6" />

He generado un archivo instalador 
<img width="999" height="453" alt="image" src="https://github.com/user-attachments/assets/478a8df7-9d71-40ca-b698-57f17a200c93" />

y he subido el .exe y el instalador con el comando gh release 
<img width="1888" height="439" alt="image" src="https://github.com/user-attachments/assets/2ea45e99-9ed3-4a08-b889-4039b4ed89a5" />

Por último, he editado el código de mi .py para que también funcione el dictado de voz.

## Cambios finales: contador de palabras mediante clase importada

En esta última edición he rehecho la parte del conteo (palabras, caracteres y tiempo estimado de lectura).  
En lugar de calcularlo con mis propias funciones y un `QLabel`, ahora lo hago mediante una clase externa proporcionada (`WordCounterWidget`) que importo desde `contadorWidget.py`.

Esta clase se encarga de:
- Contar palabras y caracteres a partir del texto actual.
- Calcular el tiempo de lectura estimado.
- Mostrar estos datos directamente en la barra de estado del editor.
- Actualizarse automáticamente cada vez que el texto cambia.

## Señales (Signals) usadas en la aplicación

En PySide6 (Qt), una **señal** es un evento que emite un componente (botón, acción, editor de texto, etc.) y se conecta a un **slot** (una función/método) que se ejecuta cuando ocurre ese evento.

A continuación se listan **todas las señales conectadas** en este proyecto:

### 1) Señales del editor de texto (QTextEdit)

- `self.area_texto.textChanged` → `lambda: self.word_counter.update_from_text(self.area_texto.toPlainText())`  
  **Descripción:** cada vez que cambia el texto del editor, se actualiza el contador (palabras, caracteres y tiempo de lectura).

---

### 2) Señales de acciones del menú/barra de herramientas (QAction)

Estas señales se disparan cuando el usuario pulsa un elemento del menú o un icono de la barra.

- `self.nuevo.triggered` → `fun_nuevo()`  
  **Descripción:** limpia el editor y crea un documento nuevo.

- `self.abrir.triggered` → `fun_abrir()`  
  **Descripción:** abre un archivo `.txt` y lo carga en el editor.

- `self.guardar.triggered` → `fun_guardar()`  
  **Descripción:** guarda el contenido del editor en un archivo `.txt`.

- `self.salir.triggered` → `fun_salir()`  
  **Descripción:** cierra la aplicación.

- `self.deshacer.triggered` → `fun_deshacer()`  
  **Descripción:** deshace la última acción en el editor.

- `self.rehacer.triggered` → `fun_rehacer()`  
  **Descripción:** rehace la última acción deshecha.

- `self.copiar.triggered` → `fun_copiar()`  
  **Descripción:** copia el texto seleccionado al portapapeles.

- `self.cortar.triggered` → `fun_cortar()`  
  **Descripción:** corta el texto seleccionado al portapapeles.

- `self.pegar.triggered` → `fun_pegar()`  
  **Descripción:** pega el contenido del portapapeles en la posición del cursor.

- `self.color.triggered` → `fun_fondo()`  
  **Descripción:** abre un selector de color y cambia el color de fondo del editor.

- `self.fuente.triggered` → `fun_dialogo_fuente()`  
  **Descripción:** abre el diálogo de selección de fuente y aplica la fuente al texto.

- `self.buscarAct.triggered` → `fun_mostrar_buscador()`  
  **Descripción:** muestra el panel (dock) de Buscar / Reemplazar.

- `self.dictado_voz.triggered` → `dictar_por_voz()`  
  **Descripción:** activa el dictado por voz, reconoce el audio y escribe el texto reconocido en el editor.

---

### 3) Señales del panel de Buscar / Reemplazar (QPushButton)

- `self.btn_sig.clicked` → `fun_encontrar_sig()`  
  **Descripción:** busca la siguiente coincidencia del texto indicado.

- `self.btn_prev.clicked` → `fun_encontrar_prev()`  
  **Descripción:** busca la coincidencia anterior del texto indicado.

- `self.btn_reemplazar.clicked` → `fun_reemplazar_uno()`  
  **Descripción:** reemplaza la coincidencia seleccionada por el texto de reemplazo.

- `self.btn_reemplazar_todo.clicked` → `fun_reemplazar_todo()`  
  **Descripción:** reemplaza todas las coincidencias del texto buscado por el texto de reemplazo.

---

### 4) Señales del selector de fuentes (QComboBox)

- `self.combobox_fuentes.currentTextChanged` → `fun_fuente(fuente)`  
  **Descripción:** cambia la fuente del texto (seleccionado o la fuente actual) según la opción elegida en el combo.

---

### 5) Señales del contador importado (WordCounterWidget)

El proyecto usa una clase externa (`WordCounterWidget`) importada desde `contadorWidget.py`.
Esta clase incluye una señal propia:

- `WordCounterWidget.conteoActualizado(int palabras, int caracteres)`  
  **Descripción:** se emite cuando se actualiza el conteo de palabras y caracteres.  
  **Nota:** en este proyecto no se conecta a ningún slot, pero existe en el widget y podría usarse para reaccionar a cambios del conteo.


