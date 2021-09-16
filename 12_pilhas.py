# Palindromo: é um texto que, quando lido de trás para frente,
# mantém o mesmo conteúdo (desprezando acentos e espaçamentos)
#Palindromo = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"
Palindromo = "BATATINHA QUANDO NASCE ESPARAMA PELO CHÃO"


lista = []

# percurso do palindromo em ordem inversa, colocado cada letra na lista
for letra in Palindromo:
    lista.append(letra)  # append() sempre acrescenta par

#lista.insert(10, 'y')
#lista.insert(19, 'g')
#lista.insert(6, 'ç')

print(lista)

inverso = ""

# Remoção de elementos em posição que não são o final
#del lista(11) # Remove a posição 11
del lista[21]
del lista[8]
del lista[25]
# Retirar cada letra da lista, de trás para frente, e coloca no inverso
while len(lista) > 0:
    inverso += lista.pop() # pop() retira sempre o ÙLTIMO elemento

print(inverso)

# PILHA
# A pilha é um tipo abstrato de dados (TDA) que permite a entrada e a saída
# de dados apenas na sua extremidade final. Como consequencia, ela segue a 
# regra LIFO(last in, first out - último a entrar, primeiro a sair), e tem
# acesso ilimitado aos seus elementos. 

