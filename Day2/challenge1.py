with open('Day2\\reports.txt', 'r') as myfile:
    reports = myfile.readlines()

def checkSafe(splitReport):
    direction = ''
    for index in range(len(splitReport)-1):
        curr = int(splitReport[index])
        nextOne = int(splitReport[index+1])
        if curr < nextOne:
            if direction == '':
                direction = 'increasing'
            elif direction == 'decreasing':
                return False
        else:
            if direction == '':
                direction = 'decreasing'
            elif direction == 'increasing':
                return False
        if 0 < abs(curr - nextOne) <= 3:
            continue
        else:
            return False
    return True

safe = 0
for report in reports:
    if checkSafe(report.split()):
        safe += 1
print(safe)