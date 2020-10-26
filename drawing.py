import numpy as np
import matplotlib.pyplot as plt

def create_plot(ptype):
    x = np.arange(-10, 10, 0.01)

    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4

    return(x,y)

plt.style.use('fivethirtyeight')
fig = plt.figure()

plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)
# From geeksforgeeks page:
# If the values of the three parameters are less than 10, 
# the function subplot can be called with one int parameter,
# where the hundreds represent ‘nrows’, the tens represent ‘ncols’ 
# and the units represent ‘plot_number’. 
# This means: Instead of subplot(2, 3, 4) we can write subplot(234).

x, y = create_plot('linear')
plt1.plot(x,y, color='r')
plt1.set_title('$y_1 = x$')

x, y = create_plot('cubic')
plt2.plot(x,y, color='b')
plt2.set_title('$y_2 = x^3$')

x, y = create_plot('quadratic')
plt3.plot(x,y, color='g')
plt3.set_title('$y_3 = x^2$')

x, y = create_plot('quartic')
plt4.plot(x,y, color='k')
plt4.set_title('$y_4 = x^4$')

fig.subplots_adjust(hspace=.5,wspace=.5)

plt.show()