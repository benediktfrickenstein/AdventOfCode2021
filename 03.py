with open('03.txt', 'r') as file:
    numbers = [line.strip() for line in file]

gama, epsilion = '', ''
for bit in range(len(numbers[0])):
    bits = [line[bit] for line in numbers]
    gama += str(int(bits.count('1') > bits.count('0')))
    epsilion += str(int(bits.count('0') > bits.count('1')))
gama, epsilion = int(str.encode(gama), 2), int(str.encode(epsilion), 2)
print(gama * epsilion)

nums_oxy, nums_car = numbers.copy(), numbers.copy()
for bit in range(len(nums_oxy[0])):
    bits_oxy = [line[bit] for line in nums_oxy]
    if bits_oxy.count('1') >= bits_oxy.count('0'):
        nums_oxy = [line for line in nums_oxy if line[bit] == '1']
    else:
        nums_oxy = [line for line in nums_oxy if line[bit] == '0']
    if len(nums_oxy) == 1:
        break

for bit in range(len(nums_car[0])):
    bits_car = [line[bit] for line in nums_car]
    if bits_car.count('1') >= bits_car.count('0'):
        nums_car = [line for line in nums_car if line[bit] == '0']
    else:
        nums_car = [line for line in nums_car if line[bit] == '1']
    if len(nums_car) == 1:
        break
nums_oxy, nums_car = int(str.encode(nums_oxy[0]), 2), int(str.encode(nums_car[0]), 2)
print(nums_oxy * nums_car)
