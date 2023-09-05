import numpy as np
list1 = [23, 34455, 56, 566666]
list2 = [12,34,243,33]
list3 = [98,6,787906708978767,678]
print(list1)
arr = np.array(list1, dtype=int)
print(arr)
arr2 = arr.reshape(2,2)
print(arr2)
multiArr = np.array([list1,list2,list3])
print(multiArr)
print("\n")
shape = multiArr.reshape(2,6)
print(shape)