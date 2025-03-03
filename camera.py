import heapq

def ucs_camera_positions(field, start_position, goal_positions):
    rows, cols = len(field), len(field[0])
    visited = set()
    pq = [(0, start_position, [])]  # (cost, position, path)

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        # If we reach a goal position (optimal camera position), return the path and cost
        if (x, y) in goal_positions:
            return path, cost

        # Explore all 4 possible movements: up, down, left, right
        for dx, dy, move_cost in [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and field[new_x][new_y] != 3:
                heapq.heappush(pq, (cost + move_cost, (new_x, new_y), path))

    return [], float('inf')  # No path found

# Sample Input: Cricket field grid representation (Players, Ball, Camera Zones, Boundary)
field = [
    [0, 0, 3, 0, 0],
    [0, 1, 0, 1, 0],
    [3, 0, 2, 0, 3],  # Pitch at (2,2), boundary as 3
    [0, 1, 0, 1, 0],
    [0, 0, 3, 0, 0]
] # 1: Players, 2: Pitch, 3: Boundary

start_position = (0, 0)  # Camera starts at (0,0)
goal_positions = [(2, 2), (4, 4)]  # Best camera positions near the pitch or open field

# Expected Output: UCS optimal path to best camera position
optimal_path, optimal_cost = ucs_camera_positions(field, start_position, goal_positions)
print("Optimal Camera Path:", optimal_path)
print("Total Cost:", optimal_cost+1)
