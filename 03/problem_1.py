def number_of_houses_delivered_to(instructions):
    x = 0
    y = 0
    grid = {0: {0: 1}}
    first_deliveries = 1

    for step in instructions:
        if step == ">":
            x += 1
        elif step == "<":
            x += -1
        elif step == "^":
            y += 1
        elif step == "v":
            y += -1

        if x not in grid:
            grid[x] = {y: 0}
        elif y not in grid[x]:
            grid[x][y] = 0

        if grid[x][y] == 0:
            first_deliveries += 1

        grid[x][y] += 1

    return first_deliveries

if __name__ == "__main__":
    with open("input.txt", "rb") as handle:
        print number_of_houses_delivered_to(handle.read())
