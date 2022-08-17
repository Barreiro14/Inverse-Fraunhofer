import matplotlib.pyplot as plt
import numpy as np

def plotter(arr):
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr[0]):
            if arr[i][j] != 0:
                plt.plot(i, j, 'ko')
            j = j +1
        i = i + 1
    plt.plot(0,0, 'bo')
    plt.show()

arr = np.array([[1,1,1], [1, 1, 1], [1, 1, 1]])
print(len(arr[0]))
plotter(arr)
'''
plt.plot(1, 2, 'bo')
plt.plot(1, 1, 'bo')
plt.plot(2, 2, 'bo')
plt.plot(2, 1, 'bo')

plt.show()




lkxszcljkvhklasdjflikjsklfjaskljkljkldj;kfljkl;fsw;kl
'''