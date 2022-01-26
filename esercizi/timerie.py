import time,random

inizioDelProgramma = time.time()

for i in range (10000000000):
    random.random()

fineDelProgramma = time.time()


print("il codice è stato eseguito in %s" % (fineDelProgramma - inizioDelProgramma))