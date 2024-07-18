# Introduction to Robotics
_Adrien Durant-Petiteville_
_adrien.durandpetiteville@ufpe.br_

## What is a robot?
- The robot is seen as a machine that, idenpendently of its exterior, is able to modify the environment in which it operates.
- This is accomplished by carrying out actions that are conditioned by certain rules of behaviour intrinsic in the machine as well as by some data the robot acquires on its status and on the environment.
- In fact, robotics is commonly defined as the science studying the intelligent connection between perception and action.

> How to proccess, in a intelligent way, the information acquired by the sensors in order to generate the appropriate actions to be executed by the actuators.

### Is a Chatbot a Robot?
- It does not have a physical body, so it is not a robot.
- It is a software that interacts with the user through a chat interface.

### Is a microwave oven a robot?
- It does not adapt to the environment, so it is not a robot.
- It is a machine that executes a pre-defined sequence of actions.

### Is a drone a robot?
- When controlled by a human, it is not a robot.
- When it is able to fly autonomously, it is a robot.

## Not a Robot:
- Software ("bots", AI, Robotic Process Automation - RPA)
- remote-controlled drones, UAV, UGV, UUV
- voice assistants
- autonomous vehicles
    - although it is very close to be considered one
- ATMs, smart washing machines, etc.

## A Robotic System:
- A robotic system is in reality a complex system, functionally represented by multiple susbsystems.
![](https://www.researchgate.net/profile/Theo-De-Vries-3/publication/265555758/figure/fig1/AS:613446592786457@1523268473641/A-typical-robotic-system.png)

ROBOT = Sense + Think + Act

## Mechanical System
- The essential component of a robot is the **mechanical system** endowed, in general, with:
    - A locomotion apparatus (wheels, crawlers, mechanical legs)
    - A manipulation apparatus (mechanical arms, end-effectors, artificial hands)
- The realization of such a system refers to the context of design of articulated mechanical systems and choice of materials.
- The complexity of each subpart depends on the type of task the robot is supposed to perform.

## Actuation System
- The capability to exert an action, both locomotion and manipulation, is provided by an **actuation system** which animates the mechanical components of the robot.
- The concept of such a system refers to the context of **motion control** dealing with servomotors, drives and transmissions.
- The actuation system is the interface between the mechanical system and the control system.
![](https://www.usinainfo.com.br/blog/wp-content/uploads/2016/04/Servo-Motor-1024x427.jpg)

## Sensory System
- The capability for perception is entrusted to a **sensory system** which can acquire data on:
    - The internal status of the mechanical system (proprioceptive sensors, such as positions transducers).
    - The external status of the environment (exteroceptive sensors, such as force and cameras).
- The realization of such a system refers to the context of material properties, signal conditions and data processing.

## Control System
- The capability for connection action to perception in an intelligent fashion is provided by a **control system** which can command the execution of the action in respect to the goals set by a task planning technique, as well as of the constraints imposed by the robot and the environment.
- The realization of such a system follows the same feedback principle devoted to the control of human movements.

## Robotics
- Therefore, it can be recognized that robotics is an interdisciplinary subject concerning the cultural areas of:
    - Mechanics
    - Control
    - Computers
    - Electronics

# Applications of Robotics

## Industrial Robotics - 1
- Industrial robotics is the discipline concerning robot design, control and applications in industry.
- Its products have by now reached the level of a mature technology.
- The connotation of a robot for industrial applications is that of operating in a structured environment whose geometrical or physical characteristics are mostly known a priori.
- Limited autonomy is required.
    - The environment is structured and the tasks are repetitive.

## Industrial Robotics - 2
- The industrial robot is a machine with significant characteristics of versatility and flexibility.
- According to the widely accepted definition of the Robot Institute of America, a robot is:
_"A reprogrammable multifunctional manipulator designed to move materials, parts, tools or specialized devices through variable programmed motions for the performance of a variety of tasks."_

## Manufactoring
- Manufactoring consists of transforming objects from raw material into finished products
- During this process, the part either changes its own physical characteristis as a result of machine operations or is assembled with other parts to form a more complex object.

# Applications: Advanced Robotics

## Advanced Robotics
- The expression advanced robotics usually refers to the science studying robots with marked characteristics of autonomy, operating in scarcely structured or unstructured environments, whose geometrical or physical characteristics would not be known a priori.
- There are many motivations which strongly encourage advances in knowledge within this field.
- Field Robotics: robots operating in outdoor environments.
- Service Robotics: robots operating in indoor environments.

### Mars Rover
- NASA succeeded in delivering some mobile robots (rovers) to Mars which navigated on the Martial soil, across rocks, hills and crevasses. Such rovers were partially teleoperated from Earth and have successfully explored the environment with sufficient autonomy.

## Service Robotics
- Service robotics is the discipline concerning robot design, control and applications in service sectors.
- The service robot is a machine with significant characteristics of autonomy, operating in a scarcely structured environment whose geometrical or physical characteristics are mostly unknown a priori.

# Robot Modeling, Planning and Control

## Robot Modeling
- In all robot applications, completion of a generic task requires the execution of a specific motion prescribed to the robot.
- The correct execution of such motion is entrusted to the control system which should provide the robot's actuators with the commands consistent with the desired motion.
- Motion control demands an accurate analysis of the characteristics of the mechanical structure, actuators and sensors.

## Planning: Robot Manipulators
- With reference to the tasks assigned to a manipulator, the issue is whether to specify the motion at the joints or directly at the end-effector.

## Planning: Mobile Robots
- The motion of a mobile robot is usually specified in terms of the position and orientation of the robot's body frame.

## Control: Robot Manipulators
- Realization of the motion specified by the control law requires the employment of actuators and sensors.
- The trajectories generated constitute the reference inputs to the motion control system of the mechanical structure.

## Control: Mobile Robots
- Control of a mobile robot substantially differs from the analogous problem for robot manipulators.

## Motors
- Electric motors are used to "actuate" some parts of your robot: its wheels, legs, tracks, arms, fingers, or camera.
- **Brushed DC Motor**: A brushed DC electric motor is an internally commutated electric motor designed to be run from a direct current power source.
- **Brushless DC Motor**: A brushless DC electric motor is a synchronous electric motor which is powered by direct-current electricity and which has an electronically controlled commutation system, instead of a mechanical commutation system based on brushes.
- **Servo Motor**: A servomotor is a rotary actuator or linear actuator that allows for precise control of angular or linear position, velocity and acceleration.
    - It consists of a suitable motor coupled to a sensor for position feedback.
    - It also requires a controller.
- **Stepper Motor**: A brushless DC electric motor that divides a full rotation into a number of equal steps.
    - The motor's position can then be commanded to move and hold at one of these steps without any position sensor for feedback.
    - As long as the motor is carefully sized to the application, it can be a very cost-effective solution.

## Collision Sensors:
- Switch Sensor: A switch sensor is a device that detects the presence or absence of an object by opening or closing an electrical circuit.
    - Very Simple
    - On/Off

## Interaction Sensors:
- Force/torque sensors
    - 3-axis force sensor
    - 3-axis torque sensor
- Artificial skin
    - Temperature
    - Pressure
    - Proximity

## Proximity/Distance sensors - 1
- Infrared (IR) sensor
    - Measures reflected light intensity which corresponds to distance.
    - Range: 10cm - 1m
    - Wide detection cone
    - Can be also used to detect black vs white color (e.g., for a line detection)
    - Unaffected by material softness
    - Sensitive to object color and transparency
    - Relatively short distance.
- Ultrasonic sensor
    - Measures time of reflected signal to return which corresponds to distance.
    - Range: 2cm - 3m
    - Wide detection cone
    - Unaffected by object color and transparency
    - Sensitive to material softness
    - Relatively slow
- LIDAR sensor (laser imaging, detection, and ranging)
    - Measures time of reflected signal to return which corresponds to distance.
    - Range: 5cm - 40 m
    - Fast and long range sensing
    - One single point (no cone)
    - Relatively expensive (1D)

## Inertial Motion Sensors
- Inertial motion unit (IMU) sensor
    - 3-axys gyroscope
    - 3-axys accelerometer
    - 3-axys magnetometer (absolute orientation)
    - Can be used for estimation of position of a mobile robot using path integration. Path reconstruction is inaccurate due to drift.
- Angular position sensor (optical encoder)
    - Measures rotary motion
    - Can be used for estimation of position of a mobile robot using path integration.
    - Path reconstruction is inaccurate and gets worse with time.

## Localization Sensors
- Global Positioning System (GPS) sensor
    - Global position
    - Requires satellite signal
    - Works only outdoors
- Indoor positioning system (IPS) sensor
    - Local position
    - Requires infrastructure
    - Works indoors
    - Radio Frequency (RF) signals from radio sources to determine robots location

## 2D Cameras
- 2D RGB cameras
    - Direct mapping of environment
    - 2D RGB image
    - Produces a lot of data: 3xWxH

## 3D Cameras
- 3D RGB-D cameras
    - Direct mapping of environment
    - 3D RGB-D image
    - Produces a lot of data: 3xWxH
    - IR camera (depth sensor)
    - Allows 3D reconstruction of the environment
    - Sensitive to object transparency
    - Produces a lot of data: 3xWxH + 1xWxH

- 3D stereo cameras
    - Two RGB cameras
    - Allows 3D reconstruction of the environment
    - Not affected by object transparency
    - Produces a lot of data: 2x 3xWxH

# Robotic Arms
- Robotic Arms are devices that have been designed to do a given activity swiftly, correctly, and effectively.
- They're usually motor-driven consisting of a collection of joints, articulations, and manipulators.
- They are employed to accomplish heavy and/or repetitive tasks.

## Advantages:
- Improved Safety: Robotic arms keep employees safe by functioning in hazardous areas and doing jobs that pose a high risk of human injury.
- Better Productivity: Robotic arms can work nonstop for 24 hours a day, seven days a week, helping organizations enhance output by keeping production, inspection, and other operations running continuously.
- Better Precision
- improved flexibility

### Why Are Industrial Robotic Arms Used in Manufacturing?
- Industrial robotic arms are used in production for several purposes:
    - Where is necessary to reduce threats to human safety.
    - Where it is necessary to increase productivity.
    - Where it is necessary to improve precision.

### Industrial Robots
- Mainly used in:
    - Manufacturing
    - Logistics
    - Agriculture
    - Animal husbandry

### Non-Industrial Robots
- Mainly used in:
    - Security
    - Medical and health care
    - Entertainment

### Conventional vs Collaborative Robots
- Conventional industrial robots are required to be installed away from people and inside a safety cage.
- Collaborative robots can work alongside humans without the need for a safety cage.

# Robot Mechanical Structure
- The mechanical structure of a robot manipulator consists of a sequence of rigit bodies (links) interconnected by means of articulations (joints).
- A manipulator is characterized by:
    - an arm that ensures mobility
    - a wrist that confers dexterity
    - an end-effector that performs tasks required of the robot.
- The fundamental structure of a manipulator is the serial or open kinematic chain: the sequence of links connecting the two ends of the chain.

## JOINTS
- A manipulator's mobility is ensured by the presence of joints.
- The articulation between two consecutive links can be realized by means of either a revolute joint or a prismatic joint.
- In an open kinematic chain, each prismatic or revolute joint provides the structure a single degree of freedom.

### Degrees of Freedom
- The degrees of freedom should be properly distributed along the mechanical structure in order to have a sufficient number to execute a given task.
- In the most general case of a task consisting of arbitrarily positioning and orienting an object in three-dimensional (3D) space, six DOFs are required.
    - Three for positioning a point on the object
    - three for orienting the object with respect to a reference coordinate frame.
- If more DOFs than task variables are available, the manipulator is said to be redundant from a kinematic viewpoint.

## System Features
- Workspace
    - The workspace represents the portion of the environment the manipulator's end-effect can access.
    - Its shape and volume depend on the manipulator structure as well as on the presence of mechanical joint limits.
- Load capacity
    - Load capacity, a primary robot specification, is closely coupled with acceleration and speed.

# The Different Types of Robot Arms
## Serial vs Parallel Link
- Robots are roughly categorized into two types according to how their links are arranged:
    - Serial Link
    - Parallel Link

## Cartesian
- Cartesian geometry is realized by three prismatic joints whose axes typically are mutually orthogonal.
- In view of the simple geometry, each DOF corresponds to a Cartesian space variable and thus it is natural to perform straight motions in space.
- The cartesian structure offers very good mechanical swiftness.

## Cylindrical
- Cylindrical geometry differs from Cartesian in that the first prismatic joint is replaced with a revolute joint.
- If the task is described in cylindrical coordinates, in this case each DOF also corresponds to a cartesian space variable.
- Wrist positioning accuracy decreases as the horizontal stroke increases.

## Spherical
- Spherical geometry differs from cylindrical in that the second prismatic joint is replaced with a revolute joint.
- Each DOF corresponds to a cartesian space variable provided that the task is described in spherical coordinates.

## Anthropomorphic
- Anthropomorphic geometry is realized by three revolute joints.
- The revolute axis of the first joint is orthogonal to the axes of the other two which are parallel.
- By virtue of its similarity with the human arm, the second joint is called the shoulder, the third the elbow.
- The Anthropomorphic structure is the most dexterous one, since all three joints are revolute.
- On the other hand, the correspondence between the DOFs and the cartesian space variables is lost.
- Wrist positioning accuracy varies inside the workspace.
- Workspace is approximately a portion of a sphere and its volume is large compared to manipulator encumbrance. Joints are typically actuated by electric motors. The range of industrial applications of Anthropomorphic manipulators is wide.
- Joints are typically actuated by electric motors.

## Parallel
- All the previous manipulators have an open kinematic chain.

## Wrist
- The manipulator structure previously presented are required to position the wrist which is then required to orient the manipulators end effect.

## End-Effector
- The end effector is the part of the robot that interacts with the environment.

## Robot and Human Motion Comparison
- A vertical articulated robot is an industrial robot with a serial link structure.
- It is generally composed of six joints (6 axes)
- 1st axis: waist
- 2nd axis: shoulder
- 3rd axis: elbow
- 4th axis: wrist (rotating)
- 5th axis: wrist (bending)
- 6th axis: Fingertip

## What is Required to move joints?
### internal structure of industrial robots
- A robot is made of many different parts
    - actuator
    - reduction gear
    - encoder
    - transmission

### Actuator
- The actuator is a component that functions as the joint of the robot.
- It allows a robot to move the arm up and down or rotate.
- It converts energy into motion.

### Reduction Gear
- A reduction gear is a device for increasing the power of the motor.
- A motor alone is limited in the amount of power it can output.
- In order to generate great power, motors are basically used in combination with this reduction gear.
- If you combine gear wheels with the different number of gears and reduce the motor's rotation by a factor of 10, the power of the motor will be multiplied by 10.

### Encoder
- An encoder is a device that indicates the position (angle) of a motor's rotational shaft.
- Having an encoder, it can provide tangible data about in what direction and how much the robot moves.
- General optical encoders have a disk attached to the rotating shaft of the motor.
- The disk has slits at regular intervals to let light passes and on both sides of the disk are light-emitting-diode (LED) and light receiving elements (photodiodes) to discriminate the light intensity (light and dark).
- When the motor rotates, the light either passes through the slits or is blocked, so the rotation angle and speed can be determined by reading the signals.
- This allows servo motors to move precisely to the desired position.

### Transmission
- The tramission is a component that transmits the power generated by the motor to the robot's arm.

### Controllers
- The controllers are the robotic arms' main processors and operate as their brains.
- They can be set to behave automatically, or they can be manually operated by receiving instrunctions from a specialist.
- They are the control consoles for mechanical arms, and they come in several forms depending on the amount of computing power required.

