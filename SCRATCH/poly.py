
import gpiosim.gpio as g


pins = {}
pins['PIN_01'] = g.gpio_3v(1, '3.3v')
pins['PIN_02'] = g.gpio_5v(2, '5v')
pins['PIN_03'] = g.gpio_pin(3, 'GPIO2')
pins['PIN_04'] = g.gpio_5v(4, '5v')


components = [g.component("a",1,2,3),g.component("b",1,2,3),g.component("c",1,2,3)]

for data in (components,pins):
    for d in data:
        print(d.name)
