from time import time
from .physic_memory import PhysicMemory
from .virutal_memory import VirtualMemory

class Simulation():

    _physicMemory = None
    _virtualMemory = None
    _startTime = None
    _tracefile = None

    def __init__(self, tracefile,  freeSpaceAlg, pageSubsAlg, interval):
        print('Iniciando simulacao')
        
        self._tracefile = tracefile

        #Inicia memoria fisica
        self._physicMemory = PhysicMemory(tracefile.maxPhysicMemory,
                                tracefile.alocationSizeUnit,
                                self.num2FreeSpaceAlg(int(freeSpaceAlg)))
        #Inicia a memoria virtual 
        self._virtualMemory = VirtualMemory(tracefile.maxVirtualMemory,
                                tracefile.pageSize,
                                tracefile.alocationSizeUnit,
                                self.num2SubsPageAlg(int(pageSubsAlg)))

    def run(self):
        startTime = time()
        print(startTime)

    def num2FreeSpaceAlg(self, num):
        alglist = [None, 'firstFit', 'nextFit', 'bestFit', 'worstFit']
        return alglist[num]

    def num2SubsPageAlg(self, num):
        alglist = [None, 'optimal', 'secondChance', 'clock', 'leastRecentlyUsed']
        return alglist[num]

