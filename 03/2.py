from santa import SantaAndRoboSanta

if __name__ == "__main__":
    santa = SantaAndRoboSanta()

    with open("input.txt", "rb") as handle:
        instruction = 0
        while True:
            step = handle.read(1)
            if not step:
                break
            santa.move(step)
        print santa.first_deliveries
