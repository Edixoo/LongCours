
import pygame
import sys

pygame.init()
main_font = pygame.font.SysFont("cambria", 50)

class Button():
	def __init__(self, x_pos, y_pos, text_input, screen) -> None:
		self.image = pygame.image.load("./images/button.png")
		button_surface = pygame.transform.scale(self.image, (400, 150))
		self.image = button_surface
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)); self.ecran = screen

	def update(self):
		self.ecran.blit(self.image, self.rect)
		self.ecran.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position, color):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, color)
		else:
			self.text = main_font.render(self.text_input, True, "white")

class Acheter(Button):
	def __init__(self, x_pos, y_pos, screen) -> None:
		super().__init__(x_pos, y_pos, "Acheter", screen)

		fond_image=pygame.image.load("./images/button.png")
		fond_surface=pygame.transform.scale(fond_image,(750,750))
		self.fond=fond_surface
		self.rectfond= self.image.get_rect(center=(750, 750))

		self.accept=Button(300,800, "Valider", screen)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.ecran.blit(self.fond, self.rectfond)
			self.accept.update()