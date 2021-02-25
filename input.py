import sys
from algorithm import *


class SimulationInfo:
    def __init__(self, line):
        firstLine = line.split(" ")
        print(firstLine)
        self.D = int(firstLine[0])       # duration of simulation
        self.I = int(firstLine[1])       # number of intersections
        self.S = int(firstLine[2])       # Number of streets
        self.V = int(firstLine[3])       # number of cars
        self.F = int(firstLine[4])       # bonus points, trim of \n


def readinput(filename):
    roads = []

    lines = open(filename, "r").readlines()
    info = SimulationInfo(lines[0])

    lineOn = 1

    intersections = []
    for i in range(info.I):
        intersections.append(Intersection(i))

    for i in range(info.S):
        street = lines[lineOn].split(" ")
        lineOn += 1
        B = int(street[0])  # leaving intersection
        E = int(street[1])  # going to intersection

        streetName = street[2]
        L = int(street[3])  # length

        r = Road(B, E, L, streetName)
        roads.append(r)

        intersections[B].outgoing.append(r)
        intersections[E].incoming.append(r)

    cars = []
    for i in range(info.V):
        cars.append(Car(lines[lineOn], roads))
        lineOn += 1

    # for i in intersections:
    #     i.setupSchedule()

    return (intersections, roads, cars, info)


def main():
    print("mad clever shit bro")

    for i, arg in enumerate(sys.argv):
        if(i > 0):
            print("===== RUNNING ON " + arg + " =====\n")
            sim_info = readinput(arg)  # g = (V,E)
            sim_result = Simulation(sim_info).run()

            outputname = arg.split(".")[0] + "_output"
            WriteOutput(sim_result, outputname)

    print("end of mad clever shit bro")


main()
