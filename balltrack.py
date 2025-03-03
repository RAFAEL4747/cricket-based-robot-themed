from collections import deque

def bidirectional_search(field, start, goal):
    def bfs(queue, visited, parent):
        if queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]) and field[new_x][new_y] != 3:
                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        parent[(new_x, new_y)] = (x, y)
                        queue.append((new_x, new_y))
    
    start_queue, goal_queue = deque([start]), deque([goal])
    start_visited, goal_visited = {start}, {goal}
    start_parent, goal_parent = {}, {}
    
    while start_queue and goal_queue:
        bfs(start_queue, start_visited, start_parent)
        bfs(goal_queue, goal_visited, goal_parent)
        
        intersection = start_visited & goal_visited
        if intersection:
            meet_point = intersection.pop()
            path = []
            node = meet_point
            while node in start_parent:
                path.append(node)
                node = start_parent[node]
            path.reverse()
            node = meet_point
            while node in goal_parent:
                path.append(node)
                node = goal_parent[node]
            return path
    
    return []

# Sample Input: Cricket field grid representation (Players, Ball, Boundary)
field = [
    [3, 3, 3, 3, 3],
    [3, 0, 0, 0, 3],
    [3, 1, 2, 0, 3],  # Ball (2) at (2,2), Bowler (1) at (2,1)
    [3, 0, 0, 0, 3],
    [3, 3, 3, 3, 3]
] # 1: Players (Bowler/Batsman/Fielders), 2: Ball, 3: Boundary

start = (2, 1)  # Bowler’s position
goal = (2, 3)   # Batsman’s position

# Expected Output: Path from bowler to batsman (or fielders in dynamic cases)
path = bidirectional_search(field, start, goal)
print("Player-Ball Interaction Path:", path)
