# 🤖 Autonomous Robot Navigation

An autonomous robot navigation project using **path planning, obstacle avoidance, and environment visualization**.

The project simulates a robot navigating through a 2D grid environment with obstacles and uses the **Breadth-First Search (BFS)** algorithm to find a valid shortest path from the starting position to the goal.

---

## 🎯 Project Overview

The goal of this project is to build a simple simulation of an autonomous robot that can:

- Navigate through a 2D environment
- Detect and avoid obstacles
- Find a path from a start position to a target
- Visualize the planned trajectory

This project provides a foundation for exploring more advanced topics in **robotics, autonomous systems, path planning, and artificial intelligence**.

---

## 🧠 Methodology

The navigation system consists of three main components:

### 1. Grid World

A 10×10 environment is created where:

- The robot starts at `(0, 0)`
- The goal is located at `(9, 9)`
- Obstacles are placed at predefined positions

The robot cannot move outside the environment or through obstacle cells.

### 2. BFS Path Planning

The project uses **Breadth-First Search (BFS)** to explore the environment and find a shortest path between the robot and the goal.

At each step, the algorithm evaluates the robot's neighboring cells while avoiding:

- Grid boundaries
- Obstacles
- Previously visited positions

### 3. Visualization

The resulting path is visualized using **Matplotlib**, showing:

- 🤖 Robot starting position
- ⭐ Goal position
- ⬛ Obstacles
- 🔵 Planned navigation path

---

## 📊 Result

The BFS planner successfully finds a path from the starting position to the goal while avoiding obstacles.

The resulting path contains **18 movement steps**.

### Navigation Visualization

![Autonomous Robot Navigation](results/navigation_path.png)

---

## 🗂️ Project Structure

```text
autonomous-robot-navigation/
│
├── data/
│
├── notebooks/
│
├── results/
│   └── navigation_path.png
│
├── src/
│   ├── grid_world.py
│   ├── path_planner.py
│   └── visualize.py
│
└── README.md


🛠️ Technologies
Python
Git & GitHub
Matplotlib
Breadth-First Search (BFS)
Object-Oriented Programming
How to Run
Clone the repository:
git clone git@github.com:negingolkar/autonomous-robot-navigation.git
Navigate to the project:
cd autonomous-robot-navigation
Run the grid world:
python3 src/grid_world.py
Run the path planner:
python3 src/path_planner.py
Generate the navigation visualization:
python3 src/visualize.py
The generated visualization will be saved in:
results/navigation_path.png


🔬 Future Improvements
Possible extensions of this project include:
Implementing A* path planning
Comparing BFS and A* performance
Adding dynamic obstacles
Introducing different map configurations
Adding robot movement simulation
Integrating real-world map data
Using Computer Vision for obstacle detection
Extending the project toward real robotic platforms

👩‍💻 Author
Negin Golkar
MSc Data Science and Engineering
Politecnico di Torino
Interests:
Robotics • Aerospace • Machine Learning • Computer Vision • Autonomous Systems