"""
    Шарик отскакивает от стенок.

    Используется библиотека PyGame.

    Используется технология фиксации fps, что обеспечивает
    движение шарика с одинаковой скоростью на разных компьютерах.

    Значение fps печатается.

    Файл ball.gif должен быть в папке с файлом pygame_ball.py
"""

# import my_module
import sys
import pygame
# import time

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600

speed = [1, 1]
#
# # BLACK = (0, 0, 0)
WHITE = (255,255,255)

screen = pygame.display.set_mode(SIZE)

ball = pygame.image.load("ball.jpg")

ballrect = ball.get_rect()
#
# MAX_FPS = 60
# FRAMETIME = 1 / MAX_FPS  # of a second
#
# time1 = time.time()
#
# fps = 0
# old_sec = 0
#
while True:

#
#     time2 = time.time()
#
#     if time2 - time1 > FRAMETIME:
#

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
#
         ballrect = ballrect.move(speed)

         if ballrect.left < 0 or ballrect.right > WIDTH:
             speed[0] = -speed[0]

         if ballrect.top < 0 or ballrect.bottom > HEIGHT:
             speed[1] = -speed[1]

         screen.fill(WHITE)

         screen.blit(ball, ballrect)

         pygame.display.flip()
#
#         fps += 1
#
#         time1 += FRAMETIME
#
#     time.sleep(0.0005)
#
#     ltime = time.localtime()
#     if ltime.tm_sec != old_sec:
#         old_sec = ltime.tm_sec
#         print(fps)
#         fps = 0
