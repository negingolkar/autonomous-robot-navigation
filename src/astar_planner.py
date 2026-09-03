import heapq


class AStarPlanner:
    def __init__(self, grid_world):
        self.grid_world = grid_world

    def get_neighbors(self, position):
        x, y = position

        possible_moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
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

    def heuristic(self, position, goal):
        x1, y1 = position
        x2, y2 = goal

        return abs(x1 - x2) + abs(y1 - y2)

    def find_path(self, start, goal):
        open_set = []

        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}

        visited = set()
        nodes_explored = 0

        while open_set:
            _, current = heapq.heappop(open_set)

            if current in visited:
                continue

            visited.add(current)
            nodes_explored += 1

            if current == goal:
                path = self.reconstruct_path(came_from, goal)

                return path, nodes_explored

            for neighbor in self.get_neighbors(current):

                if neighbor in visited:
                    continue

                tentative_g_score = g_score[current] + 1

                if (
                    neighbor not in g_score
                    or tentative_g_score < g_score[neighbor]
                ):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    f_score = (
                        tentative_g_score
                        + self.heuristic(neighbor, goal)
                    )

                    heapq.heappush(
                        open_set,
                        (f_score, neighbor)
                    )

        return None, nodes_explored

    def reconstruct_path(self, came_from, goal):
        path = []
        current = goal

        while current in came_from:
            path.append(current)
            current = came_from[current]

        path.append(current)
        path.reverse()

        return path


if __name__ == "__main__":
    from grid_world import GridWorld

    world = GridWorld()
    planner = AStarPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    print("Nodes explored:", nodes_explored)

    if path:
        print("Path found!")
        print("Number of steps:", len(path) - 1)
        print("Path:", path)
    else:
        print("No path found.")