import pgzrun
import random 

bg = "red"

WIDTH = 400
HEIGHT = 400

message = "mihika"

alien = Actor("alien")

def draw():
    screen.fill(bg)
    alien.draw()
    screen.draw.text(message, (WIDTH-100,0))

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        move()
        message = "Good shot"    
    else:
        message = "Miss"
        

def move():
    alien.x = random.randint(5,350)
    alien.y = random.randint(5,350)

        

pgzrun.go()
    
