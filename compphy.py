import math

def my_dist_2_points(xy_points, xy):
    """
    Returns an array of distances between xy and the points
    contained in the rows of xy_points

    xy: A list with a single x,y pair, [x,y]
    xy_points: A list of [x,y] pairs.  [[x1,y1], [x2,y2], [xi,yi],..., [xn,yn]]
    """
    d = []
    for xy_point in xy_points:
        dist = math.sqrt(\
            (xy_point[0] - xy[0])**2 + (xy_point[1] - xy[1])**2)
        # sqrt((xi-x)^2 + (yi-y)^2)

        d.append(dist)

    return d
    
'''test = {"val1":2,"val2":2,"val3":8}

for k in test:
    print(k, test[k])
    print(test.items())
    print(test.keys())
    print(test.values())

for k , value in test.items():
    print(k, value)
'''

# a = [1,2,3,4,5,6,7,8,9,10]
# b =["a","b","c","d","e","f","g","h","i","j"]

# zipfunc = zip(b,a)
# print(list(zipfunc))

def have_digit(s):
    for i in s:
        if i.isdigit():
            return print(True)
    return print(False)

have_digit("hello1")

