import pygame
import os as OperatingSystem

pygame.init()

OperatingSystem.environ["SDL_VIDEO_CENTERED"] = '1'
info = pygame.display.Info()

WIDTH = 1024 #info.current_w
HEIGHT = 728 #info.current_h

RES = (WIDTH, HEIGHT)

SCREEN_RES = (info.current_w, info.current_h)
