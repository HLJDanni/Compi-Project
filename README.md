# Compi-Project

Compilador en Python con PLY

Introducción

Este proyecto implementa un compilador en Python utilizando la librería PLY (Python Lex-Yacc) para procesar un lenguaje de programación de estructura similar a C.

El objetivo es desarrollar un analizador léxico y sintáctico que pueda leer un archivo con código fuente, identificar tokens y generar reportes en formato HTML. Además, el compilador permitirá la generación de código en tres direcciones optimizado para ser compilado en C++.

Características

Análisis léxico: Identificación de palabras clave, identificadores, números y símbolos.

Generación de reportes: Creación de un archivo HTML con los tokens identificados y su tipo.

Modularidad: Estructura adaptable para agregar nuevas reglas gramaticales y optimizar la generación de código.

Configurabilidad: Permite modificar la gramática y los símbolos aceptados según las necesidades del lenguaje.

Requisitos

Python 3.x

PLY (Python Lex-Yacc)

Para instalar PLY, ejecuta:

pip install ply

Ejecución

Guarda el código en un archivo Python y ejecúta:

python lexer.py

Esto generará un archivo tokens.html con los tokens analizados.

Contacto

Si tienes alguna duda o sugerencia, siéntete libre de contribuir o abrir un issue en este repositorio.
