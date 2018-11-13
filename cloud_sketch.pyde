# while loop
# increase variable
#use draw() for animation
def setup():
    size (640, 480)


def draw_cloud(x,y): 
    
    noStroke()
    if x >= 640:
        x = 0
    background(230, 153, 0)
    x += 5
    fill(250, 250, 250)
    ellipse(x, y/ 5, 50 , 50 )
    ellipse (x + 35, y / 5 , 70 , 50)
    ellipse (x - 35, y / 5 + 15, 65, 50 )
    ellipse (x - 10, y / 5 - 15, 65, 50 )
    ellipse (x, y / 5, 50, 50)
    
    
def draw_ground():
    
    fill(0, 30, 179)
    rect(0, 350, 700 , 250)

def draw():
    
    draw_cloud(0, 200)
    draw_ground()
    
    
    
