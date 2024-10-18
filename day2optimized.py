def day2optimized(puzzle):
    bag = {"red" : 12, "green" : 13, "blue" : 14}
    sum_of_id = 0
    sum_of_power = 0

    for line in puzzle:
        game_id, colors = line.strip().split(":")
        game_id = int(game_id.split()[1])
        colors = colors.split(";")
        possible = True
        max_of_colors = {"red" : 0, "green" : 0, "blue" : 0}

        for results in colors:
            colors = results.split(",")
            for color in colors:
                count, color = (int(char) if char.isdigit() else char for char in color.split())
                if bag[color] < count:
                    possible = False
                max_of_colors[color] = max(max_of_colors[color], count)
        if possible:
            sum_of_id += game_id
        sum_of_power += max_of_colors["red"] * max_of_colors["green"] * max_of_colors["blue"]

    print("(Part 1) Number of possible games: " + str(sum_of_id))
    print("(Part 2) Sum of powers: " + str(sum_of_power))

def main():
    puzzle = open("day2.txt", "r")
    day2optimized(puzzle)
    puzzle.close()

if __name__ == '__main__':
    main()