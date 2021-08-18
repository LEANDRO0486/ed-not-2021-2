# ALGORITIMO DE ORIENTAÇÃO BUBBLE SORT

# Percorre a lista a ser oordenada em sicessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menornque o primeiro. Efetua tantas passadas quanto necessárias
# até que, na ultima passada, nenhuma troca seja efetuada.

def bubble_sort(lista):
    """
       Função que implementa on algoritimode orientação Bubble Sort
    """
    while True:       # loop eterno
        trocou = False
        # loop na lista até o PENÚLTIMO elemento: len(lista) -2
        # Ex: em uma lista de 10 elementos, len(lista) == 10
        # A útima posição estará em len(lista) - 1, ou seja 9
        # A penúltima posição estará em len(lista) -2, ou seja 8
        for i in range(len(lista) - 2):    # inicia nova passada
            if lista[i + 1] < lista[i]:    # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1]  #faz a troca
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou:    # trocou == false
            break         # interrompe o while