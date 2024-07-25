#! /usr/bin/python

import rospy

rospy.init_node('hello_world')

# Definição da frequẽncia do laço while
rate = rospy.Rate(2)  # Rate(Hz) recebe valor em Hz

count = 0
# Em loop até detecção de Ctrl+C
while not rospy.is_shutdown():
    print('Hello world number {}'.format(count))
    count += 1

    # Esperar pelo fim do tempo do laço
    rate.sleep()
