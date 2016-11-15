from tracefile import Tracefile
from simulation import Simulation


class Prompt():
    
    _tracefile = None
    _freeSpaceAlg = None
    _pageSubsAlg = None
    _promptName = '(ep3): '
    _validCommands = ['carrega', 'espaco', 'substitui', 'executa', 'sair']
    _algNum = [1, 2 ,3, 4]


    def __init__(self):

        #Prompt fica rodando infinitamente
        while True:
            command = input(self._promptName).split(' ')

            #Comando invalido
            if command[0] not in self._validCommands:
                print('Comando invalido, tente novamente')
                self.promptHelp()
            elif command[0] == 'sair':
                break; #Fim do prompt
            elif command[0] == 'executa':
                if len(command) == 2:
                    self._startSimulation(command[1])
                else:
                    print('Entre com o valor do intervalo')
                    self.promptHelp()
            else:
                self.loadAlgoCommands(command)

    def loadAlgoCommands(self, command):
        comm, arg = command

        #Carrega o tracefile
        if comm == 'carrega':
            try:
                self._tracefile = Tracefile(arg)
            except IOError as err:
                print(err)
                self._tracefile = None
        else:
            if int(arg) not in self._algNum:
                print("Numero para algoritmo invalido, tente %s" % (str(self._algNum)))
            else:
                if comm == 'espaco':
                    self._freeSpaceAlg = arg
                elif comm == 'substitui':
                    self._pageSubsAlg = arg
                
    def _startSimulation(self, interval):

        if self._tracefile is not None and self._freeSpaceAlg is not None and self._pageSubsAlg is not None:
           Simulation(self._tracefile, self._freeSpaceAlg, self._pageSubsAlg, interval)
        else:
            self.promptHelp()
               
    def promptHelp(self):
        print('Help!!!!')
            


Prompt()

    
    



                
    