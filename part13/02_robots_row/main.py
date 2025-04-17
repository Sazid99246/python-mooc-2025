import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
window.blit(robot, (100, 50))
window.blit(robot, (150, 50))
window.blit(robot, (200, 50))
window.blit(robot, (250, 50))
window.blit(robot, (300, 50))
window.blit(robot, (350, 50))
window.blit(robot, (400, 50))
window.blit(robot, (450, 50))
window.blit(robot, (500, 50))
window.blit(robot, (550, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
