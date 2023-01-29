import pygame
import random
import sys
import pygbutton
import os
from button import Button
from constants import bg_color, line_color, tile_color, BLACK, GREEN
from nonogram import initialize_board, mark_square
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Main Menu')
bg = pygame.image.load("./background.jpg")
board = initialize_board()
rect_font = pygame.font.Font(None, 50)
size = [700, 500]
  #screen = pygame.display.set_mode((80,20))
clock = pygame.time.Clock()


def newBoard():
  DISPLAYSURF.fill((0,0,0))
  DISPLAYSURF.fill(bg_color)
  draw_grid()
  submitBtn.draw(DISPLAYSURF)
  restartBtn.draw(DISPLAYSURF)

def checkAnswer(userAnswer, answerKey):
    for i in range(0, len(answerKey)): #rows of the array
        for j in range(0, len(answerKey[0])): #columns of the array
            if answerKey[i][j] == '1':
              if userAnswer[i][j] != answerKey[i][j]:
                return False
            elif answerKey[i][j] != '1':
              if userAnswer[i][j] == '1':
                return False
    return True
def fill_space():
    for i in range(5):
        for j in range(5):
            if board[i][j] == "1":
              mark_surf = rect_font.render('+', 1, BLACK)
              mark_rect = mark_surf.get_rect(center=(162.5 + (25 / (5 / 5)) * j, 112.5 + (25 / (5 / 5)) * i))
              DISPLAYSURF.blit(mark_surf, mark_rect)
            elif board[i][j] == "2":
              mark_surf = rect_font.render('x', 1, (255, 0, 0))
              mark_rect = mark_surf.get_rect(center=(162.5 + (25 / (5 / 5)) * j, 112.5 + (25 / (5 / 5)) * i))
              DISPLAYSURF.blit(mark_surf, mark_rect)
            elif board[i][j] == "0":
              pygame.draw.rect(DISPLAYSURF, tile_color, 
              pygame.Rect(150 + 25*j, 100 + 25*i, 25, 25))
              pygame.draw.rect(DISPLAYSURF, line_color, pygame.Rect(150 + 25*j, 100 + 25*i, 27, 27), 2)
              
def draw_grid():
  # tiles bg
  pygame.draw.rect(DISPLAYSURF, tile_color, 
  pygame.Rect(150, 100, 125, 125))
  pygame.display.flip()
  # for horizontal lines
  for i in range(0, 5 + 1):
      pygame.draw.line(DISPLAYSURF, line_color, (100, 100 + (25*i)/(5/5)), (275, 100 + (25*i)/(5/5)), 2)
  # for vertical lines
  for i in range(0, 5 + 1):
      pygame.draw.line(DISPLAYSURF, line_color, (150 + (25*i)/(5/5), 50), (150 + (25*i)/(5/5), 225), 2)
  # borders
      pygame.draw.line(DISPLAYSURF, line_color, (100, 100), (100, 225), 2)
      pygame.draw.line(DISPLAYSURF, line_color, (150, 50), (275, 50), 2)
    
def draw_sample1():
  sample1_low = ['1', '3', '2', '3', '1'] 
  sample1_high = [' ', ' ', ' ', ' ', '3']
  sample2_low = ['3', '4', '2', '2', '1']
  sample2_high = [' ', ' ', '1', ' ', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample2():
  sample1_low = ['2', '2', '3', '2', '2'] 
  sample1_high = [' ', '2', ' ', ' ', ' ']
  sample2_low = ['2', '2', '1', '3', '3']
  sample2_high = ['1', '1', ' ', ' ', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample3():
  sample1_low = ['4', '2', '2', '2', '3'] 
  sample1_high = [' ', ' ', ' ', ' ', ' ']
  sample2_low = ['1', '3', '1', '2', '2']
  sample2_high = [' ', ' ', '3', '1', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample4():
  sample1_low = ['1', '1', '2', '1', '3'] 
  sample1_high = ['1', ' ', ' ', '3', '1']
  sample2_low = ['4', '2', '2', '1', '2']
  sample2_high = [' ', ' ', '1', ' ', '1']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample5():
  sample1_low = ['3', '2', '2', '3', '3'] 
  sample1_high = [' ', ' ', ' ', ' ', ' ']
  sample2_low = ['1', '2', '2', '3', '3']
  sample2_high = [' ', ' ', '2', ' ', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample6():
  sample1_low = ['1', '1', '1', '3', '5'] 
  sample1_high = ['2', '3', '1', ' ', ' ']
  sample2_low = ['1', '1', '2', '3', '2']
  sample2_high = ['2', '2', '2', ' ', '2']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1
def draw_sample7():
  sample1_low = ['3', '2', '1', '2', '2'] 
  sample1_high = ['1', '2', ' ', ' ', ' ']
  sample2_low = ['2', '2', '1', '2', '3']
  sample2_high = ['2', '1', ' ', ' ', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1

def draw_sample8():
  sample1_low = ['1', '1', '2', '2', '2'] 
  sample1_high = ['3', '2', ' ', ' ', ' ']
  sample2_low = ['2', '2', '1', '3', '4']
  sample2_high = [' ', ' ', '1', ' ', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1

def draw_sample9():
  sample1_low = ['1', '1', '3', '4', '1'] 
  sample1_high = [' ', ' ', ' ', ' ', '3']
  sample2_low = ['3', '4', '3', '1', '1']
  sample2_high = [' ', ' ', ' ', ' ', '1']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1

def draw_sample10():
  sample1_low = ['2', '1', '2', '2', '3'] 
  sample1_high = ['2', '1', ' ', ' ', ' ']
  sample2_low = ['1', '2', '3', '1', '1']
  sample2_high = [' ', '2', ' ', '3', ' ']
  j = 0
  for i in sample1_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 80))
    j += 1
  j = 0
  for i in sample1_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (159 + 25*j, 60))
    j += 1
  j = 0  
  for i in sample2_low:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (132, 107 + 25*j))
    j += 1
  j = 0
  for i in sample2_high:
    font = pygame.font.SysFont(None, 24)
    img = font.render(i, True, BLACK)
    DISPLAYSURF.blit(img, (112, 107 + 25*j))
    j += 1

def answer_key(sample_num):
  if sample_num == 1:
    key = [['0', '0', '1', '1', '1'],
           ['0', '1', '1', '1', '1'],
           ['0', '1', '0', '1', '1'],
           ['1', '1', '0', '0', '0'],
           ['0', '0', '0', '0', '1']]
  elif sample_num == 2:
    key = [['0', '1', '0', '1', '1'],
           ['0', '1', '0', '1', '1'],
           ['0', '0', '1', '0', '0'],
           ['1', '1', '1', '0', '0'],
           ['1', '1', '1', '0', '0']]
  elif sample_num == 3:
    key = [['1', '0', '0', '0', '0'],
           ['1', '1', '1', '0', '0'],
           ['1', '1', '1', '0', '1'],
           ['1', '0', '0', '1', '1'],
           ['0', '0', '0', '1', '1']]
  elif sample_num == 4:
    key = [['0', '1', '1', '1', '1'],
           ['0', '0', '1', '1', '0'],
           ['1', '0', '0', '1', '1'],
           ['0', '0', '0', '0', '1'],
           ['1', '0', '0', '1', '1']]
  elif sample_num == 5:
    key = [['1', '0', '0', '0', '0'],
           ['1', '1', '0', '0', '0'],
           ['1', '1', '0', '1', '1'],
           ['0', '0', '1', '1', '1'],
           ['0', '0', '1', '1', '1']]
  elif sample_num == 6:
    key = [['0', '1', '1', '0', '1'],
           ['1', '1', '0', '0', '1'],
           ['1', '1', '0', '1', '1'],
           ['0', '0', '1', '1', '1'],
           ['1', '0', '0', '1', '1']]
  elif sample_num == 7:
    key = [['1', '1', '0', '1', '1'],
           ['0', '1', '0', '1', '1'],
           ['1', '0', '0', '0', '0'],
           ['1', '1', '0', '0', '0'],
           ['1', '1', '1', '0', '0']]
  elif sample_num == 8:
    key = [['1', '1', '0', '0', '0'],
           ['1', '1', '0', '0', '0'],
           ['1', '0', '0', '0', '1'],
           ['0', '0', '1', '1', '1'],
           ['1', '1', '1', '1', '0']]

  elif sample_num == 9:
    key = [['0', '0', '1', '1', '1'],
           ['0', '1', '1', '1', '1'],
           ['0', '0', '1', '1', '1'],
           ['0', '0', '0', '1', '0'],
           ['1', '0', '0', '0', '1']]

  elif sample_num == 10:
    key = [['1', '0', '0', '0', '0'],
           ['1', '1', '0', '1', '1'],
           ['0', '0', '1', '1', '1'],
           ['1', '1', '1', '0', '1'],
           ['1', '0', '0', '0', '0']]
  return key
def set_samples(sample):
  if sample == 1:
    draw_sample1()
    winning_array = answer_key(1)
  elif sample == 2:
    draw_sample2()
    winning_array = answer_key(2)
  elif sample == 3:
    draw_sample3()
    winning_array = answer_key(3)
  elif sample == 4:
    draw_sample4()
    winning_array = answer_key(4)
  elif sample == 5:
    draw_sample5()
    winning_array = answer_key(5)
  elif sample == 6:
    draw_sample6()
    winning_array = answer_key(6)
  elif sample == 7:
    draw_sample7()
    winning_array = answer_key(7)
  elif sample == 8:
    draw_sample8()
    winning_array = answer_key(8)
  elif sample == 9:
    draw_sample9()
    winning_array = answer_key(9)
  elif sample == 10:
    draw_sample10()
    winning_array = answer_key(10)
  return winning_array
def get_font(size):
    return pygame.font.Font("./font.ttf", size)

# Menu Loop
def main_menu():
  done = False

  while not done:
      DISPLAYSURF.blit(bg, (0, 0))

      MENU_MOUSE_POS = pygame.mouse.get_pos()

      MENU_TEXT = get_font(35).render("NONOGRAMS", True, "#b68f40")
      MENU_RECT = MENU_TEXT.get_rect(center=(200, 35))

      PLAY_BUTTON = Button(image=pygame.image.load("./Quit Rect.png"), pos=(200, 115), 
                            text_input="PLAY", font=get_font(25), base_color="White", hovering_color="#d7fcd4")
      QUIT_BUTTON = Button(image=pygame.image.load("./Quit Rect.png"), pos=(200, 235), 
                            text_input="QUIT", font=get_font(25), base_color="White", hovering_color="#d7fcd4")

      DISPLAYSURF.blit(MENU_TEXT, MENU_RECT)

      for button in [PLAY_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(DISPLAYSURF)
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
              play()     
          if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
              pygame.quit()
              sys.exit()
        pygame.display.update()
# Play Loop
submitBtn = pygbutton.PygButton((300, 125, 80, 30), 'Submit!')
restartBtn = pygbutton.PygButton((300, 175, 80, 30), 'New Board')
def play():
  done = False
  pygame.display.set_caption('Nonograms')

  
  DISPLAYSURF.fill(bg_color)
  draw_grid()
  sample = random.randint(1, 10) # change sample here
  winning_array = set_samples(sample)

 
  font = pygame.font.Font(None, 10)
  
  while not done:
    # draw_grid(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

        LEFT = 1
        MIDDLE = 2
        RIGHT = 3
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
          clicked_col = (event.pos[0] - 150) // 25
          clicked_row = (event.pos[1] - 100) // 25
          if event.pos[0] > 300 and event.pos[1] < 160:
            if(checkAnswer(board, winning_array)):
              pygame.draw.rect(DISPLAYSURF, bg_color, 
              pygame.Rect(100, 10, 250, 40))
              pygame.display.flip()
              font = pygame.font.SysFont(None, 30)
              img = font.render("You win!", True, GREEN)
              DISPLAYSURF.blit(img, (180, 20))
              # displays a winning sign
              # checkAnswer(board, winning_array)
            else:
              font = pygame.font.SysFont(None, 30)
              img = font.render("Try again!", True, (210, 43, 43))
              DISPLAYSURF.blit(img, (165, 20))
              #display "Try Again sign"
          elif event.pos[0] > 300 and event.pos[1] > 160: # New board
            newBoard()
            for i in range(5):
              for j in range(5):
                mark_square(board, i, j, 'Unmark')
                fill_space()
            sample = random.randint(1, 10)
            winning_array = answer_key(sample)
            set_samples(sample)
          else:
            mark_square(board, clicked_row, clicked_col, "Mark")
            fill_space()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
          clicked_col = (event.pos[0] - 150) // 25
          clicked_row = (event.pos[1] - 100) // 25
          mark_square(board, clicked_row, clicked_col, "Flag")
          fill_space()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MIDDLE:
          clicked_col = (event.pos[0] - 150) // 25
          clicked_row = (event.pos[1] - 100) // 25
          mark_square(board, clicked_row, clicked_col, "Unmark")
          fill_space()
        
    submitBtn.draw(DISPLAYSURF)
    restartBtn.draw(DISPLAYSURF)
    
    pygame.display.update()
  
main_menu()
