import pygame
import pygame.gfxdraw
import sys
import time
import random
# the Label class is this module below
from label import *
 
 
pygame.init()
pygame.mixer.init()
#hit = pygame.mixer.Sound("sounds/hit.wav")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
 
 
 
buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style="button1",
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):
 
        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num
 
 
        self.text = text
 
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
 
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
 
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)
 
    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render
 
    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()
 
    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  
 
    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)
 
    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)
 
 
    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        self.check_collision()
 
    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0
 
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1
 
 
 
# ACTION FOR BUTTON CLICK ================
 
def on_click():
    print("Click on one answer")
 
def on_right():
    check_score("right")
 
def on_false():
    ''' if there is no 'right' as arg it means it's false '''
    check_score()
 
def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    
    # until there are questions (before last)
    #hit.play() # click sound
    if qnum < len(questions):
        print(qnum, len(questions))
        if answered == "right":
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        qnum += 1 # counter for next question in the list
        score.change_text(str(points))
        # Change the text of the question
        title.change_text(questions[qnum-1][0], color="white")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new
        
 
    # for the last question...
    elif qnum == len(questions):
        print(qnum, len(questions))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("Seu record é de " + str(points))
    time.sleep(.5)
 
 
# the first answer is right: it will be shuffled, don't worry
# ============================================================
questions = [
    ["What is the correct file extension for Python files?",
      [".py", ".pt", ".ppt", ".pdf"]],
    ["Which method can be used to remove any whitespace from both the beginning and the end of a string?",
      ["strip()", "trip()", "trim()", "len()"]],
    ["Which operator is used to multiply numbers?",
      ["*", "+", "-", "/"]],
]
# =========== END OF QUESTIONS AND ANSWERS =================
 
 
 
 
 
 
def show_question(qnum):
    ''' Show questions: '''
 
    pos = [180,218,256,294] #
    kill() # Kills the previous buttons/sprites
    def numbers():
      ''' inner function: THE NUMBERS OF THE QUESTION IN ORDER 1 2 3 4 '''
      
      # position of the numbers
      for n in range(4):
        Button((10, pos[n]),
        f"{n+1} ",
        36,
        "darkred on yellow",
        hover_colors="darkred on orange",
        style="button2",
        borderc=(255,255,0),
        command=None)
      
    def questions_shuffler():
      # show numbers and answers text
      # ============== TEXT: question and answers ====================
      comm =[on_right, on_false, on_false, on_false]
      for n in range(4):
        pass
        Button(
          (50, pos[n]),
          questions[qnum-1][1][n],
          36,
          "blue on yellow",
          hover_colors="blue on orange",
          style="button2",
          borderc=(255,255,0),
          command=comm[n])
 
    numbers()
    random.shuffle(pos) # randomized, so that the right one is not on top
    questions_shuffler()
 
def kill():
  ''' delete buttons when go to the next question '''
  for _ in buttons:
      _.kill()
 
qnum = 1
points = 0
# ================= SOME LABELS ==========================
num_question = Label(screen, str(qnum), 0, 0)
title = Label(screen, questions[qnum-1][0], 10, 10, 50, color="cyan")
score = Label(screen, "AV2 Programming", 50, 335)
write1 = Label(screen, "Maria Eduarda, Joana, Rafaela, Rafael", 50, 360, 20, color="white")
 
def start_again():
    pass
 
def loop():
    global game_on
 
    show_question(qnum)
 
    while True:
        screen.fill(0)
        for event in pygame.event.get(): # ====== quit / exit
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        buttons.update() #                     update buttons
        buttons.draw(screen)
        show_labels()        
        # update labels
        if points == 3:
          winimg = pygame.image.load("python_pygame.png")
          screen.blit(winimg, (100, 100))
        clock.tick(60)
        pygame.display.update()
    pygame.quit()
 
if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()