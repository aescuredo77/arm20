#!/usr/bin/env python3

import rospy
from arm20_srv.srv import *
from arm20_msg.msg import arm_msg
from arm20_msg.msg import cmd_robot_msg
from sensor_msgs.msg import JointState
import socket
import select
import time

pub = rospy.Publisher('pub_arm_msg', arm_msg, queue_size=1)
joint_before=JointState()

class robot_arm_msg:
    def __init__(self):
        # init ros
        rospy.init_node('arm_msg_00', anonymous=False)
        rospy.Subscriber('cmd_arm_msg', cmd_robot_msg, self.send_cmd_to_esp8266)
        rospy.Subscriber('joint_states', JointState, self.send_seq_cmd_to_esp8266)
        
        self.get_string_from_esp8266()
        
    


    def send_cmd_to_esp8266(self, data):
        message=bytearray([data.id,data.instruction,data.op1,data.op2,data.op3,data.op4,data.op5,data.id])
        sock.sendto(message, (UDP_IP, UDP_PORT))
        time.sleep(0.05)
    

    def send_seq_cmd_to_esp8266(self, data):
        global joint_before
        rospy.wait_for_service('cmd_service_arm_seq')
        try:
            if(data.position != joint_before.position):
                cmd_service_arm_seq = rospy.ServiceProxy('cmd_service_arm_seq', arm_seq_send)
                resp = cmd_service_arm_seq(data)
                joint_before=data
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
            
    def get_string_from_esp8266(self):
        global UDP_IP,UDP_PORT,id_robot
        message=bytearray([id_robot,21,0,0,0,0,0,id_robot]) # to open the channell
        sock.sendto(message, (UDP_IP, UDP_PORT))
        #sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        pub = rospy.Publisher('pub_arm_msg', arm_msg, queue_size=1)
        r = rospy.Rate(10)
        msg = arm_msg()
        while not rospy.is_shutdown():
            sock.setblocking(0)
            sock.connect((UDP_IP,UDP_PORT))
            ready=select.select([sock],[],[],0.05)
            if ready[0]:		
                data, addr = sock.recvfrom(1024)
                rospy.loginfo(data)
                data = data.decode('ASCII')
                dat = data.split(',')            
                if dat[0] == 'ARM':
                    msg.type = dat[0]
                    msg.ip = dat[1]
                    msg.port = int(dat[2])
                    msg.id = int(dat[3])
                    msg.inst_before = int(dat[4])
                    msg.battery = float(dat[5])
                    msg.servo0.ID = int(dat[6])
                    msg.servo0.LED = int(dat[7])
                    msg.servo0.speed=int(dat[8])
                    msg.servo0.Goal_Position = int(dat[9])
                    msg.servo0.Present_Position = abs(int(dat[10]))
                    msg.servo1.ID = int(dat[11])
                    msg.servo1.LED = int(dat[12])
                    msg.servo1.speed=int(dat[13])
                    msg.servo1.Goal_Position = int(dat[14])
                    msg.servo1.Present_Position = abs(int(dat[15]))
                    msg.servo2.ID = int(dat[16])
                    msg.servo2.LED = int(dat[17])
                    msg.servo2.speed=int(dat[18])
                    msg.servo2.Goal_Position = int(dat[19])
                    msg.servo2.Present_Position = abs(int(dat[20]))
                    msg.servo3.ID = int(dat[21])
                    msg.servo3.LED = int(dat[22])
                    msg.servo3.speed=int(dat[23])
                    msg.servo3.Goal_Position = int(dat[24])
                    msg.servo3.Present_Position = abs(int(dat[25]))
                    msg.servo4.ID = int(dat[26])
                    msg.servo4.LED = int(dat[27])
                    msg.servo4.speed=int(dat[28])
                    msg.servo4.Goal_Position = int(dat[29])
                    msg.servo4.Present_Position = abs(int(dat[30]))
                    msg.servo5.ID =int(dat[31])
                    msg.servo5.LED = int(dat[32])
                    msg.servo5.speed=int(dat[33])
                    msg.servo5.Goal_Position = int(dat[34])
                    msg.servo5.Present_Position = abs(int(dat[35]))
                    msg.camera.type = dat[36]
                    msg.camera.id = int(dat[37])
                    msg.camera.targx = int(dat[38])
                    msg.camera.targy = int(dat[39])
                    msg.camera.targw = int(dat[40])
                    msg.camera.targh = int(dat[41])
                    msg.magnet= int(dat[42])
                    msg.status=dat[43]
                    pub.publish(msg)
                    r.sleep()
           

    
   
            
        
            
            
        
    
    

if __name__ == '__main__':
    UDP_IP = "192.168.0.154"   #esp8266 ip and port
    UDP_PORT = 8888
    id_robot=238
    joint_before = JointState()
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message=bytearray([id_robot,21,0,0,0,0,0,id_robot])
    sock.sendto(message, (UDP_IP, UDP_PORT)) 

    try:
        robot_arm_msg()
    except rospy.ROSInterruptException: 
        pass
