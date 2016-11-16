from .memory_file import MemoryFile

#classe memoria fisica em arquivo
class PhysicMemoryFile(MemoryFile):
    
    _path = '/tmp/ep3.mem'

    def __init__(self, memorySize):
        MemoryFile.__init__(self, self._path, memorySize)

#Classe manipula memoria e seus algoritmos
class PhysicMemory():

    _totalMemory = None
    _alocationUnit = None
    _bitMap = []
    _spaceManagerAlg = None #Qual algoritmo ira usar para alocar
    _lastPositionFit = 0 #Guarda a ultima posicao para o nextfit
    _memoryFile = None
    
    #Construtor
    def __init__(self, totalMemory, alocationUnitSize, spaceManager):
        #total de memoria disponivel
        self._totalMemory = totalMemory
        #unidade de alocacao 
        self._alocationUnitSize = alocationUnitSize
        #prepara o bitmap
        self._bitMap = [False for x in range(self._totalMemory)]
        #Cria a memoria em arquivo
        self._memoryFile = PhysicMemoryFile(self._totalMemory)

        try:
            #define o algoritmo padrao da classe
            print('Usando o algoritmo %s' % (spaceManager))
            self._spaceManagerAlg = getattr(self, spaceManager)        
        except AttributeError:
            raise NotImplementedError("Algoritmo %s nao existe" % spaceManager)
    
    '''Algoritmo generico para bestfit e worstfit'''
    def _maxMinFit(self, processSize, id, func=min):
        freeList = []
        fits = [] #guarda as posicoes que melhor se ajustaram
        processSize += processSize % self._alocationUnitSize

        for m in range(0, self._totalMemory):
            if not self._bitMap[m]:
                freeList.append(m)
                if len(freeList) == processSize:
                    fits.append(freeList)
                    freeList = []
            else:
                freeList = []
        
        
        #Pega a menor lista em fits
        freePos = func(fits)
        for x in freePos:
            self._bitMap[x] = True

        #Escreve na memoria fisica
        self._memoryFile.setIdMemoryPosition(id, freePos[0], freePos[-1])    

    '''Algoritmo generico para firstFit e nextFit'''
    def _positionFit(self, processSize, id, start=0):
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
                    #Escreve na memoria fisica
                    self._memoryFile.setIdMemoryPosition(id, freeList[0], freeList[-1]) 
            else:
                freeList = [] #Zera a lista pois nao tem espacoa contiguo livre
            

    #Imprime a memoria 
    def log(self):
        print([ 1 if x else 0 for x in self._bitMap ])
        #print(self._memoryFile.readMemory())

    def newProcess(self, processSize, id):  
        self._spaceManagerAlg(processSize, id)

    def firstFit(self, processSize, id):
        self._positionFit(processSize, id, 0)

    def nextFit(self, processSize, id):
        self._positionFit(processSize, id, self._lastPositionFit)

    def bestFit(self, processSize, id):
        self._maxMinFit(processSize, id, min)

    def worstFit(self, processSize, id):
       self._maxMinFit(processSize, id, max)
