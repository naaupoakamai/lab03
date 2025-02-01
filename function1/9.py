import math

def volume_ball(r):
    return (4/3) * math.pi * (r ** 3)

r = int(input('R? '))
print(f"Объем равен {volume_ball(r)}")
