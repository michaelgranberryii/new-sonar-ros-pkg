#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import Range
import time #Delay
from geometry_msgs.msg import Twist

t1 = 'sonar112_range_topic'
t2 = 'sonar114_range_topic'
t3 = 'sonar116_range_topic'

class ObstDet():
	def __init__(self):
		rospy.init_node('sonar_listener_algo', anonymous=True)

		# Sonar Vars
		self.range_sonar_left = 25 #0x70
		self.range_sonar_center = 25 #0x71
		self.range_sonar_right = 25 #0x72

		# Sonar Array List
		self.sonar_list = []

		# Sonar Array indecies
		self.l=0
		self.c=1
		self.r=2

		# Safe Distance
		self.safe_dist = 10
		self.min_range_reading = 0
		
		# Sonar Subscribers
		self.sub_sonar0x70 = rospy.Subscriber(t1, Int32, self.update_range0x70)
		self.sub_sonar0x72 = rospy.Subscriber(t2, Int32, self.update_range0x72)
		self.sub_sonar0x74 = rospy.Subscriber(t3, Int32, self.update_range0x74)
	
		rospy.loginfo("Subscribers set")
		
	def update_range0x70(self, message):
		self.range_sonar_left = message.data
		rospy.loginfo(str(message.data))

	def update_range0x72(self, message):
		self.range_sonar_center = message.data
		rospy.loginfo(str(message.data))
	 
	def update_range0x74(self, message):
		self.range_sonar_right = message.data
		rospy.loginfo(str(message.data))


	def listener(self):
            self.sub_sonar0x70 = rospy.Subscriber(t1, Int32, self.update_range0x70)
            self.sub_sonar0x72 = rospy.Subscriber(t2, Int32, self.update_range0x72)
            self.sub_sonar0x74 = rospy.Subscriber(t3, Int32, self.update_range0x74)
            rospy.spin()

	
if __name__ == '__main__':
	
	obst_det = ObstDet()
	obst_det.listener()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
