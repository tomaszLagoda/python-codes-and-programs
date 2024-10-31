import pygame, sys, random, time

# General Stuff
pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 250, 250
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tile Movement")

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(10, 160, 100)

# Classes
class Tile:
    tile_size = 50
    objs = []
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x+1, y+1, Tile.tile_size-2, Tile.tile_size-2)
        Tile.objs.append(self)
    
    @classmethod
    def Update(cls, color):
        for obj in cls.objs:
            pygame.draw.rect(screen, color, obj)

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
        self.move_delay = 0.1 * 1000 # How much seconds of delay before the player can move again
        self.last_moved = pygame.time.get_ticks()
    
    def Update(self, color):
        # Stops the player from going outside the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screenWidth:
            self.rect.right = screenWidth
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screenHeight:
            self.rect.bottom = screenHeight
            
        # Draws the instance
        pygame.draw.rect(screen, color, self)
    
    def Input(self):
        if curTicks - self.last_moved > self.move_delay:
            if event.type == pygame.KEYDOWN:
                self.last_moved = curTicks
                # Moves player left and right
                if event.key == pygame.K_DOWN:
                    self.rect.y += Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}") # Debug
                if event.key == pygame.K_UP:
                    self.rect.y -= Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")
                # Moves player up and down
                if event.key == pygame.K_RIGHT:
                    self.rect.x += Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")
                if event.key == pygame.K_LEFT:
                    self.rect.x -= Tile.tile_size
                    print(f"Tile Pos: {int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size)}")

    def CurrentPosition(self):
        return (int(self.rect.x / Tile.tile_size), int(self.rect.y / Tile.tile_size))


# Variables
tile_list = []

player = Player(100, 200, 50, 50)

destination = Player(0, 50, 50, 50)

rows = 5
columns = 5

# Prepares the grid
for row_index in range(columns):
    for col_index in range(rows):
        x = row_index * Tile.tile_size
        y = col_index * Tile.tile_size
        
        tile_list.append(Tile(x, y))

# Game loop
while True:
    # Gets the amount of ingame ticks that have passed
    curTicks = pygame.time.get_ticks()

    # Generate random kayboard event from list
    keys = [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]

    newevent = pygame.event.Event(
        pygame.KEYDOWN, key=random.choice(keys),
        mod=pygame.KMOD_NONE)  #create the event
    pygame.event.post(newevent)  #add the event to the queue

    time.sleep(0.2)

    # Checks for events like quiting and player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [768, 769]:
            if player.CurrentPosition() == destination.CurrentPosition():
                pygame.quit()
                sys.exit()

        # print(event)
        
        player.Input()

    
    # This draws everything        
    screen.fill(white)
    
    Tile.Update(black)
    player.Update(green)

    destination.Update(blue)
    
    # Updates the screen
    pygame.display.flip()
    clock.tick(60)