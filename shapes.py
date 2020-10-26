import numpy as np
import matplotlib.pyplot as plt

x1 = [1,3,3,1,1]
y1 = [1,1,3,3,1]

x2 = [1,3]
y2 = [1,3]

plt.plot(x1,y1)
plt.plot(x2,y2, linestyle='dashed')

plt.ylim(0,4)
plt.xlim(0,4)

plt.title('Shape')

plt.show()