from adventminer import AdventMiner

with open("input.txt", "rb") as handle:
    seed = handle.read()
    a = AdventMiner(seed.strip())
    n = a.run()
    print n
