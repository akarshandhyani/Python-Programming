import random

# Generate a 5x5 matrix with unique values from 1 to 99, ensuring 1 is at center and 99 is not
def generate_matrix():
    values = list(range(1, 100))
    values.remove(1)  # 1 will be added at center
    random.shuffle(values)
    
    # Place 1 at center
    matrix = [[0]*5 for _ in range(5)]
    center = (2, 2)
    matrix[center[0]][center[1]] = 1

    idx = 0
    for i in range(5):
        for j in range(5):
            if (i, j) != center:
                matrix[i][j] = values[idx]
                idx += 1

    # Make sure 99 is present and not at center
    if 99 not in [val for row in matrix for val in row]:
        matrix[0][0] = 99  # Place it in top-left corner as an example

    return matrix

# Movement directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Execute traversal from center
def traverse_matrix(matrix):
    x, y = 2, 2  # Start from center
    path = [(x, y)]
    values = [matrix[x][y]]

    while matrix[x][y] != 99:
        max_val = -1
        next_pos = (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if matrix[nx][ny] > max_val:
                    max_val = matrix[nx][ny]
                    next_pos = (nx, ny)

        if next_pos == (x, y):
            break  # Stuck

        x, y = next_pos
        path.append((x, y))
        values.append(matrix[x][y])

    return path, values

# Run it
matrix = generate_matrix()
path, values = traverse_matrix(matrix)

# Output
print("Generated Matrix:")
for row in matrix:
    print(row)

print("\nTraversal Path (row, col):", path)
print("Values on path:", values)