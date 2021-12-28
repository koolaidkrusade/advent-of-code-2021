# From https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

# Adapted from a function of a previous assignment in 15-112 at CMU
def formatDataset(filename):
    text = readFile(filename)
    depthMeasurements = []
    
    # Splits the dataset by lines
    for line in text.splitlines():
        measurement = int(line)
        depthMeasurements.append(measurement)

    return depthMeasurements

# Checks to see if a measurement is higher than its previous measurement
# in a list
def increased(depthMeasurements):
    previousMeasurement = depthMeasurements[0]
    increaseCount = 0
    
    for measurement in depthMeasurements:
        if previousMeasurement < measurement:
            increaseCount += 1
        previousMeasurement = measurement
    
    return increaseCount

# Answer to puzzle 1
print(increased(formatDataset('input.txt')))

# Checks to see if a set of 3 measurements is higher than the 
# previous set of 3 measurements in a list
def increasedSets(depthMeasurements):
    previousSum = (depthMeasurements[0] + depthMeasurements[1] + 
                   depthMeasurements[2])
    count = 0

    # The minus 2 accounts for the leftover measurements
    # not able to make a new 3 measurement window
    for measurement in range(len(depthMeasurements) - 2):
        sum = (depthMeasurements[measurement] + 
               depthMeasurements[measurement + 1] + 
               depthMeasurements[measurement + 2])
        
        if previousSum < sum:
            count += 1

        previousSum = sum
    
    return count

# Answer to puzzle 2
print(increasedSets(formatDataset('input.txt')))
        