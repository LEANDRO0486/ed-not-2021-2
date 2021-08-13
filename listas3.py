# listas de strings
frutas = ['laranja', 'maça', 'uva', 'pera', 'mamão', 'abacate', 'amora']

# imprimindo apenas a fruta 'uva'
print(frutas[2])

#Substituindo 'pera' por 'melão'
frutas[3] = 'melão'
print(frutas)

# descobrindo quantos elementos há na listas de frutas
print(len(frutas))

print('------------------------------------------')

# percorendo e imprimindo cada um dos elementos da lista
for fruta in frutas:
    print(fruta)

print('------------------------------------------')
# percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f'{frutas[i]} está na posição {i}')

print('------------------------------------------')
# percurso em ordem invertida
# 1º agumento: len(frutas) - 1: a lista presisa começar no ultimo elemento, que # é determinado por len() - 1
# 2º argumento: -1 porque o final nao entra e presisamos terminar em 0
# 3º argumento: -1 porque a lista precisa ser descrecente
for j in range(len(frutas) - 1, -1, -1):
    print(frutas[j])

print('------------------------------------------')

# ordenando o vetor em ordem alfabética
frutas.sort()
print(frutas)