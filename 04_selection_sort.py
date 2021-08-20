# ALGORITIMO DE ORDENAÇÃO SELECTION SORT
#
# Isola (seleciona) o primeiro elemento da lista e, em seguida, 
# encontra o menor valor no restante da lista. Se o valor encontrado 
# for menor que o valor selecionado, efetua a troca.
# Em seguida, isola o segundo número da lista, buscando pelo menor 
# valor das posições subsequentes. Faz a troca entre as os dois valores,
# se necessario. Continua o processo, até isolar o penultimo da lista.

comps = 0
passadas = 0
trocas = 0

def selection_sort(lista):
    """
        Função que implementa o algoritmo de ordenação selection sort

    """
    global comps, passadas, trocas
    comps = 0
    passadas = 0
    trocas = 0   

       # Percurso da lista até a penúltima posição    
    for pos_sel in range(len(lista) - 1):
        pos_menor = pos_sel + 1
       # Seleciona (isola) o elemento que será comparado

       # Rotina para encontrar o menor número no resto da lista       
       # Percurso da lista da posição i + 2 até o fim
       
        for j in range(pos_sel + 2, len(lista)):
       # Se o elemento da posição atual (j) for menor            
       # que o elemento na posição do menor (pos_menor),         
       # atualizamos pos_menor
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        
        # Comparamos lista[sel] com lista[pos_menor] e, se segundo        
        # for menor que o primeiro, efetuamos a troca entre eles
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]

#########################################################################