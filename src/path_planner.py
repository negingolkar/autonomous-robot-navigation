from collections import deque


class PathPlanner:
    def __init__(self, grid_world):
        self.grid_world = grid_world

    def get_neighbors(self, position):
        x, y = position

        possible_moves = [
            (1, 0),   # Right
            (-1, 0),  # Left
            (0, 1),   # Up
            (0, -1),  # Down
        ]

        neighbors = []

        for dx, dy in possible_moves:
            new_x = x + dx
            new_y = y + dy
            new_position = (new_x, new_y)

            if not (0 <= new_x < self.grid_world.width):
                continue

            if not (0 <= new_y < self.grid_world.height):
                continue

            if new_position in self.grid_world.obstacles:
                continue

            neighbors.append(new_position)

        return neighbors

    def find_path(self, start, goal):
        queue = deque([start])
        visited = {start}
        parent = {start: None}

        while queue:
            current = queue.popleft()

            if current == goal:
                return self.reconstruct_path(parent, goal)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        return None

    def reconstruct_path(self, parent, goal):
        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path


if __name__ == "__main__":
    from grid_world import GridWorld

    world = GridWorld()
    planner = PathPlanner(world)

    path = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    if path:
        print("Path found!")
        print("Number of steps:", len(path) - 1)
        print("Path:", path)
    else:
        print("No path found.")