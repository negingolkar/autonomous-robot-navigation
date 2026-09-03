import time
import matplotlib.pyplot as plt

from grid_world import GridWorld
from path_planner import PathPlanner
from astar_planner import AStarPlanner


def run_bfs(world, repetitions=1000):
    planner = PathPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    if path is None:
        return None, nodes_explored, None

    steps = len(path) - 1

    start_time = time.perf_counter()

    for _ in range(repetitions):
        planner.find_path(
            world.robot_position,
            world.goal_position
        )

    total_time = time.perf_counter() - start_time
    average_time = total_time / repetitions

    return steps, nodes_explored, average_time


def run_astar(world, repetitions=1000):
    planner = AStarPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    if path is None:
        return None, nodes_explored, None

    steps = len(path) - 1

    start_time = time.perf_counter()

    for _ in range(repetitions):
        planner.find_path(
            world.robot_position,
            world.goal_position
        )

    total_time = time.perf_counter() - start_time
    average_time = total_time / repetitions

    return steps, nodes_explored, average_time


if __name__ == "__main__":

    maps = ["easy", "medium", "hard"]
    repetitions = 1000

    print("\nPlanner Benchmark")
    print("=================")
    print(f"Average execution time over {repetitions} runs")

    results = {}

    for map_name in maps:

        world = GridWorld(map_name=map_name)

        bfs_steps, bfs_nodes, bfs_time = run_bfs(
            world,
            repetitions
        )

        astar_steps, astar_nodes, astar_time = run_astar(
            world,
            repetitions
        )

        results[map_name] = {
            "bfs_steps": bfs_steps,
            "bfs_nodes": bfs_nodes,
            "bfs_time": bfs_time,
            "astar_steps": astar_steps,
            "astar_nodes": astar_nodes,
            "astar_time": astar_time,
        }

        print(f"\nMap: {map_name.upper()}")
        print("-----------------")

        print(
            f"BFS   | "
            f"Path: {bfs_steps} | "
            f"Nodes: {bfs_nodes} | "
            f"Avg Time: {bfs_time:.8f} s"
        )

        print(
            f"A*    | "
            f"Path: {astar_steps} | "
            f"Nodes: {astar_nodes} | "
            f"Avg Time: {astar_time:.8f} s"
        )

    # -------------------------
    # Path Length Comparison
    # -------------------------

    plt.figure(figsize=(8, 5))

    x = range(len(maps))
    width = 0.35

    bfs_steps = [
        results[m]["bfs_steps"]
        for m in maps
    ]

    astar_steps = [
        results[m]["astar_steps"]
        for m in maps
    ]

    plt.bar(
        [i - width / 2 for i in x],
        bfs_steps,
        width,
        label="BFS"
    )

    plt.bar(
        [i + width / 2 for i in x],
        astar_steps,
        width,
        label="A*"
    )

    plt.xticks(x, [m.upper() for m in maps])

    plt.title("BFS vs A* Path Length")
    plt.xlabel("Map")
    plt.ylabel("Path Length (steps)")
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "results/path_length_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # -------------------------
    # Nodes Explored Comparison
    # -------------------------

    plt.figure(figsize=(8, 5))

    bfs_nodes = [
        results[m]["bfs_nodes"]
        for m in maps
    ]

    astar_nodes = [
        results[m]["astar_nodes"]
        for m in maps
    ]

    plt.bar(
        [i - width / 2 for i in x],
        bfs_nodes,
        width,
        label="BFS"
    )

    plt.bar(
        [i + width / 2 for i in x],
        astar_nodes,
        width,
        label="A*"
    )

    plt.xticks(x, [m.upper() for m in maps])

    plt.title("BFS vs A* Nodes Explored")
    plt.xlabel("Map")
    plt.ylabel("Nodes Explored")
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "results/nodes_explored_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # -------------------------
    # Execution Time Comparison
    # -------------------------

    plt.figure(figsize=(8, 5))

    bfs_times = [
        results[m]["bfs_time"] * 1_000_000
        for m in maps
    ]

    astar_times = [
        results[m]["astar_time"] * 1_000_000
        for m in maps
    ]

    plt.bar(
        [i - width / 2 for i in x],
        bfs_times,
        width,
        label="BFS"
    )

    plt.bar(
        [i + width / 2 for i in x],
        astar_times,
        width,
        label="A*"
    )

    plt.xticks(x, [m.upper() for m in maps])

    plt.title("BFS vs A* Average Execution Time")
    plt.xlabel("Map")
    plt.ylabel("Average Time (microseconds)")
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "results/execution_time_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()