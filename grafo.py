class Grafo:
    "Classe de um grafo"
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.lista_vertices = []
        self.lista_arestas = [] 
        self.lista_arestas_pesos = []
        self.lista_vertices_pesos = []

    def add_vertice(self,vertice):
        if not vertice in self.lista_vertices:
            self.lista_vertices.append({vertice : 0})
            self.lista_vertices_pesos.append(float('inf'))

    def add_aresta(self,aresta,peso):
        self.lista_arestas.append(aresta)
        self.lista_arestas_pesos.append(peso)

    def dijkstra(self,inicial):
        #Inicializa distancia do vertice inicial com zero
        #rever
        pos = self.lista_vertices.index(inicial.key())
        self.lista_vertices_pesos.index(pos) = 0

        lista_vertices_fechados = []
        lista_vertices_abertos = self.lista_vertices

        #while not lista_vertice_abertos.isEmpty():


    def __str__(self):
        return 'Arestas: ' + ','.join(map(str,self.lista_arestas)) + '\nPesos: ' + ','.join(map(str,self.lista_arestas_pesos))
