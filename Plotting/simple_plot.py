import datetime
import time
import random
import matplotlib.pyplot as plt

# make up some data

t = time.time()


x = [datetime.datetime.now() + datetime.timedelta(days=i) for i in range(60)]
y = [i + random.gauss(0, 1) for i, _ in enumerate(x)]

# plot
plt.plot(x, y)
# beautify the x-labels
plt.gcf().autofmt_xdate()


plt.show()
