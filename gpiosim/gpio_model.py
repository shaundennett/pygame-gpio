import pygame
import time
import math
from gpiosim import gpio
class gpio_model():
    def __init__(self):
        ''' sets up the pins'''


        self.i_am_doing = 0

        self.pins = {}
        self.pins['PIN_01'] = gpio.gpio_3v(1, '3.3v')
        self.pins['PIN_02'] = gpio.gpio_5v(2, '5v')
        self.pins['PIN_03'] = gpio.gpio_pin(3, 'GPIO2')
        self.pins['PIN_04'] = gpio.gpio_5v(4, '5v')
        self.pins['PIN_05'] = gpio.gpio_pin(5, 'GPIO3')
        self.pins['PIN_06'] = gpio.gpio_gnd(6, 'GND')
        self.pins['PIN_07'] = gpio.gpio_pin(7, 'GPIO4')
        self.pins['PIN_08'] = gpio.gpio_pin(8, 'GPIO14')
        self.pins['PIN_09'] = gpio.gpio_gnd(9, 'GND')
        self.pins['PIN_10'] = gpio.gpio_pin(10, 'GPIO15')
        self.pins['PIN_11'] = gpio.gpio_pin(11, 'GPIO17')
        self.pins['PIN_12'] = gpio.gpio_pin(12, 'GPIO18')
        self.pins['PIN_13'] = gpio.gpio_pin(13, 'GPIO27')
        self.pins['PIN_14'] = gpio.gpio_gnd(14, 'GND')
        self.pins['PIN_15'] = gpio.gpio_pin(15, 'GPIO22')
        self.pins['PIN_16'] = gpio.gpio_pin(16, 'GPIO23')
        self.pins['PIN_17'] = gpio.gpio_3v(17, '3v')
        self.pins['PIN_18'] = gpio.gpio_pin(18, 'GPIO24')
        self.pins['PIN_19'] = gpio.gpio_pin(19, 'GPIO10')
        self.pins['PIN_20'] = gpio.gpio_gnd(20, 'GND9')
        self.pins['PIN_21'] = gpio.gpio_pin(21, 'GPIO25')
        self.pins['PIN_22'] = gpio.gpio_pin(22, 'GPIO25')
        self.pins['PIN_23'] = gpio.gpio_pin(23, 'GPIO11')
        self.pins['PIN_24'] = gpio.gpio_pin(24, 'GPIO8')
        self.pins['PIN_25'] = gpio.gpio_gnd(25, 'GND')
        self.pins['PIN_26'] = gpio.gpio_pin(26, 'GPIO7')
        self.pins['PIN_27'] = gpio.gpio_pin(27, 'GPIO0')
        self.pins['PIN_28'] = gpio.gpio_pin(28, 'GPIO1')
        self.pins['PIN_29'] = gpio.gpio_pin(29, 'GPIO5')
        self.pins['PIN_30'] = gpio.gpio_gnd(30, 'GND')
        self.pins['PIN_31'] = gpio.gpio_pin(31, 'GPIO6')
        self.pins['PIN_32'] = gpio.gpio_pin(32, 'GPIO12')
        self.pins['PIN_33'] = gpio.gpio_pin(33, 'GPIO13')
        self.pins['PIN_34'] = gpio.gpio_gnd(34, 'GND')
        self.pins['PIN_35'] = gpio.gpio_pin(35, 'GPIO19')
        self.pins['PIN_36'] = gpio.gpio_pin(36, 'GPIO16')
        self.pins['PIN_37'] = gpio.gpio_pin(37, 'GPIO26')
        self.pins['PIN_38'] = gpio.gpio_pin(38, 'GPIO20')
        self.pins['PIN_39'] = gpio.gpio_gnd(39, 'GND')
        self.pins['PIN_40'] = gpio.gpio_pin(40, 'GPIO21')
        self.component = gpio.component("template", 0, 50, 500)

        self.all_components = []
        self.transient_component = None
        self.all_connections = []
        self.transient_connection = None



    def toString(self):
        for pin in self.pins.values():
            pin.toString()

    def update(self,screen: pygame.Surface):
        #pygame.draw.circle(screen, (255, 255, 255), (200, 50), 30)
        for pin in self.pins.values():
            pin.update(screen)
        for comp in self.all_components:
            comp.update(screen)

        self.component.update(screen)
        if self.transient_component is not None:
            self.transient_component.update(screen)

    def set_pin_type(self, id: str, type: int):
        self.pins[id].type = type

    def start_create_transient_component(self, x:int, y:int, name:str ):
        self.transient_component = gpio.component("temp",1,x,y)

    def place_transient_component(self):
        self.transient_component.type = 2
        self.transient_component.name = str(len(self.all_components)+1)
        self.all_components.append(self.transient_component)
        self.abandon_transient_component()


    def abandon_transient_component(self):
        self.transient_component = None

    def component_collision(self) -> bool:
        for comp in self.all_components:
            if comp.is_overlapping(self.transient_component) == True:
                return True
        return False

    def check_connectors(self,x:int,y:int) -> gpio.Connector:
        for comp in self.all_components:
            result = comp.check_connector(x,y)
            if type(result) == gpio.Connector:
                return result

        for pin in self.pins.values():
            result = comp.check_connector(x,y)
            if type(result) == gpio.Connector:
                return result

    def create_transient_connection(self,start_connector:gpio.Connector):
        self.transient_connection = gpio.Connection(gpio.Connector(),None)

    def find_connection(self):
        pass

    def get_transient_connection(self):
        pass

    def convert_transient_connection(self):
        pass

    def add_connection(self,connection:gpio.Connection):
        pass

    def remove_connection(self, connection: gpio.Connection):
        pass

