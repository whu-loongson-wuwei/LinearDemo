import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
import pandas
from matplotlib.animation import FuncAnimation
dataset = np.array([[1, 1.64385, 1.29556, 1],
                    [1, 1.83075, 2.42741,   1],
                    [1, 0.21004, 1.98691,  1],
                    [1, 2.14351, 0.3153,   -1],
                    [1, -0.32142, 0.42772,   -1],
                    [1, -0.32142, -0.42772,   -1],
                    [1, 0.87208, 1.75063, 1],
                    ])
xGloal = np.arange(-0.8, 2.8, 0.05)
pause = False
line = None
point = None
def pla():
    W = np.array([1, 1, 1])  # initial all weight with 1
    lineLastOne = -(W[0] + W[1] * xGloal) * 1.0 / W[2]
    count = 0
    while True:
        #count += 1
        iscompleted = True
        for i in range(0, len(dataset)):
            X = dataset[i,:-1]
            Y = np.dot(W, X)  # matrix multiply
            if np.sign(Y) == np.sign(dataset[i, -1]):
                continue
            else:
                iscompleted = False
                if not pause:
                	   W = W + (dataset[i, -1]) * np.array(X)
                yield[lineLastOne,X]
                lineLastOne = -(W[0] + W[1] * xGloal) * 1.0 / W[2]
        if iscompleted :
            break
    print("final W is :", W)
    yield[lineLastOne,[200,200,200]]
    #print("count is :", count)
def update(data):
    line.set_ydata(data[0])
    point.set_data(data[1][1],data[1][2])
    return line,point
def onClick(event):
    global pause
    pause ^= True
def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylim(-1, 3)
    ax.set_xlim(-1, 3)
    flag = []
    for label in dataset[:, -1]:
        if label == 1:
            flag.append('r')
        else:
            flag.append('g')
    ax.scatter(dataset[:, 1], dataset[:, 2], marker='o', c=flag)
    global line
    line, = ax.plot(xGloal, xGloal, 'b-', linewidth=2)
    global point
    point, = ax.plot([], [], 'yo', ms=15)
    fig.canvas.mpl_connect('button_press_event', onClick)
    anim = FuncAnimation(fig, update, frames=pla, interval=1000, repeat=False)
    plt.show()

if __name__ == '__main__':
    main()
