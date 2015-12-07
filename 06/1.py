from grid import LightGrid

lg = LightGrid()

with open("input.txt", "rb") as handle:
    for line in handle:
        lg.parse_instruction(line)

print "Lights on: %d" % lg.lights_on()
