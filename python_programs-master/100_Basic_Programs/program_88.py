# 88. By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[[0 for col in range(8)] for col in range(5) for col in range(3)]]
print(array)