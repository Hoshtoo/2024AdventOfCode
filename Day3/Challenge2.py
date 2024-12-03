import re

def mul(int1, int2):
    return int1 * int2

def process_memory(input):
    enabled = True
    total = 0

    instrs = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", input)
    for instr in instrs:
        if instr == "do()":
            enabled = True
        elif instr == "don't()":
            enabled = False
        elif enabled and instr.startswith("mul"):
            total += eval(instr)
    return total

with open('Day3\input.txt', 'r') as myfile:
    result = process_memory(myfile.readline())
print(result)