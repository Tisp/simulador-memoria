from time import time
from .physical_memory import PhysicalMemory
from .virutal_memory import VirtualMemory

class Simulation():

    _physicalMemory = None
    _virtualMemory = None
    _startTime = None
    _tracefile = None
    _interval = 0

    def __init__(self, tracefile,  freeSpaceAlg, pageSubsAlg, interval):
        
        self._tracefile = tracefile

        self._interval = interval

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
        startTime = time()
        runTime = 0
        logStartTime = time()
        processes = self._tracefile.processes
        lastProcessTimeEnd = processes[-1]['tf']
        
        while runTime < lastProcessTimeEnd:
            runTime = int(time() - startTime)
            for  pid, process in enumerate(processes):
                #Verifica se precisa por na memoria ou se ja terminou
                if runTime <= process['t0'] and len(process['memory']) > 0:
                    p, t = process['memory'][0]
                    if t <= runTime:
                        self._virtualMemory.alloc(p, pid, process['b'])
                        process['memory'].remove((p, t))
            #LOG
            if int(time() - logStartTime) >= int(self._interval):
                self._virtualMemory.log()
                logStartTime = time()

        print(self._virtualMemory._pageFault)

    def num2FreeSpaceAlg(self, num):
        alglist = [None, 'firstFit', 'nextFit', 'bestFit', 'worstFit']
        return alglist[num]

    def num2SubsPageAlg(self, num):
        alglist = [None, 'optimal', 'secondChance', 'clock', 'leastRecentlyUsed']
        return alglist[num]

