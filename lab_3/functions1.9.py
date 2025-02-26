import math

def volume_of_sphere():

    radius = float(input())

    volume =  math.pi * (4/3) * radius**3
    
    return volume

print(volume_of_sphere())