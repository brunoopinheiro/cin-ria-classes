# Joint Control System
- Components of a **robot joint control system**
    - Joint Controller
    - Motor Drive
    - Actuator
    - Mechanical Transmission
    - Position Sensor

# Configuration Space
- Robot Configuration is described by a vector of generalised joint coordinates
- Each coordinate can be:
    - an angle, for a rotational (revolute) joint
    - a length, for a sliding (prismatic) joint

# Robot Kinematics
- We consider two kinematic problems in robotics
    - Foward kinematic problem
        - Given the joint angles, where is the robot's tool tip?
    - Inverse kinematic problem
        - Given the pose of the robot's tool tip, what joint angles are required?