from collections import deque

def bfs_monitor_field(field, start_position):
    rows, cols = len(field), len(field[0])
    visited = set()
    queue = deque([start_position])
    monitored_positions = []

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        monitored_positions.append((x, y))
        
        # Explore all 4 possible movements: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and field[new_x][new_y] == 1:
                queue.append((new_x, new_y))
    
    return monitored_positions

# Sample Input: Cricket field grid representation (11 players + pitch at (2,2))
field = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 2, 1, 0],  # Pitch is marked as 2 at (2,2)
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0]
] # 11 players marked as 1, pitch as 2
start_position = (1, 0)  # Start monitoring from a valid player position

# Expected Output: BFS traversal order of monitored positions
monitored_positions = bfs_monitor_field(field, start_position)
print("Monitored Positions:", monitored_positions)
