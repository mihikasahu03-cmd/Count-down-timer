import pgzrun

bg = "red"

WIDTH = 400
HEIGHT = 400

alien = Actor("alien")

def draw():
    screen.fill(bg)
    alien.draw()

pgzrun.go()
    
