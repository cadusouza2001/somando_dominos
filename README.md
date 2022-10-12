# Somando Dominós
Trabalho de Grau B da disciplina de Análise e Projeto de Algoritmos  
Alunos: Carlos Souza e Gabriel Alves  
Professora: Andriele Busatto do Carmo  

# Descrição: 
## 1. Definição do problema
Você foi convidado a criar um desafio matemático usando dominós. Depois de
pensar por algum tempo, você elaborou o seguinte jogo:
O jogo inicia com um jogador recebendo um pequeno conjunto de dominós.
Esses dominós devem ser escolhidos aleatoriamente de um outro conjunto de
peças, esse último grande e variado. Usando o conjunto de dominós recebido, o
jogador deve encontrar uma combinação na qual os dominós colocados lado a lado
na mesa, devem apresentar a mesma soma tanto para a parte de cima quanto para
a parte de baixo dos dominós. Por exemplo, para o conjunto de dominós [2, 1], [6,
3], [3, 1], uma combinação correta seria:  
**1 6 1**  
**2 3 3**    
Se não for possível encontrar uma combinação usando todos os dominós
escolhidos, o jogador pode descartar um deles, mas o valor da soma na
combinação deve ser a maior possível. Além disso, se existir mais de um dominó
que possa ser descartado mantendo a mesma soma (para a parte de baixo e para a
parte de cima), o jogador deve descartar o dominó [a, b] de modo que a ≤ b e a é o
menor valor possível considerando todos os dominós que podem ser descartados.
Você deve escrever um programa que, dado um conjunto de dominós, tenta
encontrar uma combinação que satisfaz as condições do desafio, descartando um
dominó se necessário. Note que um dominó [a, b] também pode ser escrito como
[b, a].
## Entrada
Seu programa deve processar diversos casos de testes. A primeira linha de um caso
de teste contém um único inteiro N, a quantidade de dominós no teste (0 ≤ N ≤ 400).
Cada uma das N linhas seguintes contém dois inteiros Xi e Yi descrevendo um
dominó que foi dado ao jogador (0 ≤ Xi ≤ 1000 e 0 ≤ Yi ≤ 1000). O valor N = 0 indica
o fim da entrada. As informações devem ser lidas de arquivos.
## Saída
Para cada caso de teste, seu programa deve produzir uma linha descrevendo o
resultado. Se não for possível encontrar uma combinação, imprima a palavra
“impossível”. Se for possível encontrar uma combinação, imprima sua soma e a
descrição do dominó descartado (se houver algum). Se você precisou realmente
descartar um dominó, descreva na forma: “descartado o dominó X Y”, onde X ≤ Y;
senão, imprima “nenhum dominó descartado”. Todas as mensagens devem sem
impressas na saída padrão: tela.  
### Exemplo de entrada  
4  
1 4  
2 9  
2 1  
0 4  
2  
8 1  
9 4  
3  
6 3  
1 2  
3 1  
0  
### Exemplo de saída
10 descartado o dominó 1 2  
impossível  
8 nenhum dominó descartado  

