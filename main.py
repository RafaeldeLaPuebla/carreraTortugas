import turtle

class Circuito(): #Voy a crear el circuito.
    corredores = []
    __posStartY = (-30, -10, 10, 30) #Ponemos posición de inicio de las tortugas
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        
        self.__screen = turtle.Screen() #Lo hacemos privado,  para que nadie pueda cambiar la anchura y altura de la pantalla.
        self.__screen.setup(width, height) #Lo hacemos privado, para que nadie pueda cambiar la anchura y altura de la pantalla.
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
     
        self.__createRunners()

    def __createRunners(self): #Voy a crear los corredores
        for i in range(4): #Me creo los 4 corredores y los tengo que distinguir.
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() #Método que levanta el boli (mirado en la documentación de Turtle)
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)




if __name__== '__main__':
    circuito = Circuito(640, 480)
    
        
        