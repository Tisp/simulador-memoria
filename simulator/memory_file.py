class MemoryFile():

    _path = None
    _file = None
    _memorySize = None
    _EMPTY_VALUE_ = 255 #Define um valor para vazio

    def __init__(self, path, memorySize):
        self._path = path
        self._file = open(self._path, 'w+b')
        self._memorySize = memorySize

        #Escreve dados iniciais
        self.writeMemory([self._EMPTY_VALUE_] * self._memorySize)

    def __del__(self):
        if self._file:
            self._file.close()

    def setIdMemoryPosition(self, id, init, end):
        memoryList = self.readMemory()
        for i in range(init, end):
            memoryList[i] = id
        self.writeMemory(memoryList)


    def writeMemory(self, memoryList):
        #Retorna a posicao inicial do arquivo
        self._file.seek(0)
        self._file.write(bytes(memoryList))

    def readMemory(self):
        #Retorna a posicao inicial do arquivo
        self._file.seek(0)
        return list(self._file.read())



