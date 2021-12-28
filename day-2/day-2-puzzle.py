# From https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

# Adapted from a function of a previous assignment in 15-112 at CMU
def calculatePosition(filename, puzzle):
    text = readFile(filename)
    x = 0
    y = 0
    aim = 0

    # Splits the dataset by lines, then the lines by spaces to get the tuple
    # showing the direction and count
    for line in text.splitlines():
        direction, count = line.split()
        count = int(count)

        # For puzzle 1
        if puzzle == 1:
            if direction == 'up':
                y -= count
            
            elif direction == 'down':
                y += count
            
            elif direction == 'forward':
                x += count
        
        # For puzzle 2
        if puzzle == 2:
            if direction == 'up':
                aim -= count
        
            elif direction == 'down':
                aim += count
        
            elif direction == 'forward':
                x += count
                y += aim * count
    
    return x * y

# Answer to puzzle 1
print(calculatePosition('input.txt', 1))

# Answer to puzzle 2
print(calculatePosition('input.txt', 2))