#!/bin/bash

i=1
mkdir saidas
# Executa o programa sobre todos os arquivos de entrada
for arquivo in entradas/*.txt
do
	python principal.py $arquivo saidas/saida_$i.txt;
	i=$((i+1))
done