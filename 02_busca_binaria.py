#ALGORITIMO BUSCA BINARIA
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de 
#busca, divide a lista em duas metades e procura pelo valor de busca
#apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na lista.

from time import time
from data.lista_nomes import nomes 

comps = 0

def busca_binaria(lista, valor_busca):
    """
       função que implementa o algoritimo de busca biária

       Retorna a posição onde valor_busca foi encontrado ou
       ou valor convencial -1 se valor_busca não existir na lista
    """
    ini = 0                   # primeira posição
    fim = len(lista) - 1      # útima posição

    while ini <= fim:
        meio = (ini + fim) // 2     # Operador //(duas barras) é divisão inteira

        # 1º caso: lista[meio] é igual a valor busca
        if lista[meio] == valor_busca:  # Encontrou!
            return meio  # meio é a posição onde valor_busca está na lista
        
        # 2º caso: valor_busca é menor que lista[meio]
        elif valor_busca <lista[meio]:
            fim = meio - 1  # descarta a 2º metade da lista

        # 3º caso: valor_busca é maior que lista[meio]
        else:
            ini = meio + 1   #descartar a 1º metade da lista

        # 4º caso: valor_busca não encontrado na lista
    return - 1

hora_ini = time()
print(f"posição de LEANDRO: {busca_binaria(nomes, 'LEANDRO')}")
hora_fim = time()
print(f"Tempo gasto procurando LEANDRO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"posição de ZUZIVALDO: {busca_binaria(nomes, 'ZUZIVALDO')}")
hora_fim = time()
print(f"Tempo gasto procurando ZUZIVALDO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"posição de BELERINA: {busca_binaria(nomes, 'BELERINA')}")
hora_fim = time()
print(f"Tempo gasto procurando BELERINA: {(hora_fim - hora_ini) * 1000}ms")