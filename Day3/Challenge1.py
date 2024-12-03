import re

def findMulMatches(file_path):
    pattern = r"mul\(\d+,\d+\)"
    
    with open('Day3\input.txt', 'r') as file:
        content = file.readline()
    matches = re.findall(pattern, content)
    
    return matches

def mul(int1, int2):
    return int1 * int2

matched = findMulMatches()
#print(matched)

total = 0
for pattern in matched:
    total += eval(pattern)
print(total)