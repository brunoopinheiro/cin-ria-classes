#! /usr/bin/python3


import rospy
# importação do módulo de mensagens padrões
from std_msgs.msg import Int32


# Criação do nó com o nome simple_publisher
rospy.init_node('simple_publisher')

# criação do publisher no topic counter de uma mensagem
# do tipo Int32
pub = rospy.Publisher('counter', Int32, queue_size=1)

rate = rospy.Rate(2)

count = 0

while not rospy.is_shutdown():
    # publicação de mensagens no tópico
    # msg = Int32(count)
    pub.publish(count)

    count += 1
    rate.sleep()
