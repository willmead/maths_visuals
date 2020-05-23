import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import copy


def get_random_grid(size):
    grid = []
    for row in range(size):
        grid.append([])
        for column in range(size):
            val = 1 if random.randint(1, 5) == 5 else 0
            grid[row].append(val)
    print_grid(grid)
    return(grid)


def print_grid(grid):
    for row in grid:
        print(f"{row}\n")


def get_live_neighbors(row, col, size, grid):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                neighbours += grid[((row + i) % size)][((col + j) % size)]
    return neighbours


def update(frame, img, grid, size):
    grid_copy = copy.deepcopy(grid)
    for row in range(size):
        for column in range(size):
            neighbours = get_live_neighbors(row, column, size, grid_copy)

            if grid_copy[row][column] == 1 and neighbours not in [2, 3]:
                grid[row][column] = 0
            elif grid_copy[row][column] == 0 and neighbours == 3:
                grid[row][column] = 1

    img.set_data(grid)
    return img,


size = 100
interval = 50
grid = get_random_grid(size)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = FuncAnimation(fig,
                    update,
                    fargs=(img, grid, size),
                    frames=10,
                    interval=50,
                    save_count=50)
plt.show()
