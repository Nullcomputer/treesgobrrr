#hi this very cool, super epic code was made by nullcomputer/taryn

#imports
import pygame
import time
import tkinter as tk
import random
import numpy as np

#init
root = tk.Tk()
pygame.init()


#settings
vel = 0.6
x = root.winfo_screenwidth()/2
y = root.winfo_screenheight()/2
playersize_height = 100
playersize_width = 100


#resize and load images
img_test = pygame.image.load('img\\test-img.png')
img_acorn = pygame.image.load('img\\acorn.png')

img_player1 = pygame.image.load('img\\player1.png')
img_player1 = pygame.transform.scale(img_player1, (playersize_height, playersize_width))

img_tree1 = pygame.image.load('img\\tree1.png')
img_tree1 = pygame.transform.scale(img_tree1, (random.randrange(10, 200), playersize_width))

#img_tree2 = pygame.image.load('img\\tree2.png')


#colors
#color_ = (, , )
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_backroundgreen = (0, 90, 0)


#get and set window size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window = pygame.display.set_mode((screen_width-100, screen_height-100), pygame.RESIZABLE)


#set title and icon
pygame.display.set_caption('treesgobrrr')
img_acorn = pygame.transform.scale(img_acorn, (playersize_width, playersize_height))
pygame.display.set_icon(img_acorn)


#tree placement
trees = []
def treeplace(tree_x, tree_y):
    if random.randint(0, 10000) > 9981:
        trees.append(random.randrange())
        trees.append(random.randrange())
    elif random.randint(0, 10000) > 9986:
        if (i % 2) == 0:
            trees.pop()
        else:
            trees.pop()
    for i in trees:
        window.blit(img_tree1, (tree_x, tree_y))


#main loop
running = True


while(running):
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
      

    if keys[pygame.K_LEFT] and x>0:
        x -= vel

    if keys[pygame.K_RIGHT] and x<screen_width-75-playersize_width:
        x += vel
         
    if keys[pygame.K_UP] and y>0:
        y -= vel
          
    if keys[pygame.K_DOWN] and y<screen_height-75-playersize_height:
        y += vel

    screen_width, screen_height = window.get_size()

    window.fill(color_backroundgreen)


    treeplace(random.randrange(100, screen_width), random.randrange(100, screen_height ))
    window.blit(img_player1, (x, y))

    pygame.display.update() 