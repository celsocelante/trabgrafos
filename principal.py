from grafo import Grafo
f = open('entrada.txt', 'r')

lista_grafos = []
j=0;
line = f.readline().rstrip()
while line != '':

    n = int(line[0])
    m = int(line[2])
    source = int(line[4])
    target = int(line[6])

#    print n
#    print m
#    print source
#    print target

    lista_grafos.append(Grafo(n,m))

    for i in range(m):
        string = f.readline().rstrip()
        a1 = int(string[0])
        a2 = int(string[2])
        peso = int(string[4:])

        lista_grafos[j].add_aresta((a1,a2),peso)
        lista_grafos[j].add_vertice(a1)
        lista_grafos[j].add_vertice(a2)

    print lista_grafos[j]
    j+=1

    line = f.readline().rstrip() # linha em branco
    line = f.readline().rstrip()
