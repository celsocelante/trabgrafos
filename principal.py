from grafo import Grafo
import sys

# Verifica se os argumentos de entrada sao consistentes
if len(sys.argv) != 3:
    print "Uso: \"python %s [arquivo de entrada] [arquivo de saida]\"" % (sys.argv[0])
    exit()

# Obtem os nomes dos arquivos de entrada e saida por parametro
entrada = sys.argv[1]
saida = sys.argv[2]

# Verifica se o arquivo de entrada pode ser aberto
try:
    f = open(entrada, 'r')
except (IOError, OSError) as e:
    print "Erro ao tentar ler o arquivo de entrada"
    exit()

nf = open(saida, 'w')

# Estrutura para armazenar todos os grafos lidos do arquivo
lista_grafos = []
j = 0;

# Le a primeira do arquivo e remove o /n
linha = f.readline().rstrip()

# Enquanto nao for o fim do arquivo, le todas os dados
while linha != '':
    try:
        # Armazena o numero de vertices
        n = int(linha[0])
        # Armazena o numero de arestas
        m = int(linha[2])
        # Armazena o vertice de origem
        inicio = int(linha[4])
        # Armazena o vertice de destino
        fim = int(linha[6])
    except (IndexError, ValueError) as e:
        print "Arquivo de entrada inconsistente"
        exit()

    # Constroi um objeto de com os dados anteriores e adiciona a lista
    lista_grafos.append(Grafo(n,m))

    # Iteracao para proximas as m linhas do arquivo
    for i in range(m):
        try:
            # Le a linha
            linha = f.readline().rstrip()
            # Armazena o primeiro vertice da aresta
            v1 = int(linha[0])
            # Armazena o segundo vertice da aresta
            v2 = int(linha[2])
            # Armazena o custo da aresta
            peso = int(linha[4:])
        except (IndexError, ValueError) as e:
            print "Arquivo de entrada inconsistente"
            exit()

        # Adiciona a aresta lida ao objeto
        lista_grafos[j].add_aresta(v1,v2,peso)

    # Escreve no arquivo de saida
    nf.write(lista_grafos[j].caminhoMaisCurto(lista_grafos[j],inicio,fim))

    j += 1

    # Linha em branco a ser descartada
    linha = f.readline().rstrip()
    # Proxima linha a ser lida
    linha = f.readline().rstrip()

print "Arquivo de saida %s gerado" % (saida)
