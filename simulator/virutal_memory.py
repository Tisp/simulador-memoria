from .memory_file import MemoryFile
#classe memoria fisica em arquivo
class VirtualMemoryFile(MemoryFile):
    
    _path = '/tmp/ep3.vir'

    def __init__(self, memorySize):
        MemoryFile.__init__(self, self._path, memorySize)

class VirtualMemory():
    
    _memoryList = None
    _totalMemory = None
    _pageSize = None
    _memoryFile = None
    _alocationUnitSize = None
    _subsPageAlg = None
    _page = { 'pid': -1, 'R': 0, 'M': 0, 'inMemory': False }

    def __init__(self, totalMemory, pageSize, alocationUnitSize, subsPageAlg):
        self._totalMemory = totalMemory
        self._pageSize = pageSize #tamanho da pagina
        self._alocationUnitSize = alocationUnitSize #tamanho da unicade de alocacao
        self._subsPageAlg = subsPageAlg #algoritmo de substituicao de pagina
        self._memoryList = [self._page] * int(totalMemory / self._alocationUnitSize)
        self._memoryFile = VirtualMemoryFile(totalMemory)

    
    def log(self):
        print([p['pid'] for p in self._memoryList])
        print(self._memoryFile.readMemory()) 


    def newProcess():
        pass

