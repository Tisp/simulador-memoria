from .memory_file import MemoryFile
from queue import Queue
#classe memoria fisica em arquivo
class VirtualMemoryFile(MemoryFile):
    
    _path = '/tmp/ep3.vir'

    def __init__(self, memorySize):
        MemoryFile.__init__(self, self._path, memorySize)

class VirtualMemory():
    _pageTable = []
    _totalMemory = None
    _pageSize = None
    _memoryFile = None
    _alocationUnitSize = None
    _subsPageAlg = None
    _physicalMemory = None
    _pageFault = 0
    _optimalPages = []
    _fifoQueue = Queue()

    def __init__(self, physicalMemory, totalMemory, pageSize, alocationUnitSize, subsPageAlg):
        self._physicalMemory = physicalMemory
        self._totalMemory = totalMemory
        self._pageSize = pageSize #tamanho da pagina
        self._alocationUnitSize = alocationUnitSize #tamanho da unicade de alocacao
        self._subsPageAlg = subsPageAlg #algoritmo de substituicao de pagina
        self._memoryFile = VirtualMemoryFile(totalMemory)

        for p in range(0, int(totalMemory / self._alocationUnitSize)):
            self._pageTable.append({'pid': -1, 'R': 0, 'inMemory': False, 'start': -1, 'end' : -1})

    def log(self):
        print('Memoria virtual:')
        print([p['pid'] for p in self._pageTable])
        self._physicalMemory.log()

    def alloc(self, p, pid, processSize):
        page = self._pageTable[p]
        page['pid'] = pid

        if not page['inMemory']:
            self._pageFault +=  1

        #chama algoritmo de troca de paginas
        self.secondChance(processSize, page)

    def free(self):
        pass

    def optimal(self, pid, process):
        pass

    def _optimalPageRotulation(self, tracefile):
        pass
    
    def secondChance(self, processSize, page):
        
        if self._fifoQueue.empty():
            page['inMemory'] = True
            page['start'], page['end'] = self._physicalMemory.alloc(processSize, page['pid'])
            self._fifoQueue.put(page)
        else:
            pageQueue = self._fifoQueue.get()
            if pageQueue['R'] == 1:
                pageQueue['R'] = 0
                self._fifoQueue.put(pageQueue)
                self.secondChance(pid, processSize, page)
            else:
                self._physicalMemory.free(pageQueue['start'], pageQueue['end'])
                pageQueue['inMemory'] = False
                page['inMemory'] = True
                page['R'] = 1
                page['start'], page['end'] = self._physicalMemory.alloc(processSize, page['pid'])
                self._fifoQueue.put(page) 
        
    def clock(self, pid):
        pass
    
    def LRU(self):
        pass
        
        
