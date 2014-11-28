class Fila:
	fila = {}

	def __init__(self):
		return

	def push(self,vertice,peso):
		self.fila[vertice] = peso

	def pop(self):
		menor = 10000
		chave_menor = None
		for vertice in self.fila:
			if self.fila[vertice] < menor:
				menor = self.fila[vertice]
				chave_menor = vertice

		del self.fila[chave_menor]
		return chave_menor

	def vazia(self):
		return not self.fila.keys() == []