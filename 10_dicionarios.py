# Dicionário é uma estrutura de linguagem python
# capaz de armazenar multiplos valores em uma uníca
# variavel, por meio de pares de chave-valor

pessoa = {
    # "nome" é a chave
    # "fulano de tal" é o valor
    "nome": "fulano de tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}

# Calculando o IMC (índice de massa corporal)
imc = pessoa["peso"] / (pessoa["altura"]** 2)
print(f"O IMC de pessoa {pessoa['nome']} é {imc}.")

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"          # triangolo
}
forma3 = {
    "base": 5,
    "altura": 2.5,
    "tipo": "E"         # elipse
}

forma4 = {

    "base": 10,
    "altura": 5,
    "tipo": "W"      # tipo não reconhecido
}

forma5 ={
    "legume": "batata",
    "fruta": "banana",
    "tipo": "T"
}

def calcular_area(forma):
    if forma["tipo"] == "R":   # Retangulo
        return forma[base] + forma["altura"]
    elif forma["tipo"] == "T":  # Triangulo
        return forma["base"] + forma["altura"] / 2
    elif forma["tipo"] == "E":  # Elipse
        return forma["base"] / 2 * forma["altura"] / 2 * pi 
    else:
        # gera erro
        raise Exception("tipo de forma não reconhecida.")

    print(f"A area de um retangulo de 7.5x12: {calcular_area(forma1)}")
    print(f"A area de um triangulo de 6x2.5: {calcular_area(forma2)}")
    print(f"A area de um elipse de 5x3: {calcular_area(forma3)}")
    print(f"A area de uma desconhecido de 10x5: {calcular_area(forma4)}")
    