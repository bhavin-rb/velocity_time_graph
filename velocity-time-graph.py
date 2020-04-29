import matplotlib.pyplot as plt
'''
Plot a Velocity-Time graph of a car as per below table. Find the following from the graph:

Acceleration of the car
Deceleration of the car
Total distance covered by the car

time = 0, 5, 10, 15, 20, 25, 30, 35, 40
velocity = 0, 10, 20, 20, 20, 15, 10, 5, 0
'''


def velocityTimeGraph():
    time_distance = zip([0, 5, 10, 15, 20, 25, 30, 35, 40], [0, 10, 20, 20, 20, 15, 10, 5, 0])
    # print(*time_distance)
    x, y = zip(*time_distance)  # This is like calling zip((0, 0), (5, 10), (10, 15, (15, 20), (20, 20), (25, 20),
    # (30, 15), (35, 5), (40, 0))
    print(x)
    print(y)
    # plotting the velocity-time graph
    plt.plot(x, y)
    plt.gca().fill_between(x, y)
    plt.xlabel('Time(seconds)')
    # add a label to the y axis
    plt.ylabel('Velocity(m/s)')
    # add a title
    plt.title('Velocity-time Graph of Uniform Motion')
    return plt.show()


'''
Acceleration is change in velocity over time. In other words it is the slope of the the triangle formed between 
time 0s and 10s, having vertices (height) of 20.
'''


def acceleration():
    # acceleration = change in velocity / time
    # From the plotted graph, v0 = 0m/s, v1 = 20 m/s, t0 = 0s, s and t1 = 10s.
    v0 = 0
    t0 = 0
    v1 = 20
    t1 = 10
    # for printing superscript for S.I Unit of acceleration
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    # acceleration in uniform motion formula (equation)
    a = (v1 - v0) / (t1 - t0)
    # f"Acceleration of the car is {a}" + " " f"m/s2".translate(sup)
    return print("Acceleration is : " + str(a) + "m/s2".translate(sup))


'''
Deceleration is negative acceleration. In other words it is the slope of the the triangle formed between 
time 20s and 40s, having vertices (height) of 20.  It is slope of the triangle, which is negative.
'''


def deceleration():
    # Deceleration  = negative acceleration
    # From the plotted graph, v0 = 20m/s, v1 = 0 m/s, t0 = 20s, s and t1 = 40s.
    v0 = 20
    t0 = 20
    v1 = 0
    t1 = 40
    # for printing superscript for S.I Unit of acceleration
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    # acceleration in uniform motion formula (equation)
    a = (v1 - v0) / (t1 - t0)
    # f"Acceleration of the car is {a}" + " " f"m/s2".translate(sup)
    return print("Deceleration is : " + str(a) + "m/s2".translate(sup))


'''
Total Distance travelled by a Car is equal to the area under the graph. The plot (graph) is a Trapezium and area of 
Trapezium is given by:
area = (a+b)h/2
'''

def distanceTravelled():
    # lets define our variables
    a = 20 - 10  # from 10s to 20s
    b = 40 - 0  # from 0s to 40s
    h = 20

    area = ((a + b) * h) / 2
    return print("Distance travelled by the car is : " + str(area) + "m")


velocityTimeGraph()
acceleration()
deceleration()
distanceTravelled()
