import Lexeador
import ply.yacc as yacc
from sys import stderr

# Lista de tokens (idéntica a la del analizador léxico)
tokens = Lexeador.tokens

# Lista de reglas
parsero = [ "Ascendente" ]

# Error sintáctico
def p_error(p):
    if p:
        stderr.write("Error de sintaxis en la línea {}: Token {} inesperado\n".format(p.lineno, Lexeador.imprimeToken(p)))
        while True:
            tok = parser.token()  # Get the next token
            if not tok or tok.type == 'RBRACE':
                break
        parser.restart()
    else:
        print('Error de sintaxis: Se ha llegado al final del fichero')

# Reglas de analísis sintáctico, mucho más claras en el fichero parser.out

def p_program_declaracionesYsentencias(p):
    'program : declaracionesYsentencias program'
    parsero.append("1")

def p_program_funcion(p):
    'program : funcion program'
    parsero.append("2")

def p_program_fin(p):
    'program :'
    parsero.append("3")

def p_declaraciones(p):
    'declaracionesYsentencias : VAR tipo ID PUNTOYCOMA'
    parsero.append("4")

def p_if(p):
    'declaracionesYsentencias : IF LPAREN expresion RPAREN sentencia'
    parsero.append("5")

def p_while(p):
    'declaracionesYsentencias : WHILE LPAREN expresion RPAREN LBRACE interiorFuncion RBRACE'
    parsero.append("6")

def p_sentencia(p):
    'declaracionesYsentencias : sentencia'
    parsero.append("7")

def p_int(p):
    'tipo : INT'
    parsero.append("8")

def p_string(p):
    'tipo : STRING'
    parsero.append("9")

def p_boolean(p):
    'tipo : BOOLEAN'
    parsero.append("10")

def p_sentencia_asignacion(p):
    'sentencia : ID asignacion'
    parsero.append("11")

def p_sentencia_return(p):
    'sentencia : RETURN sentenciaReturn PUNTOYCOMA'
    parsero.append("12")

def p_sentencia_print(p):
    'sentencia : PRINT LPAREN expresion RPAREN PUNTOYCOMA'
    parsero.append("13")

def p_sentencia_input(p):
    'sentencia : INPUT LPAREN ID RPAREN PUNTOYCOMA'
    parsero.append("14")

def p_sentencia_funcion(p):
    'sentencia : ID LPAREN argumentosLlamada RPAREN PUNTOYCOMA'
    parsero.append("15")

def p_asignacion(p):
    'asignacion : IGUAL expresion PUNTOYCOMA'
    parsero.append("16")

def p_asignacion_orequal(p):
    'asignacion : ORIGUAL expresion PUNTOYCOMA'
    parsero.append("17")

def p_return_expresion(p):
    'sentenciaReturn : expresion'
    parsero.append("18")

def p_return_fin(p):
    'sentenciaReturn :'
    parsero.append("19")

def p_argumentosLlamada_expresion(p):
    'argumentosLlamada : expresion argumentosLlamadaExtra'
    parsero.append("20")

def p_argumentosLlamada_fin(p):
    'argumentosLlamada :'
    parsero.append("21")

def p_argumentosLlamadaExtra(p):
    'argumentosLlamadaExtra : COMA expresion argumentosLlamadaExtra'
    parsero.append("22")

def p_argumentosLlamadaExtra_fin(p):
    'argumentosLlamadaExtra :'
    parsero.append("23")

def p_funcion(p):
    'funcion : FUNCTION declaracionArgumentos ID LPAREN argumentos RPAREN LBRACE interiorFuncion RBRACE'
    parsero.append("24")

def p_declaracionArgumentos(p):
    'declaracionArgumentos : tipo'
    parsero.append("25")

def p_declaracionArgumentos_fin(p):
    'declaracionArgumentos :'
    parsero.append("26")

def p_interiorFuncion(p):
    'interiorFuncion : declaracionesYsentencias interiorFuncion'
    parsero.append("27")

def p_interiorFuncion_fin(p):
    'interiorFuncion :'
    parsero.append("28")

def p_argumentos(p):
    'argumentos : tipo ID argumentosExtra'
    parsero.append("29")

def p_argumentos_fin(p):
    'argumentos :'
    parsero.append("30")

def p_argumentosExtra(p):
    'argumentosExtra : COMA tipo ID argumentosExtra'
    parsero.append("31")

def p_argumentosExtra_fin(p):
    'argumentosExtra :'
    parsero.append("32")

def p_expresion_or(p):
    'expresion : expresion OR expresionMAYOR'
    parsero.append("33")

def p_expresion_or_mayor(p):
    'expresion : expresionMAYOR'
    parsero.append("34")

def p_expresion_mayor(p):
    'expresionMAYOR : expresionMAYOR MAYOR expresionMAS'
    parsero.append("35")

def p_expresion_mayor_mas(p):
    'expresionMAYOR : expresionMAS'
    parsero.append("36")

def p_expresion_mas(p):
    'expresionMAS : expresionMAS MAS expresionLiteral'
    parsero.append("37")

def p_expresion_mas_literal(p):
    'expresionMAS : expresionLiteral'
    parsero.append("38")

def p_expresionLiteral_id(p):
    'expresionLiteral : ID'
    parsero.append("39")

def p_expresionLiteral_integer(p):
    'expresionLiteral : INTEGER'
    parsero.append("40")

def p_expresionLiteral_true(p):
    'expresionLiteral : TRUE'
    parsero.append("41")

def p_expresionLiteral_false(p):
    'expresionLiteral : FALSE'
    parsero.append("42")

def p_expresionLiteral_cadena(p):
    'expresionLiteral : CADENA'
    parsero.append("43")

def p_expresionLiteral_llamada(p):
    'expresionLiteral : ID LPAREN argumentosLlamada RPAREN'
    parsero.append("44")

def p_expresionLiteral_expresion(p):
    'expresionLiteral : LPAREN expresion RPAREN'
    parsero.append("45")

parser = yacc.yacc()



