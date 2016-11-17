from array import array
#Classe para escrever a memoria em arquivo
class MemoryFile():

    _path = None
    _file = None
    _memorySize = None
    _EMPTY_VALUE_ = -1 #Define um valor para vazio

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
        '''Utilizando tamanhos de 4 bytes, entao arquivo ficara com 4 * maxMemory 
        https://docs.python.org/3/library/array.html '''
        self._file.write(array('i', memoryList).tobytes())

    def readMemory(self):
        #Retorna a posicao inicial do arquivo
        self._file.seek(0)
        mem = []
        b = self._file.read(1)
        while b: 
            mem.append(int.from_bytes(b, byteorder='big', signed=True))
            #tamnho dos valores e de 4 bytes, continuar lendo ate 4
            i = 0
            while i != 4:
                b = self._file.read(1)
                i+=1
        return mem


