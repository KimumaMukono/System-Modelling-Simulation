import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define DH parameters for a 3DOF robotic arm
# [theta, d, a, alpha] for each joint
# theta: joint angle, d: link offset, a: link length, alpha: link twist
dh_params = [
    [0, 0, 0.1, np.pi/2],  # Joint 1: base to link 1
    [0, 0, 0.1, 0],        # Joint 2: link 1 to link 2
    [0, 0, 0.1, 0]         # Joint 3: link 2 to end-effector
]

# Link lengths (m)
L1, L2, L3 = 0.1, 0.1, 0.1

# Forward kinematics function using DH parameters
def dh_transform(theta, d, a, alpha):
    """Compute transformation matrix for a DH parameter set."""
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def forward_kinematics(joint_angles):
    """Compute end-effector position and transformation matrices for 3DOF arm."""
    T = np.eye(4)  # Initialize transformation matrix
    points = [[0, 0, 0]]  # Base point
    for i in range(3):
        T_i = dh_transform(joint_angles[i], dh_params[i][1], dh_params[i][2], dh_params[i][3])
        T = T @ T_i
        point = T[:3, 3]
        points.append(point.tolist())
    return np.array(points), T

# Animation setup
def animate_arm(joint_angles_traj):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    def update(frame):
        ax.cla()  # Clear previous frame
        # Compute joint positions for current angles
        angles = joint_angles_traj[frame]
        points, _ = forward_kinematics(angles)
        
        # Plot arm
        ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b-', linewidth=2, marker='o')
        ax.scatter(points[-1, 0], points[-1, 1], points[-1, 2], color='r', s=100, label='End-Effector')
        
        # Set plot limits
        ax.set_xlim([-0.3, 0.3])
        ax.set_ylim([-0.3, 0.3])
        ax.set_zlim([0, 0.3])
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        ax.set_title(f'3DOF Robot Arm\nθ1={angles[0]:.2f}°, θ2={angles[1]:.2f}°, θ3={angles[2]:.2f}°')
        ax.legend()
        ax.grid(True)
        return ax
    
    ani = animation.FuncAnimation(fig, update, frames=len(joint_angles_traj), interval=50, blit=False)
    plt.show()

# Generate joint angle trajectory for animation
num_frames = 100
theta1_traj = np.linspace(0, np.pi/2, num_frames)  # Joint 1: 0 to 90 degrees
theta2_traj = np.linspace(0, np.pi, num_frames)    # Joint 2: 0 to 180 degrees
theta3_traj = np.linspace(0, np.pi/2, num_frames)  # Joint 3: 0 to 90 degrees
joint_angles_traj = np.vstack((theta1_traj, theta2_traj, theta3_traj)).T

# Static plot for initial position
initial_angles = [0, 0, 0]
points, T_end = forward_kinematics(initial_angles)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b-', linewidth=2, marker='o')
ax.scatter(points[-1, 0], points[-1, 1], points[-1, 2], color='r', s=100, label='End-Effector')
ax.set_xlim([-0.3, 0.3])
ax.set_ylim([-0.3, 0.3])
ax.set_zlim([0, 0.3])
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('3DOF Robot Arm Initial Position')
ax.legend()
ax.grid(True)
plt.show()

# Run animation
animate_arm(joint_angles_traj)