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


class Simulation:
    def __init__(self, attrs):
        self.Intersections = attrs[0]
        self.Roads = attrs[1]
        self.Cars = attrs[2]
        self.info = attrs[3]

    def Step(self):
        theAlgorithm(self.Intersections)
        for road in self.Roads:
            road.updateCars()
        for intersection in self.Intersections:
            intersection.stepForwardsLights()

    def getReachedEndPercentage(self):
        length = float(len(self.Cars))
        num = 0.0
        for car in self.Cars:
            if car.hasReachedDestination():
                num += 1
        return (float(num) / float(length)) * 100

    def run(self):
        print(self.info.D)
        for i in range(self.info.D):
            self.Step()
        return self.Intersections


def ChooseRoad(intersection):
    chosenRoad = intersection.incoming[0]
    highestHeuristic = 2 ^ 32 - 1
    for road in intersection.incoming:
        heuristic = 0
        for otherroad in intersection.incoming:
            if (otherroad != road):
                heuristic += len(road.queue)

        if heuristic < highestHeuristic:
            chosenRoad = road

    return chosenRoad


def theAlgorithm(intersections):

    for intersection in intersections:
        chosenRoad = ChooseRoad(intersection)

        added = False
        # print(intersection.schedule)
        for item in intersection.schedule:
            # print(chosenRoad.Name, item.Road.Name)
            if (chosenRoad == item.Road):  # if chosen before
                # if current is the last in schedule
                if (item == intersection.schedule[-1]):
                    oldCommand = intersection.schedule[-1]
                    newCommand = TrafficCommand(
                        chosenRoad, oldCommand.SecondsGreen + 1)
                    intersection.schedule[-1] = newCommand
                    added = True
                else:
                    added = True
                    break

        if added == False:
            # print("Adding")
            intersection.schedule.append(TrafficCommand(chosenRoad, 1))
