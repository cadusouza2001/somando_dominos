#Trabalho GB - Somando Dominós
#Alunos: Carlos Souza e Gabriel Alves
#Professora: Andriele Busatto do Carmo

#Lógica: ver a diferença entre os valores dos dominós e somar de forma que o resultado seja 0
#Após pegar os resultados que deram certo, verificar qual dá a maior soma

import itertools

def main():
    #Entrada por arquivo
    #TODO resolver caminho do arquivo
    #TODO ler mais do que uma entrada por vez
    arquivo = open("3 Semestre\Análise e Projeto de Algoritmos\Trab GB\entrada.txt", "r")
    n = int(arquivo.readline())
    dominos = []
    for j in range(n):
        dominos.append([int(x) for x in arquivo.readline().split()])
    arquivo.close()
    
    somas = []
    for j in range(n):
        somas.append([dominos[j][0] - dominos[j][1],j])
    possibleCombinations = []

    # Conseguindo todas as combinações de tamanho n ou n-1
    for L in range(len(somas)-1,len(somas) +1,):
        for subset in itertools.combinations(somas, L):
        #Combinações válidas
            possibleCombinations.append(subset) 

    maiorSoma = 0
    dominoDescartado = []
    achouSolucao = False

    #Itera por todas as combinações possíveis
    for i in range(len(possibleCombinations)):
        #Itera por todos os elementos da combinação i para pegar os valores de tamanho diferente
        for j in range(len(possibleCombinations[i])):
            # Separa novamente as combinações em subsets para verificar se a soma deles é igual a do complemento
            for subset in itertools.combinations(possibleCombinations[i], j+1):
                    complemento = [x for x in possibleCombinations[i] if x not in subset]
                    soma = sum(abs(num[0]) for num in subset)
                    somaComplemento = sum(abs(num[0]) for num in complemento)

                    if(soma == somaComplemento):
                        achouSolucao = True
                        solucao = []
                        solucaoIndices = []
                        for item in subset:
                            solucaoIndices.append(item[1])
                            if(item[0]>=0):
                                solucao.append(dominos[item[1]])
                            else:
                                solucao.append(dominos[item[1]][::-1])
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
            # Quebra o loop externo se achar uma solução para evitar repetição na mesma combinação
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