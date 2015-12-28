import reindeerrace


with open('input.txt', 'rb') as handle:
    race = reindeerrace.ReindeerRace()
    for line in handle:
        race.add_reindeer(line)
    print race.race_new_scoring(2503)
