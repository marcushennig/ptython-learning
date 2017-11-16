from time import gmtime
from time import time
from time import strftime

t = 1510840260
t2 = int(time())
print(strftime('%d.%m.%Y', gmtime(t)))
