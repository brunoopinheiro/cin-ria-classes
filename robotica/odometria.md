# Odometria
- Existem várias soluções para descrever a orientação de um corpo rígido:
    - Quaternion
    - Ângulos de Euler
    - Matriz de Orientação
    - ...
- ROS dá orientação como um quaternion
- Precisamos fazer a conversão Quaternion -> Angulos de Euler

## A mensagem `nav_msgs/Odometry`
- Para compartilhar os dados de odometria usamos a mensagem padrão **Odometry** `http://docs.ros.org/en/melodic/api/nav_msgs/html/msg/Odometry.html`
- [Code Sample](/robotica/ROS/odometry.py)
- 