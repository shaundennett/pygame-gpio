import pygame
import time
import math


class GPIO():
    def __init__(self, pos: int, name: str):
        self.name = name
        self.pos = pos
        self.pin_type = ""
        self.mode = 0
        self.linked_pin = None
        self.xpos = 0
        self.ypos = 0
        self.loc = 0
        self.set_x_and_y()
        self.current_state = 0

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Courier', 12)

    def set_x_and_y(self):

        if self.is_even(self.pos):
            self.xpos = 800
            self.loc = 1
        else:
            self.xpos = 100
            self.loc = 0
        self.ypos = (math.floor((self.pos + 1) / 2) * 22)

    def is_even(self, val) -> bool:
        if (val % 2) == 0:
            return True
        else:
            return False

    def toString(self):
        print(str(self.pos) + " : " + self.name + ": (" + str(self.xpos) + "," + str(self.ypos) + "),  " + str(self.loc))

    def update(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos, self.ypos), 10)
        self.set_pin_colour(screen)
        self.create_label(screen)

    def set_pin_colour(self, screen: pygame.Surface):
        if self.current_state == 5 or self.current_state == 3 or self.current_state == 1:
            pygame.draw.circle(screen, (200, 0, 0), (self.xpos, self.ypos), 8)
        if self.current_state == -1:
            pygame.draw.circle(screen, (0, 0, 0), (self.xpos, self.ypos), 8)
        if self.current_state == 0:
            pygame.draw.circle(screen, (0, 200, 0), (self.xpos, self.ypos), 8)

    def create_label(self,screen: pygame.Surface):
        textsurface = self.myfont.render(str(self.pos) + ":" + str(self.name), False, (50, 120, 120))

        if self.loc == 0:
            screen.blit(textsurface,(self.xpos - 80, self.ypos - 5))
        else:
            screen.blit(textsurface,(self.xpos + 20, self.ypos - 5))

class gpio_pin(GPIO):
    def __init__(self, pos: int, name: str):
        super().__init__(pos, name)
        self.type = 0
        self.current_state = 0
        self.pin_type = 'gpio'
        self.mode = 0

class gpio_5v(GPIO):
    def __init__(self, pos: int, name: str):
        super().__init__(pos, name)
        self.current_state = 5
        self.pin_type = '5v'
        self.mode = 1

class gpio_3v(GPIO):
    def __init__(self, pos: int, name: str):
        super().__init__(pos, name)
        self.current_state = 3
        self.pin_type = '3v'
        self.mode = 1

class gpio_gnd(GPIO):
    def __init__(self, pos: int, name: str):
        super().__init__(pos, name)
        self.current_state = -1
        self.pin_type = 'gnd'
        self.mode = 0


class component():
    def __init__(self, name:str, type:int, xpos:int, ypos:int):
        self.name = name
        self.conn_in = None
        self.conn_out = None
        self.xpos = xpos
        self.ypos = ypos
        self.pick_x_pos = 0
        self.pick_y_pos = 0
        self.component_size = 12
        self.connector_size = 6
        self.connector_relative_loc = (self.component_size) + (self.connector_size)
        self.type = type
    def update(self, screen:pygame.Surface):
        colour = (0,0,0)
        if self.type == 0:
            colour = (255,255,255)
        elif self.type == 1:
            colour = (120, 120, 0)
        elif self.type == 2:
            colour = (0, 255, 0)

        pygame.draw.circle(screen, colour, (self.xpos, self.ypos), self.component_size, 1)
        self.draw_input_connector(colour, screen)
        self.draw_output_connector(colour, screen)
    def is_selected(self,x:int, y:int) -> bool:
        print(str(x) + " " + str(y))

        if self.type == 0 and abs(math.sqrt(pow(self.xpos - x, 2) + pow(self.ypos - y, 2))) <= self.component_size:
            print("IN")
            return True
    def draw_input_connector(self,colour:(), screen:pygame.Surface):
        pygame.draw.circle(screen, colour, (self.xpos , self.ypos - self.connector_relative_loc), self.connector_size, 1)
    def draw_output_connector(self, colour:(), screen: pygame.Surface):
        pygame.draw.circle(screen, colour, (self.xpos , self.ypos + self.connector_relative_loc), self.connector_size)

    def set_position(self,x:int,y:int):
        self.xpos = x
        self.ypos = y


