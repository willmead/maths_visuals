import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

ON = 255
OFF = 0
vals = [ON, OFF]


def get_random_grid(size):
    return np.random.choice(vals, size*size, p=[0.2, 0.8]).reshape(size, size)


def update(frame_num, img, grid, size):
    new_grid = grid.copy()

    for i in range(size):
        for j in range(size):
            neighbours = int((grid[i, (j-1) % size] + grid[i, (j+1) % size] +
                              grid[(i-1) % size, j] + grid[(i+1) % size, j] +
                              grid[(i-1) % size, (j-1) % size] + grid[(i-1) % size, (j+1) % size] +
                              grid[(i+1) % size, (j-1) % size] + grid[(i+1) % size, (j+1) % size])/255)

            if grid[i, j] == ON:
                if (neighbours < 2) or (neighbours > 3):
                    new_grid[i, j] = OFF
            else:
                if neighbours == 3:
                    new_grid[i, j] = ON

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


size = 100
interval = 50
grid = get_random_grid(size)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
plt.axis('off')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, size),
                              frames=10,
                              interval=interval,
                              save_count=50)
plt.show()
