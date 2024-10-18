def part1(puzzle):
    mreds = 12
    mgreens = 13
    mblues = 14
    sum_of_id = 0

    for line in puzzle:
        id, colors = line.strip().split(":")
        id = int(id.split()[1])
        colors = colors.split(";")
        possible = True
        for results in colors:
            colors = results.split(",")
            for color in colors:
                count, color = (int(char) if char.isdigit() else char for char in color.split())
                if color == "red" and mreds < count:
                    possible = False
                    break
                if color == "green" and mgreens < count:
                    possible = False
                    break
                if color == "blue" and mblues < count:
                    possible = False
                    break
        if possible:
            sum_of_id += id

    print("Number of possible games: " + str(sum_of_id))

def part2(puzzle):
    sum_of_power = 0
    puzzle = open("day2.txt", "r")
    for line in puzzle:
        id, colors = line.strip().split(":")
        id = int(id.split()[1])
        colors = colors.split(";")
        max_of_colors = {"red" : 0, "green" : 0, "blue" : 0}
        for results in colors:
            colors = results.split(",")
            for color in colors:
                count, color = (int(char) if char.isdigit() else char for char in color.split())
                max_of_colors[color] = max(max_of_colors[color], count)
        sum_of_power += max_of_colors["red"] * max_of_colors["green"] * max_of_colors["blue"]

    print("Sum of powers: " + str(sum_of_power))

def main():
    puzzle = open("day2.txt", "r")
    part1(puzzle)
    part2(puzzle)
    puzzle.close()

if __name__ == '__main__':
    main()