puzzle = open("day1.txt", "r")

#Part 1
cal_value = 0
for line in puzzle:
    i = 0
    j = 0
    for char in line:
        if char.isdigit():
            i = char
            break
    for char in line[::-1]:
        if char.isdigit():
            j = char
            break
    cal_value += int(str(i + j))

print("Part 1: " + str(cal_value))
puzzle.close()

#Part 2
puzzle = open("day1.txt", "r")
cal_value = 0
# To handle edge cases such as "eighthree" where the last letter of the first digit
# is the first letter of the following digit, integers maintain their first and last
# letter in the dictionary values.
values = {"one" : "o1e", "two" : "t2o", "three" : "t3e",
          "four" : "f4r", "five" : "f5e", "six" : "s6x",
          "seven" : "s7n", "eight" : "e8t", "nine" : "n9e"}

for line in puzzle:
    n = 0
    # Converts any integers spelled out into numerical digits
    while n <= len(line):
        for k, v in values.items():
            if line[n:n + len(k)] == k:
                line = line.replace(k, v)
        n += 1
    i = 0
    j = 0
    for char in line:
        if char.isdigit():
            i = char
            break
    for char in line[::-1]:
        if char.isdigit():
            j = char
            break
    cal_value += int(str(i + j))

print("Part 2: " + str(cal_value))
puzzle.close()