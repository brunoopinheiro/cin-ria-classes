# Fundamentals for Robot Manipulators
- A fundamental requirement in robotics is to represent the position and orientation of objects in an environment.
    - The problem is the same in a robotic arm or a mobile robot. It is necessary to know a matrix that can be used to find the position and orientation of the robot.

## Point
- A point in space can be described by a coordinate vector.
- The vector represents the displacement of the point with respect to some reference coordinate frame.
- A coordinte frame, or Cartesian frame, is a set of three orthogonal axes, usually denoted by x, y, and z.

### Set of Points
- More frequently we need to consider a set of points that comprise some object.
- We assume that the object is rigid and that its constituent points maintain a constant relative position with respect to the object's coordinate frame.
- Instead of describing the individual points we describe the position and orientation of the object by the position and orientation of its coordinate frame.

## Relative Pose
- The relative pose of a frame with respect to a reference coordinate frame is denoted by the symbol $\xi$
- Relative pose $^A\xi_B$ describes {B} with respect to {A}.
    - The superscript denotes the reference coordinate frame.
    - The superscript denotes the frame being described.
- We could also thing of $^A\xi_B$ as describing some motion: applying a displacement and rotation of {A} so that it is transformed to {B}.
> Pose = Position + Orientation

### Point Coordinates
- The point $P$ can be described with respect to either coordinate frame
- Formally we express this as: $^A P = ^A\xi_B \cdot ^B P$
    - The point $P$ is described with respect to {A} by transforming it from {B} to {A}.
- The operator $\cdot$ denotes the transformation of the point from one coordinate frame to another. It transforms the vector, resulting in a new vector that describes the same point but with respect to a different coordinate frame.

### Composition of Relative Poses
- Relative poses can be composed.
- If one frame can be described in terms of another by a relative pose then they can be applied sequentially.
- $^A\xi_C = ^A\xi_B \oplus ^B\xi_C$

- For this case the point $P$ can be described:
    - $^Ap = (^A\xi_B \oplus ^B\xi_C) \cdot ^Cp$

### 3-dimensional coordinate frames
- So far we have shown 2-dimensional coordinate frames
- For other problems we require 3-dimensional coordinate frames to describe objects in our 3-dimensional world such as the pose of the end of a tool carried by a robot arm.

## Directed Graph
- An alternative representation of the spatial relationships is a directed graph
    - Each node represents a pose
    - Each edge represents a relative pose
- We can compose relative poses using the $oplus$ operator

# Representing Pose in 2-Dimensions
- To represent a 2-dimensional world, we use a Cartesian coordinate system
    - Two orthogonal axes denoted $x$ and $y$ and typically drawn with the x-axis horizontal and the y-axis vertical.
    - The point of intersection is called the origin.
- Unit-vectors parallel to the axes are denoted $\hat{x}$ and $\hat{y}$
- A point is represented by its x- and y- coordinates (x,y) or as a bound vector:
    - $p = x\hat{x} + y\hat{y}$

## Representation of pose: first approach
- Let's consider a coordinate frame {B} to describe with respect to the reference frame {A}.
- The origin of {B} has been displaced by the vector $t = (x, y)$ and then rotated counter-clockwise by an angle $\theta$.
- A concrete representation of pose is therefore the 3-vectors $^A\xi_B ~ (x, y, \theta)$

...

## Representation of pose: second approach
- Let's consider a point $P$ with respect to each of the coordinate frames and to determine the relationship between $^A P$ and $^B P$.
- We first consider the **rotation** problem.
- We create a new frame {V} whose axes are parallel to those of {A} but whose origin is the same as {B}
- We can express the point $P$ with respect to {V} in termis of the unit-vectors that define the axes of the frame:
- $^V P = ^Vx\hat{x}_V + ^Vy\hat{y}_V = (\hat{x}V \hat{y}V) (V_x V_y)$

## Rotation
- The coordinate frame {B} is completely described by its two orthogonal axes which we represent by two unit vectors
- $\hat{x}_B = \cos\theta\hat{x}_V + \sin\theta\hat{y}_V$
- $\hat{y}_B = -\sin\theta\hat{x}_V + \cos\theta\hat{y}_V$
- It can be factorized into matrix form as
    - $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$

### Rotation Matrix
- The rotation matrix $^VR_B$ is orthonormal.
- Orthonormal matrices have the very convenient property that $R^{-1} = R^T$, that is, the inverse of the matrix is equal to its transpose.

## Translation
- The second part of representing pose is to account for the translation between the origins of the frames.
- Since the axes {V} and {A} are parallel this is simply vectorial addition.

## Homogeneous Transformation
- $^AT_B$ is referred to as **homogeneous transformation**.
- The coordinate vectors for point $P$ are now expressed in homogeneous form as
    - $^AP = \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$

...

## Exercise: Spatialmath Python
[FILE](/samples/spatialmath_sample.ipynb)

# Representing Pose in 3-Dimensions
- The 3-dimensional case is an extension of the 2-dimensional
- We add an extra coordinate axis, typically denoted by $z$ and drawn as a line perpendicular to the x-y plane.
- A coordinate frame {B} has to be described with respect to the reference frame {A}.
- We can see clearly that the origin of {B} has been displaced by the vector $t = (x, y, z)$ and then rotated by the matrix $R$.
- Just as for the 2-dimensional case the way we represent orientation is very important.

> Any two independent orthonormal coordinate frames can be related by a sequence of rotations (not more than three) about coordinate axes, where no two successive rotations may be about the same axis. Euler's rotation theorem (Kuipers 1999)

- Rotation in x axis can be interpreted as a rotation about the x-axis from y to z
- Rotation in y axis can be interpreted as a rotation about the y-axis from z to x
- Rotation in z axis can be interpreted as a rotation about the z-axis from x to y

> y -> z -> x -> y

- Sequence of two rotations applied in different orders:
    - The final orientation depends on the order in which the rotations are applied
    - This is a deep and confounding characteristic of the 3-dimensional world
    - The implication for the pose algebra is that the $\oplus$ operator is not commutative. **The order in which rotations are applied is very importante.**
    - There exists many ways to represent rotations
        - Orthonormal rotation matrices
        - Euler and Cardan angles
        - Rotation axis and angle
        - Unit quaternions

## Orthonormal Rotation Matrix
- Just as for the 2-dimensional case we can represent the orientation of a coordinate frame by a 3x3 matrix.
- The orthonormal rotation matrices for rotation of $\theta$ about the $x-$, $y-$ and z-axes are:
    - $R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}$
    - $R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}$
    - $R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$

## Three-Angle Representation
- Euler's rotation theorem requires successive rotation about three axes such that no two successive rotations are about the same axis.
- There are two classes of rotation sequences: Eulerian and Cardanian, named after Euler and Cardano respectively
- The eulerian type involves repetition, but not successive, of rotations about one particular axis: XYX, XZX, YZY, ZXZ, or ZYZ

...

- It is common practice to refer to all 3-angle representations as Euler angles, but this is underspecified since there are twelve different types to choose from.
- The ZYZ sequence $R = R_z(\theta)R_y(\phi)R_z(\psi)$ is often used in aeronautics. (...)
[Roll Pitch Yaw Visualization](https://danceswithcode.net/engineeringnotes/rotations_in_3d/demo3D/rotations_in_3d_tool.html)

## Unit Quaternions
- The quaternion is an extension of the complex number - a hyper-complex number - and is written as a scalar plus a vector.
- Where $s E \!R$, $v E \!R^3$ (adjust E to contained in) and the orthogonal complex numbers i, j and k are defined such that $i^2 = j^2 = k^2 = ijk = -1$

# Combining Translation and Rotation
- We return now to representing relative pose in three dimensions, the **position and orientation** change, between two coordinate frames
