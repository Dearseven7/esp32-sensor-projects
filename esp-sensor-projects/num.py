from machine import Pin
from time import sleep
leda = Pin(21,Pin.OUT)
ledb = Pin(22,Pin.OUT)
ledc = Pin(16,Pin.OUT)
ledd = Pin(17,Pin.OUT)
lede = Pin(18,Pin.OUT)
ledf = Pin(00,Pin.OUT)
ledg = Pin(05,Pin.OUT)
ledh = Pin(04,Pin.OUT)

leda.value(1)
ledb.value(1)
ledc.value(1)
ledd.value(1)
lede.value(1)
ledf.value(1)
ledg.value(1)
ledh.value(0)


def display_0():
    leda.value(0)
    ledb.value(0)
    ledc.value(0)
    ledd.value(0)
    lede.value(0)
    ledf.value(0)
    ledg.value(1)
def display_1():
    leda.value(1)
    ledd.value(1)
    lede.value(1)
    ledf.value(1)
    ledg.value(1)
    ledh.value(1)

    ledb.value(0)
    ledc.value(0)
def display_2():
    ledc.value(1)
    ledd.value(1)
    ledf.value(1)
        
    leda.value(0)
    ledb.value(0)
    ledg.value(0)
    lede.value(0)
    ledd.value(0)
def display_3():
    lede.value(1)
    ledf.value(1)
        
    leda.value(0)
    ledb.value(0)
    ledg.value(0)
    ledc.value(0)
    ledd.value(0)
def display_4():
    leda.value(1)
    ledd.value(1)
    lede.value(1)
        
    ledb.value(0)
    ledc.value(0)
    ledg.value(0)
    ledf.value(0)
def display_5():
    ledb.value(1)
    lede.value(1)
    
    leda.value(0)
    ledf.value(0)
    ledg.value(0)
    ledc.value(0)
    ledd.value(0) 
def display_6():
    ledb.value(1)

    leda.value(0)
    ledc.value(0)
    ledd.value(0)
    lede.value(0)
    ledf.value(0)
    ledg.value(0)
def display_7():
    ledd.value(1)
    lede.value(1)
    ledf.value(1)
    ledg.value(1)

    leda.value(0)
    ledb.value(0)
    ledc.value(0) 
def display_8():
    leda.value(0)
    ledb.value(0)
    ledc.value(0)
    ledd.value(0)
    lede.value(0)
    ledf.value(0)
    ledg.value(0)
def display_9():
    leda.value(0)
    ledb.value(0)
    ledc.value(0)
    ledd.value(0)
    lede.value(1)
    ledf.value(0)
    ledg.value(0)
'''    
while True:
    num = input('The number you want to light: ')
            
    if num == '0':
        display_0()
        
    if num == '1':
        display_1()

    if num == '2':
        display_2()

    if num == '3':
        display_3()

    if num == '4':
        display_4()

    if num == '5':
        display_5()
    
    if num == '6':
        display_6()

    if num == '7':
        display_7()
        
    if num == '8':
        display_8()
        
    if num == '9':
        display_9()
'''

