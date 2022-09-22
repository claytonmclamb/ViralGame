import pygame as p
import random


class Virus(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.y = HEIGHT / 2
        self.vel = 5
        self.width = 30
        self.height = 30
        self.health = 3
        
        #IMAGES
        
        self.virus = p.image.load("cartoonv.png")
        self.virus = p.transform.scale(self.virus, (self.width, self.height))
        
        self.image = self.virus
        self.rect = self.image.get_rect()
    
        
    def get_damage(self):
        global HEALTH
        if self.health > 0:
            self.health -= 1
            HEALTH -= 1
    
    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)
        
    def collision(self):
        global mucus, stomach, skin
        hit = p.sprite.spritecollide(self, firstline_group, False, p.sprite.collide_mask)
        if hit:
            self.get_damage()
            self.x = 50
        
    def movement(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -= self.vel
        elif keys[p.K_RIGHT]:
            self.x += self.vel
        elif keys[p.K_UP]:
            self.y -= self.vel
        elif keys[p.K_DOWN]:
            self.y += self.vel
            
    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2
        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width/2
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
        
class Cell(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.width = 30
        self.height = 30
        
        #IMAGES
        
        self.virus = p.image.load("cellcartoon.png")
        self.virus = p.transform.scale(self.virus, (self.width, self.height))
        
        self.image = self.virus
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = (self.x, self.y)
    
    def randomize_location(self):
        random_x = random.randint(100, 400)
        random_y = random.randint(100, 400)
        self.x = random_x
        self.y = random_y
            
class Enemies(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        #Level 2 Photos
        if number == 1:
            self.x = 150
            self.image = p.image.load("skincell.png")
            self.vel = -4      
            self.width = 100
            self.height = 150
        elif number == 2:
            self.x = 280
            self.image = p.image.load("mucus.png")
            self.vel = 10
            self.width = 67
            self.height = 100
        elif number == 3: 
            self.x = 410
            self.image = p.image.load("stomach.png")
            self.vel = -7
            self.width = 55
            self.height = 82.5
        elif number == 7:
            self.x =  540
            self.image = p.image.load("vomit.png")
            self.vel = -4
            self.width = 82.5
            self.height = 82.5
        #Level 1 Photos
        elif number == 4: 
            self.x = 200
            self.image = p.image.load("hands.png")
            self.vel = -5
            self.width = 55
            self.height = 82.5
        elif number == 5:
            self.x = 360 
            self.image = p.image.load("vaccine.png")
            self.vel = 4
            self.width = 55
            self.height = 82.5
        elif number == 6:
            self.x =  510
            self.image = p.image.load("mask.jpg")
            self.vel = -4
            self.width = 55
            self.height = 82.5
        #Level 3 Photos
        elif number == 8:
            self.x =  200
            self.image = p.image.load("antibody.jpg")
            self.vel = -12
            self.width = 55
            self.height = 82.5
        elif number == 9:
            self.x =  340
            self.image = p.image.load("TCell.png")
            self.vel = 10
            self.width = 82.5
            self.height = 82.5
        elif number == 10:
            self.x =  480
            self.image = p.image.load("Bcell.png")
            self.vel = -13
            self.width = 82.5
            self.height = 82.5
            
        self.y = HEIGHT / 2
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)
        
    def movement(self):
        self.y += self.vel
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1
   
class Screen(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.img = p.image.load("office.jpg")
            self.img = p.transform.scale(self.img, (WIDTH, HEIGHT))
        elif number == 2:
            self.img = p.image.load("skin.png")
            self.img = p.transform.scale(self.img, (WIDTH, HEIGHT))
        elif number == 3:
            self.img = p.image.load("inside.png")
            self.img = p.transform.scale(self.img, (WIDTH, HEIGHT))
        elif number == 4:
            self.img = p.image.load("cell.png")
            self.img = p.transform.scale(self.img, (WIDTH, HEIGHT))
        
        self.image = self.img
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.topleft = (self.x, self.y)
        
        
     
def HealthDisplay():
    health_text = health_font.render("HEARTS: " + str(HEALTH) + " / 3", True, (255, 0, 0))
    win.blit(health_text, (10, 10))
def LevelDisplay():
    global level
    if level == 1:
        level_text = level_font.render("Level: " + str(level) + " PREEMPTIVE MEASURES", True, (0, 0, 0))
    elif level == 2:
        level_text = level_font.render("Level: " + str(level) + " INNATE IMMUNE SYSTEM", True, (0, 0, 0))
    elif level == 3:
        level_text = level_font.render("Level: " + str(level) + " ADAPIVE IMMUNE SYSTEM", True, (0, 0, 0))
    else:
        level_text = level_font.render("Level: " + str(level) + " VIRUS SPREAD", True, (0, 0, 0))
    win.blit(level_text, (10, 30))
def ScoreDisplay():
    health_text = health_font.render("SCORE: " + str(SCORE), True, (255, 0, 255))
    win.blit(health_text, (500, 10))
        

WIDTH = 640
HEIGHT = 480

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Immune Defense")
clock = p.time.Clock()

HEALTH = 3
health_font = p.font.SysFont("comicsans", 15, True)

SCORE = 0
health_font = p.font.SysFont("comicsans", 15, True)

bg = Screen(1)
screen_group = p.sprite.Group()
screen_group.add(bg)


virus = Virus()
virus_group = p.sprite.Group()
virus_group.add(virus)

# Level 1!
hands = Enemies(4)
vaccine = Enemies(5)
mask = Enemies(6)
pre_group = p.sprite.Group()
pre_group.add(hands, vaccine, mask)


#Level 2!
skin = Enemies(1)
mucus = Enemies(2)
stomach = Enemies(3)
vomit = Enemies(7)
firstline_group = p.sprite.Group()
firstline_group.add(skin, mucus, stomach, vomit)

#Level 3!
antibody = Enemies(8)
Tcell = Enemies(9)
Bcell = Enemies(10)
adaptive_group = p.sprite.Group()
adaptive_group.add(antibody, Tcell, Bcell)

#Level 4
cell = Cell()
cell_group = p.sprite.Group()
cell_group.add(cell)

lose = p.image.load("lose.png")
winner = p.image.load("win.png")

level = 1
level_font = p.font.SysFont("comicsans", 15, True)

def text_objects(text, font):
    textSurface = font.render(text, True, (255,51,51))
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, size):
    largeText = p.font.Font("freesansbold.ttf",size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    win.blit(TextSurf, TextRect)


def crash_scene(primary, secondary):
    global HEALTH
    if HEALTH < 3:
        sceneExit = False
        time = 6500  # 6000 milliseconds until we continue
        while not sceneExit:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()
            win.fill((21,71,52))
            message_display (primary, (WIDTH/2),(HEIGHT/2) - 100, 35)
            x = 40
            lines = []
            for i in range(0, len(secondary), 30):
                lines.append(secondary[i:i+30])
            for line in lines:
                message_display (line, (WIDTH/2),(HEIGHT/2) - 100 + x, 35)
                x += 40
            p.display.update()
            passed_time = clock.tick(60)
            time -= passed_time
            if time <= 0:
                sceneExit = True
            

run = True
intro = True
First_Level = True
Second_Level = True
Third_Level_P1 = True
Third_Level_P2 = True
Fourth_Level = True

while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    screen_group.draw(win)
    if intro:
        sceneExit = False
        time = 4000  # 2000 milliseconds until we continue
        while not sceneExit:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()
            win.fill((21,71,52))
            message_display ("WELCOME", (WIDTH/2),(HEIGHT/2) - 75, 35)
            x = 40
            lines = []
            secondary = "You are playing as a virus     trying to infect someone.    Good luck getting past the    defenses."
            for i in range(0, len(secondary), 30):
                lines.append(secondary[i:i+30])
            for line in lines:
                message_display (line, (WIDTH/2),(HEIGHT/2) - 75 + x, 35)
                x += 40
            p.display.update()
            passed_time = clock.tick(60)
            time -= passed_time
            if time <= 0:
                sceneExit = True
        intro = False
    else:
        if HEALTH == 0:
            win.fill((21, 71, 52))
            ScoreDisplay()
            win.blit(lose, (60, 60))
            message_display("Would You Like To Play Again?", 250, 25, 30)
            message_display("Hit 'Y' to keep playing or hit X-Button to not!", 250, 50, 15)
            keys = p.key.get_pressed()     
            if keys[p.K_y]:
                level = 1
                intro = True
                First_Level = True
                Second_Level = True
                Third_Level_P1 = True
                Third_Level_P2 = True
                Fourth_Level = True
                SCORE = 0
                virus.health = 3
                HEALTH = 3
                virus.vel = 5
                virus.x = 15
                virus.y = HEIGHT / 2
                bg = Screen(1)
                screen_group = p.sprite.Group()
                screen_group.add(bg)
                
        elif level == 1:
            if First_Level:
                bg = Screen(1)
                sceneExit = False
                time = 4000
                while not sceneExit:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            quit()
                    win.fill((21,71,52))
                    message_display ("FIRST LEVEL", (WIDTH/2),(HEIGHT/2) - 75, 35)
                    x = 40
                    lines = []
                    secondary = "You are attempting to get past preemptive measures for      stopping viruses. This is     stuff YOU can do!"
                    for i in range(0, len(secondary), 30):
                        lines.append(secondary[i:i+30])
                    for line in lines:
                        message_display (line, (WIDTH/2),(HEIGHT/2) - 75 + x, 35)
                        x += 40
                    p.display.update()
                    passed_time = clock.tick(60)
                    time -= passed_time
                    if time <= 0:
                        sceneExit = True
                First_Level = False
            if virus.rect.colliderect(hands.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("WASHED", "Washing your hands with soap  for 20 seconds kills almost   ALL the germs on   your hands! This makes sure you AND      others do not get sick!")
            if virus.rect.colliderect(vaccine.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15 
                crash_scene("VACCINATED", "Vaccines boost immunity by    preparing your immune system  for future infections! By     giving you a 'dead' virus,    cells in the adaptive immune  system are better prepared to fight the virus!")
            if virus.rect.colliderect(mask.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("MASKED", "Masks have the potential to   block illness causing viruses, or germs! Germs are passed   when you cough or sneeze into your hands and touch other    objects, or when you don’t    cover your mouth and nose when you cough or sneeze.")
            if virus.x >= 620:
                bg = Screen(2)
                screen_group = p.sprite.Group()
                screen_group.add(bg)
                virus.x = 15
                level += 1
            virus_group.draw(win)
            pre_group.draw(win)
            
            virus_group.update()
            pre_group.update()
            screen_group.update()
            HealthDisplay()
            LevelDisplay()
            ScoreDisplay()
        elif level == 2:
            if Second_Level:
                sceneExit = False
                time = 4000
                while not sceneExit:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            quit()
                    win.fill((21,71,52))
                    message_display ("SECOND LEVEL", (WIDTH/2),(HEIGHT/2) - 75, 35)
                    x = 40
                    lines = []
                    secondary = "You are attempting to get past the innate immune system!     This is stuff your body comes equipped with ready to kill  viruses!"
                    for i in range(0, len(secondary), 30):
                        lines.append(secondary[i:i+30])
                    for line in lines:
                        message_display (line, (WIDTH/2),(HEIGHT/2) - 75 + x, 35)
                        x += 40
                    p.display.update()
                    passed_time = clock.tick(60)
                    time -= passed_time
                    if time <= 0:
                        sceneExit = True
                Second_Level = False
            if virus.rect.colliderect(skin.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("BLOCKED", "The skin is the bodies first  line of defense against       diseases. It acts as the      natural, or innate, barrier     against germs!")
            if virus.rect.colliderect(mucus.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("MUCKED", "Mucus traps allergens or      bacteria from further          spreading into your body!    Mucus is in your lungs throat, mouth, and nose!")
            if virus.rect.colliderect(stomach.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("BURNED", "Acid located in the stomach   keeps your gut clean from     harmful microbiomes!")
            if virus.rect.colliderect(vomit.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("VOMMITTED", "When your stomach takes in    harmful substances, your body makes you throw them up to get rid of them and stop them    from going any further!")
            if virus.x >= 620:
                bg = Screen(3)
                screen_group = p.sprite.Group()
                screen_group.add(bg)
                virus.x = 15
                level += 1
            virus_group.draw(win)
            firstline_group.draw(win)
            virus_group.update()
            firstline_group.update()
            screen_group.update()
            HealthDisplay()
            LevelDisplay()
            ScoreDisplay()
        elif level == 3:
            if Third_Level_P1:
                sceneExit = False
                time = 4000
                while not sceneExit:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            quit()
                    win.fill((21,71,52))
                    message_display ("THIRD LEVEL", (WIDTH/2),(HEIGHT/2) - 75, 35)
                    x = 40
                    lines = []
                    secondary = "You have made it to the       ADAPTIVE immune system! This  part of the immune system has special cells whose job is to kill viruses!"
                    for i in range(0, len(secondary), 30):
                        lines.append(secondary[i:i+30])
                    for line in lines:
                        message_display (line, (WIDTH/2),(HEIGHT/2) - 75 + x, 35)
                        x += 40
                    p.display.update()
                    passed_time = clock.tick(60)
                    time -= passed_time
                    if time <= 0:
                        sceneExit = True
                Third_Level_P1 = False
            if Third_Level_P2:
                sceneExit = False
                time = 4000
                while not sceneExit:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            quit()
                    win.fill((21,71,52))
                    x = 0
                    lines = []
                    secondary = "Oh no! You have been detected by this immune system before! The ADAPTIVE immune system is ready to fight you!"
                    for i in range(0, len(secondary), 30):
                        lines.append(secondary[i:i+30])
                    for line in lines:
                        message_display (line, (WIDTH/2),(HEIGHT/2) - 75 + x, 35)
                        x += 40
                    p.display.update()
                    passed_time = clock.tick(60)
                    time -= passed_time
                    if time <= 0:
                        sceneExit = True
                Third_Level_P2 = False
            if virus.rect.colliderect(antibody.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("BODIED", "Antibodies are part of the    adaptive immune system and    respond to specific viruses to stop them in their tracks!")
            if virus.rect.colliderect(Tcell.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("TERMINATED", "T-Cell's, made in the thymus, have many types. Overall,     T-Cell's try and destroy cells that have been infected by   the virus!")
            if virus.rect.colliderect(Bcell.rect) and virus.x > 100:
                virus.get_damage()
                virus.x = 15
                crash_scene("BROKEN", "B-Cell's, made in the bone    marrow, find viruses before   they enter a cell. They signal other cell's to destroy the  virus and remember what       viruses they have seen before, producing the antibodies     needed to kill the virus.")
            if virus.x >= 620:
                bg = Screen(4)
                screen_group = p.sprite.Group()
                screen_group.add(bg)
                virus.x = 15
                level += 1
            virus_group.draw(win)
            adaptive_group.draw(win)
            virus_group.update()
            adaptive_group.update()
            screen_group.update()
            HealthDisplay()
            LevelDisplay()
            ScoreDisplay()
        elif level == 4:
            if Fourth_Level:
                sceneExit = False
                time = 6000
                while not sceneExit:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            quit()
                    win.fill((21,71,52))
                    message_display ("LAST LEVEL (INFECTION TIME)", (WIDTH/2),(HEIGHT/2) - 130, 35)
                    x = 40
                    lines = []
                    secondary = "You have made it past the     immune system defenses, you   can now infect the cells of   this organism. The more       cells you infect, the more         infectious you can become because the virus may mutate and create a new variant!"
                    for i in range(0, len(secondary), 30):
                        lines.append(secondary[i:i+30])
                    for line in lines:
                        message_display (line, (WIDTH/2),(HEIGHT/2) - 130 + x, 35)
                        x += 40
                    p.display.update()
                    passed_time = clock.tick(60)
                    time -= passed_time
                    if time <= 0:
                        sceneExit = True
                timer_event = p.USEREVENT + 1
                p.time.set_timer(timer_event , 30000)
                Fourth_Level = False
            if virus.rect.colliderect(cell.rect) and virus.x > 99:
                cell.randomize_location()
                SCORE += 1
                if SCORE % 5 == 0 and SCORE != 0:
                    virus.vel += 1
            if event.type == timer_event:
                level = 5
            virus_group.draw(win)
            virus_group.update()
            cell_group.draw(win)
            cell_group.update()
            screen_group.update()
            HealthDisplay()
            LevelDisplay()
            ScoreDisplay()
        else:
            win.fill((21, 71, 52))
            ScoreDisplay()
            win.blit(winner, (60, 60))
            message_display("Would You Like To Play Again?", 250, 25, 30)
            message_display("Hit 'Y' to keep playing or hit X-Button to not!", 250, 50, 15)
            keys = p.key.get_pressed()     
            if keys[p.K_y]:
                level = 1
                intro = True
                First_Level = True
                Second_Level = True
                Third_Level_P1 = True
                Third_Level_P2 = True
                Fourth_Level = True
                SCORE = 0
                virus.health = 3
                HEALTH = 3
                virus.vel = 5
                virus.x = 15
                virus.y = HEIGHT / 2
                bg = Screen(1)
                screen_group = p.sprite.Group()
                screen_group.add(bg)
                
            
            
            
        
    p.display.update()
    
            
p.quit()