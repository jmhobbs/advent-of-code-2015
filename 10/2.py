from looksay import LookAndSay

ls = LookAndSay("1321131112")
for i in xrange(0, 50):
    ls.iterate()
print len(ls.start)
