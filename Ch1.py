import random
import math

LIST_A = [(1,1),(2,1),(3,1)]

def nearest_neighbor(points):
    # Pick a random starting point
    p0 = random.choice(points)
    points.remove(p0)
    path = [{"dist":None, "point":p0}]
    i = 0

    # cycle through list to find nearest point, add it to path, remove it from list, repeat until empty
    while(len(points) > 0):
        i = i + 1
        nearest = find_nearest(path[-1]["point"],points)
        points.remove(nearest["point"])
        path.append(nearest)

    # connect back to p0 (calculate distance between last point found and p0)
    final_dist = dist(len(p0),p0,path[-1]["point"])
    path[0]["dist"] = final_dist

    return path


def find_nearest(pointA, lst):
    nearest = {
        "dist": float('inf'),
        "point": None
    }
    for pointB in lst:
        p_dist = dist(len(pointA),pointA,pointB)
        if (p_dist < nearest["dist"]):
            nearest["dist"] = p_dist
            nearest["point"] = pointB
    return nearest


def dist(dimensions, pointA, pointB):
    if len(pointA) != len(pointB):
        raise ValueError("Both points must have same number of dimensions")
    if len(pointA) != dimensions:
        raise ValueError("Number of dimensions must match the points")

    return math.sqrt(sum((pointA[i] - pointB[i])**2 for i in range(dimensions)))

result = nearest_neighbor(LIST_A)
print(result)


