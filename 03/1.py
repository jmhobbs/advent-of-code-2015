from santa import Santa

if __name__ == "__main__":
    santa = Santa()

    with open("input.txt", "rb") as handle:
        while True:
            step = handle.read(1)
            if not step:
                break
            santa.move(step)
        print santa.first_deliveries
