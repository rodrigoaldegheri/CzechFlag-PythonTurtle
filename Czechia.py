from turtle import *
import math

#la bandiera ceca in proporzione fedele disegnata con PythonTurtle

pi = 3.141592653589793232748626433950
bgcolor("black")

def Czechia(l):
    color("#ffffff")
    begin_fill()
    for i in range(2):
        fd(3/2*l)
        rt(90)
        fd(l/2)
        rt(90)
    end_fill()

    setpos(0,-l/2)
    color("#d80c13")
    begin_fill()
    for i in range(2):
        fd(3/2*l)
        rt(90)
        fd(l/2)
        rt(90)
    end_fill()

    color("#08437f")
    begin_fill()
    setpos(0,-l)

    lt(math.atan(2/3)*180/pi) 
    fd(math.sqrt(13)*l/4)
    lt(180-2*(math.atan(2/3)*180/pi))
    fd(math.sqrt(13)*l/4)
    
    end_fill()

Czechia(500)

done()