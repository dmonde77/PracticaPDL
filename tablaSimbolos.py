
class Gestor:
	def __init__(self):
		self.contador = 0
		self.stack = []	

	def __str__(self):
		strings = []

		for t in self.stack:
			strings.append(str(t))

		return "\n".join(strings)

	def crearTabla(self):
		tabla = Tabla(self.contador)
		self.stack.append(tabla)
		self.contador += 1
		return tabla

	def eliminarTabla(self):
		self.stack.pop()
		return





class Tabla:

	def __init__(self, contador):

		# Key: simbolo.name 	Value: objecto Símbolo
		self.symbols = {}
		self.contador = contador

	def __str__(self):
		strings = [ "Tabla de símbolos # {} :".format(self.contador) ]
		
		for s in self.symbols.values():
			strings.append(str(s))

		return "\n".join(strings)

	def getSimbolos(self):
		return self.symbols

	def insertar(self, simbolo):
		if self.symbols.__contains__(simbolo.name):
			return False
		else:
			self.symbols[simbolo.name] = simbolo
			return True
		
	def insertarAtributo(self):
		return

	def buscarLex(self):
		return

class Simbolo:

	def __init__(self, name):
		self.name = name
		self.atributos = [ ["tipo", ""], ["despl", ""] ]

	def __str__(self):
		return "\t * LEXEMA : \'{}\'".format(self.name)

	def setTipo(self, tipo):
		self.atributos[0][1] = tipo	

	def setDespl(self, despl):
		self.atributos[1][1] = despl

	atributos = [
		"tipo",
		"despl"
	]

	atributosF = [
		"numParam",
		"tipoParam",
		"modoParam",
		"tipoRetorno",
		"etiq",
		"param"
	]
