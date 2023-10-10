
# Graphical Representation of numpy.linspace()
import numpy as np
import pylab as p
import matplotlib.pyplot as plt
import array as ar

plt.style.use('_mpl-gallery')
# Start = 0
# End = 2
# Samples to generate = 15
x = np.linspace(50, -50, 101, endpoint = True,dtype = int)
x1 = np.linspace(50, 0, 51, endpoint = True,dtype = int)
x2 = np.linspace(0, -50, 51, endpoint =True,dtype = int)
x_arr = np.concatenate((x1, x2),axis=None)
x_list = np.array(x_arr)
y1 = np.linspace(1,10,51, endpoint = True,dtype = int)
y2 = np.linspace(10,1,51, endpoint = True,dtype = int)
y_arr = np.concatenate((y1, y2), axis=None)
y_list = np.array(y_arr)
# x_arr = ar.array('i', x)
# y_arr = ar.array('i', y)
# print(len(x_arr))
# print((x_arr))


# x_id = np.where( x_arr == 50)[0]
ind = x_list.index(50)
print(ind)
# print(y_list[ind])
# print(type(np.int_(y_arr[x_id])))
# for index, x in enumerate(x):
#        print(f'{x} { y[index] }')
# print()
# print(y[x_id])
# plt.title("direction to speed curve")
  
# # plot scatter plot with x and y data
# plt.scatter(x, y)
  
# # plot with x and y data
# plt.plot(x, y)

# plt.show()