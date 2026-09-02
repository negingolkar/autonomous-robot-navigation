# 🤖 Autonomous Robot Navigation

An autonomous robot navigation project that explores **path planning, obstacle avoidance, and intelligent navigation** in a simulated 2D environment.

The project implements and compares two classical path planning algorithms:

- **Breadth-First Search (BFS)**
- **A\* (A-Star)**

The goal is to evaluate how different planning strategies affect navigation efficiency in an obstacle-filled environment.

---

## 🎯 Project Overview

The project simulates a robot navigating through a **10×10 grid environment** containing obstacles.

The robot:

- Starts at `(0, 0)`
- Must reach the goal at `(9, 9)`
- Cannot move through obstacles
- Uses path planning algorithms to determine a valid route

The project is designed as a foundation for studying **robotics, autonomous systems, artificial intelligence, and intelligent path planning**.

---

## 🧠 Path Planning Algorithms

### 1. Breadth-First Search (BFS)

BFS explores the environment level by level.

Because every movement has the same cost, BFS is guaranteed to find a shortest path in this grid environment.

However, BFS may explore many unnecessary nodes before reaching the goal.

### 2. A\* Search

A\* improves the search process by combining:

- The cost of reaching the current position
- A heuristic estimate of the remaining distance

The project uses **Manhattan distance** as the heuristic:

```text
h(n) = |x₁ - x₂| + |y₁ - y₂|
This allows A* to focus the search toward the goal instead of exploring the environment uniformly.
📊 Results
Both algorithms successfully found a shortest path of 18 movement steps.
However, A* explored significantly fewer nodes:

| Algorithm | Path Length | Nodes Explored |
| --------- | ----------: | -------------: |
| BFS       |          18 |             92 |
| A*        |          18 |             68 |
A* explored 24 fewer nodes than BFS, corresponding to approximately a 26% reduction in explored nodes while maintaining the same path length.
e
autonomous-robot-navigation/
│
├── data/
│
├── notebooks/
│
├── results/
│   ├── navigation_path.png
│   ├── path_length_comparison.png
│   └── nodes_explored_comparison.png
│
├── src/
│   ├── grid_world.py
│   ├── path_planner.py
│   ├── astar_planner.py
│   ├── compare_planners.py
│   └── visualize.py
│
└── README.md
🛠️ Technologies
Python
Git & GitHub
Matplotlib
Breadth-First Search (BFS)
A* Search
Object-Oriented Programming
🚀 How to Run
Clone the repository:
git clone git@github.com:negingolkar/autonomous-robot-navigation.git
Navigate to the project:
cd autonomous-robot-navigation
Run the Grid World
python3 src/grid_world.py
Run BFS
python3 src/path_planner.py
Run A*
python3 src/astar_planner.py
Compare BFS and A*
python3 src/compare_planners.py
This generates:
results/path_length_comparison.png
results/nodes_explored_comparison.png
Generate Navigation Visualization
python3 src/visualize.py
This generates:
results/navigation_path.png
🔬 Future Improvements
Possible extensions include:
Dynamic obstacles
Different environment configurations
Weighted terrain and movement costs
Real-time robot movement simulation
Computer Vision-based obstacle detection
Reinforcement Learning for navigation
Integration with real robotic platforms
ROS-based implementation
Real-world map data
👩‍💻 Author
Negin Golkar
MSc Data Science and Engineering
Politecnico di Torino

Interests:
Robotics • Aerospace • Machine Learning • Computer Vision • Autonomous Systems




