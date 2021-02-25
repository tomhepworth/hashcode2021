from output import *
import random
random.seed()

print("hello world")

squares = [i * i for i in range(20)]
alphabet = [x for x in 'abcdefghijklmnopqrstuvwxy']


class Car:
    def __init__(self, line, roads):
        splits = line.split(" ")
        self.Route = []
        self.RouteLength = int(splits[0])
        self.CurrentIndex = 0

        for roadName in splits[2:]:
            self.Route.append(roadName)

        # Now add the car to the road
        for road in roads:
            if road.Name == splits[1]:
                road.addCar(self)

    def hasReachedDestination(self):
        return self.currentIndex == len(self.Route) - 1

    def getNextIndex(self):
        toret = self.Route[self.CurrentIndex]
        self.CurrentIndex + turn


class Road:
    def __init__(self, intersectionFrom, intersectionTo, lengthToPass, name):
        self.L = lengthToPass  # L value for this road
        self.From = intersectionFrom
        self.To = intersectionTo
        self.Name = name
        self.queue = []
        self.OnCar = []
        self.OnCarTimeLeft = []

    def addCar(self, car):
        self.OnCar.append(car)
        self.OnCarTimeLeft.append(self.L)

    def updateCars(self):
        # If there are no cars moving on the road, this is irrelevent
        if len(OnCar) == 0:
            return

        # Otherwise update all the positions of the cars
        for i in range(len(self.OnCarTimeLeft)):
            if self.OnCarTimeLeft > 0:
                self.OnCarTimeLeft[i] -= 1

        # If the first car is at the end, pop it. Only it could possibly be at the end
        if self.OnCarTimeLeft[0] == 0:
            car = self.OnCar.pop(0)
            self.OnCarTimeLeft.pop(0)
            self.queue.append(car)

    def hasCarWaiting(self):
        return len(self.queue) > 0

    def removeCar(self):
        car = self.queue.pop(0)
        return car


class TrafficCommand:
    # no proper constructor because idk what to do
    def __init__(self, roadRelevantTo):
        self.Road = roadRelevantTo  # The road name
        # How long the lights are green for
        self.SecondsGreen = random.randint(2, 4)
        # sets it up as random for now


class Intersection:
    def __init__(self, intersectionNumber):
        self.intersectionNumber = intersectionNumber
        self.incoming = []  # Incoming roads
        self.outgoing = []  # Outgoing roads
        self.schedule = []  # List of TrafficCommand
        self.timeOnCurrentLight = 0
        self.currentScheduleIndex = 0

    def stepForwardsLights(self):

        currentOn = self.schedule[self.currentScheduleIndex]
        if currentOn.Road.hasCarWaiting():
            car = currentOn.Road.removeCar()
            if not car.hasReachedDestination():
                # If it needs to keep going somewhere
                nextPlace = car.getNextIndex()
                for road in self.outgoing:
                    if road.Name == nextPlace:
                        road.addcar(car)
                        break

        self.timeOnCurrentLight += 1
        if self.timeOnCurrentLight == self.schedule[self.currentScheduleIndex].SecondsGreen:
            # Update to be on the next part of hte schedule
            self.timeOnCurrentLight = 0
            self.currentScheduleIndex += 1
            # Make sure we don't go out of range
            if self.currentScheduleIndex > len(self.schedule):
                self.currentScheduleIndex = 0

    def setupSchedule(self):
        for income in self.incoming:
            command = TrafficCommand(income)
            self.schedule.append(command)
