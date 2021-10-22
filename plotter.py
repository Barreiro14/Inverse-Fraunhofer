import matplotlib.pyplot as plt

def plotter(arr):
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr[0]):
            if arr[i][j] != 0:
                plt.plot(i, j)
            j = j +1
        i = i + 1
    plt.show()

