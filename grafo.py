from filaminima import Fila

class Grafo:
    "Classe de um grafo"
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.lista_adjacencias = {}

    def add_aresta(self, v, u, peso):
        if v not in self.lista_adjacencias.keys() :
            self.lista_adjacencias[v] = {u : peso}
        else : self.lista_adjacencias[v][u] = peso

        if u not in self.lista_adjacencias.keys():
            self.lista_adjacencias[u] = {v : peso}
        else : self.lista_adjacencias[u][v] = peso

    def dijkstra(self,inicial):

        distancias = {} 
        fila_prioridade = Fila()
        predecessor = {}

        for vertice in self.lista_adjacencias:
            distancias[vertice] = 10000
            fila_prioridade.push(vertice,distancias[vertice])
            predecessor[vertice] = -1

        fila_prioridade.push(inicial,0)
        distancias[inicial] = 0
        #predecessor[inicial] = inicial

        while fila_prioridade.vazia():
            ultimo_fechado = fila_prioridade.pop()

            for vizinho in self.lista_adjacencias[ultimo_fechado].keys():
                distancia = self.lista_adjacencias[ultimo_fechado][vizinho]
                nova_distancia = distancia + distancias[ultimo_fechado]
                if(nova_distancia < distancias[vizinho]):
                    fila_prioridade.push(vizinho,nova_distancia)
                    distancias[vizinho] = nova_distancia
                    predecessor[vizinho] = ultimo_fechado


        print 'Arvore: ' + ','.join(map(str,predecessor.items()))
      #  print 'Distancias: ' + ','.join(map(str,distancias.items()))

        return distancias, predecessor


    def caminhoMaisCurto(self,grafo,inicio,fim):

        D, P = grafo.dijkstra(0)
        A = dict.fromkeys(P.keys())

            for v in P and e in A:
                A[v] = P[v]
    
        caminho = []

        while 1:
            caminho.append(fim)
            if fim == inicio:
                break


            fim = P[fim]

        caminho.reverse()
        return caminho

    def __str__(self):
        return 'Grafo: ' + ','.join(map(str,self.lista_adjacencias.items()))

