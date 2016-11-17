from memory_file import MemoryFile
#classe memoria fisica em arquivo
class VirtualMemoryFile(MemoryFile):
    
    _path = '/tmp/ep3.vir'

    def __init__(self, memorySize):
        MemoryFile.__init__(self, self._path, memorySize)

class VirtualMemory():
    
    _memoryList = None
    _totalMemory = None
    _alocationUnitSize = None
    _memoryFile = None
    _page = { 'pid': -1, 'R': 0, 'M': 0, inMemory: False }

    def __init__(self, totalMemory, alocationUnitSize):
        self._totalMemory = totalMemory
        self._alocationUnitSize = alocationUnitSize
        self._memoryList = [self._page] * totalMemory
        self._memoryFile = VirtualMemoryFile(totalMemory)

    
    def log(self):
        print([p['pid'] for p in self._memoryList])

        

    
