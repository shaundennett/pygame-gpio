from typing import Union

import pygame
from pygame import Surface
from pygame.locals import *
import sys
from gpiosim.gpio import Connector

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from pygame.surface import SurfaceType
from gpiosim import gpio
from gpiosim import gpio_model

class pin_display():


    def __init__(self):

        self.NOTHING = 0
        self.PLACING_COMPONENT = 1
        self.SELECTING_COMPONENT = 2
        self.DROPPING_COMPONENT = 3
        self.SELECTED_CONNECTOR = 4

        self.COMPONENT_ZONE = 4
        self.MAIN_PANEL_ZONE = 3
        self.GPIO_ZONE = 1
        self.TRASH_ZONE = 2
        self.zone = 0

        self.state = 0

        pygame.init()
        self.DISPLAY = pygame.display.set_mode((1000, 600))
        self.model = gpio_model.gpio_model()
        self.model.toString()
        self.runner()


    def runner(self):
        while True:
            #pygame.draw.circle(self.DISPLAY, (255, 255, 255), (200, 50), 30)
            for event in pygame.event.get():

                x, y = pygame.mouse.get_pos()
                zone = self.check_zone(x, y)

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == self.NOTHING:
                    if zone == self.COMPONENT_ZONE:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # check if a component is to be created
                            #could be creating a new transient component or moving an existing one
                            if self.model.component.is_selected(x, y):
                                self.model.start_create_transient_component(x,y,"trans")
                                self.state = self.PLACING_COMPONENT
                    elif (zone == self.GPIO_ZONE or zone == self.MAIN_PANEL_ZONE) and event.type == pygame.MOUSEBUTTONDOWN:
                        #Could be
                        #Clicking a link
                        #Clicking and moving a component
                        result = self.model.check_connectors(x, y)
                        if type(result) == Connector:

                            print(result.parent.name)


                if event.type == pygame.MOUSEBUTTONUP and self.state == self.PLACING_COMPONENT and not self.model.component_collision():
                    # check if a component is to be created
                    #could be creating a new transient component or moving an existing one
                    #x, y = pygame.mouse.get_pos()
                    if self.within_bounds(x, y, self.state):
                        self.state = self.NOTHING
                        self.model.place_transient_component()

                if event.type == pygame.MOUSEMOTION and self.state == self.PLACING_COMPONENT:
                    # check if a component is to be created
                    #print("moving")
                    if self.model.transient_component is not None:
                        #x, y = pygame.mouse.get_pos()
                        self.model.transient_component.set_position(x,y)





                self.DISPLAY.fill((0,0,0))
                self.model.update(self.DISPLAY)
                #x, y = pygame.mouse.get_pos()
                iv_font = pygame.font.SysFont('Courier', 12)
                textsurface = iv_font.render(str(x) + ":" + str(y), False, (50, 120, 120))
                self.DISPLAY.blit(textsurface, (10,580))
                textsurface = iv_font.render(str(zone), False, (50, 120, 120))
                self.DISPLAY.blit(textsurface, (100,580))

                pygame.display.update()

    def within_bounds(self, xpos:int, ypos:int, state:int) -> bool:
        if state == self.PLACING_COMPONENT and xpos >= 150 and xpos <= 750 and ypos >=10 and ypos <= 450:
            return True
        else:
            return False
    def allowed_action(self,xpos:int, ypos:int):
        if xpos >= 150 and xpos <= 750 and ypos >=10 and ypos <= 450:
            return self.PLACING_COMPONENT

    def check_zone(self,xpos:int, ypos:int) -> int:
        if ypos > 460:
            if xpos > 800:
                return self.TRASH_ZONE
            else:
                return self.COMPONENT_ZONE
        elif xpos > 780 or xpos < 150:
            return self.GPIO_ZONE
        else:
            return self.MAIN_PANEL_ZONE

if __name__ == '__main__':
    pin = pin_display()