"""
   ALGORITIMOS DE EXPRESSÕES MATEMÁTICAS 
"""
from lib.stack import stack

simbolos = {
    "P": "parêntese",
    "C": "colchete",
    "X": "chave"
}

#expressao = "2 * 4 -{7 / [5 - (7 * 9) + 1] * 3} / 5"
expressao = "2 * 4 -{7 / [5 - (7 * 9) + 1] * 3] / 5"

analisador = stack()   # cria pilha 

def verif_fechamento(tipo_fecha, pos_fecha,dados_abre):
    # Se o tipo que veio da pilha for igual ao tipo encontrado
    # no fechamento
    print(f"DEBUG -> tipo_fecha: {tipo_fecha}, pos_fecha: {pos_fecha}, daods_abre: {dados_abre}")
    
    # Apilha ficou vazia antes d termino da análise da expressão
    if dados_abre["tipo"] == tipo_fecha:
        print(f"simbolo tipo {tipo_fecha} aberto na posição {dados_abre['pos']} e fechado na posição {pos_fecha}")
    else: # tipos errados
        print(f"ERRO: simbolo de fechamento do tipo {tipo_fecha} encontrado na posição {pos_fecha}; esperando simbolo do tipo {dados_abre['tipo']}")

# Percorre a expressão em busca de parêntese, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parênteses
         analisador.push({"tipo": "P", "pos": pos})
    elif expressao[pos] == "[":
        # Empilha informaões sobre o abre colchetes
        analisador.push({"tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        # Empilha informaões sobre o abre chaves
        analisador.push({"tipo": "X", "pos": pos})
        # verifica fechamentos
    elif expressao[pos] == ")":
        verif.verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif.verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif.verif_fechamento("X", pos, analisador.pop())

    # verificando se houve sobra(s) na pilha
    while not analisador.is_empty():
        sobra = analisador.pop()
        print(f"ERRO: ")
