class Grafo:
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.lista_vertices = []
        self.lista_arestas = []
        self.lista_arestas_pesos = []
        
    def add_vertice(self,vertice):
        if not vertice in self.lista_vertices:
            self.lista_vertices.append(vertice)

    def add_aresta(self,aresta,peso):
        self.lista_arestas.append(aresta)
        self.lista_arestas_pesos.append(peso)

    def dijkstra(source,target):
        return "Menor caminho"

    def __str__(self):
        return 'Arestas: ' + ','.join(map(str,self.lista_arestas)) + '\nPesos: ' + ','.join(map(str,self.lista_arestas_pesos))
