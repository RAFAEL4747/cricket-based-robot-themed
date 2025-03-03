def dfs_ball_trajectory(field, start_position, direction, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    x, y = start_position
    dx, dy = direction  # Initial direction of the ball
    
    # Stop DFS if out of bounds or if already visited
    if (x, y) in visited:
        return path[:-1]
    
    # Mark as visited and add to trajectory path
    visited.add((x, y))
    path.append((x, y))
    
    # Move in the same direction
    new_x, new_y = x + dx, y + dy
    
    # If ball hits a player, reverse direction
    if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]) and field[new_x][new_y] == 1:
        return dfs_ball_trajectory(field, (x - dx, y - dy), (-dx, -dy), path, visited)
    
    # If ball crosses boundary, determine if it's a 4 or 6
    if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]) and field[new_x][new_y] == 3:
        if abs(new_x - start_position[0]) >= 2 or abs(new_y - start_position[1]) >= 2:
            print("SIX!")
        else:
            print("FOUR!")
        return path
    
    # Continue in the same direction
    if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
        return dfs_ball_trajectory(field, (new_x, new_y), direction, path, visited)
    
    return path

# Sample Input: Cricket field grid representation (Players, Pitch, Boundary)
field = [
    [3, 3, 3, 3, 3],
    [3, 0, 1, 0, 3],
    [3, 0, 2, 0, 3],  # Ball starts at (2,2) (pitch)
    [3, 0, 1, 0, 3],
    [3, 3, 3, 3, 3]
] # 1: Players, 2: Pitch, 3: Boundary

start_position = (2, 2)  # Ball starts from the pitch
initial_direction = (0, 1)  # Ball moves right

# Expected Output: DFS traversal order of ball trajectory
trajectory = dfs_ball_trajectory(field, start_position, initial_direction)
print("Ball Trajectory:", trajectory)