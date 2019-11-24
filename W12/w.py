import numpy as np
x1 = np.array([5.1, 3.8, 1.6, 0.2])
x2 = np.array([4.6, 3.2, 1.4, 0.2])
x3 = np.array([5.3, 3.7, 1.5, 0.2])
x4 = np.array([5, 3.3, 1.4, 0.2])
x5 = np.array([7, 3.2, 4.7, 1.4])
x6 = np.array([6.4, 3.2, 4.5, 2.5])
x7 = np.array([6.9, 3.2, 4.9, 1.5])
x8 = np.array([5.5, 2.3, 4, 1.3])
x9 = np.array([6.5, 2.8, 4.6, 1.5])
x10 = np.array([5.7, 2.8, 4.5, 1.3])
C1=[x1,x3,x7,x8]
C2=[x2,x4,x5,x6,x9,x10]
x0=np.array([0.0,0.0,0.0,0.0])
for i in C1:
    x0+=i
for i in x0:
    print(f'{i/C1.__len__()}')

for i in C2:
    x0+=i
for i in x0:
    print(f'{i/C2.__len__()}')
#5.7 3.25 3 0.8
#9.67 5.25 5.517 1.717