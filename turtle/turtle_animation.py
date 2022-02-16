import turtle
import random




col_list = ('red','blue','purple','#003153','#98FB98','#77DDE7','green','#6A5ACD','#FF033E','#480607','#BD33A4','#DF73FF','#240935',
            '#62639B','#755D9A','#C9A0DC','#C154C1','#531A50','#240935','#0E294B','#FF47CA','#6D3F5B','#53377A','#8673A1'
)
screen = turtle.Screen()
screen.bgcolor('black') 
turtle.speed(-1) 

def aa():
    for i in range(200):
        turtle.forward(i*4)
        turtle.right(91)
        turtle.color(random.choice(col_list))
        for a in range(3):
            turtle.forward(i*4)
            turtle.right(91)
            turtle.color(random.choice(col_list))
            for b in range(2):
                turtle.forward(i*4)
                turtle.right(91)
            
                
            
for i in range(999):
    aa()



 


            
    