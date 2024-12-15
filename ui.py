from puzzle import PipesPuzzle
from ui_component import Pipe
from ui_component import Button
import pygame
import os
import color


pygame.init()
width = 700
height = 700

class SelectionInterface:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Select puzzle")
        dfs_image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','dfs.png'))
        self.dfs = Button(300, 50, dfs_image, 1)
        astar_image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','Astar.png'))
        self.astar = Button(450, 50, astar_image, 1)
        level_image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','level.png'))
        self.level_button = [
            Button(350, 150, level_image, 1),
            Button(400, 150, level_image, 1),
            Button(450, 150, level_image, 1),
            Button(350, 200, level_image, 1),
            Button(400, 200, level_image, 1),
            Button(350, 250, level_image, 1),
            Button(400, 250, level_image, 1),
        ]
        self.font = pygame.font.Font(None, 50)

        self.config = [0, 0]

    def run(self):
        self.screen.fill(color.white)
        pipe_text = self.font.render("Pipe puzzle: ", True, color.navy_blue)
        self.screen.blit(pipe_text, (50, 50))
        self.screen.blit(self.dfs.image, (self.dfs.rect.topleft[0],self.dfs.rect.topleft[1]))
        self.screen.blit(self.astar.image, (self.astar.rect.topleft[0],self.astar.rect.topleft[1]))
        pygame.display.update()
        run = True
        while run:        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run == False
                    pygame.quit()
                    return
                
            if self.dfs.clicked():
                self.config[0] = 1
                self.display_level()
            
            if self.astar.clicked():
                self.config[0] = 2
                self.display_level()
            
            for i in range(len(self.level_button)):
                if self.level_button[i].clicked():
                    self.display_wait()
                    self.config[1] = i + 1
                    return self.config

    def display_level(self):
        simple_text = self.font.render("Simple level: ", True, color.navy_blue)
        immediate_text = self.font.render("Immediate level: ", True, color.navy_blue)
        advance_text = self.font.render("Advance level: ", True, color.navy_blue)
        self.screen.blit(simple_text, (50, 150))
        self.screen.blit(immediate_text, (50, 200))
        self.screen.blit(advance_text, (50, 250))
        for i in range(len(self.level_button)):
            self.screen.blit(self.level_button[i].image, (self.level_button[i].rect.topleft[0],self.level_button[i].rect.topleft[1]))
            text = self.font.render(str(i + 1), True, color.navy_blue)
            self.screen.blit(text, (self.level_button[i].rect.topleft[0]+10,self.level_button[i].rect.topleft[1]+5))
        pygame.display.update()

    def display_wait(self):
        wait_text = self.font.render("Please wait...", True, color.red)
        self.screen.blit(wait_text, (50, 350))
        pygame.display.update()

class PuzzleInterface:
    def __init__(self, puzzle_obj: PipesPuzzle, time, memory):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pipe puzzles")
        self.pipe_puzzle = puzzle_obj
        self.index = 0
        self.head = []
        self.auto = False
        self.execution_time = time
        self.memory = memory

        # load button image 
        next_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','next.png'))
        self.next_button = Button(520, 100, next_img, 1)
        pre_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','previous.png'))
        self.pre_button = Button(400, 100, pre_img, 1)   
        auto_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images','autorun.png'))
        self.auto_button = Button(470, 200, auto_img, 1)
        self.font = pygame.font.Font(None, 50)
        
        
        # load label 
        if len(self.pipe_puzzle.path) != 0:
            for i in range(5):
                for j in range(5):
                    t = self.pipe_puzzle.path[0].head[i][j]["type"]
                    if j == 0:
                        self.head.append([Pipe(self.screen, f"type{t}",(100 + j * 50,300 - 50 * i))])
                    else:
                        self.head[i].append(Pipe(self.screen, f"type{t}",(100 + j * 50, 300 - i * 50)))
                    if self.pipe_puzzle.path[0].head[i][j]["pumped"] == True:
                        self.head[i][j].angle = self.pipe_puzzle.path[0].head[i][j]["heading"]
                        self.head[i][j].pumpWater()
                    else:
                        self.head[i][j].rotatePipe(self.pipe_puzzle.path[0].head[i][j]["heading"])  
        self.display()
        pygame.display.update() 

    def display(self):
        self.screen.blit(self.next_button.image, (self.next_button.rect.topleft[0],self.next_button.rect.topleft[1]))
        self.screen.blit(self.pre_button.image, (self.pre_button.rect.topleft[0],self.pre_button.rect.topleft[1]))
        self.screen.blit(self.auto_button.image, (self.auto_button.rect.topleft[0],self.auto_button.rect.topleft[1]))
        display_step = self.font.render("STEP: " + str(self.index), True, color.red)
        self.screen.blit(display_step, (50, 20))
        display_time = self.font.render("Solving time: " + str(self.execution_time), True, color.navy_blue)
        self.screen.blit(display_time, (50, 400))
        display_memory = self.font.render("Memory used: " + str(round(self.memory/(2**20), 2)) + " MB", True, color.navy_blue)
        self.screen.blit(display_memory, (50, 450))
        for i in range(5):
            for j in range(5):
                self.head[i][j].display()  
        pygame.draw.circle(self.screen, color.red, [225,225], 10, 0)
                    

    def next_step(self):
        if self.index == len(self.pipe_puzzle.path) - 1:
            return False
        self.index += 1
        for i in range(5):
            for j in range(5):
                if self.pipe_puzzle.path[self.index].head[i][j]["heading"] != self.pipe_puzzle.path[self.index - 1].head[i][j]["heading"]:
                    if self.pipe_puzzle.path[self.index].head[i][j]["pumped"] == self.pipe_puzzle.path[self.index - 1].head[i][j]["pumped"]:
                        self.head[i][j].rotatePipe(self.pipe_puzzle.path[self.index].head[i][j]["heading"])
                    else:
                        if self.pipe_puzzle.path[self.index].head[i][j]["pumped"]:
                            self.head[i][j].angle = self.pipe_puzzle.path[self.index].head[i][j]["heading"] 
                            self.head[i][j].pumpWater()
                        else:
                            self.head[i][j].angle = self.pipe_puzzle.path[self.index].head[i][j]["heading"] 
                            self.head[i][j].resetWater()             
                else:
                    if self.pipe_puzzle.path[self.index].head[i][j]["pumped"] != self.pipe_puzzle.path[self.index - 1].head[i][j]["pumped"]:
                        if  self.pipe_puzzle.path[self.index].head[i][j]["pumped"]:
                            self.head[i][j].pumpWater()
                        else:
                            self.head[i][j].resetWater()
        return True

    def previous_step(self):
        if self.index == 0:
            return False
        self.index -= 1
        for i in range(5):
            for j in range(5):
                if self.pipe_puzzle.path[self.index].head[i][j]["heading"] != self.pipe_puzzle.path[self.index + 1].head[i][j]["heading"]:
                    if self.pipe_puzzle.path[self.index].head[i][j]["pumped"] == self.pipe_puzzle.path[self.index + 1].head[i][j]["pumped"]:
                        self.head[i][j].rotatePipe(self.pipe_puzzle.path[self.index].head[i][j]["heading"])
                    else:
                        if self.pipe_puzzle.path[self.index].head[i][j]["pumped"]:
                            self.head[i][j].angle = self.pipe_puzzle.path[self.index].head[i][j]["heading"] 
                            self.head[i][j].pumpWater()
                        else:
                            self.head[i][j].angle = self.pipe_puzzle.path[self.index].head[i][j]["heading"] 
                            self.head[i][j].resetWater()             
                else:
                    if self.pipe_puzzle.path[self.index].head[i][j]["pumped"] != self.pipe_puzzle.path[self.index + 1].head[i][j]["pumped"]:
                        if  self.pipe_puzzle.path[self.index].head[i][j]["pumped"]:
                            self.head[i][j].pumpWater()
                        else:
                            self.head[i][j].resetWater()
        return True
    
    def run(self):
        self.screen.fill(color.white)
        self.display()
        pygame.display.update()
        run = True
        while run:        
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run == False
                    pygame.quit()
                    return
                
            if self.auto_button.clicked():
                self.auto = not(self.auto)    

            if self.auto == True:
                font1 = pygame.font.Font(None,30)
                autoTurnOn = font1.render("Auto-run is on" , True, color.black)
                self.screen.blit(autoTurnOn, (440, 300))
                pygame.display.update()

            if self.auto == False:
                self.screen.fill( color.white,(440,300, 200, 100))
                pygame.display.update()

            if self.next_button.clicked():
                if self.auto:
                    while self.next_step():
                        self.screen.fill(color.white,(0,0, 300, 200))
                        self.display()
                        pygame.display.update()
                        pygame.time.delay(200) 
                    self.auto = False                      
                else:
                    self.next_step()
                    self.screen.fill(color.white,(0,0, 300, 100))
                    self.display()
                    pygame.display.update()
                    pygame.time.delay(500)

            if self.pre_button.clicked():
                if self.auto:
                    while self.previous_step():   
                        self.screen.fill(color.white,(0,0, 300, 100)) 
                        self.display()
                        pygame.display.update()
                        pygame.time.delay(200)
                        self.auto = False
                else:
                    self.previous_step()
                    self.screen.fill(color.white,(0,0, 300, 100))
                    self.display()
                    pygame.display.update()
                    pygame.time.delay(500) 
        




