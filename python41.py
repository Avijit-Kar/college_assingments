#Avijit kumar kar
import numpy as np
x=np.arange(start = 100, stop = 220, step = 10, dtype=int)
result=x.reshape((6,2))
print('6 cross 2 array of which differnence between two element is 10')
print(result)
print('after spliting into 3 subarrays of 4 elements:')
print(np.split(x,3))

"""result

6 cross 2 array of which differnence between two element is 10
[[100 110]
 [120 130]
 [140 150]
 [160 170]
 [180 190]
 [200 210]]
after spliting into 3 subarrays of 4 elements:
[array([100, 110, 120, 130]), array([140, 150, 160, 170]), array([180, 190, 200, 210])]

"""