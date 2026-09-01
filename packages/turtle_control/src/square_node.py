#!/usr/bin/env python3
"""
ECEN 433 - Lab 2, Part II
=========================

Drive the turtlesim turtle in a repeating square.

Your node publishes geometry_msgs/Twist messages on the `turtle1/cmd_vel`
topic - the same topic you inspected with `rostopic info` in Part I.

Twist has two parts:

    msg.linear   In 2D you can only use x and y for linear speed, in 
                    "turtle units" per second
    msg.angular  In 2D you can only use component z for angular speed, 
                    in radians per second (positive = left)

For this node we want you to try and make the turtle drive in a square
by spinning so only using the x component of linear and the z component of angular.
This is comparable to how you would get a duckiebot to drive in a square. 

"""

import rospy
from geometry_msgs.msg import Twist

# How often we publish a command, in Hz. Commands need to be
# sent at a continous rate because the turtlesim will timeout 
# if it does not receive a command for a few seconds.
PUBLISH_RATE_HZ = 10.0


class SquareNode:
    def __init__(self):
        rospy.init_node("square_node")

        # Create the publisher on the turtle1/cmd_vel with msg type Twist. 
        self.pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

        self.rate = rospy.Rate(PUBLISH_RATE_HZ)

        rospy.loginfo("square_node started")

    def run(self):

        while not rospy.is_shutdown():
            # This will loop until the node is shutdown (Ctrl-C)

            msg = Twist()

            # --------------------------------------------------------------
            # TODO (Part II): make the turtle drive in a repeating square.
            # Do this by filling in the the Twist message
            # --------------------------------------------------------------


            # This command uses the publisher method to send out the message
            # It will be sent to the topic defined in the publisher 
            self.pub.publish(msg)

            # This will hold the loop for (1/PUBLISH_RATE_HZ) seconds
            self.rate.sleep()


if __name__ == "__main__":
    try:
        SquareNode().run()
    except rospy.ROSInterruptException:
        pass
