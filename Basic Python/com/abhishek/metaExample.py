from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# x= np.linspace(0,5,20)
# y = x ** 2
# figure()
# plot(x,y,'r')
# show()
# close()

figure("my graph")
plot([2,3,4,5],[5,10,15,20],'r')
xlabel('x')
ylabel('y')
show()
title("my wonderful graph")
close()

fig =plt.figure()

