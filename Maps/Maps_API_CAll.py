import pygame
import requests
import sys
import os
from map import get_map, bbox
 
response = None
try:
    args = ["X coordinate: ", "Y coordinate: ", "Zoom: "]
    args = list(map(lambda x: int(input(x)), args))
    args.append('tmp.png')
    map_file = get_map(x=args[0],y=args[1],zoom=args[2],filename=args[3])
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)
 
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((450, 450))
# Рисуем картинку, загружаемую из только что созданного файла.

screen.blit(pygame.image.load(args[3]), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
running = True
args[2] = int(args[2])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            print(args[2])
            if event.key == 280: 
                if args[2] != 20:
                    args[2] += 1
            if event.key == 281:
                if args[2] != 0:
                    args[2] -= 1
            if event.key == 273:
                bbox([[args[0],args[1]+2],[[args[0],args[1]+4]]])
    args[2] = abs(args[2])
    map_file = get_map(args[0],args[1],args[2],args[3])
    screen.blit(pygame.image.load(args[3]), (0, 0))
    pygame.display.flip()
    pass
pygame.quit()
 
# Удаляем за собой файл с изображением.
os.remove(args[3])