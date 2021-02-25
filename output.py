

def filterIntersections(intersections):
    ret = []
    for i in intersections:
        if len(i.schedule) != 0:
            ret.append(i)
    return ret

# Will read the schedule from the intersections
# @param nameOfOutput should be the file name with no extension


def WriteOutput(listOfIntersections, nameOfOutput):
    file = open(nameOfOutput + ".txt", "w")
    filteredIntersections = filterIntersections(listOfIntersections)
    file.write(str(len(listOfIntersections)) + "\n")

    for intersection in filteredIntersections:
        file.write(str(intersection.intersectionNumber) + "\n")
        file.write(str(len(intersection.schedule)) + "\n")

        for sched in intersection.schedule:
            line = sched.Road.Name + " " + str(sched.SecondsGreen) + "\n"
            file.write(line)

    file.close()
    print(nameOfOutput + ".txt has been written out")


print("Output is imported")
