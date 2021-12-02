horizontal = 0
depth = 0
with open('02.txt', 'r') as file:
    instructions = file.readlines()

for instruction in instructions:
    instruction = instruction.strip().split(' ')
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
    if instruction[0] == 'up':
        depth -= int(instruction[1])
    if instruction[0] == 'down':
        depth += int(instruction[1])
print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0
for instruction in instructions:
    instruction = instruction.strip().split(' ')
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        depth += int(instruction[1]) * aim
    if instruction[0] == 'up':
        aim -= int(instruction[1])
    if instruction[0] == 'down':
        aim += int(instruction[1])
print(horizontal * depth)
