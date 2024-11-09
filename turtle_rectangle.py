#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def move_rectangle(length, breadth):
    # Initialize the ROS node
    rospy.init_node('turtle_rectangle', anonymous=True)
    # Create a publisher to send velocity commands
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Define the Twist message
    vel_msg = Twist()

    # Function to move the turtle in a straight line
    def move_straight(distance):
        vel_msg.linear.x = 1.0  # Set a constant forward speed
        vel_msg.angular.z = 0.0
        duration = distance / vel_msg.linear.x
        # Publish the velocity for the specified duration
        start_time = time.time()
        while time.time() - start_time < duration:
            velocity_publisher.publish(vel_msg)
        # Stop the turtle after moving
        vel_msg.linear.x = 0.0
        velocity_publisher.publish(vel_msg)

    # Function to turn the turtle by 90 degrees
    def turn_right():
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -1.0  # Negative for clockwise turn
        duration = 1.57 / abs(vel_msg.angular.z)  # π/2 radians (90 degrees)
        start_time = time.time()
        while time.time() - start_time < duration:
            velocity_publisher.publish(vel_msg)
        # Stop the turtle after turning
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)

    # Move in a rectangular path
    for _ in range(2):
        move_straight(length)
        turn_right()
        move_straight(breadth)
        turn_right()

    # Stop the turtle after completing the rectangle
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Define the length and breadth of the rectangle
        length = 2  # Customize the length
        breadth = 4  # Customize the breadth
        move_rectangle(length, breadth)
    except rospy.ROSInterruptException:
        pass
