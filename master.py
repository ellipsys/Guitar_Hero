# -*- coding: utf-8 -*-
import pygame
import random
from pygame.locals import *
import time, sys, os
import threading
import ctypes
global sounds, introm,nombre,edad,genero
import game
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
pygame.init()
size = (800,600)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
orange = (255,137,0)
messageBox = ctypes.windll.user32.MessageBoxW
global datos1
font = "Retro.ttf"

clock = pygame.time.Clock()
FPS=30



#sounds["begin"].play()
songs = ["Legado 47- Fantasmas e Monstros","System Of A Down - Chop Suey!","Limp Bizkit - My Generation","Rage Against the Machine - Bulls on Parade","Heart"]
#modules.game.star
def text_format(message, textFont, textSize, textColor):
	newFont=pygame.font.Font(textFont, textSize)
	newText=newFont.render(message, 0, textColor)
	return newText
def datos1(name,edad,genero):
	if (genero == ("f" or "F")):
		genero = "Mujer"
	else: 
		genero = "Hombre"
	datos1 = (name + "; "+ str(edad)+ "; "+ genero)
	return datos1

def datos():
	os.system("cls")
	intro   = False
	namein = False
	while not namein:
		#size = (800,600)
		nombre = raw_input("Ingrese nombre: ")
		edad = raw_input("ingrese Edad: ")
		genero = raw_input("Ingrese genero (F o M): ")
		os.system("cls")
		if len(nombre) > 0 and nombre.isalpha() and (len(edad) > 0 and edad.isdigit()) and len(genero)>0 and (genero == ("M" or "m") or genero == ("F" or "f")):
			os.system("cls")
			jugador = datos1(nombre,edad,genero)
			main_menu(nombre,edad,genero)


def playSong(i):
	if (i==0) or (i==-5):
		x = "0"
	elif (i==1) or (i==-4):
		x = "1"
	elif (i==2) or (i==-3):
		x = "2"
	elif (i==3) or (i==-2):
		x = "3"
	elif(i==4) or (i==-1):
		x = "4"
	return x

def main_menu(nombre,edad,genero):#size
	sounds = {
	"ok" : pygame.mixer.Sound("sounds/beep-01a.wav"),
	"begin" : pygame.mixer.Sound("sounds/intromusic.wav"),
	"error"   : pygame.mixer.Sound("sounds/buzzer.wav"),
	"0"	: pygame.mixer.Sound("sounds/Legado 47- Fantasmas e Monstros.wav"),
	"1"	: pygame.mixer.Sound("sounds/System Of A Down - Chop Suey!.wav"),
	"2"	: pygame.mixer.Sound("sounds/Limp Bizkit - My Generation.wav"),
	"3"	: pygame.mixer.Sound("sounds/Rage Against the Machine - Bulls on Parade.wav"),
	"4"	: pygame.mixer.Sound("sounds/Heart.wav")
}
	sounds["begin"].play()
	
	size = (800,600)
	surface = pygame.display.set_mode(size)	
	surface.fill(black)
	pygame.display.set_caption("GUITAR HERO TEST DE REACCION")
	running = True
	introm = True
	surface = pygame.display.set_mode(size)
	songs = ["Legado 47- Fantasmas e Monstros","System Of A Down - Chop Suey!","Limp Bizkit - My Generation","Rage Against the Machine - Bulls on Parade","Heart"]
	menu=True
	i = 0
	selected=songs[i]

	while menu:
		
		if (i == -4 or i == 4):
			i = 0
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					selected=songs[i+1]
					pygame.draw.polygon(surface, red, [(410,213),(433,268),(385,268)])
					
					pygame.display.update()
					time.sleep(0.2)
					
					print songs[i+1]
					
					i = i + 1
				elif event.key==pygame.K_DOWN:
					pygame.draw.polygon(surface, red, [(410,470),(433,416),(385,416)])
					
					pygame.display.update()
					time.sleep(0.2)
					selected=songs[i-1]
					print songs[i-1]
					
					i = i - 1
				if event.key==pygame.K_RETURN:
					#print songs[i]
					if selected==songs[i]:
						cancion = playSong(i)
						sounds["begin"].stop()
						#sounds[cancion].play()
						game.star(nombre,edad,genero,cancion)
						os.system("cls")

						
					
						
		surface.fill(black)
		title=text_format("<-Guitar Hero Test->", font, 110, orange)
		title2=text_format("Select a song", font, 60, yellow)
		#title3=text_format("Up or Down", font, 20, yellow)
		pygame.draw.polygon(surface, yellow, [(410,213),(433,268),(385,268)])
		pygame.draw.polygon(surface, yellow, [(410,470),(433,416),(385,416)])
		
		if (i == -4 or i == 4):
			i = 0
		text_start=text_format(songs[i], font, 40, white)
			#text_quit=text_format(songs[i], font, 40, red
		title_rect=title.get_rect()
		#title2 = title2.get_rect()
		start_rect=text_start.get_rect()
		surface.blit(title, (400 - (title_rect[2]/2), 10))
		surface.blit(title2, (400 - (title_rect[2]/5), 100))
		#surface.blit(title3, (400 - (title_rect[2]/6), 200))
		surface.blit(text_start, (400 - (start_rect[2]/2), 300))
		pygame.display.update()
		clock.tick(FPS)
		pygame.display.set_caption("Guitar Hero Test")

datos()
