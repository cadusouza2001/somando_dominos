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
    possibleCombinations = []

    # Conseguindo todas as combinações de tamanho n ou n-1, que são as combinações onde até 1 dominó foi retirado
    for L in range(len(somas)-1,len(somas) +1,):
        for subset in itertools.combinations(somas, L):
        #Combinações válidas
            #TODO checar se a soma é par, se não for não tem como dividir em duas partes iguais
            absolute_values = [abs(x[0]) for x in subset]
            if(sum(absolute_values) % 2 == 0 and pseudo_polynomial_partition_problem(absolute_values)):
                possibleCombinations.append(subset)
    #             print("Set possivel: ",subset)
    #             print("Tamanho do set: ",len(subset))
    # print("Combinações possíveis: ",len(possibleCombinations))

    maiorSoma = 0
    dominoDescartado = []
    achouSolucao = False

    #Itera por todas as combinações possíveis
    for combination in possibleCombinations:
        #Itera por todos os tamanhos de combinações possíveis
        
        somaCombinacao = sum([abs(x[0]) for x in combination])//2
        
        for j in range(len(combination)):
            # Separa novamente as combinações em subsets de tamanhos diferentes
            for subset in itertools.combinations(combination, j+1):
                # TODO iterar só metade dos subsets em função própria pois o outro é o complementar
                    soma = 0
                    for num in subset:
                        soma += abs(num[0])
                        if(soma > somaCombinacao):
                            continue
                    #Pega o complemento do subset para verificar se a soma dos valores do complemento é igual a soma dos valores do subset               
                    if(soma==somaCombinacao):
                        complemento = [x for x in combination if x not in subset]
                        achouSolucao = True
                        solucao = []
                        solucaoIndices = []
                        # É arbitrado que os valores dos dominós no subset são positivos, então caso o valor da soma seja negativo, inverte-se o valor dos dominós para a parte de cima ser maior que a de baixo
                        for item in subset:
                            solucaoIndices.append(item[1])
                            if(item[0]>=0):
                                solucao.append(dominos[item[1]])
                            else:
                                solucao.append(dominos[item[1]][::-1])
                        # É arbitrado que os valores dos dominós no complemento do subset são negativos, então caso o valor da soma seja positivo, inverte-se o valor dos dominós para a parte de cima ser menor que a de baixo
                        # Com isso, os valores dos dominós no subset e no complemento são opostos e a soma dos valores dos dominós é 0
                        for item in complemento:
                            solucaoIndices.append(item[1])
                            if(item[0]>=0):
                                solucao.append(dominos[item[1]][::-1])
                            else:
                                solucao.append(dominos[item[1]])

                        solucaoSoma = sum(x[0] for x in solucao)
                        
                        if(solucaoSoma > maiorSoma):
                            maiorSoma = solucaoSoma
                            somasIndices = [x[1] for x in somas]
                            dominoDescartado = [x for x in somasIndices if x not in solucaoIndices]                   
                        break
            # Quebra o loop externo se achar uma solução. É utilizado para evitar repetição na mesma combinação quando o subset iterado for o complemento de um subset já encontrado
            else:
                continue
            break
    
    resultado = ""
    if(achouSolucao):
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
    soma = sum(set)//2
    matrix=[[True]]
    for number in set:
        matrix.append([True])
    for i in range(0,soma):
        matrix[0].append(False)

    for i in range(1,len(set)+1):
        for j in range(1,soma+1):
            if j<set[i-1]:
                matrix[i].append(matrix[i-1][j])
            else:
                matrix[i].append(matrix[i-1][j-set[i-1]] or matrix[i-1][j])
    # for linha in matrix:
    #     print(linha)
    return matrix[len(set)][soma]        

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
        n = int(arquivo.readline())
    arquivo.close()

if __name__ == "__main__":
    main()