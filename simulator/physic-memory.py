class PhysicMemory():

    _totalMemory = None
    _alocationUnit = None
    _bitMap = []
    _lastPositionFit = 0 #Guarda a ultima posicao para o nextfit

    def __init__(self, totalMemory, alocationUnitSize):
        #total de memoria disponivel
        self._totalMemory = totalMemory
        #unidade de alocacao 
        self._alocationUnitSize = alocationUnitSize
        #prepara o bitmap
        self._bitMap = [False for x in range(self._totalMemory)]
    
    #Imprime a memoria 
    def log(self):
        print([ 1 if x else 0 for x in self._bitMap ])

    def firstFit(self, processSize, start=0):
        freeList = []
        #Ja deixa o processo com o tamanho para alocation size2
        processSize += processSize % self._alocationUnitSize
        #Percore o vetor bitmap em tamnhos de unit size
        for m in range(start, self._totalMemory):
            #Espaco livre
            if not self._bitMap[m]:
                freeList.append(m)
                if len(freeList) == processSize:
                    for x in freeList:
                        self._bitMap[x] = True
                    self._lastPositionFit = m % self._totalMemory
            else:
                freeList = [] #Zera a lista pois nao tem espacoa contiguo livre


    def nextFit(self, processSize):
        self.firstFit(processSize, self._lastPositionFit)

    def bestFit(self, processSize):
        pass

    def worstFit(self, processSize):
        pass





pm = PhysicMemory(10, 3)
pm.nextFit(4)
pm.log()
pm.firstFit(1)
pm.log()

