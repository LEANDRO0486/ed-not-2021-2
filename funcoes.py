# Importar o valor da constante pi

from math import pi
# Função é um trecho de código que tem um nome e pode 
# receber informações externas para fazer seu trabalho.
# opcionalmente, uma função pode também produzir um valor
# de resultado.
#Uma funçaõ é definida apenas uma vez e pode ser utilizada
# (chamada) varias vezes, evitando repetições de códigos.
# Existem funções já providas pela linguagem, como, por exemplo,
# len(), range() e sort(), e podemos definir também nossas próprias funções.

def imc(peso, altura):
    '''
       Função que calcula o indice de massa corporal(imc)
    '''
#trechos entre aspas tripas são um tipo especial de 
#comentario chamado docstring, e servem para documentar
# o proposito de uma função ou classe.
    return peso / altura ** 2 # peso / (altura)²

# float(): converte o valor informado em um número com casas decimais
# (floating point)

p = float(input('informe o peso da massa: '))
a = float(input('informe o peso da altura: '))

# fazendo uma chamada á função imc()
resultado = imc(p, a)
print(f' o imc calculado é {resultado}.')
    
def area_forma(base, altura, forma = "R"):
    """
       funçao que calcula a area de uma das seguintes
       formas geometricas: retangulo ou elipse
       parametro forma:
       "R" == retangulo
       "T" == triangulo
       "E" == elipse
    """
    area = 0
    if forma == "R":  #Retangulo (parametro opcional com valor padrão)
        area = base * altura
    elif forma == "T": # Triangulo
        area = base * altura / 2
    elif forma == "E":  # Elipse
        area = (base / 2) * (altura / 2) * pi
    return area

    print('---------------------------------------')

    print(f"Retangulo 7.5x11: {area_forma(7.5, 11, 'R')}")
    print(f"Triangulo 8x12: {area_forma(8, 12, 'T')}")
    print(f"Elipse 15x15: {area_forma(15, 15, 'E')}")
    print(f"Retangulo 9.5x9: {area_forma(9.5, 9.5)}")

