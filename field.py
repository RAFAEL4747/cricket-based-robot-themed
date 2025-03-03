def dls_field_scan(field, start_position, depth, current_depth=0, visited=None):
    if visited is None:
        visited = set()
    
    x, y = start_position

    # Stop if depth limit is reached or already visited
    if current_depth > depth or (x, y) in visited:
        return []
    
    visited.add((x, y))
    scanned_positions = [(x, y)]

    # Explore all 4 directions with depth limitation
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
            scanned_positions.extend(dls_field_scan(field, (new_x, new_y), depth, current_depth + 1, visited))

    return scanned_positions

# Sample Input: Cricket field grid representation (Players, Pitch, Boundary)
field = [
    [0, 0, 3, 0, 0],
    [0, 1, 0, 1, 0],
    [3, 0, 2, 0, 3],  # Pitch at (2,2), boundary marked as 3
    [0, 1, 0, 1, 0],
    [0, 0, 3, 0, 0]
] # 1: Players, 2: Pitch, 3: Boundary

start_position = (2, 2)  # Start scanning from the pitch
depth_limit = 2  # Limit scanning to 2 levels deep

# Expected Output: DLS traversal order of scanned positions
scanned_positions = dls_field_scan(field, start_position, depth_limit)
print("Scanned Positions:", scanned_positions)
