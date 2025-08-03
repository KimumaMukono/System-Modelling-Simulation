# 3DOF Robotic Arm Forward Kinematics Simulation

This repository contains a Python script to simulate and visualize the forward kinematics of a 3-degree-of-freedom (3DOF) robotic arm with three revolute joints. The simulation computes the end-effector position based on joint angles using the Denavit-Hartenberg (DH) convention and visualizes the arm’s motion in 3D with Matplotlib. It includes both a static plot of the initial configuration and an animated plot showing the arm’s movement with an end-effector trace.

## Features
- Models a 3DOF robotic arm with three 0.1 m links using DH parameters.
- Computes forward kinematics to determine joint and end-effector positions.
- Visualizes the arm in a static 3D plot for the initial configuration.
- Animates the arm’s motion with a dynamic trajectory, including an end-effector path trace.
- Uses NumPy for kinematic calculations and Matplotlib for 3D visualization.

## Prerequisites
- Python 3.6 or higher
- Required Python packages:
  - `numpy`
  - `matplotlib`
- Optional (for saving animations):
  - `ffmpeg-python` (for saving the animation as a video)
  - FFmpeg installed on your system

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/KimumaMukono/Applied_Mathematics_Modelling/robot-arm-fk.git
   cd 3dof-robot-arm-fk
   ```
2. Install the required Python packages:
   ```bash
   pip install numpy matplotlib
   ```
3. (Optional) For saving animations, install FFmpeg and the Python package:
   ```bash
   pip install ffmpeg-python
   ```
   Install FFmpeg on your system:
   - **Windows**: Download from [FFmpeg’s website](https://ffmpeg.org/download.html) and add to PATH.
   - **macOS** (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - **Ubuntu**:
     ```bash
     sudo apt-get install ffmpeg
     ```

## Usage
1. Run the Python script to generate the visualizations:
   ```bash
   python robot_arm_3dof_fk3.py
   ```
2. The script produces two windows:
   - **Static Plot**: Shows the arm’s initial configuration (all joint angles at 0°).
   - **Animated Plot**: Displays the arm moving through a trajectory (\(\theta_1\): sinusoidal -45° to 45°, \(\theta_2\): 0° to 180°, \(\theta_3\): sinusoidal -45° to 45°), with a green dashed line tracing the end-effector’s path.
3. (Optional) To save the animation as a video, uncomment the following line in `robot_arm_3dof_fk.py`:
   ```python
   # ani.save('robot_arm.mp4', writer='ffmpeg')
   ```
   Ensure FFmpeg is installed, then run the script again.

## Mathematical Basis
The simulation uses the Denavit-Hartenberg (DH) convention for forward kinematics. Key equations include:
- **DH Transformation Matrix**:
  \[
  A_i = \begin{bmatrix}
  \cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
  \sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\
  0 & \sin\alpha_i & \cos\alpha_i & d_i \\
  0 & 0 & 0 & 1
  \end{bmatrix}
  \]
- **Forward Kinematics**: \( T_0^3 = A_1 \cdot A_2 \cdot A_3 \)
- **DH Parameters**:
  - Joint 1: \( \theta_1 \), \( d_1 = 0 \), \( a_1 = 0.1 \, \text{m} \), \( \alpha_1 = \pi/2 \)
  - Joint 2: \( \theta_2 \), \( d_2 = 0 \), \( a_2 = 0.1 \, \text{m} \), \( \alpha_2 = 0 \)
  - Joint 3: \( \theta_3 \), \( d_3 = 0 \), \( a_3 = 0.1 \, \text{m} \), \( \alpha_3 = 0 \)

For a detailed explanation, see [3dof_robot_arm_equations.md](3dof_robot_arm_equations.md).

## File Structure
- `robot_arm_3dof_fk.py`: Main Python script for simulation and visualization.
- `3dof_robot_arm_equations.md`: Documentation of the mathematical equations used.
- `README.md`: This file, providing project overview and instructions.

## Customization
- **Arm Geometry**: Modify `dh_params` or `L1, L2, L3` in `robot_arm_3dof_fk.py` to change link lengths or joint configurations.
- **Trajectory**: Adjust `theta1_traj`, `theta2_traj`, or `theta3_traj` to define custom motion patterns.
- **Animation Speed**: Change the `interval` parameter in `FuncAnimation` to adjust animation speed.
- **Plot Limits**: Update `set_xlim`, `set_ylim`, `set_zlim` to modify the visualization range.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, improvements, or new features.

## Contact
For questions or feedback, please open an issue on this repository or contact [your-email@example.com](mailto:your-email@example.com).