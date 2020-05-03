import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Add the filepath as a string")
args = parser.parse_args()

if args.path == None:
    print("Please pass in the path argument for this to work")
    exit()


style.use('seaborn-darkgrid')

file = args.path
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open(file,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
