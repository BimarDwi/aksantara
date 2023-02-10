import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

coord1 = list(map(int, input("First 3D coordinates (x y z): ").split()))
coord2 = list(map(int, input("Second 3D coordinates (x y z): ").split()))

x1, y1, z1 = coord1
x2, y2, z2 = coord2

print("The distance between the two points is:", distance(x1, y1, z1, x2, y2, z2))