
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN CADENA COMA FALSE FUNCTION ID IF IGUAL INPUT INT INTEGER LBRACE LPAREN MAS MAYOR OR ORIGUAL PRINT PUNTOYCOMA RBRACE RETURN RPAREN STRING TRUE VAR WHILEprogram : declaracionesYsentencias programprogram : funcion programprogram :declaracionesYsentencias : VAR tipo ID PUNTOYCOMAdeclaracionesYsentencias : IF LPAREN expresion RPAREN sentenciadeclaracionesYsentencias : WHILE LPAREN expresion RPAREN LBRACE interiorFuncion RBRACEdeclaracionesYsentencias : sentenciatipo : INTtipo : STRINGtipo : BOOLEANsentencia : ID asignacionsentencia : RETURN sentenciaReturn PUNTOYCOMAsentencia : PRINT LPAREN expresion RPAREN PUNTOYCOMAsentencia : INPUT LPAREN ID RPAREN PUNTOYCOMAsentencia : ID LPAREN argumentosLlamada RPAREN PUNTOYCOMAasignacion : IGUAL expresion PUNTOYCOMAasignacion : ORIGUAL expresion PUNTOYCOMAsentenciaReturn : expresionsentenciaReturn :argumentosLlamada : expresion argumentosLlamadaExtraargumentosLlamada :argumentosLlamadaExtra : COMA expresion argumentosLlamadaExtraargumentosLlamadaExtra :funcion : FUNCTION declaracionArgumentos ID LPAREN argumentos RPAREN LBRACE interiorFuncion RBRACEdeclaracionArgumentos : tipodeclaracionArgumentos :interiorFuncion : declaracionesYsentencias interiorFuncioninteriorFuncion :argumentos : tipo ID argumentosExtraargumentos :argumentosExtra : COMA tipo ID argumentosExtraargumentosExtra :expresion : expresion OR expresionMAYORexpresion : expresionMAYORexpresionMAYOR : expresionMAYOR MAYOR expresionMASexpresionMAYOR : expresionMASexpresionMAS : expresionMAS MAS expresionLiteralexpresionMAS : expresionLiteralexpresionLiteral : IDexpresionLiteral : INTEGERexpresionLiteral : TRUEexpresionLiteral : FALSEexpresionLiteral : CADENAexpresionLiteral : ID LPAREN argumentosLlamada RPARENexpresionLiteral : LPAREN expresion RPAREN'
    
_lr_action_items = {'$end':([0,1,2,3,7,13,14,19,48,56,60,61,72,74,79,80,86,93,],[-3,0,-3,-3,-7,-1,-2,-11,-12,-4,-16,-17,-15,-5,-13,-14,-6,-24,]),'VAR':([0,2,3,7,19,48,56,60,61,72,74,75,79,80,83,86,88,93,],[4,4,4,-7,-11,-12,-4,-16,-17,-15,-5,4,-13,-14,4,-6,4,-24,]),'IF':([0,2,3,7,19,48,56,60,61,72,74,75,79,80,83,86,88,93,],[6,6,6,-7,-11,-12,-4,-16,-17,-15,-5,6,-13,-14,6,-6,6,-24,]),'WHILE':([0,2,3,7,19,48,56,60,61,72,74,75,79,80,83,86,88,93,],[8,8,8,-7,-11,-12,-4,-16,-17,-15,-5,8,-13,-14,8,-6,8,-24,]),'FUNCTION':([0,2,3,7,19,48,56,60,61,72,74,79,80,86,93,],[9,9,9,-7,-11,-12,-4,-16,-17,-15,-5,-13,-14,-6,-24,]),'ID':([0,2,3,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,37,38,39,48,49,50,51,52,56,59,60,61,62,72,74,75,77,79,80,83,86,88,92,93,],[5,5,5,-7,-26,32,40,-8,-9,-10,-11,32,32,32,32,32,47,-25,32,32,55,-12,32,32,32,32,-4,32,-16,-17,5,-15,-5,5,85,-13,-14,5,-6,5,94,-24,]),'RETURN':([0,2,3,7,19,48,56,60,61,62,72,74,75,79,80,83,86,88,93,],[10,10,10,-7,-11,-12,-4,-16,-17,10,-15,-5,10,-13,-14,10,-6,10,-24,]),'PRINT':([0,2,3,7,19,48,56,60,61,62,72,74,75,79,80,83,86,88,93,],[11,11,11,-7,-11,-12,-4,-16,-17,11,-15,-5,11,-13,-14,11,-6,11,-24,]),'INPUT':([0,2,3,7,19,48,56,60,61,62,72,74,75,79,80,83,86,88,93,],[12,12,12,-7,-11,-12,-4,-16,-17,12,-15,-5,12,-13,-14,12,-6,12,-24,]),'INT':([4,9,64,90,],[16,16,16,16,]),'STRING':([4,9,64,90,],[17,17,17,17,]),'BOOLEAN':([4,9,64,90,],[18,18,18,18,]),'LPAREN':([5,6,8,10,11,12,20,21,22,23,24,32,37,38,47,49,50,51,52,59,],[20,23,24,37,38,39,37,37,37,37,37,52,37,37,64,37,37,37,37,37,]),'IGUAL':([5,],[21,]),'ORIGUAL':([5,],[22,]),'RBRACE':([7,19,48,56,60,61,72,74,75,79,80,82,83,86,87,88,91,],[-7,-11,-12,-4,-16,-17,-15,-5,-28,-13,-14,86,-28,-6,-27,-28,93,]),'PUNTOYCOMA':([10,27,28,29,30,31,32,33,34,35,36,40,43,44,57,65,66,67,69,70,71,78,],[-19,48,-18,-34,-36,-38,-39,-40,-41,-42,-43,56,60,61,72,-33,-35,-37,-45,79,80,-44,]),'INTEGER':([10,20,21,22,23,24,37,38,49,50,51,52,59,],[33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TRUE':([10,20,21,22,23,24,37,38,49,50,51,52,59,],[34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FALSE':([10,20,21,22,23,24,37,38,49,50,51,52,59,],[35,35,35,35,35,35,35,35,35,35,35,35,35,]),'CADENA':([10,20,21,22,23,24,37,38,49,50,51,52,59,],[36,36,36,36,36,36,36,36,36,36,36,36,36,]),'RPAREN':([20,29,30,31,32,33,34,35,36,41,42,45,46,52,53,54,55,58,64,65,66,67,68,69,73,76,78,81,85,89,94,95,],[-21,-34,-36,-38,-39,-40,-41,-42,-43,57,-23,62,63,-21,69,70,71,-20,-30,-33,-35,-37,78,-45,-23,84,-44,-22,-32,-29,-32,-31,]),'OR':([28,29,30,31,32,33,34,35,36,42,43,44,45,46,53,54,65,66,67,69,73,78,],[49,-34,-36,-38,-39,-40,-41,-42,-43,49,49,49,49,49,49,49,-33,-35,-37,-45,49,-44,]),'COMA':([29,30,31,32,33,34,35,36,42,65,66,67,69,73,78,85,94,],[-34,-36,-38,-39,-40,-41,-42,-43,59,-33,-35,-37,-45,59,-44,90,90,]),'MAYOR':([29,30,31,32,33,34,35,36,65,66,67,69,78,],[50,-36,-38,-39,-40,-41,-42,-43,50,-35,-37,-45,-44,]),'MAS':([30,31,32,33,34,35,36,66,67,69,78,],[51,-38,-39,-40,-41,-42,-43,51,-37,-45,-44,]),'LBRACE':([63,84,],[75,88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,13,14,]),'declaracionesYsentencias':([0,2,3,75,83,88,],[2,2,2,83,83,83,]),'funcion':([0,2,3,],[3,3,3,]),'sentencia':([0,2,3,62,75,83,88,],[7,7,7,74,7,7,7,]),'tipo':([4,9,64,90,],[15,26,77,92,]),'asignacion':([5,],[19,]),'declaracionArgumentos':([9,],[25,]),'sentenciaReturn':([10,],[27,]),'expresion':([10,20,21,22,23,24,37,38,52,59,],[28,42,43,44,45,46,53,54,42,73,]),'expresionMAYOR':([10,20,21,22,23,24,37,38,49,52,59,],[29,29,29,29,29,29,29,29,65,29,29,]),'expresionMAS':([10,20,21,22,23,24,37,38,49,50,52,59,],[30,30,30,30,30,30,30,30,30,66,30,30,]),'expresionLiteral':([10,20,21,22,23,24,37,38,49,50,51,52,59,],[31,31,31,31,31,31,31,31,31,31,67,31,31,]),'argumentosLlamada':([20,52,],[41,68,]),'argumentosLlamadaExtra':([42,73,],[58,81,]),'argumentos':([64,],[76,]),'interiorFuncion':([75,83,88,],[82,87,91,]),'argumentosExtra':([85,94,],[89,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaracionesYsentencias program','program',2,'p_program_declaracionesYsentencias','Parseador.py',26),
  ('program -> funcion program','program',2,'p_program_funcion','Parseador.py',30),
  ('program -> <empty>','program',0,'p_program_fin','Parseador.py',34),
  ('declaracionesYsentencias -> VAR tipo ID PUNTOYCOMA','declaracionesYsentencias',4,'p_declaraciones','Parseador.py',38),
  ('declaracionesYsentencias -> IF LPAREN expresion RPAREN sentencia','declaracionesYsentencias',5,'p_if','Parseador.py',42),
  ('declaracionesYsentencias -> WHILE LPAREN expresion RPAREN LBRACE interiorFuncion RBRACE','declaracionesYsentencias',7,'p_while','Parseador.py',46),
  ('declaracionesYsentencias -> sentencia','declaracionesYsentencias',1,'p_sentencia','Parseador.py',50),
  ('tipo -> INT','tipo',1,'p_int','Parseador.py',54),
  ('tipo -> STRING','tipo',1,'p_string','Parseador.py',58),
  ('tipo -> BOOLEAN','tipo',1,'p_boolean','Parseador.py',62),
  ('sentencia -> ID asignacion','sentencia',2,'p_sentencia_asignacion','Parseador.py',66),
  ('sentencia -> RETURN sentenciaReturn PUNTOYCOMA','sentencia',3,'p_sentencia_return','Parseador.py',70),
  ('sentencia -> PRINT LPAREN expresion RPAREN PUNTOYCOMA','sentencia',5,'p_sentencia_print','Parseador.py',74),
  ('sentencia -> INPUT LPAREN ID RPAREN PUNTOYCOMA','sentencia',5,'p_sentencia_input','Parseador.py',78),
  ('sentencia -> ID LPAREN argumentosLlamada RPAREN PUNTOYCOMA','sentencia',5,'p_sentencia_funcion','Parseador.py',82),
  ('asignacion -> IGUAL expresion PUNTOYCOMA','asignacion',3,'p_asignacion','Parseador.py',86),
  ('asignacion -> ORIGUAL expresion PUNTOYCOMA','asignacion',3,'p_asignacion_orequal','Parseador.py',90),
  ('sentenciaReturn -> expresion','sentenciaReturn',1,'p_return_expresion','Parseador.py',94),
  ('sentenciaReturn -> <empty>','sentenciaReturn',0,'p_return_fin','Parseador.py',98),
  ('argumentosLlamada -> expresion argumentosLlamadaExtra','argumentosLlamada',2,'p_argumentosLlamada_expresion','Parseador.py',102),
  ('argumentosLlamada -> <empty>','argumentosLlamada',0,'p_argumentosLlamada_fin','Parseador.py',106),
  ('argumentosLlamadaExtra -> COMA expresion argumentosLlamadaExtra','argumentosLlamadaExtra',3,'p_argumentosLlamadaExtra','Parseador.py',110),
  ('argumentosLlamadaExtra -> <empty>','argumentosLlamadaExtra',0,'p_argumentosLlamadaExtra_fin','Parseador.py',114),
  ('funcion -> FUNCTION declaracionArgumentos ID LPAREN argumentos RPAREN LBRACE interiorFuncion RBRACE','funcion',9,'p_funcion','Parseador.py',118),
  ('declaracionArgumentos -> tipo','declaracionArgumentos',1,'p_declaracionArgumentos','Parseador.py',122),
  ('declaracionArgumentos -> <empty>','declaracionArgumentos',0,'p_declaracionArgumentos_fin','Parseador.py',126),
  ('interiorFuncion -> declaracionesYsentencias interiorFuncion','interiorFuncion',2,'p_interiorFuncion','Parseador.py',130),
  ('interiorFuncion -> <empty>','interiorFuncion',0,'p_interiorFuncion_fin','Parseador.py',134),
  ('argumentos -> tipo ID argumentosExtra','argumentos',3,'p_argumentos','Parseador.py',138),
  ('argumentos -> <empty>','argumentos',0,'p_argumentos_fin','Parseador.py',142),
  ('argumentosExtra -> COMA tipo ID argumentosExtra','argumentosExtra',4,'p_argumentosExtra','Parseador.py',146),
  ('argumentosExtra -> <empty>','argumentosExtra',0,'p_argumentosExtra_fin','Parseador.py',150),
  ('expresion -> expresion OR expresionMAYOR','expresion',3,'p_expresion_or','Parseador.py',154),
  ('expresion -> expresionMAYOR','expresion',1,'p_expresion_or_mayor','Parseador.py',158),
  ('expresionMAYOR -> expresionMAYOR MAYOR expresionMAS','expresionMAYOR',3,'p_expresion_mayor','Parseador.py',162),
  ('expresionMAYOR -> expresionMAS','expresionMAYOR',1,'p_expresion_mayor_mas','Parseador.py',166),
  ('expresionMAS -> expresionMAS MAS expresionLiteral','expresionMAS',3,'p_expresion_mas','Parseador.py',170),
  ('expresionMAS -> expresionLiteral','expresionMAS',1,'p_expresion_mas_literal','Parseador.py',174),
  ('expresionLiteral -> ID','expresionLiteral',1,'p_expresionLiteral_id','Parseador.py',178),
  ('expresionLiteral -> INTEGER','expresionLiteral',1,'p_expresionLiteral_integer','Parseador.py',182),
  ('expresionLiteral -> TRUE','expresionLiteral',1,'p_expresionLiteral_true','Parseador.py',186),
  ('expresionLiteral -> FALSE','expresionLiteral',1,'p_expresionLiteral_false','Parseador.py',190),
  ('expresionLiteral -> CADENA','expresionLiteral',1,'p_expresionLiteral_cadena','Parseador.py',194),
  ('expresionLiteral -> ID LPAREN argumentosLlamada RPAREN','expresionLiteral',4,'p_expresionLiteral_llamada','Parseador.py',198),
  ('expresionLiteral -> LPAREN expresion RPAREN','expresionLiteral',3,'p_expresionLiteral_expresion','Parseador.py',202),
]
