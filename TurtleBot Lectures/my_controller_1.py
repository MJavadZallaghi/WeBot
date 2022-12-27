"""my_controller_1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import numpy as np
import matplotlib.pyplot as plt

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
rwm = robot.getDevice("right wheel motor")
lwm = robot.getDevice("left wheel motor")


gyro = robot.getDevice("gyro")
gyro.enable(timestep)

def move_forwrd(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(speed)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(speed)
    
def turn_left(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(speed/2)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(-speed/2)
    
def turn_right(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(-speed/2)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(speed/2)
theta_z = 0    
def angPosVel():
    global theta_z
    wx, wy, wz = gyro.getValues()[0], gyro.getValues()[1], gyro.getValues()[2]
    theta_z = theta_z + wz*timestep*0.001
    if theta_z>=2*np.pi:
        theta_z = 0
    # print(wz)
    # print(theta_z)
    theta_z_archive.append(theta_z)
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
sim_time = 0
time_archive = [0]
theta_z_archive = [0]
while robot.step(timestep) != -1:
    # print("Hello world")
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    # move_forwrd(6.28)
    # Process sensor data here.
    turn_left(6)
    angPosVel()
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    # pass
    sim_time = sim_time + timestep*0.001
    time_archive.append(sim_time)
    print(sim_time)
    if sim_time>=10:
        break
plt.figure()
plt.plot(time_archive, theta_z_archive)
plt.show()
# Enter here exit cleanup code.
