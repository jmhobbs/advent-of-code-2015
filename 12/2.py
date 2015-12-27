import json
import elfaccounting

with open("input.txt", "rb") as handle:
    doc = json.load(handle)
    numbers = elfaccounting.extract_numbers_from_object(doc, True)
    print "Total:", sum(numbers)
