import math
import math as m
from platform import system

import matplotlib.pyplot as plt
import numpy as np
from numpy import integer

#import tkinter as tk

g= float(input('''On which planet/satellite would you want simulate the launch?
         1- Earth
         2- Moon
         3- Mars
         4- Neptune
         5- Venus
         6- Mercury
         7- Saturn
         8- Uranus
         9- Jupiter:
         '''))

def gravity(g):
    if g == "earth":
        return 9.8
    elif g == "moon":
        return 1.16
    elif g == "mars":
        return 3.7
    elif g == "neptune":
        return 11.1
    elif g == "venus":
        return 8.87
    elif g == "mercury":
        return 3.7
    elif g == "saturn":
        return 10.4
    elif g == "uranus":
        return 8.7
    elif g == "jupiter":
        return 24.8
    else:
        return 'planet not listed'

#gravidade em m/s^2
try:
    V0 = float(input('Initial speed of the launch in m/s: '))
    angle = float(input('Angle of the launch in degrees: '))
    h0 = float(input('Initial height of the object in m: '))
    if (V0 <= 0) or angle not in range (0, 91):
        raise ValueError('Please enter valid values for speed and initial angle')
except ValueError as er:
    raise UserWarning('Please enter valid values for speed and initial angle')
except UserWarning as er:
    print(er)
    exit(0)

#sin45 = (math.sqrt(2))/2
angle_rad = m.radians(angle)
V0y = V0 * m.sin(angle_rad)
V0x = V0 * m.cos(angle_rad) #V0x e V0y sao as componentes dos vetores verticais e horizontais durante o lancamento, sendo uma seno e outra cosseno

#print(f'Original: {angle}, depois de converter: {angle_rad}')

#Hmax = (((V0** 2) * (m.sin(angle_rad))** 2) / 2 * g) + h0 # altura maxima que o objeto chega no lancamento, massa e tamanho nao importam e outros fatores estao sendo desconsiderados
Hmax = (((V0y)** 2) / (2 * g) + h0) #usar essa
#Hmax = (V0y** 2)/ (2 * g) #ignorar
#Dmax = (((V0** 2) * 2 * sin45) / g) #ignorar
Dmax = ((V0**2 * m.sin(2 * (angle_rad))) / g) # distancia maxima do lancamento
Tvoo = ((2 * V0y) / g)


#mover aqui

#height = (V0y * Tvoo) - 0.5 * g * Tvoo ** 2   # nao usado

t = np.linspace(0, Tvoo, 1000) # parametros para plotar o grafico
x = V0x * t
y = V0y * t - (0.5 * g * t ** 2)

Hmax_total = max(y)

plt.title('Oblique launch')
plt.xlabel('Distance (m) / Vx ')
plt.ylabel('Height (m) / Vy')
plt.plot(x, y, label='Object trajetory', color='r')
#plt.annotate(xy='Altura inicial: {h0} m')
plt.axhline(Hmax_total, color='b', linestyle='--', label=f'Maximum height: {Hmax_total:.2f} m ')
plt.axvline(Dmax, color='g', linestyle='--', label=f'Maximum distance: {Dmax:.2f} m ')
plt.grid(True)
plt.ylim(bottom=h0, top=Hmax+(Hmax / 20))
plt.legend()
plt.show()

print(f'Maximum height: {Hmax:.2f} meters')
print(f'Maximum distance: {Dmax:.2f} meters')
print(f'Time the object was in the air: {Tvoo:.2f} seconds')

try:
    time_calculate = float(input('Want to calculate speed at a determined instante of time? Enter in seconds: '))
    if isinstance(time_calculate, int):
        raise ValueError('Please enter valid values for speed and initial angle')
except ValueError as er:
#        raise UserWarning('Please enter valid values for speed and initial angle')
#except UserWarning as er:
    print(er)
    exit(0)

Vy_inst = (V0y - g * time_calculate) # velocidade vertical com base no tempo
Vx_inst = V0x # velocidade horizontal nao se altera sem atrito
V_inst = math.sqrt(Vy_inst**2 + Vx_inst**2) #velocidade instantanea em algum momento
print(f'The speed at the moment you have informed was:{V_inst:.2f} m/s ')
