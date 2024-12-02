with open('Day1\locationIDlists.txt', 'r') as myfile:
    leftSide = []
    rightSide = []
    for line in myfile.readlines():
        splitLine = line.split()
        leftSide.append(int(splitLine[0]))
        rightSide.append(int(splitLine()[1]))
leftSide.sort()
rightSide.sort()

# Part 1
difference = 0
for index in range(len(leftSide)):
    difference += abs(leftSide[index] - rightSide[index])
print(difference)

# Part 2
similarityScore = 0
for leftItem in leftSide:
    similarityScore += (leftItem * rightSide.count(leftItem))
print(similarityScore)