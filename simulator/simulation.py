from .physic_memory import PhysicMemory

class Simulation():

    _physicMemory = None

    def __init__(self, tracefile,  freeSpaceAlg, pageSubsAlg, interval):
        print('Iniciando simulacao')
        
        #Inicia memoria fisica
        self._physicMemory = PhysicMemory(tracefile.maxPhysicMemory,
                                tracefile.alocationSizeUnit,
                                self.num2FreeSpaceAlg(int(freeSpaceAlg)))

    def num2FreeSpaceAlg(self, num):
        alglist = ['firstFit', 'nextFit', 'bestFit', 'worstFit']
        return alglist[num]
