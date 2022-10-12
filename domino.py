#Trabalho GB - Somando Dominós
#Alunos: Carlos Souza e Gabriel Alves
#Professora: Andriele Busatto do Carmo

#Lógica: ver a diferença entre os valores dos dominós e somar de forma que o resultado seja 0
#Após pegar os resultados que deram certo, verificar qual dá a maior soma

import itertools


def main():
    print("Somando Dominós")

    #Entrada por arquivo
    #TODO resolver caminho do arquivo
    arquivo = open("3 Semestre\Análise e Projeto de Algoritmos\Trab GB\entrada.txt", "r")
    n = int(arquivo.readline())
    dominos = []
    for j in range(n):
        dominos.append([int(x) for x in arquivo.readline().split()])
    arquivo.close()
    print("Dominós",dominos)

    somas = []
    for j in range(n):
        somas.append(dominos[j][0] - dominos[j][1])
    print("Somas",somas)

    
    possibleCombinations = []
    print("")
    # Conseguindo todas as combinações de tamanho n ou n-1
    for L in range(len(somas)-1,len(somas) +1,):
        for subset in itertools.combinations(somas, L):
            #Combinações válidas
            possibleCombinations.append(subset)
        # TODO fazer uma versão própria disso para poder pegar o índice do elemento removido
        # TODO verificar qual dá a maior soma
        # TODO pegar o index e fazer a logica de inversão dos dominos
                
    for i in range(len(possibleCombinations)):
        for j in range(len(possibleCombinations[i])):
            for subset in itertools.combinations(possibleCombinations[i], j+1):
                    somaSubset = sum(abs(num) for num in subset)
                    complemento = set.difference(set(possibleCombinations[i]),set(subset))
                    somaComplemento = sum(abs(num) for num in complemento)
                    if(somaSubset == somaComplemento):
                        print("Combinação:\n",possibleCombinations[i])
                        print("Soma do subset:",somaSubset,"é igual a soma do complemento:",somaComplemento)
                        print("Dominos:",subset,"e",complemento)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
            # Quebra o loop externo se achar uma solução para evitar repetição
            else:
                continue
            break
        


main()