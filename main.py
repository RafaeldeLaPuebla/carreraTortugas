import turtle
import random #Importamos el módulo random para lanzar el dado que nos diga cuánto va a avanzar cada tortuga.

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
    
    def competir(self):
        
        hayGanador = False #Cuando empiezo no hay ganador. Esto no es un atributo. No se puede invocar. Sólo tiene existencia cuando competir está activo.
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
            
                if tortuga.position()[0] >= self.__finishLine: #Cojo la posición 0 de la tupla que es la coordenada x de la tortuga. En el momento en que toca con el pecho la cinta, es el ganador y se puede pasar.
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0])) #Es un Getter. Lleva paréntesis porque es una función. Si quieres que se ejecute, tienes que poner paréntesis.
                    break #Para parar el bucle y que sólo haya un ganador.

if __name__== '__main__':
    circuito = Circuito(640, 480)
    circuito.competir() #Invoco la competición.
    
        
        