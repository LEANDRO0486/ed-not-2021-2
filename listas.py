# criando uma lista
primos = [2, 3, 5, 7, 11, 15, 17, 19, 25, 29]

#percurso
for num in primos:
    print(num)

# acresentar um novo elemento no fim da lista: append()
primos.append(31)
print(primos)

# inserindo um elemento em uma posição especifica: insert()
#1º informa a posição de inserção
#2º elemento a ser inserido
primos.insert(0, 1)
print(primos)

# insere o valor 37 na posição 5
primos.insert(5, 37)
print(primos)

# retirando o ultimo elemento da lista: pop()
ultimo = primos.pop()
print(f'ultimo: {ultimo}')
print(primos)

# removendo por valor: remove()
primos.remove(37)
print(primos)

# Removendo por posição: del()
# removendo o elemento da posição 4
del primos[4]
print(primos)

# fatiando uma lista
# exibindo apenas do elemento da posição o (inclusive)a posição 7 (exclusive)
print(primos[0:7])

# da posição 2 á posição 8
print(primos[2:8])

# fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)


