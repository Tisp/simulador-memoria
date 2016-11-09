'''Classe para manipulacao do prompt'''
class Prompt():

    ''' Nome do prompt '''
    __promptName = '(ep3):'

    ''' Path do arquivo de trace '''
    __traceFile = None

    ''' Valor do algoritmo de gerenciamento de espaco '''
    __spaceAlg = None

    ''' Valor do algoritmo de substituicao de paginas  '''
    __substPageAlg = None

    ''' Intervalo do debug '''
    __debugInterval = None
    ''' Comandos permitidos '''
    __allowedCommands = ['carrega', 'espaco', 'substitui', 'executa', 'sai']

    def __init__(self):
        pass

    def run(self):
        pass

    def getArgs(self, command):
        ''' Verifica se o commando é valido '''
        if self.isValidCommand(command):
            
            
    def isValidCommand(self, command):
        return command.rstrip() in self.__allowedCommands
    