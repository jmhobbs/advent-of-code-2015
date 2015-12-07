from grid import VariableBrightnessLightGrid

lg = VariableBrightnessLightGrid()

with open("input.txt", "rb") as handle:
    for line in handle:
        lg.parse_instruction(line)

print "Total brightness: %d" % lg.lights_on()
