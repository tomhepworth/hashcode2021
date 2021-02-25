from hello import *

'''


the Simulation class

Step function: Move the simulation forwards by one second
Getter functions:
    Get all roads
    Get all Intersections
    Get all Cars
--------------------------

Every time step:
    Update cars on roads
    Calc heuristic for the intersections
    adjust green lights
    
    O(n!)

repeat until no time left
done

'''

# (intersections, roads, cars, info)


class Simulation:
    def __init__(self, attrs):
        self.Intersections = attrs[0]
        self.Roads = attrs[1]
        self.Cars = attrs[2]
        self.info = attrs[3]

    def Step(self):
        for road in self.Roads:
            road.updateCars()
        for intersection in self.Intersections:
            intersection.stepForwardsLights()


def ChooseRoad(intersection):
    chosenRoad = intersection.incoming[0]
    highestHeuristic = 999999999999999999999999999999999999999999999
    for road in intersection.incoming:
        heuristic = 0
        for otherroad in intersection.incoming:
            if (otherroad != road):
                heuristic += len(road.queue)

        if heuristic < highestHeuristic:
            chosenRoad = road

    return chosenRoad


def theAlgorithm(simulation_info):
    # G = (V,E) = (Intersections,Roads) - John would be proud
    graph = simulation_info[0]
    simulationTime = simulation_info[3]
    greenLights = []
    for intersection in graph[0]:
        chosenRoad = ChooseRoad(intersection)
        intersection.green = chosenRoad  # set the road with lowest heuristic to green
        greenLights.append(chosenRoad)

        oldCommand = intersection.schedule.pop()
        newCommand = TrafficCommand()
