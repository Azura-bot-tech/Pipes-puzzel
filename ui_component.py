import pygame
import os
import color

class Pipe:

   def __init__(self, display_surface, imageName, location) -> None:
      self.display_surface = display_surface
      self.location = location
      self.imageName = imageName
      self.image = None
      self.load()
      self.angle = 0
      self.pumped = False

   def load(self):
      self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'images',self.imageName +'.png'))
      self.image = pygame.transform.scale(self.image, (50,50))
   
   def display(self):
      self.display_surface.blit(self.image, self.location)
      empty_rect = pygame.Rect(self.location[0] , self.location[1], 50, 50)
      pygame.draw.rect(self.display_surface, color.gray, empty_rect, 1) 

   
   def rotate(self):
      '''
      Quay một góc 90
      '''
      self.angle -= 90
      self.angle %= 360
      self.image = pygame.transform.rotate(self.image, self.angle)
      self.display_surface.blit(self.image, self.location)
   
   def pumpWater(self):
      '''
      Chuyển ống thành ống có nước
      '''
      if '-' not in self.imageName:
         self.imageName = self.imageName[0:5] + '-water'
      self.load()
      temp = abs(self.angle)
      self.angle = 0
      self.rotatePipe(temp)

   def resetWater(self):
      if '-' in self.imageName:
         self.imageName = self.imageName[0:5]
      self.load()
      temp = abs(self.angle)
      self.angle = 0
      self.rotatePipe(temp)

   def rotatePipe(self, x):
      '''
      Quay một góc cụ thể
      '''
      x = - x
      
      if  x < self.angle:
         self.image = pygame.transform.rotate(self.image, -abs(x - self.angle))
      elif x > self.angle:
         self.image = pygame.transform.rotate(self.image, abs(x - self.angle))
      self.angle = x
      self.display()

class Button:

	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.pressed = False

	def clicked(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
				self.pressed = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.pressed = False

		return action