from time import time
from .physical_memory import PhysicalMemory
from .virutal_memory import VirtualMemory

class Simulation():

    _physicalMemory = None
    _virtualMemory = None
    _startTime = None
    _tracefile = None

    def __init__(self, tracefile,  freeSpaceAlg, pageSubsAlg, interval):
        print('Iniciando simulacao')
        
        self._tracefile = tracefile

        #Inicia memoria fisica
        self._physicalMemory = PhysicalMemory(tracefile.maxPhysicalMemory,
                                tracefile.alocationSizeUnit,
                                self.num2FreeSpaceAlg(int(freeSpaceAlg)))
        #Inicia a memoria virtual 
        self._virtualMemory = VirtualMemory(
                                self._physicalMemory,
                                tracefile.maxVirtualMemory,
                                tracefile.pageSize,
                                tracefile.alocationSizeUnit,
                                self.num2SubsPageAlg(int(pageSubsAlg)))

    def run(self):
        #posicao, pid, size
        self._virtualMemory.alloc(1, 5, 3)
        self._virtualMemory.log()
        self._virtualMemory.alloc(5, 10, 2)
        self._virtualMemory.log()
        print(self._virtualMemory._pageFault)

    def num2FreeSpaceAlg(self, num):
        alglist = [None, 'firstFit', 'nextFit', 'bestFit', 'worstFit']
        return alglist[num]

    def num2SubsPageAlg(self, num):
        alglist = [None, 'optimal', 'secondChance', 'clock', 'leastRecentlyUsed']
        return alglist[num]

