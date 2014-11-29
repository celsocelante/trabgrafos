from grafo import Grafo
f = open('entrada.txt', 'r')
nf = open('saida.txt', 'w')


lista_grafos = []
j=0;

line = f.readline().rstrip()
while line != '':

    n = int(line[0])
    m = int(line[2])
    inicio = int(line[4])
    fim = int(line[6])

    lista_grafos.append(Grafo(n,m))

    for i in range(m):
        string = f.readline().rstrip()
        v1 = int(string[0])
        v2 = int(string[2])
        peso = int(string[4:])

        lista_grafos[j].add_aresta(v1,v2,peso)


    nf.write(lista_grafos[j].caminhoMaisCurto(lista_grafos[j],inicio,fim))

    j+=1

    line = f.readline().rstrip() # linha em branco
    line = f.readline().rstrip()
