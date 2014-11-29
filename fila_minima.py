class Fila:
	# Estrutura da fila
	fila = {}

	def __init__(self):
		return

	def push(self,vertice,peso):
		# Adiciona a entrada a fila
		self.fila[vertice] = peso

	def pop(self):
		# Seta o menor como infinito para comparacoes posteriores
		menor = float("inf")
		chave_menor = None
		# Determina a menor chave da fila
		for vertice in self.fila:
			if self.fila[vertice] < menor:
				menor = self.fila[vertice]
				chave_menor = vertice
		# Retorna e remove a menor chave da fila
		del self.fila[chave_menor]
		return chave_menor

	def vazia(self):
		# Verifica se a fila esta vazia
		return self.fila.keys() == []
