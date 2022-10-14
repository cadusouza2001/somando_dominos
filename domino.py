#Trabalho GB - Somando Dominós
#Alunos: Carlos Souza e Gabriel Alves
#Professora: Andriele Busatto do Carmo

#Lógica: ver a diferença entre os valores dos dominós e somar de forma que o resultado seja 0
#Após pegar os resultados que deram certo, verificar qual dá a maior soma

import itertools
import os
from time import time



def encontra_soma(dominos):
    # tempo = time()
    somas = []
    # Pega a diferença entre o valor de cima e de baixo de cada dominó para poder comparar
    for j in range(len(dominos)):
        somas.append([dominos[j][0] - dominos[j][1],j])

    melhorSolucao=[]
    maiorSoma=0
    dominoDescartado=[]
    # Conseguindo todas as combinações de tamanho n ou n-1, que são as combinações onde até 1 dominó foi retirado
    for L in range(len(somas)-1,len(somas) +1,):
        for subset in itertools.combinations(somas, L):
        #Combinações válidas
            absolute_values = [abs(x[0]) for x in subset]
            if(sum(absolute_values) % 2 == 0):
                (combinacoes)=pseudo_polynomial_partition_problem(subset)
                if(combinacoes):
                    soma=0
                    solucao=[]
                    solucaoIndices=[]
                    for valor in combinacoes[0]:
                        solucaoIndices.append(valor[1])
                        if(valor[0]>=0):
                            solucao.append(dominos[valor[1]])
                        else:
                            solucao.append(dominos[valor[1]][::-1])
                    for valor in combinacoes[1]:
                        solucaoIndices.append(valor[1])
                        if(valor[0]>=0):
                            solucao.append(dominos[valor[1]][::-1])
                        else:
                            solucao.append(dominos[valor[1]])
                    for valor in solucao:
                        soma+=valor[0]
                    if(soma>maiorSoma):
                        maiorSoma=soma
                        melhorSolucao=solucao
                        dominoDescartado=[x[1] for x in somas if x[1] not in solucaoIndices]
                        

    resultado = ""
    if(melhorSolucao):
        resultado = str(maiorSoma) + " "
        if dominoDescartado:
            dominoEscolhido = dominos[dominoDescartado[0]]
            if dominoEscolhido[0]>dominoEscolhido[1]:
                dominoEscolhido = dominoEscolhido[::-1]
            resultado= resultado + "descartado o dominó " + str(dominoEscolhido[0]) + " " + str(dominoEscolhido[1])
        else:
            resultado = resultado + "nenhum dominó descartado"
    else:
        resultado = "impossível"
    # print("Tempo de execução para este conjunto: ",time()-tempo)
    return(resultado)
    


def pseudo_polynomial_partition_problem(set):
    valoresSet=[abs(x[0]) for x in set]
    soma = sum(valoresSet)//2
    matrix=[[True]]
    for number in valoresSet:
        matrix.append([True])
    for i in range(0,soma):
        matrix[0].append(False)

    for i in range(1,len(valoresSet)+1):
        for somaAtual in range(1,soma+1):
            if somaAtual<valoresSet[i-1]:
                matrix[i].append(matrix[i-1][somaAtual])
            else:
                matrix[i].append(matrix[i-1][somaAtual-valoresSet[i-1]] or matrix[i-1][somaAtual])

    set1, set2 = [], []
    if(matrix[len(valoresSet)][soma]):
        i, somaAtual = len(valoresSet), soma
        while i > 0 and somaAtual >= 0:
            if matrix[i-1][somaAtual]:
                i-=1
                set1.append(set[i])
            elif matrix[i-1][somaAtual-valoresSet[i-1]]:
                i -= 1
                somaAtual -= valoresSet[i]
                set2.append(set[i])
        return set1,set2
    else:
        return False     

def main():
    #Entrada por arquivo chamado "entrada.txt"
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    arquivo = open(os.path.join(__location__,"entrada.txt"), "r")

    n = int(arquivo.readline())
    while(n!=0):
        dominos = []
        for j in range(n):
            dominos.append([int(x) for x in arquivo.readline().split()])
        print(encontra_soma(dominos))
        # encontra_soma(dominos)
        n = int(arquivo.readline())
    arquivo.close()

if __name__ == "__main__":
    main()