import numpy as np
import matplotlib.pyplot as plt

def plot_curve(num_data):
    x_val = []
    y_val = []

    for i in range(num_data):
        v_x = float(input(f"Enter the x value #{i+1}: "))
        x_val.append(v_x)

    for i in range(num_data):
        v_y = float(input(f"Enter the y value #{i+1}: "))
        y_val.append(v_y)

    plt.plot(x_val, y_val, marker='o', linestyle='-')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Curve Plot")
    plt.grid(True)
    plt.show()

def plot_hr_d(dat):
    temperature = []
    luminosity = []

    for i in range(dat):
        temp = float(input(f"Enter the x value #{i+1}: "))
        temperature.append(temp)

    for i in range(dat):
        lumn= float(input(f"Enter the y value #{i+1}: "))
        luminosity.append(lumn)

    plt.scatter(temperature, luminosity, c=temperature, cmap='inferno', edgecolors='k')
    plt.gca().invert_xaxis() 
    plt.xlabel("Temperature (K)")
    plt.ylabel("Luminosity (Lâ˜‰)")
    plt.title("Hertzsprung-Russell Diagram")
    plt.colorbar(label="Temperature (K)")
    plt.show()

def plot_density(data, color_map='gray'):
    plt.hist2d(data[:, 0], data[:, 1], bins=50, edgecolor="white")
    plt.title("Density plot")
    plt.colorbar(label="Density")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

if __name__ == "__main__":
    num_data = int(input("Enter the number of values: "))
    plot_curve(num_data)
    dat= int(input("Enter the number of values: "))
    plot_hr_d(dat)
    np.random.seed(0)
    data = np.random.randn(1000, 2)  # Generating random 2D data
    plot_density(data, 'hot')
