class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
    
    def setPropiedadPrivada (self, valor):
        self.__propiedad_privada = valor
    
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    
    
    
if __name__== '__main__':
    c = ClaseConGetterySetter()