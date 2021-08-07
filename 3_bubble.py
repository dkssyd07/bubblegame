# making arraow and pointer 


import pygame
import os

# making bubble class 
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image , color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)

#making map
def setup():
    global map
    map = [
        #["R","R","Y","Y","B","B","G","G",]
        list("RRYYBBGG"),
        list("RRYYBBG/"),
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
    ]

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".","/"]:
                continue 
            pos = get_bubble_position(row_idx,col_idx)
            image = get_bubble_image(col)
            bubble = Bubble(image,col, pos)
            bubble_group.add(Bubble(image,col,pos))
            

def get_bubble_position(row_idx,col_idx):
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1:
        pos_x += CELL_SIZE // 2
    return pos_x, pos_y
def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "P":
        return bubble_images[4]
    else:
        return bubble_images[5]#[-1]

    



pygame.init()
screen_width= 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Puzzle Bobble')
clock = pygame.time.Clock()

#upload background image 
current_path = os.path.dirname(__file__) 
back = pygame.image.load(os.path.join(current_path, "background.png"))

#upload bubble image 
bubble_images = [
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "Purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha(),
]




#game variables 
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
map = []#map
bubble_group = pygame.sprite.Group()
setup()


running = True
while running:
    clock.tick(60)# FPS 60

    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False
            
    screen.blit(back,(0,0))
    bubble_group.draw(screen)    
    pygame.display.update()

pygame.quit()