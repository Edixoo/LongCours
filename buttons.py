
import pygame

pygame.init()

class Button():
	def __init__(self, position, taille, text_input, screen, text_taille) -> None:
		self.image = pygame.image.load("./images/bouton.png")
		button_surface = pygame.transform.scale(self.image, taille)
		self.image = button_surface
		self.x_pos = position[0]
		self.y_pos = position[1]
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.font = pygame.font.SysFont("Arial", text_taille)
		self.text = self.font.render(self.text_input, True, "black")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.ecran = screen

	def display(self):
		self.ecran.blit(self.image, self.rect)
		self.ecran.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return 1
		return 0

	
	def update(self, position, color):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, color)
		else:
			self.text = self.font.render(self.text_input, True, "black")

class Acheter(Button):
	def __init__(self, position, screen) -> None:
		super().__init__(position, [250, 100], "Acheter", screen, 20)

class Cancel(Button):
	def __init__(self, x_pos, y_pos, screen) -> None:
		super().__init__([x_pos, y_pos], [100,50], "Annuler", screen, 20)
		
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return 1
		return 0

	def update(self, position, color):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, color)
		else:
			self.text = self.font.render(self.text_input, True, "black")