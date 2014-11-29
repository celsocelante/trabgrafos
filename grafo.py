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
        del predecessor[inicial]

        while fila_prioridade.vazia():
            ultimo_fechado = fila_prioridade.pop()

            for vizinho in self.lista_adjacencias[ultimo_fechado].keys():
                distancia = self.lista_adjacencias[ultimo_fechado][vizinho]
                nova_distancia = distancia + distancias[ultimo_fechado]
                if(nova_distancia < distancias[vizinho]):
                    fila_prioridade.push(vizinho,nova_distancia)
                    distancias[vizinho] = nova_distancia
                    predecessor[vizinho] = ultimo_fechado


    #    print 'Arvore: ' + str(predecessor)
    #    print 'Distancias: ' + str(distancias)

        return distancias, predecessor


    def caminhoMaisCurto(self,grafo,inicio,fim):
        i = inicio
        f = fim
        D, P = grafo.dijkstra(inicio)


        caminho = []
        
        if inicio not in P.keys() and inicio not in P.values() :
            print caminho
            return 'Envio de mensagens de %d a %d: nao ha caminho entre %d e %d.\n' %(i, f, i, f)
        if fim not in P.keys() and fim not in P.values() :
            print caminho
            return 'Envio de mensagens de %d a %d: nao ha caminho entre %d e %d.\n' %(i, f, i, f)

        if inicio in P.keys() :
            while 1:
                caminho.append(inicio)
                if inicio == fim:
                    break
                inicio = P[inicio]
        else :
            while 1:
                caminho.append(fim)
                if inicio == fim:
                    caminho.reverse()
                    break
                fim = P[fim]


        print caminho
        return 'Envio de mensagens de %d a %d: %d\n' %(i, f, D[f])


    def __str__(self):
        return 'Grafo: ' + str(self.lista_adjacencias)















#
