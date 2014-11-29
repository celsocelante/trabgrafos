from fila_minima import Fila

class Grafo:
    "Classe de um grafo"
    def __init__(self,n,m):
        # Constroi os atributos do objeto
        self.n = n
        self.m = m
        self.lista_adjacencias = {}

    def add_aresta(self, v, u, peso):
        # Adiciona uma aresta ao grafo, garantindo bidirecionalidade de toda aresta
        if v not in self.lista_adjacencias.keys():
            self.lista_adjacencias[v] = {u : peso}
        else: self.lista_adjacencias[v][u] = peso

        if u not in self.lista_adjacencias.keys():
            self.lista_adjacencias[u] = {v : peso}
        else: self.lista_adjacencias[u][v] = peso

    def dijkstra(self,inicial):
        # Cria as estruturas para a execucao do algoritmo
        distancias = {}
        fila_prioridade = Fila()
        predecessor = {}

        # Seta a distancia para todos os vertices como infinito e -1 para o predecessor
        for vertice in self.lista_adjacencias:
            distancias[vertice] = float("inf")
            # Adiciona cada vertice e sua distancia a fila de prioridade
            fila_prioridade.push(vertice,distancias[vertice])
            predecessor[vertice] = -1

        # Configura a distancia do inicial como 0 e insere na fila
        distancias[inicial] = 0
        fila_prioridade.push(inicial,distancias[inicial])
        # Remove o predecessor do inicial
        del predecessor[inicial]

        while not fila_prioridade.vazia():
            # Enquanto a fila possuir elementos, remove o menor elemento dela (o ultimo fechado)
            ultimo_fechado = fila_prioridade.pop()
            # Itera sobre os vizinhos do ultimo vertice fechado
            for vizinho in self.lista_adjacencias[ultimo_fechado].keys():
                distancia = self.lista_adjacencias[ultimo_fechado][vizinho]
                # Calcula nova distancia
                nova_distancia = distancia + distancias[ultimo_fechado]
                ''' Se a distancia for menor, insere o novo vertice a fila de prioridade, atualiza a distancia
                com a ultima calculada e altera o predecessor '''
                if nova_distancia < distancias[vizinho]:
                    fila_prioridade.push(vizinho,nova_distancia)
                    distancias[vizinho] = nova_distancia
                    predecessor[vizinho] = ultimo_fechado

        # Retorna uma estrutura com as distancias e a arvore de caminhos minimos
        return distancias, predecessor

    # Metodo para iterar sobre a arvore minima
    def caminhoMaisCurto(self,grafo,inicio,fim):
        i = inicio
        f = fim

        # Executa Dijkstra no grafo de entrada e armazena a arvore de caminhos minimos minima e distancias
        D, P = grafo.dijkstra(inicio)
        # Estrutura que armazena o caminho calculado
        caminho = []

        # Se os vertices de entrada nao estiverem arvore de caminhos minimos, nao ha caminho entre eles
        if inicio not in P.keys() and inicio not in P.values():
            print caminho
            return 'Envio de mensagens de %d a %d: nao ha caminho entre %d e %d.\n' %(i, f, i, f)
        if fim not in P.keys() and fim not in P.values():
            print caminho
            return 'Envio de mensagens de %d a %d: nao ha caminho entre %d e %d.\n' %(i, f, i, f)

        # Determina o caminho iterando sobre a arvore de caminhos minimos
        if inicio in P.keys():
            while True:
                caminho.append(inicio)
                if inicio == fim:
                    break
                inicio = P[inicio]
        else:
            while True:
                caminho.append(fim)
                if inicio == fim:
                    caminho.reverse()
                    break
                fim = P[fim]

        print caminho
        # Retorna custo de envio de mensagens
        return 'Envio de mensagens de %d a %d: %d\n' %(i, f, D[f])


    def __str__(self):
        # Metodo 'stringfy' da classe
        return 'Grafo: ' + str(self.lista_adjacencias)















#
