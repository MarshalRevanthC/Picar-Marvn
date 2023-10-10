import numpy as np  

y1 = np.linspace(1,10,26, endpoint = True)
y2 = np.linspace(10,1,25, endpoint = True)
jd = np.concatenate((y1, y2), axis=None)
# print(type(y2))
print(len(jd))