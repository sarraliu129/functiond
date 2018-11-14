# while loop
# increase variable
#use draw() for animation
cloud_x = 0
cloud_y = 200


def setup():
    size (640, 480)


def draw_cloud(x,y): 
    
    noStroke()
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
    
    global cloud_x
    
    # update cloud
    if cloud_x >= 640:
        cloud_x = 0
    cloud_x += 5
    
    background(230, 153, 0)
    draw_cloud(cloud_x, 200)
    draw_ground()
    
    
    
