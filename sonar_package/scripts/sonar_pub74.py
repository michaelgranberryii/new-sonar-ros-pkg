#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import Range
from smbus2 import SMBus #I2C
import time #Delay

addr =0x74


class Sonar:
	def __init__(self, i2cAddress):
		self.i2cAddress = i2cAddress
		self.writeRangeCmd = 0x51 #Write range Command. 81 in decimal
		self.initRead = 0xe1 #Initiate read. 225 in decimal
		self.delay1 = 0.1 #100ms

	def read_range(self):
		try:
			i2cbus = SMBus(1)
			i2cbus.write_byte_data(self.i2cAddress, 0, self.writeRangeCmd) #Write the range command byte.
			time.sleep(self.delay1)
			rawData = i2cbus.read_word_data(self.i2cAddress, self.initRead) #Initiate a read at the sensor address. Word = 2bytes.
			rangeValue = (rawData >> 8) & 0xff #Right shift 8-bits. Mask with 0x00ff.
			i2cbus.close()
			self.delay1 = 0.1 #100ms
			return rangeValue
		except IOError as err:
			print(err)

def sonar_talker():
	pub = rospy.Publisher('sonar' + '74' + '_range_topic', Int32, queue_size=10) # publisher object
	rospy.init_node('sonar' + str(addr) + '_publisher_node', anonymous=True) # initialize publisher node
	rate = rospy.Rate(10) # ros rate
	rospy.loginfo("Ros sonar node now publishing.")
	sp = Sonar(addr)
	# s = sp.Sonar(addr)
	while not rospy.is_shutdown():
		rangeValue = sp.read_range()
		rospy.loginfo(rangeValue)
		pub.publish(rangeValue)
		rate.sleep()

if __name__ == "__main__":
	try:
		sonar_talker()
	except rospy.ROSInterruptException:
		pass
