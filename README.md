Sure! Let’s create a comprehensive and unique `README.md` file specifically tailored for your ROS (Robot Operating System) project involving the turtle simulation, where the turtle moves in a rectangular path. This README will provide a clear description of the project, instructions for setup, and usage details.

---

# 🐢 ROS TurtleSim: Move in a Rectangular Path

Welcome to the **ROS TurtleSim** project! 🐢 This project demonstrates the use of **ROS (Robot Operating System)** to control a turtle in the TurtleSim simulation environment, making it move in a **rectangular path**.

## 🚀 Project Overview

In this project, we use ROS to control a simulated turtle, making it trace a rectangular path in the TurtleSim environment. The script:
- Initializes the ROS node for turtle control.
- Commands the turtle to move in straight lines and make precise 90-degree turns.
- Executes a complete rectangular trajectory using specified length and breadth values.

This is a great project for beginners to get hands-on experience with ROS, learn about `geometry_msgs/Twist` messages, and understand basic motion control in a simulation environment.

## 🛠️ Prerequisites

Ensure you have the following installed:
- **Ubuntu 20.04** or later
- **ROS Noetic** (or your preferred ROS distribution)
- **TurtleSim package** (comes pre-installed with ROS)

## 🖥️ Installation

1. **Install ROS Noetic** (if you haven’t already):
   ```bash
   sudo apt update
   sudo apt install ros-noetic-desktop-full
   ```

2. **Install TurtleSim package**:
   ```bash
   sudo apt install ros-noetic-turtlesim
   ```

3. **Clone this repository**:
   ```bash
   git clone https://github.com/rishiarora123/ros-turtlesim-rectangle.git
   cd ros-turtlesim-rectangle
   ```

4. **Build your ROS workspace**:
   ```bash
   catkin_make
   source devel/setup.bash
   ```

## 📜 Usage

1. **Launch the ROS core**:
   ```bash
   roscore
   ```

2. **Start the TurtleSim node**:
   ```bash
   rosrun turtlesim turtlesim_node
   ```

3. **Run the rectangle script**:
   ```bash
   rosrun your_package_name turtle_rectangle.py
   ```

Replace `your_package_name` with the name of your ROS package.

### 📝 Example

The turtle will move in a rectangular path based on the specified **length** and **breadth** in the script. You can customize these values to create different shapes.

- Default values:
  - **Length**: 5.0 units
  - **Breadth**: 3.0 units

### 🔧 Customization

To change the dimensions of the rectangle, edit the following lines in `turtle_rectangle.py`:

```python
length = 5.0  # Set your desired length
breadth = 3.0  # Set your desired breadth
```

## 🧩 Code Breakdown

- **move_straight()**: Moves the turtle forward by a specified distance.
- **turn_right()**: Rotates the turtle 90 degrees clockwise.
- **move_rectangle()**: Combines the movements to trace a rectangular path.

### Example Code Snippet

```python
def move_straight(distance):
    vel_msg.linear.x = 1.0  # Forward speed
    vel_msg.angular.z = 0.0  # No rotation
    velocity_publisher.publish(vel_msg)

def turn_right():
    vel_msg.angular.z = -0.5  # Clockwise turn
    velocity_publisher.publish(vel_msg)
```

## 🐛 Troubleshooting

1. **Turtle not moving in a straight line**:
   - Ensure the angular velocity (`angular.z`) is set to `0` during straight movement.
   - Reduce the speed if the turtle is drifting.

2. **ROS environment not set up properly**:
   - Run `source devel/setup.bash` in every new terminal session.
   - Check if `roscore` is running before executing the script.

## 🌟 Features

- Simple control of TurtleSim using ROS
- Demonstrates use of `geometry_msgs/Twist` for motion
- Configurable length and breadth of the rectangle

## 🤝 Contribution

Feel free to fork this repository, open issues, and submit pull requests. Contributions are always welcome!

## 📄 License

This project is open-source and available under the **MIT License**. Feel free to use, modify, and distribute.

## 📝 Acknowledgements

This project was inspired by the ROS tutorials and the desire to learn basic motion control in simulation.

---

**Happy Coding!** 🐢💻
