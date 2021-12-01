increase_score = 0
with open('01.txt', 'r') as file:
    numbers = list(map(int, file.readlines()))

for i in range(len(numbers)):
    if numbers[i] > numbers[(i - 1)]:
        increase_score += 1
print(increase_score)

increase_score = 0
for i in range(len(numbers) - 3):
    first_sum = numbers[i] + numbers[i + 1] + numbers[i + 2]
    second_sum = numbers[i + 1] + numbers[i + 2] + numbers[i + 3]
    if first_sum < second_sum:
        increase_score += 1
print(increase_score)
