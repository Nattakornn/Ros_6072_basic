#!/usr/bin/env python
import rospy
import getch

from geometry_msgs.msg import Twist

class mark:
    def __init__(self):
        self.getkey = ""
        self.lastget = ""
        self.vel_x = 0.1
        self.ang_z = 1.0
        self.twist_new = Twist()
    
    def get_keyboard(self):
        self.getkey = getch.getch()

    def condition(self):
        #speed control 
        if self.getkey == "r":
            self.vel_x += 0.1
            if self.vel_x > 3:
                self.vel_x = 3
            self.getkey = self.lastget
        elif self.getkey == "f":
            if self.vel_x <= 0.2:
                self.vel_x = 0.1
            self.vel_x -= 0.1
            self.getkey = self.lastget

    def main(self):
        rospy.init_node('Teleop_Rb')
        tw = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        r = rospy.Rate(1000) 
        while not rospy.is_shutdown():
            self.get_keyboard()
            self.condition()
            if self.getkey == "w":
                self.twist_new.linear.x = self.vel_x
                self.lastget = "w"
            elif self.getkey == "x":
                self.twist_new.linear.x = -(self.vel_x)
                self.lastget = "x"
            elif self.getkey == "a":
                self.twist_new.angular.z = self.ang_z
            elif self.getkey == "d":
                self.twist_new.angular.z = -(self.ang_z)
            elif self.getkey == "s":
                self.twist_new.linear.x = 0.0
                self.twist_new.angular.z = 0.0
                self.vel_x = 0.1
            elif self.getkey == "b":
                break
            tw.publish(self.twist_new)
            r.sleep()

if __name__ == '__main__':
    try:
        mark().main()
    except rospy.ROSInterruptException:
        pass
