# ALGORITIMO DE ORDERNAÇÃO MERGE SORT
# 
# No processo de ordenação, esse algoritimo "desmonta" o vetor original
# contendo N elementos até obter N vetores de apenas um elemento cada um
# Em seguida, usando a técnica de mesclagem (merge), "remonta" o valor,
# dessa vez com os elementos já em ordem.

def merge_sort(lista):
    """
       Função que implementa o algoritimo merge sort usando o
       método RECURSIVO
    """
    print(f'Lista recebida: {lista}')

    # Só continua se a lista tiver mais de um elemento
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    # Gera cópia de primeira metade da lista
    lista_esq = lista[:meio] # Do inicio ao meio -1
    # Dera cópia da segunda metade da lista
    lista_dir = lista[meio:] #do meio ao fim

    # chamamos recuesivamente a função para continuar
    # repartindo a lista em metades
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    print(f'>>> lista_esq: {lista_esq}')
    print(f'>>> lista_dir: {lista_dir}')

    # Junta as duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = []   # lista vazia

    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        # O elemento que se encontra na lista da direita
        # é menor que o elemento se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        # o contrario
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1

    sobra = None     # A sobra da lista que ficou para trás

    if pos_esq < pos_dir:   # Houve sobra á esquerda
        sobra = lista_esq[pos_esq:]    # Sobra da pos_esq até o final
    else:      # Se houve sobra a direita
        sobra = lista_dir[pos_dir:]   # Sobra do pos_dir até o final
    
    # Retornamos a lista final ordenada, composta da ordenada + sobra
    return ordenada + sobra   # "soma" de duas listas


###################################################################

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

nums_ord = merge_sort(nums)

print(nums_ord)