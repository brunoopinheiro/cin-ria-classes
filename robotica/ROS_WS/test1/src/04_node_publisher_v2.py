#! /usr/bin/python3

from random import random
import rospy
# importação do módulo de mensagens padrões
from std_msgs.msg import Float32MultiArray


# Criação do nó com o nome simple_publisher
rospy.init_node('simple_publisher_v2')

# criação do publisher no topic counter de uma mensagem
# do tipo Int32
pub = rospy.Publisher('counter_v2', Float32MultiArray, queue_size=1)

rate = rospy.Rate(2)

variable_to_publish = Float32MultiArray()
variable_to_publish.data = [random()*10, random()*10]


while not rospy.is_shutdown():
    # publicação de mensagens no tópico
    # msg = Int32(count)
    pub.publish(variable_to_publish)

    rate.sleep()
