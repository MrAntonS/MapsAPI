import pygame
import requests
import sys
import os
from map import get_map
 
response = None
try:
    x = input().split()
    map_file = get_map(x[0],x[1],x[2],x[3])
    with open(x[3], "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)
 
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.

screen.blit(pygame.image.load(x[3]), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
 
# Удаляем за собой файл с изображением.
os.remove(x[3])