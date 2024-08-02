#! /usr/bin/python3


import rospy


# Import the service class: service definition, response message
from test1.srv import AddTwoInts, AddTwoIntsResponse, AddTwoIntsRequest


# Definition of the function called by the service
def callback_addtwoints(req: AddTwoIntsRequest):
    # create a response variable
    res = AddTwoIntsResponse()
    # Compute the sum
    res.Sum = req.A + req.B
    # Return the response variable
    return res


if __name__ == "__main__":
    rospy.init_node('AddTwoInts_server_node')

    # Start the service server
    my_service = rospy.Service(
        'add_two_ints_service_name',
        AddTwoInts,
        callback_addtwoints,
    )

    print('Ready to add two ints.')

    # Wait to be closed by the user
    rospy.spin()
