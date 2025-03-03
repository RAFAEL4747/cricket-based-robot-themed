def iddfs_performance_monitoring(player_stats, player_id, max_depth):
    def dls(stats, player, depth, limit):
        if depth > limit:
            return []
        
        performance_data = [f"Depth {depth}: {metric}: {stats[player][metric]}" for metric in stats[player].keys() if depth >= stats[player][metric]["depth"]]
        
        for next_depth in range(depth + 1, max_depth + 1):
            performance_data.extend(dls(stats, player, next_depth, limit))
        
        return performance_data
    
    for depth in range(max_depth + 1):
        print(f"Checking up to depth {depth}...")
        report = dls(player_stats, player_id, 0, depth)
        for entry in report:
            print(entry)
        print("---")

# Sample Input: Incremental player performance data
player_stats = {
    "Player1": {
        "Runs": {"value": 50, "depth": 0},
        "Strike Rate": {"value": 135.5, "depth": 1},
        "Fours": {"value": 8, "depth": 1},
        "Sixes": {"value": 3, "depth": 2},
        "Average": {"value": 45.2, "depth": 2},
        "Consistency Index": {"value": 78.3, "depth": 3},
    }
}

player_id = "Player1"
max_depth = 3  # Expanding performance analysis up to advanced metrics

# Expected Output: Incremental performance report generation using IDDFS
iddfs_performance_monitoring(player_stats, player_id, max_depth)