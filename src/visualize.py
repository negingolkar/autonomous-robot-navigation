import matplotlib.pyplot as plt

from grid_world import GridWorld
from path_planner import PathPlanner


world = GridWorld()
planner = PathPlanner(world)

path, nodes_explored = planner.find_path(
    world.robot_position,
    world.goal_position
)


fig, ax = plt.subplots(figsize=(8, 8))

# Draw grid
ax.set_xlim(-0.5, world.width - 0.5)
ax.set_ylim(-0.5, world.height - 0.5)

ax.set_xticks(range(world.width))
ax.set_yticks(range(world.height))

ax.grid(True)

# Draw obstacles
for x, y in world.obstacles:
    ax.scatter(x, y, marker="s", s=500)

# Draw path
if path:
    path_x = [position[0] for position in path]
    path_y = [position[1] for position in path]

    ax.plot(
        path_x,
        path_y,
        linewidth=3,
        marker="o"
    )

# Draw robot
robot_x, robot_y = world.robot_position

ax.scatter(
    robot_x,
    robot_y,
    marker="o",
    s=250
)

# Draw goal
goal_x, goal_y = world.goal_position

ax.scatter(
    goal_x,
    goal_y,
    marker="*",
    s=400
)

ax.set_title("Autonomous Robot Navigation - BFS")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.savefig(
    "results/navigation_path.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()