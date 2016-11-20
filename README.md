# simulador-memoria
Simulador para gerência de memória

A tarefa neste EP e implementar um simulador de gerencia de memoria com diversos algoritmos para 
gerencia do espaco livre e para substituicao de paginas. 
O simulador de gerencia de memoria deve receber como entrada um arquivo de trace, em texto puro,
que possui como primeira linha:
total virtual s p
seguida de varias linhas com o seguinte formato: 
t0 nome tf b p1 t1 p2 t2 p3 t3 [pn tn]
total e o total de memoria fısica que deve ser simulada, virtual e o total de memoria virtual 
que deve ser simulada e s e o tamanho da unidade de alocacao a ser considerada para a execucao dos
algoritmos para gerencia do espaco livre. p e o tamanho da pagina a ser considerada para a execucao dos
algoritmos de substituicao de pagina.t0 e o instante de tempo em segundos que um processo chega no 
sistema, nome e uma string sem espacos em branco que identifica o processo,tf e o instante de tempo 
no qual o processo e finalizado,b e a quantidade de memoria utilizada pelo processo. 
Os valores p1, t1, ... pn, tn dizem respeito as posic ` oes de memoria, no espaco de endereco “local” 
do processo, acessadas pelo processo. p1, t1 por exemplo informa que no instante de tempo t1, a
posicao˜ p1 e acessada pelo processo. 
Todos os valores no arquivo de entrada sao numeros inteiros. 
O simulador deve finalizar sua execucao assim que todos os processos do arquivo de entrada forem
finalizados.
Com relacao aos algoritmos para gerencia do espaco livre, neste EP o simulador deve implementar
os seguintes algoritmos, considerando que o controle de qual espaco esta livre e qual esta ocupadoe feito 
usando bitmap:
1. First Fit
2. Next Fit
3. Best Fit
4. Worst Fit
1
Com relacao aos algoritmos de substituicao de pagina, neste EP o simulador deve implementar os 
seguintes algoritmos:
1. Optimal (nesse caso o arquivo de entrada deve ser lido antes para gerar os rotulos das paginas) 
2. Second-Chance
3. Clock
4. Least Recently Used (Quarta versao)
2 Interacao com o simulador
Quando executado na linha de comando (sem parametros) o simulador deve fornecer o prompt: ˆ
(ep3):
Neste prompt os seguintes comandos precisam ser implementados:
• carrega <arquivo>: carrega o arquivo de nome <arquivo> para a simulacao. Pode ser
tanto o caminho relativo como absoluto do arquivo;
• espaco <num>: informa ao simulador que ele sera executado com o algoritmo de gerencia- 
mento de espaco livre de numero<num>, de acordo com a numeracao dos algoritmos apresentada
anteriormente neste documento;
• substitui <num>: informa ao simulador que ele sera executado com o algoritmo de substituicao˜
de paginas de numero<num>, de acordo com a numeracao dos algoritmos apresentada anterior-
mente neste documento;
• executa <intervalo>: executa o simulador e imprime o estado das memorias na tela de 
<intervalo> em <intervalo> segundos, juntamente com o conteudo do bitmap que mantem
o status da memoria; 
• sai: finaliza o simulador e volta para o shell do sistema operacional.
A memoria deve ser simulada utilizando o arquivo/tmp/ep3.mem para a memoria fısica e o arquivo
/tmp/ep3.vir para a memoria virtual. Estes arquivos devem ser criados toda vez que osimulador
for inicializado e devem ter inicialmente um tamanho igual aos valores total e virtual
definido no arquivo de entrada do simulador. Estes arquivos devem ser arquivos binariose devem conter
inicialmente diversos valores -1 informando que toda a memoria esta livre para ser usada.A medida `
que a memoria for sendo utilizada pelos processos simulados, as posicoes utilizadas por esses processos
devem ser marcadas com numeros inteiros que identifiquem unicamente cada processo.Toda vez que um
processo for carregado na memoria ele deve escrever o numerounico que identifica ele (seria o equiva- 
lente ao PID no Linux) nas posicoes corretas dos arquivos. Toda vez que uma posicao de memoria for 
acessada, o PID tambem deve ser escrito nas posicoes corretas dos arquivos.
Em todos os momentos da simulacao sempre havera espaco na memoria virtual suficiente para a soma 
dos tamanhos de todos os processos em execucao nesses momentos.
