#!/usr/bin/env python3

from __future__ import print_function
import rospy
from arm20_srv.srv import arm_seq_send,arm_seq_sendResponse
from arm20_msg.msg import cmd_robot_msg
import time

pi=3.1415926535897931
coe=614.4/pi

pub = rospy.Publisher('cmd_arm_msg', cmd_robot_msg, queue_size=1)

def send_commands_to_arm(req):
    global UDP_PORT,UDP_IP,id_robot
    response = arm_seq_sendResponse()
    cmd=cmd_robot_msg()
    for x in range(1,7):
        aux = 512 + req.joint_data.position[x-1]*coe
        aux=int(aux)
        cmd.ip=UDP_IP
        cmd.port=UDP_PORT
        cmd.id=id_robot
        cmd.instruction=17
        cmd.op1=x-1
        cmd.op2 = (aux >> 8) & 0xff
        cmd.op3 = aux & 0xff
        cmd.op4=0
        cmd.op5=0
        time.sleep(0.2)
        pub.publish(cmd)		# publish the position of each joint 
        #rospy.loginfo(message)
    cmd.instruction=18    
    pub.publish(cmd)			# publish the command to move to new position
    response.status="sended"
    return response

def set_arm_commands_server():
    rospy.init_node('set_arm_server')
    s = rospy.Service('cmd_service_arm_seq', arm_seq_send, send_commands_to_arm)
    rospy.spin()

if __name__ == "__main__":
    UDP_IP = "192.168.0.154"   #esp8266 ip and port
    UDP_PORT = 8888
    id_robot=238
    set_arm_commands_server()
