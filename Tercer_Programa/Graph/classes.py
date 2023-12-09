import turtle as t

class state:
    
    def __init__(self, x, y, radius, label):
        
        self.x = x
        self.y = y
        self.radius = radius
        self.label = label
    
    def draw(self):
        
        font_size = 16
        style = ('Times New Roman', font_size,'bold')
        move(self.x, self.y - self.radius, 's')
        t.circle(self.radius)  # Draw the circle
        move(self.x, self.y, 's')  # Move to write the text
        t.write(self.label, align='center', font=style)  # Write the label

class transition:
    
    def __init__(self, initial_x, initial_y, final_x, final_y, label_x, label_y, label, angle):
        
        self.xi = initial_x
        self.yi = initial_y
        self.xf = final_x
        self.yf = final_y
        self.xl = label_x
        self.yl = label_y
        self.label = label
        self.angle = angle
        
    def draw(self):
        
        font_size = 16
        style = ('Times New Roman', font_size,'bold')
        move(self.xi, self.yi, 's')
        move(self.xf, self.yf, '')
        t.right(self.angle)
        t.stamp() # Stop and draw a copy of the arrow
        t.left(self.angle)
        move(self.xl, self.yl, 's') # Move to write the text
        t.write(self.label, align='center', font=style)  # Write the labe
        
        
class self_transition:
    
    def __init__(self, x_transition, y_transition, x_label, y_label, label, radius, extent):
        
        self.xt = x_transition
        self.yt = y_transition
        self.xl = x_label
        self.yl = y_label
        self.label = label
        self.radius = radius
        self.extent = extent
        
        
    def draw(self):
        
        font_size = 16
        style = ('Times New Roman', font_size,'bold')
        move(self.xt, self.yt, 's')
        t.circle(self.radius, self.extent)
        t.stamp()
        t.right(-90)
        move(self.xl, self.yl, 's')
        t.write(self.label, align='center', font=style)
        
class special_transition():
    
    def __init__(self, direction_1, points_1, direction_2, points_2, direction_3, points_3, x_label, y_label, label):
        
        self.direction1 = direction_1
        self.points1 = points_1
        self.direction2 = direction_2
        self.points2 = points_2
        self.direction3 = direction_3
        self.points3 = points_3
        self.xl = x_label
        self.yl = y_label
        self.label = label
    
    def draw(self):
        
        font_size = 16
        style = ('Times New Roman', font_size,'bold')
        t.right(self.direction1)
        t.forward(self.points1)
        t.right(self.direction2)
        t.forward(self.points2)
        t.right(self.direction3)
        t.forward(self.points3)
        t.stamp() # Stop and draw a copy of the arrow
        t.setheading(0) # Move the arrow to horizontal right direction
        move(self.xl, self.yl, 's') # Move to write the text
        t.write(self.label, align='center', font=style)  # Write the labe

        
        

def move(x,y,c):
    if(c == 's'):
        t.up()
    t.goto(x,y)
    t.pendown()