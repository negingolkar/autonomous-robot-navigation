class GridWorld:
    MAPS = {
        "easy": {
            (2, 0),
            (2, 1),
            (2, 2),
            (4, 3),
        },

        "medium": {
            (2, 0),
            (2, 1),
            (2, 2),
            (4, 3),
            (5, 3),
            (6, 3),
            (7, 6),
            (7, 7),
        },

        "hard": {
            (1, 0),
            (1, 1),
            (1, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (5, 4),
            (5, 5),
            (2, 6),
            (3, 6),
            (4, 6),
            (7, 7),
            (8, 7),
            (8, 8),
        },
    }

    def __init__(self, width=10, height=10, map_name="medium"):
        self.width = width
        self.height = height

        self.robot_position = (0, 0)
        self.goal_position = (width - 1, height - 1)

        if map_name not in self.MAPS:
            raise ValueError(
                f"Unknown map '{map_name}'. "
                f"Choose from: {list(self.MAPS.keys())}"
            )

        self.map_name = map_name
        self.obstacles = self.MAPS[map_name]

    def move_robot(self, dx, dy):
        x, y = self.robot_position

        new_x = x + dx
        new_y = y + dy

        # Check boundaries
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            print("Move blocked: outside the grid.")
            return

        # Check obstacles
        if (new_x, new_y) in self.obstacles:
            print("Move blocked: obstacle detected.")
            return

        self.robot_position = (new_x, new_y)

    def reached_goal(self):
        return self.robot_position == self.goal_position


if __name__ == "__main__":
    world = GridWorld(map_name="medium")

    print("Map:", world.map_name)
    print("Robot position:", world.robot_position)
    print("Goal position:", world.goal_position)

    # Move right
    world.move_robot(1, 0)
    print("Robot position:", world.robot_position)

    # Try to move into an obstacle
    world.move_robot(1, 0)
    print("Robot position:", world.robot_position)