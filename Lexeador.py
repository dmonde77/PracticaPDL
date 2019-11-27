
import ply.lex as lex
import tablaSimbolos as ts


# Palabras reservadas
reserved = {
    'while': 'WHILE',
    'input': 'INPUT',
    'print': 'PRINT',
    'var': 'VAR',
    'int': 'INT',
    'function': 'FUNCTION',
    'string': 'STRING',
    'boolean': 'BOOLEAN',
    'if': 'IF',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Lista de tokens
tokens = list(reserved.values()) + [

    # Operadores
    'MAS',
    'OR',
    'MAYOR',

    # Asignaciones
    'IGUAL',
    'ORIGUAL',

    # Delimitadores
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMA', 'PUNTOYCOMA',

    # Identificadores y literales
    'ID', 'INTEGER', 'CADENA',

]

# Gestor de la tabla de símbolos
gestorTS = ts.Gestor()

# Tabla global
tablaG = gestorTS.crearTabla()

# Acciones para cada token

# Ignorar
t_ignore        = ' \t'

# Operadores
t_MAS           = r'\+'
t_OR            = r'\|\|'
t_MAYOR         = r'>'

# Operadores de asignación
t_IGUAL         = r'='
t_ORIGUAL       = r'\|='

# Delimitadores
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LBRACE        = r'\{'
t_RBRACE        = r'\}'
t_COMA          = r','
t_PUNTOYCOMA    = r';'

# Identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved.get(t.value)
    else:
        tablaG.insertar(ts.Simbolo(t.value))
        t.value = list(tablaG.getSimbolos().keys()).index(t.value)
    return t

# Enteros
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Cadenas
t_CADENA = r'\"([^\\\n]|(\\.))*?\"'

# Comentarios
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Errores
def t_error(t):
    print("Error léxico")
    print("Carácter no admitido: '{}'".format(t.value[0]))
    print("En línea ")
    t.lexer.skip(1)

# Salto de línea
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Imprime los tokens en el formato pedido
def tokeniza():
    tokenizado = []

    # Recorre la lista de tokens
    for tok in lexer:
        tokenizado.append(imprimeToken(tok))

    return "\n".join(tokenizado)

def imprimeToken(tok):
    # Es una palabra reservada, se busca su índice para cumplir con el formato de la asignatura
    if tok.type.lower() in reserved:
        return " < palRes , {} > // palRes: {}".format(list(reserved.values()).index(tok.value.upper()), tok.value)

    # Es un identificador, se busca su posición en la tabla de símbolos para cumplir con el formato de la asignatura
    elif tok.type == "ID":
        return " < {} , {} > // identificador: {}".format(tok.type, tok.value, list(tablaG.getSimbolos().keys())[int(tok.value)])

    # Es un literal
    elif tok.type in ["CADENA", "INTEGER"]:
        return " < {} , {} >".format(tok.type, tok.value)

    # Es cualquier otro token
    else:
        return " < {} , - >".format(tok.type)

    # Token tal cúal lo ve el analizador
    # print("REAL: < {} , {} >".format(tok.type, tok.value))

lexer = lex.lex()