import random
import math

LIST_A = [(1,1),(2,1),(3,1)]

def nearest_neighbor(points):
    # Pick a random starting point
    p0 = random.choice(points)
    points.remove(p0)
    path = [p0]
    i = 0

    # cycle through list to find nearest point, add it to path, remove it from list, repeat until empty
    while(len(points) > 0):
        i = i + 1
        nearest = find_nearest(path[-1],points)
        points.remove(nearest)
        path.append(nearest)

    # connect beginning to end
    path.append(path[0])

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
    return nearest["point"]

def closest_pair(points):
    # convert to a list of lists to represent individual chains
    cList = list(map(lambda p: [p],points))
    
    # Cycle through each list and pair with nearest endpoint in other lists 
    # After pairing, add both points to a new list as its own chain, a new list of lists. Repeat until 0 or 1 item left. If 1 left, append last item to list of lists 
    # Repeat until list of lists contains one single list
    while (len(cList) > 1):
        cList = connect_chains(cList)

    # connect beginning to end
    cList[0].append(cList[0][0])

    return cList[0]
        

def connect_chains(chain_list):
    cList = []
    while (len(chain_list) > 1):
        c0 = random.choice(chain_list)
        chain_list.remove(c0)
        c1 = find_nearest_chain(c0,chain_list)
        chain_list.remove(c1) if c1 in chain_list else chain_list.remove(c1[::-1])
        c0.extend(c1)
        cList.append(c0)
    # Handle straggling chain if there was odd number of chains
    if (len(chain_list) > 0):
        cList.append(chain_list[0])
    return cList


def find_nearest_chain(chain,chain_list):
    endpoint1 = chain[-1]
    nearest = {
        "dist": float('inf'),
        "chain": None
    }
    for c in chain_list:
        dist_endpoint1 = dist(len(endpoint1),endpoint1,c[0])
        dist_endpoint2 = dist(len(endpoint1),endpoint1,c[-1])
        if (dist_endpoint1 < nearest["dist"]):
            nearest["dist"] = dist_endpoint1
            nearest["chain"] = c
        if (dist_endpoint2 < nearest["dist"]):
            nearest["dist"] = dist_endpoint2
            nearest["chain"] = c[::-1]
    return nearest["chain"]





def dist(dimensions, pointA, pointB):
    if len(pointA) != len(pointB):
        raise ValueError("Both points must have same number of dimensions")
    if len(pointA) != dimensions:
        raise ValueError("Number of dimensions must match the points")

    return math.sqrt(sum((pointA[i] - pointB[i])**2 for i in range(dimensions)))

# result = nearest_neighbor(LIST_A.copy())
# print(result)

def generate_point_list(dimensions,num_points,min_val,max_val):
    # num_points = random.randint(minPoint,maxPoints)
    points = set()
    while len(points) < num_points:
        points.add(generate_point(dimensions,min_val,max_val))
    return list(points)

def generate_point(dimensions,min,max):
    return tuple(random.randint(min,max) for _ in range(dimensions))


def get_path_dist(dimensions,path):
    total_dist = 0
    for i in range(len(path)-1):
        total_dist += dist(dimensions,path[i],path[i+1])
    return total_dist


# for _ in range(5):
#     print(generate_point_list(4,5,10,-5,5))


DIMENSIONS = 4
NUM_POINTS = 10
MIN_VAL = -8
MAX_VAL = 8
ITERATIONS = 100
print("CLOSEST PAIR")
c_dists = []
for _ in range(ITERATIONS):
    result = closest_pair(generate_point_list(DIMENSIONS,NUM_POINTS,MIN_VAL,MAX_VAL))
    # print(result)
    path_dist = get_path_dist(DIMENSIONS,result)
    c_dists.append(path_dist)
    # print("dist: " + str(path_dist))

print("")
print("NEAREST NEIGHBOR")
p_dists = []
for _ in range(ITERATIONS):
    result = nearest_neighbor(generate_point_list(DIMENSIONS,NUM_POINTS,MIN_VAL,MAX_VAL))
    # print(result)
    path_dist = get_path_dist(DIMENSIONS,result)
    p_dists.append(path_dist)
    # print("dist: " + str(path_dist))

print("Average closest pair: " + str(sum(c_dists) / len(c_dists)))
print("Average nearest neighbor: " + str(sum(p_dists) / len(p_dists)))


