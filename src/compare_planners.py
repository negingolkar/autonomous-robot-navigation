import matplotlib.pyplot as plt

from grid_world import GridWorld
from path_planner import PathPlanner
from astar_planner import AStarPlanner


def run_bfs(world):
    planner = PathPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    steps = len(path) - 1

    return steps, nodes_explored


def run_astar(world):
    planner = AStarPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    steps = len(path) - 1

    return steps, nodes_explored


if __name__ == "__main__":
    world = GridWorld()

    print("\nPlanner Comparison")
    print("------------------")

    bfs_steps, bfs_nodes = run_bfs(world)
    astar_steps, astar_nodes = run_astar(world)

    print("\nSummary")
    print("------------------")
    print("BFS path length:", bfs_steps)
    print("BFS nodes explored:", bfs_nodes)
    print("A* path length:", astar_steps)
    print("A* nodes explored:", astar_nodes)

    algorithms = ["BFS", "A*"]

    # Path length comparison
    plt.figure(figsize=(7, 5))

    plt.bar(
        algorithms,
        [bfs_steps, astar_steps]
    )

    plt.title("BFS vs A* Path Length")
    plt.xlabel("Algorithm")
    plt.ylabel("Path Length (steps)")

    plt.tight_layout()

    plt.savefig(
        "results/path_length_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # Nodes explored comparison
    plt.figure(figsize=(7, 5))

    plt.bar(
        algorithms,
        [bfs_nodes, astar_nodes]
    )

    plt.title("BFS vs A* Nodes Explored")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes Explored")

    plt.tight_layout()

    plt.savefig(
        "results/nodes_explored_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()