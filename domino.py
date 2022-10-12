#Trabalho GB - Somando Dominós
#Alunos: Carlos Souza e Gabriel Alves
#Professora: Andriele Busatto do Carmo

#Lógica: ver a diferença entre os valores dos dominós e somar de forma que o resultado seja 0
#Após pegar os resultados que deram certo, verificar qual dá a maior soma

import itertools
import os

def main():
    #Entrada por arquivo chamado "entrada.txt"
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    arquivo = open(os.path.join(__location__,"entrada.txt"), "r")

    n = int(arquivo.readline())
    while(n!=0):
        dominos = []
        for j in range(n):
            dominos.append([int(x) for x in arquivo.readline().split()])
        encontra_soma(dominos)
        n = int(arquivo.readline())
    arquivo.close()

def encontra_soma(dominos):
    somas = []
    # Pega a diferença entre o valor de cima e de baixo de cada dominó para poder comparar
    for j in range(len(dominos)):
        somas.append([dominos[j][0] - dominos[j][1],j])
    possibleCombinations = []

    # Conseguindo todas as combinações de tamanho n ou n-1, que são as combinações onde até 1 dominó foi retirado
    for L in range(len(somas)-1,len(somas) +1,):
        for subset in itertools.combinations(somas, L):
        #Combinações válidas
            possibleCombinations.append(subset) 

    maiorSoma = 0
    dominoDescartado = []
    achouSolucao = False

    #Itera por todas as combinações possíveis
    for i in range(len(possibleCombinations)):
        #Itera por todos os elementos da combinação iterada para pegar subsets de tamanhos diferentes
        for j in range(len(possibleCombinations[i])):
            # Separa novamente as combinações em subsets de tamanhos diferentes
            for subset in itertools.combinations(possibleCombinations[i], j+1):
                    #Pega o complemento do subset para verificar se a soma dos valores do complemento é igual a soma dos valores do subset
                    complemento = [x for x in possibleCombinations[i] if x not in subset]
                    soma = sum(abs(num[0]) for num in subset)
                    somaComplemento = sum(abs(num[0]) for num in complemento)

                    #Se a soma for igual, significa que há uma combinação onde a soma dos valores dos dominós é 0
                    if(soma == somaComplemento):
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

    if(achouSolucao):
        print(maiorSoma,end=" ")
        if dominoDescartado:
            dominoEscolhido = dominos[dominoDescartado[0]]
            if dominoEscolhido[0]>dominoEscolhido[1]:
                dominoEscolhido = dominoEscolhido[::-1]
            print("descartado o dominó",dominoEscolhido[0],dominoEscolhido[1])
        else:
            print("nenhum dominó descartado")
    else:
        print("impossível")    
        


main()