# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    num_row = len(grid)
    num_col = len(grid[0])
    total_p = 0
    
    for i in range(num_row):
        row_i = [beliefs[i][j] * p_hit if color == grid[i][j] else beliefs[i][j] * p_miss for j in range(num_col)]
        total_p += sum(row_i)
        new_beliefs.append(row_i)
        
    for i in range(num_row):
        for j in range(num_col):
            new_beliefs[i][j] /= total_p
        
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
#             pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)