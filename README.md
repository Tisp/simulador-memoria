# simulador-memoria
Simulador para gerência de memória

A tarefa neste EP e implementar um simulador de ger ´ encia de mem ˆ oria com diversos algoritmos para ´
gerencia do espac¸o livre e para substituic¸ ˆ ao de p ˜ aginas. ´
O simulador de gerencia de mem ˆ oria deve receber como entrada um arquivo de trace, em texto p ´ uro,
que possui como primeira linha:
total virtual s p
seguida de varias linhas com o seguinte formato: ´
t0 nome tf b p1 t1 p2 t2 p3 t3 [pn tn]
total e o total de mem ´ oria f ´ ´ısica que deve ser simulada, virtual e o total de mem ´ oria virtual ´
que deve ser simulada e s e o tamanho da unidade de alocac¸ ´ ao a ser considerada para a execuc¸ ˜ ao dos ˜
algoritmos para gerencia do espac¸o livre. ˆ p e o tamanho da p ´ agina a ser considerada para a execuc¸ ´ ao dos ˜
algoritmos de substituic¸ao de p ˜ agina. ´ t0 e o instante de tempo em segundos que um processo chega no ´
sistema, nome e uma string sem espac¸os em branco que identifica o processo, ´ tf e o instante de tempo ´
no qual o processo e finalizado, ´ b e a quantidade de mem ´ oria utilizada pelo processo. ´
Os valores p1, t1, ... pn, tn dizem respeito as posic¸ ` oes de mem ˜ oria, no espac¸o de enderec¸o “local” ´
do processo, acessadas pelo processo. p1, t1 por exemplo informa que no instante de tempo t1, a
posic¸ao˜ p1 e acessada pelo processo. ´
Todos os valores no arquivo de entrada sao n ˜ umeros inteiros. ´
O simulador deve finalizar sua execuc¸ao assim que todos os processos do arquivo de entrada forem ˜
finalizados.
Com relac¸ao aos algoritmos para ger ˜ encia do espac¸o livre, neste EP o simulador deve implementa ˆ r
os seguintes algoritmos, considerando que o controle de qual espac¸o esta livre e qual est ´ a ocupado ´ e feito ´
usando bitmap:
1. First Fit
2. Next Fit
3. Best Fit
4. Worst Fit
1
Com relac¸ao aos algoritmos de substituic¸ ˜ ao de p ˜ agina, neste EP o simulador deve implementar os ´
seguintes algoritmos:
1. Optimal (nesse caso o arquivo de entrada deve ser lido antes para gerar os rotulos das p ´ aginas) ´
2. Second-Chance
3. Clock
4. Least Recently Used (Quarta versao) ˜
2 Interac¸ao com o simulador ˜
Quando executado na linha de comando (sem parametros) o simulador deve fornecer o prompt: ˆ
(ep3):
Neste prompt os seguintes comandos precisam ser implementados:
• carrega <arquivo>: carrega o arquivo de nome <arquivo> para a simulac¸ao. Pode ser ˜
tanto o caminho relativo como absoluto do arquivo;
• espaco <num>: informa ao simulador que ele sera executado com o algoritmo de gerencia- ´
mento de espac¸o livre de numero ´ <num>, de acordo com a numerac¸ao dos algoritmos apresentada ˜
anteriormente neste documento;
• substitui <num>: informa ao simulador que ele sera executado com o algoritmo de substituic¸ ´ ao˜
de paginas de n ´ umero ´ <num>, de acordo com a numerac¸ao dos algoritmos apresentada anterior- ˜
mente neste documento;
• executa <intervalo>: executa o simulador e imprime o estado das memorias na tela de ´
<intervalo> em <intervalo> segundos, juntamente com o conteudo do bitmap que mant ´ em´
o status da memoria; ´
• sai: finaliza o simulador e volta para o shell do sistema operacional.
A memoria deve ser simulada utilizando o arquivo ´ /tmp/ep3.mem para a memoria f ´ ´ısica e o arquivo
/tmp/ep3.vir para a memoria virtual. Estes arquivos devem ser criados toda vez que o ´ simulador
for inicializado e devem ter inicialmente um tamanho igual aos valores total e virtual
definido no arquivo de entrada do simulador. Estes arquivos devem ser arquivos binarios ´ e devem conter
inicialmente diversos valores -1 informando que toda a memoria est ´ a livre para ser usada. ´ A medida `
que a memoria for sendo utilizada pelos processos simulados, as posi ´ c¸oes utilizadas por esses processos ˜
devem ser marcadas com numeros inteiros que identifiquem unicamente cada processo. ´ Toda vez que um
processo for carregado na memoria ele deve escrever o n ´ umero ´ unico que identifica ele (seria o equiva- ´
lente ao PID no Linux) nas posic¸oes corretas dos arquivos. Toda vez que uma posic¸ ˜ ao de mem ˜ oria for ´
acessada, o PID tambem deve ser escrito nas posic¸ ´ oes corretas dos arquivos. ˜
Em todos os momentos da simulac¸ao sempre haver ˜ a espac¸o na mem ´ oria virtual suficiente para a soma ´
dos tamanhos de todos os processos em execuc¸ao nesses momentos.
