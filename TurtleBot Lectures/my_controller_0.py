"""my_controller_0 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

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

def move_forwrd(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(speed)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(speed)
    
def turn_left(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(speed)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(speed/3)
def turn_right(speed):
    rwm.setPosition(float("inf"))
    rwm.setVelocity(speed/3)
    lwm.setPosition(float("inf"))
    lwm.setVelocity(speed)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # print("Hello world")
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    # move_forwrd(6.28)
    # Process sensor data here.
    turn_left(6.28)
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    # pass

# Enter here exit cleanup code.
