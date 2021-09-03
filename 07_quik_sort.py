# escolhe um dos elementos da lista para ser o pivô (na nossa implementação
# o ultimo elemento) e, na primeira passada, divide a lista, a partir, da #posição final da lista, em um sublista á esquerda contendo apenas valores #maiores que o pivô e outro sublista a direita, que contem apenas valores #maiores que o pivô.

# Em seguda, recursivamente, repete o processo em cada uma das sublista até que #toda a lista esteja ordenada.

passadas = 0
comps = 0
trocas = 0

def quik_sort(lista, ini = 0, fim = None):
    """
       função que implementa o algoritimo de ordenação quik Sort
       de forma recursiva
    """
    
    # Se fim for None, então consideramos a ultima posição da lista
    if fim <= ini:
        fim = len(lista) -1

    # Para continuarmos, precisamos que a lista tenha pelo menos
    # DOIS elementos para ordernar
    if fim <= ini:
        return        # Sai da função sem fazer nada

    global passadas, comps, trocas

    passadas += 1
    pivot = fim       # o pivô é o último elemento
    div = ini - 1     # o divisor inicia antes do primeiro elemento

    # percorre a lista da posição ini até a posição fim -1
    for i in range(ini, fim):
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1    # incrementa o divisor
            # lista[div] e lista[i] trocam de lugar entre si,
            # caso não sejam o mesmo elemento
            if div != i:
                lista[div], lista[i] = lista[i], lista[div]
                trocas += 1

    # Depois que o percurso de i acaba, div ainda é incrementado
    # mais uma vez
    div += 1

    # Colocamos o pivô em seu definitivo. A troca acontece
    # se o valor do pivô for menor que o valor da posição div
    comps += 1
    if lista[pivot] < lista[div] and pivot:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # chamamos recursivamente a funçao para o sublista á direita
    # da posicão div
    quik_sort(lista, ini,div - 1)

    # chamamos recursivamente a função para a direita 
    # da posição
    quik_sort(lista, div + 1, fim)

###################################################

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

print(nums)
print(f'Passadas: {passadas}, Comparações: {comps}, trocas: {trocas}')

################################################

from data.nomes_desord import nomes
from time import time

