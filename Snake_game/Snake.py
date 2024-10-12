import random
import pygame
import time

SIZE=40

class Apple:
    def __init__(self,parent_screen,snake):
        self.parent_screen=parent_screen
        self.snake=snake
        self.block = pygame.Surface((30, 30))
        self.block.fill((255,0,0))
        self.x=SIZE*4
        self.y=SIZE*4
        self.move()
        
    def draw(self):
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        while True:
            self.x=random.randint(1,24)*SIZE
            self.x=random.randint(1,19)*SIZE
            if not self.is_in_snake():
                break

    def is_in_snake(self):
        for i in range(self.snake.length):
            if(self.snake.x[i]==self.x and self.snake.y[i] == self.y):
                return True           
        return False
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface=pygame.display.set_mode((1000,500))
        self.snake=Snake(self.surface,2)
        self.apple=Apple(self.surface, self.snake)
        self.play_sound('startGame')
        self.snake.draw()
        
    def display_score(self):
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score: {self.snake.length-2}",True,(255,255,255))
        self.surface.blit(score,(850,10))
    
    def game_over(self):
        self.surface.fill((52,200,100))
        font=pygame.font.SysFont('arial',30)
        line1=font.render(f"Game Over, your Score is: {self.snake.length-2}",True,(255,0,0))
        self.surface.blit(line1,(300,200))
        line1=font.render(f"Press enter to restart",True,(255,0,0))
        self.surface.blit(line1,(300,230))
        pygame.display.flip()
    
    def play_sound(self,sound):
        if (sound=='food'):
            play=pygame.mixer.Sound("resources/EatFood.mp3")
        elif(sound=='gameOver'):
            play=pygame.mixer.Sound("resources/gameOver.mp3")
        elif(sound=='startGame'):
            play=pygame.mixer.Sound("resources/startGame.mp3")    
        pygame.mixer.Sound.play(play)
    
    def play(self):
        self.snake.walk()  
        self.apple.draw() 
        self.display_score()
        pygame.display.flip()
        
        for i in range(self.snake.length):
            if (self.is_collision(self.snake.x[i],self.snake.y[i], self.apple.x,self.apple.y)):
                self.snake.increse_length()
                self.play_sound('food')
                self.apple.move()
        
        for i in range(2,self.snake.length):
            if(self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i])):
                self.play_sound('gameOver')
                raise "game over"       
    def is_collision(self, x1, y1, x2, y2):
        if abs(x1 - x2) < SIZE and abs(y1 - y2) < SIZE:
            return True
        return False

    def reset(self):
        self.snake=Snake(self.surface,2)      
    
    def display_pause_screen(self):
        font = pygame.font.SysFont('arial', 50)
        line1 = font.render(f"Game Paused", True, (255, 255, 255))
        self.surface.blit(line1, (350, 200))  # Position pause message
        line2 = font.render(f"Press Space to Resume", True, (255, 255, 255))  # Resume prompt
        self.surface.blit(line2, (280, 260))
        pygame.display.flip()
        
    def run(self):
        
        running =True
        pause=False
        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause= not pause
                        if pause:
                            self.display_pause_screen()  # Show pause screen
                        else:
                            self.play_sound('startGame')
                    if event.key==pygame.K_RETURN:
                        pause=False
                        self.play_sound('startGame')
                    if not pause:
                        if event.key==pygame.K_UP:
                            self.snake.move_up()
                        if event.key==pygame.K_DOWN:
                            self.snake.move_down()
                        if event.key==pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key==pygame.K_RIGHT:
                            self.snake.move_right()
                    
                        
                        
                elif event.type==pygame.QUIT:
                    running =False
            
            try:
                if not pause:
                    self.play()     
            except Exception as e:
                self.game_over()
                pause=True
                self.reset()
            if self.snake.length < 5:
                speed = 0.4
            elif 5 <= self.snake.length < 15:
                speed = 0.3
            elif 15 <= self.snake.length < 30:
                speed = 0.2
            elif self.snake.length >= 30:
                speed = 0.1
            time.sleep(speed)

class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen=parent_screen
        self.length=length
        self.block = pygame.Surface((30, 30))
        self.block.fill((255,255,0))
        self.x=[SIZE]*self.length
        self.y=[SIZE]*self.length
        self.direction="right"
        
    def draw(self):
        self.parent_screen.fill((52,200,100))
        
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction="up"
        
    def move_down(self):
        self.direction="down"
        
    def move_left(self):
        self.direction="left"
        
    def move_right(self):
        self.direction="right"
    
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        
        if(self.direction=="right"):
            self.x[0]+=SIZE
            self.draw()
        elif(self.direction=="left"):
            self.x[0]-=SIZE
            self.draw()
        elif(self.direction=="up"):
            self.y[0]-=SIZE
            self.draw()
        elif(self.direction=="down"):
            self.y[0]+=SIZE
            self.draw()

        if self.x[0] >= 1000:  
            self.x[0] = 0
        if self.x[0] < 0:      
            self.x[0] = 960  
        if self.y[0] >= 500:   
            self.y[0] = 0
        if self.y[0] < 0:      
            self.y[0] = 460 
        self.draw()
    
  
    def increse_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
    
   
if __name__=="__main__":
    game=Game()
    game.run()
    
    

   
                
        