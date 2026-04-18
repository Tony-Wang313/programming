import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
#d1= 6
#d2= 5
#k = 5
#shift = 1
#n_points = 26
#frame_step = 6

#A1
def plot_graph(num):

    x_lst = []
    if num==0:
        return "Invalid"

    for i in range(num):
        temp = float(input(f"Enter the x value #{i+1}: "))
        x_lst.append(temp)
    y_lst=[a**2 for a in x_lst]

    plt.figure(figsize=(8, 5))
    plt.plot(x_lst, y_lst, marker="o", linestyle="-", color="red")
    plt.title("Function")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
#B1
    y2 = [5 * a + 1 for a in x_lst]
    z_lst = list(zip(x_lst, y2))
    print(z_lst[0:5])
    plt.figure(figsize=(8, 5))
    plt.plot(x_lst, y2, marker="s", linestyle=":", color="green")
    plt.title("Student Number: 2586965 k=5 shift=1")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()


#A2
def plot_distrib(num2):
    data_values=[]
    if num2 < 30:
        print("Invalid")
    else:   
        for i in range(num2):
            data= int(input(f"Enter the x value #{i+1}: "))
            data_values.append(data)
        val=data_values[0:10]
        print(val)
        plt.hist( val, bins=50, edgecolor="black")
        plt.title("Density plot")
        plt.xlabel("Measurements")
        plt.ylabel("Repeated time")
        plt.grid(True)
        plt.show()
        # By looking at the graph, we can see which of the ten first data is the most repeated with the height of the bar.
    
#B2
def TD_fig():
    x=[]
    n_points=26
    shift=1
    k=5
    for i in range(1, n_points+1):
        x.append(i)
    y = [a + shift for a in x]
    z = [k * a for a in x]
    deb_lst = list(zip(x, y, z))
    print(deb_lst[0:5])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.title("3D Graph")
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.show()

if __name__ == "__main__":
    num = int(input("Enter the number of data points: "))
    plot_graph(num)
    num2 = int(input("Enter the number of data points for the distribution graph: "))
    plot_distrib(num2)
    TD_fig()

#B3
n_points=26
shift=1
k=5
x=[]
for i in range(0, n_points):
     x.append(i)
y = [a + shift for a in x]
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(x[0],x[-1])
ax.set_ylim(min(y),max(y))

def init():
    line.set_data([], [])
    return line,

def update(frame):
    if frame < 5:
        print("Animating frame:", frame)
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)
plt.show()



    