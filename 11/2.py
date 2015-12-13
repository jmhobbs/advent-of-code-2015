from pswd import SantaPasswordGenerator, ElfPasswordCheck


spg = SantaPasswordGenerator("hepxxyzz")
while True:
    pwd = spg.iterate()
    if ElfPasswordCheck(pwd):
        print pwd, "VALID"
        break
