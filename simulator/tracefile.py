import os
from .util import listPairs

class Tracefile():
        
    maxPhysicMemory = None
    maxVirtualMemory = None
    alocationSizeUnit = None
    pageSize = None
    processes = [] 

    def __init__(self, tracefile):
        if not os.path.exists(tracefile):
            raise IOError('Arquivo %s nao encontrado' % tracefile)

        with open(tracefile) as trace:
            #le as linhas do tracefile
            tracelines = trace.readlines()

            #pega os dados da primeira linha
            self._getFirstLine(tracelines)

            #Pega os dados dos processos
            self._getProcessData(tracelines)


    #pega os dados da primeira linha        
    def _getFirstLine(self, tracelines):
        firstLineData = tracelines[0].rstrip().split(' ')
        
        if len(firstLineData) != 4:
            raise IOError('Arquivo trace errado, veja a linha 0')
        
        #Captura os primeiros dados do arquivo trace
        self.maxPhysicMemory, self.maxVirtualMemory, \
        self.alocationSizeUnit, self.pageSize = map(int, firstLineData)
    
    #pega os dados da 2 linha em diante, dados dos processos
    def _getProcessData(self, tracelines):
        for t in tracelines[1:]:
                process_data = t.rstrip().split(' ')
                process = {'t0' : None,
                           'nome': None,
                           'tf': None,
                           'b': None,
                           'memory': [] }

                process['t0'], process['nome'], \
                process['tf'], process['b'] = process_data[0:4]

                process['memory'] = listPairs(process_data[4:])

                #Verifico se os dados estao corretos
                if process['memory'] is None:
                     raise IOError('Arquivo trace errado, veja a linha %d' % (tracelines.index(t)))

                self.processes.append(process)
            
        
