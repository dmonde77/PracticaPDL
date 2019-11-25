#!/usr/bin/env python

from pathlib import Path
import Lexeador, Parseador, argparse

# Ayuda del programa y gestión de argumentos
argumentsParse = argparse.ArgumentParser(description='Procesador para el lenguaje Javascript-PDL')

# Argumento verbosidad
argumentsParse.add_argument("-v", action="store_true", help="Verbosidad")

# Argumento fichero de entrada obligatorio
argumentsParse.add_argument("-i", type=str, required=True, help="Archivo de entrada")

# Obtiene los argumentos
arguments = argumentsParse.parse_args()

# Argumento de archivo a analizar
inputFile = arguments.i

# Base de la ruta
sourceFolder = Path.home() / Path("PycharmProjects/PracticaPDL/archivos")

# Ruta completa a archivo a analizar
source = sourceFolder / inputFile

# Informamos del archivo que estamos abriendo
print("Procesando {}".format(inputFile))

# Parseamos el fichero
Parseador.parser.parse(source.read_text())
parser = " ".join(Parseador.parsero)

# Lo tokenizamos haciéndolo pasar por el analizador léxico de nuevo
Lexeador.lexer.input(source.read_text())
tokenizado = Lexeador.tokeniza()

# Crea diferentes carpetas para los dónde guardar los archivos de salida
outputFolder = inputFile + "_out"
outputFolder = sourceFolder / outputFolder
outputFolder.mkdir(exist_ok=True)

# Establece los ficheros
ficheroTokens = outputFolder / "tokens.txt"
ficheroTS = outputFolder / "ts.txt"
ficheroParser = outputFolder / "parser.txt"

print("Escribiendo fichero de tokens en {}".format(ficheroTokens))
print("Escribiendo fichero de tabla de símbolos en {}".format(ficheroTokens))
print("Escribiendo fichero de parser en {}".format(ficheroTokens))

# Escribe en los ficheros
ficheroTokens.write_text(tokenizado)
ficheroTS.write_text(str(Lexeador.gestorTS))
# Se necesita añadir un salto de línea al final del fichero del parser para que VASt no explote
ficheroParser.write_text(parser + "\n")

# Opción de verbosidad
if arguments.v:
    print("----Resultados----")
    print("Tokenks:\n" + tokenizado + "\n")
    print("Tablas de símbolos:\n" + str(Lexeador.gestorTS) + "\n")
    print("Parser:\n" + parser)
