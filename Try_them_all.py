import md5

h = '1bb42d555ddf42b48b15e66b31b9810a'
s0 = '4996'
s1 = '4996'.decode('hex')

f = open('dictionary.txt')

for line in f:
  ln = line.strip()

  for p in [
    s0 + ln,
    s1 + ln,
    s0 + ln + s0,
    s1 + ln + s1,
    ln + s0,
    ln + s1
  ]:
    pp = md5.md5(p).hexdigest()
    if pp == h:
      print "password:", ln, "\ndecrypted:", p