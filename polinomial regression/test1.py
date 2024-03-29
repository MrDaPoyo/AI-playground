from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = [8,4,8,8,3,9]

mymodel = np.poly1d(np.polyfit(x, y, 3))
print(mymodel)

myline = np.linspace(0, 5, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
plt.savefig('plot.png')