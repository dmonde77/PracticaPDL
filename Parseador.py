import Lexeador
import ply.yacc as yacc

# Lista de tokens (idéntica a la del analizador léxico)
tokens = Lexeador.tokens

# Lista de reglas
parsero = [ "Ascendente" ]

def p_error(p):
    if p:
        print("Error de sintaxis en la línea {}: Token ({}, '{}') inesperado".format(p.lineno, p.type, p.value))
        # exit(1);
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
    'interiorFuncion   : declaracionesYsentencias interiorFuncion'
    parsero.append("27")

def p_interiorFuncion_fin(p):
    'interiorFuncion   :'
    parsero.append("28")

def p_argumentos(p):
    'argumentos   : tipo ID argumentosExtra'
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
    'expresion : expresion OR erre'
    parsero.append("33")

def p_expresion_erre(p):
    'expresion : erre'
    parsero.append("34")

def p_erre_mayor(p):
    'erre : erre MAYOR uu'
    parsero.append("35")

def p_erre_uu(p):
    'erre : uu'
    parsero.append("36")

def p_uu_plus(p):
    'uu : uu MAS uve'
    parsero.append("37")

def p_uu_uve(p):
    'uu : uve'
    parsero.append("38")

def p_uve_id(p):
    'uve : ID'
    parsero.append("39")

def p_uve_integer(p):
    'uve : INTEGER'
    parsero.append("40")

def p_uve_true(p):
    'uve : TRUE'
    parsero.append("41")

def p_uve_false(p):
    'uve : FALSE'
    parsero.append("42")

def p_uve_cadena(p):
    'uve : CADENA'
    parsero.append("43")

def p_uve_funcion(p):
    'uve  : ID LPAREN argumentosLlamada RPAREN'
    parsero.append("44")

def p_uve_expresion(p):
    'uve  : LPAREN expresion RPAREN'
    parsero.append("45")

parser = yacc.yacc(debug=True)



