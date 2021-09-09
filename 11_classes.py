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
    base = 0
    altuta = 0
    tipo = "R"    # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÈTODOS

    # Este métodos é execultado quando um objeto é criado a partir
    # de uma classe (Construtor)

    def __init__(self, base = 0, altura = 0, tipo = "R"):
        # Recebe os valores passados do construtor e os armazena
        # dentro dos atributos
        if base <= 0:
            raise Exception("A base deve ser maior que zero.")
        elif altura <= 0:
            raise Exception("A altura deve ser maior que zero.")
        elif tipo not in ["R", "T", ou , "E"]
            raise Exception("O tipo deve ser R, T, ou T")

        self.base = base
        self.altura = altura
        self.tipo = tipo

###########################################################

# criando objetos a partir da classe

retangulo1 = FormaGeometrica(15, 10, "R") # Chama o __init__
triangulo1 = FormaGeometrica(6, 9, "T")

print(f"[retangulo1] base: {retangulo1.base}, altutra: {retangulo1.altura}, tipo: {retangulo1.tipo}")

print(f"[triangulo1] base: {triangulo1.base}, altutra: {triangulo1.altura}, tipo: {triangulo1.tipo}")