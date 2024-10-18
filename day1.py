def part1():
    puzzle = open("day1.txt", "r")
    cal_value = 0

    for line in puzzle:
        i, j = 0, 0
        for char in line:
            if char.isdigit():
                i = char
                break
        for char in line[::-1]:
            if char.isdigit():
                j = char
                break
        cal_value += int(str(i + j))

    print("(Part 1) Sum of all calibration values: " + str(cal_value))
    puzzle.close()

def part2():
    puzzle = open("day1.txt", "r")
    cal_value = 0

    for line in puzzle:
        # Converts any integers spelled out into numerical digits
        # To handle edge cases such as "eighthree" where the last letter of the first digit
        # is the first letter of the following digit, integers maintain their first and last
        # letter in the dictionary values.
        values = {"one" : "o1e", "two" : "t2o", "three" : "t3e",
            "four" : "f4r", "five" : "f5e", "six" : "s6x",
            "seven" : "s7n", "eight" : "e8t", "nine" : "n9e"}
        n = 0

        while n <= len(line):
            for k, v in values.items():
                if line[n:n + len(k)] == k:
                    line = line.replace(k, v)
            n += 1

        i, j = 0, 0
        for char in line:
            if char.isdigit():
                i = char
                break
        for char in line[::-1]:
            if char.isdigit():
                j = char
                break
        cal_value += int(str(i + j))

    print("(Part 2) Sum of all calibration values: " + str(cal_value))
    puzzle.close()

def main():
    part1()
    part2()
    

if __name__ == '__main__':
    main()