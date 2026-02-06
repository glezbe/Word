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



