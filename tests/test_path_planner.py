import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from grid_world import GridWorld
from path_planner import PathPlanner


def test_bfs_finds_path():
    world = GridWorld(map_name="medium")
    planner = PathPlanner(world)

    path, nodes_explored = planner.find_path(
        world.robot_position,
        world.goal_position
    )

    assert path is not None
    assert path[0] == world.robot_position
    assert path[-1] == world.goal_position
    assert len(path) - 1 == 18
    assert nodes_explored > 0