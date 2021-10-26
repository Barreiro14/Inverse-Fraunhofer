import matplotlib.pyplot as plt
import numpy as np

def plotter(arr):
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr[0]):
            if arr[i][j] != 0:
                plt.plot(i, j, 'bo')
            j = j +1
        i = i + 1
    plt.show()

arr = np.array([[0,1,1], [1, 0, 0], [1, 0, 1]])
print(len(arr[0]))
plotter(arr)
#plt.plot(1, 2, 'bo')
#plt.show()