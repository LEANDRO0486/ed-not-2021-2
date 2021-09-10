# Classe é uma estruturada que representa conjuntamente
# dados e algoritimos. Uma classe é uma como "forma de bolo"
# com a qual podemos criar diferentes "bolos" (objeto).
# Cada "bolo" (objeto) pode ser feito com seus próprios
# ingredientes (dados) e modos de fazer (algoritmo), mas
# terão sempre o formato determinado pela "forma" (classe)

class FormaGeometrica():
    #Dados
    #quando pertencem a uma classe, ganham o nome de 
    # ATRIBUTOS.

    # base
    #base = 0
    #altura = 0
    #tipo = "R"    # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÈTODOS

    # Este métodos é execultado quando um objeto é criado a partir
    # de uma classe (Construtor)


    def __init__(self, base = 0, altura = 0, tipo = "R"):
        # Recebe os valores passados do construtor e os armazena
        # dentro dos atributos

        print(f"base: {base} ({type(base)}), altura: {altura} ({type(altura)}")


        if type(base) not in [int,float] or base <= 0:
            raise Exception("A base deve ser maior que zero.")
        elif type(altura) not in [int,float] or altura <= 0:
            raise Exception("A altura deve ser maior que zero.")
        elif tipo not in ["R","T","E"]:
            raise Exception("O tipo deve ser R, T, ou E")

        # ajustando o valor dos atributos privados
        self.__base = base
        self.__altura = altura
        self.__tipo = tipo

    # Getter é um método que possibilita saber o valor de um atributo
    # privado do lado de fora da classe
    # 
    def __get_base(self):
        return self.__base  
  
    #Setter é um método que possibilita alterar o valor de um atributo
    #privado inclusive do lado de fora da classe
    def __set_base(self, valor):

        if type(valor) not in [int,float] or valor <= 0:
            raise Exception('* A base deve ser numérica e maior que zero')

        self.__base = valor

    # property "esconde" as funções getter e setter dentro do nome de 
    # um atributo, tornando mais simples a manipulação do objeto 
    base = property(__get_base, __set_base)

    # Essas linhas começadas @ são chamadas "decoractors"
    # os decorators instruem o python a criar uma property com
    # um getter e um setter na hora da execulção

    @property
    def altura(self):          # Grtter para propriedade chamada "altura"
        return self.altura

    @altura.setter
    def altura(self, valor):  # Settrer para propriedade chamada "altura"  
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception('* altura deve ser numérica e maior que zero')
        self.__altura = valor         

###########################################################

# criando objetos a partir da classe

retangulo1 = FormaGeometrica(15, 10, "R") # Chama o __init__
triangulo1 = FormaGeometrica(6, 9, "T")

#retangulo1.__base = 5
#retangulo1.set_base(9.6)
retangulo1.base = 8     # vai execultar set_base da clase
#retangulo1.set_base(12.5)

#retangulo1.base = 0
#triangulo1.tipo = "udgftrhhd"


#problematico = FormaGeometrica(8, 8, "E")

print(f"[retangulo1] base: {retangulo1.base}")  # vai execultar o getter

#print(f"[retangulo1] base: {retangulo1.__base}, altutra: {retangulo1.__altura}, tipo: {retangulo1.__tipo}")

#print(f"[triangulo1] base: {triangulo1.__base}, altutra: {triangulo1.__altura}, tipo: {triangulo1.__tipo}")