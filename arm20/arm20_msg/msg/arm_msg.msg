string type # type of robot  ”ARM20”
string ip # address of the robot ESP8866
uint32 port # Port for comunication
uint8 id # identyti of robot a uint8_t
uint8 inst_before # the last instruction runner 
float32 battery # % of the battery
robots_msg/xl320 servo0 # only arm20
robots_msg/xl320 servo1 # only arm20
robots_msg/xl320 servo2 # only arm20
robots_msg/xl320 servo3 # only arm20
robots_msg/xl320 servo4 # only arm20
robots_msg/xl320 servo5 # only arm20
robots_msg/jevois camera # Aruco info
uint8 magnet            # status magnet 1 ON 0 OFF
string status # "Completed" or "Error tipo 3"