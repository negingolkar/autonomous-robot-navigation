class GridWorld:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

        self.robot_position = (0, 0)
        self.goal_position = (width - 1, height - 1)

        # Obstacles in the environment
        self.obstacles = {
            (2, 0),
            (2, 1),
            (2, 2),
            (4, 3),
            (5, 3),
            (6, 3),
            (7, 6),
            (7, 7),
        }

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
    world = GridWorld()

    print("Robot position:", world.robot_position)
    print("Goal position:", world.goal_position)

    # Move right
    world.move_robot(1, 0)
    print("Robot position:", world.robot_position)

    # Try to move into an obstacle
    world.move_robot(1, 0)
    print("Robot position:", world.robot_position)