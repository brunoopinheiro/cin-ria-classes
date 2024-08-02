#! /usr/bin/python3


import rospy
from test1.srv import AddTwoInts, AddTwoIntsRequest, AddTwoIntsResponse


if __name__ == "__main__":
    rospy.wait_for_service('add_two_ints_service_name')
    print('Add Two Ints is active')
    try:
        # Connect to the server
        h_add_two_ints = rospy.ServiceProxy(
            'add_two_ints_service_name',
            AddTwoInts,
        )

        # Create and fill the request
        request = AddTwoIntsRequest()
        print('Service call')
        request.A = 2
        request.B = 3

        # Call the service
        response: AddTwoIntsResponse = h_add_two_ints(request)
        print(response.Sum)

    # If the connection fails (DEBUG)
    except rospy.ServiceException as e:
        print('Service call failed: ', e)
