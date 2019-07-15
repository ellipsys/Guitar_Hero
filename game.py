# -*- coding: utf-8 -*-
import pygame
import random
from pygame.locals import *
import time
import ctypes, sys, os
#ondo = pygame.image.load('image/fondo.png')
global fondo
global surface
fondo = pygame.image.load('fondo.png')
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
messageBox = ctypes.windll.user32.MessageBoxW
running = True 
puntaje = 0
size = (800,600)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
orange = (255,137,0)
end = False
purple = (255,0,127)
global nombre, edad, genero, sounds


def evaluar(puntaje1):
	puntaje1 = int(puntaje1)
	
	bajo =  ((puntaje1 > 0 ) and (puntaje1 < 6))
	medio =  (puntaje1 > 5) and (puntaje1 < 11)
	alto = (puntaje1 > 10) and (puntaje1 < 16)
	excelent = (puntaje1 > 15) and (puntaje1 < 21)

	if bajo == True:
		messageBox(None,u'diagnostico: \n Motricidad leve , dirgirse a donde un doctor con urgencia',u'Test Hero',0x40 | 0x0)

	if medio == True:
		messageBox(None,u'diagnostico: \n ',u'Motricidad fina aceptable, intent hacer trabajos ludicos',0x40 | 0x0)

	if alto == True:
		messageBox(None,u'diagnostico: \n Motrcidad fina buena, sigue practicando',u'Test Hero',0x40 | 0x0)

	if excelent == True:
		messageBox(None,u'diagnostico: \n Motricidad fina Excelente, puedes pilotear un avio',u'Test Hero',0x40 | 0x0)

def timer(start): 
	seconds = 90
	elapsed = 0
	while elapsed < seconds:
			elapsed = time.time() - start
			return elapsed
def good():
	size = (800,600)
	surface = pygame.display.set_mode(size)
	
	myfont = pygame.font.SysFont("arial", 30)
	scoretext = myfont.render("BIEN", 1, (37,222,255))
	surface.blit(scoretext, (30, 30))
	pygame.display.flip()
	time.sleep(0.4)

def bad():
	
	size = (800,600)
	surface = pygame.display.set_mode(size)
	myfont = pygame.font.SysFont("arial", 32)
	scoretext = myfont.render("MAL", 1, (255,0,0)) 
	surface.blit(scoretext, (30, 30))
	pygame.display.flip()
	time.sleep(0.4)
	
	
def star(nombre,edad,genero,cancion):
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
	print nombre
	score = 0
	print cancion
	print nombre
	start = time.time()
	size = (800,600)
	surface = pygame.display.set_mode(size)	
	nCircles = 0
	end = False
	pygame.display.set_caption("Guitar Hero Test")
	#fondo = pygame.image.load('fondo.png')
	fondo = pygame.image.load('fondo.png')
	
	sounds[str(cancion)].play()
	speed = 4
	while not end:
		
		for i in range(0,8):
			pos = random.randint(1,4)
			
			if nCircles == 0:
				pos2 = 0
				if pos == 1:
					pos1 = 100
					COLOUR = red
					nCircles = 1
					drawcircle = 1
				if pos == 2:
					pos1 = 300
					COLOUR = green
					nCircles = 1
					drawcircle = 1
				if pos == 3:
					pos1 = 500
					COLOUR = orange
					nCircles = 1
					drawcircle = 1	
				if pos == 4:
					pos1 = 700
					COLOUR = blue
					nCircles = 1
					drawcircle = 1
			retardo = int(timer(start))
			
		if running == True:
			
			pygame.draw.circle(fondo,red,(100,500), 60,4)
			pygame.draw.circle(fondo,green,(300,500), 60,4)
			pygame.draw.circle(fondo,orange,(500,500), 60,4)
			pygame.draw.circle(fondo,blue,(700,500), 60,4)

			pygame.draw.lines(fondo,white,False,[(200,0),(200,600)],2)
			pygame.draw.lines(fondo,white,False,[(400,0),(400,600)],2)
			pygame.draw.lines(fondo,white,False,[(600,0),(600,600)],2)
			surface.blit(fondo,(0,0))
			
			pos2 = pos2 + speed
			if pos2 == 560:
				nCircles = 0
				drawcircle = 0
		
		if drawcircle == 1:
			pygame.display.update()
			myCircle = pygame.draw.circle(surface,COLOUR,(pos1,pos2), 50,0)
		
	
		pygame.display.flip()	
		
		if retardo == 90:
			sounds[str(cancion)].stop()
			#pygame.mixer.music.stop()
			msg = u'nombre: '+ nombre+u' : edad '+edad+u' : genero: '+genero 
			messageBox(None,msg,u'Test velocidad de respuesta',0x40 | 0x0)#########################################
			score = int(score)
			evaluar(score)
			print score
			pygame.quit()
			quit()

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # If user clicked close
				end = True
				pygame.quit()
				quit()# Flag that we are done so we exit this loop
			if pos2 >= 600:
			
				drawcircle = 0
				nCircles = 0

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					is_inside = myCircle.collidepoint(100,500) ############### coordenada 1 
					if is_inside:
						drawcircle = 0
						nCircles = 0
						score = score + 1
						
						good()
						pygame.draw.circle(fondo,purple,(100,500), 59,8)
						surface.blit(fondo,(0,0))
						pygame.draw.circle(fondo,red,(100,500), 60,4)
						surface.blit(fondo,(0,0))
			
				
					
					else:
						drawcircle = 0
						nCircles = 0
						bad()
						sounds["error"].play()
				if event.key == pygame.K_2: #verde
					is_inside = myCircle.collidepoint(300,500) ################3coordenada 2
					if is_inside:
						drawcircle = 0
						nCircles = 0
						score = score + 1
						good()
						pygame.draw.circle(fondo,purple,(300,500), 59,5)
						surface.blit(fondo,(0,0))
						pygame.draw.circle(fondo,red,(100,500), 60,4)
						surface.blit(fondo,(0,0))
					else:
					
						sounds["error"].play()
						drawcircle = 0
						nCircles = 0
						bad()
				if event.key == pygame.K_3: #negro
					is_inside = myCircle.collidepoint(500,500) ################3coordenada 3
					if is_inside:
						drawcircle = 0
						nCircles = 0
						score = score + 1
						
						good()
						pygame.draw.circle(fondo,purple,(500,500), 59,5)
						surface.blit(fondo,(0,0))
						pygame.draw.circle(fondo,red,(100,500), 60,4)
						surface.blit(fondo,(0,0))
					else:
						sounds["error"].play()	
						drawcircle = 0
						nCircles = 0
						bad()
				if event.key == pygame.K_4: #rojo
					is_inside = myCircle.collidepoint(700,500) ################3coordenada 4
					if is_inside:
						drawcircle = 0
						nCircles = 0
						score = score + 1
						
						good()
						pygame.draw.circle(fondo,purple,(700,500), 59,5)
						surface.blit(fondo,(0,0))
						pygame.draw.circle(fondo,red,(100,500), 60,4)
						
					
					else:
						sounds["error"].play()
						drawcircle = 0
						nCircles = 0
						bad()

				score = str(score)
				myfont = pygame.font.SysFont("arial", 28)
				scoretext = myfont.render(score, 1, (37,222,255))
				surface.blit(scoretext, (200, 656))
				pygame.display.flip()
