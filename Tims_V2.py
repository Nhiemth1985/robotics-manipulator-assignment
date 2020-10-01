# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import numpy as np
RDK = Robolink()


# Initialize
robot = RDK.Item('UR5')
world_frame = RDK.Item('UR5 Base')
target_home = RDK.Item('Home')

robot.setPoseFrame(world_frame)
robot.setPoseTool(robot.PoseTool())


# Targets
grinder_approach = RDK.Item('Lux Rest Approach')
grinder_mate = RDK.Item('Lux Rest Mated')

# Custom Targets
intermediate = [-80.640000, -85.030000, -72.070000, -113.070000, 89.500000, -185.690000]
grinder_intermediate = [-6.476325, -81.638717, -149.649052, -111.057543, -37.627386, 133.643]

# Note for the report: finding appropriate intermediate joint angles sometimes required finding
#   the opposite equivalent angle to make it easier to move between joint angles without hitting anything
grinder_rest_approach = [-13.815385, -92.211762, -144.12, -114.908578, -58.969983, 135.458]
grinder_stop_approach = [-61.107196, -148.511559, -51.002562, -160.515472, 176.405029, -40.031784]
grinder_start_approach = [-61.208056, -145.437313, -57.067153, -157.524321, 176.304169, -40.030976]
grinder_stop_press = [-58.752518, -147.601066, -52.803127, -159.681532, 178.759706, -40.087954]
grinder_start_press = [-58.787624, -144.584541, -58.741238, -156.757587, 178.724600, -40.085595]

grinder_lever_approach = [-50.601499, -119.661808, -91.614578, -148.721936, -110.601373, -129.997491]
grinder_lever_pull_0 = [-48.257997, -115.858025, -97.690815, -146.449506, -108.257871, -129.997563]
grinder_lever_pull_1 = [-46.489258, -111.275445, -104.688084, -144.035216, -97.295584, -129.997695]
#grinder_lever_pull_2 = [-39.433879, -103.776906, -114.550852, -141.671506, -76.958955, -129.997793]
grinder_lever_pull_2 = [-36.615796, -101.373065, -117.680736, -140.945553, -71.640872, -129.997801]

tamper_level_approach = [-8.063858, -114.463801, -111.981385, -124.030028, -127.943230, 145.889671]
tamper_press_approach = [130.247688, -87.550834, -208.082242, -101.577011, 12.462490, 176.553340]
tamper_level_1 = [-8.063843, -112.915219, -111.371733, -126.188263, -127.943216, 145.889668]
tamper_level_2 = [-18.107326, -106.294823, -121.562597, -120.935006, -137.824646, 148.353094]
tamper_press_1 = [148.796873, -79.567094, -222.797280, -73.042598, 29.420526, 153.496873]
tamper_press_2 = [7.321906, -98.160660, -134.443571, -119.261240, -112.735810, 143.161025]

bstart_approach_np = np.array([
    
 [  -0.4116   ,-0.3454  ,  0.8434 , 385.6817],
 [   0.6461 ,   0.5421  ,  0.5373, -612.6833],
  [ -0.6428 ,   0.7660  ,       0,   86.4500],
  [       0   ,      0  ,       0  ,  1.0000]],)

bstop_approach_np = np.array([
      [ -0.4116  , -0.3454    ,0.8434 , 377.3392],
      [  0.6461  ,  0.5421   , 0.5373 ,-598.0040],
      [ -0.6428  ,  0.7660   ,      0 ,  86.4500],
      [       0  ,       0   ,      0 ,   1.0000]])

rest_approach_np = np.array([
  [ -0.6022,   -0.3851 ,   0.6993,  348.9033],
   [-0.4808 ,  -0.5243  , -0.7028 ,-299.6841],
    [0.6373 ,  -0.7595  ,  0.1305 ,  91.8089],
     [    0 ,        0   ,      0 ,   1.0000]])

lever_approach_np = np.array([

  [  0.4545  , -0.5417 ,   0.7071 , 436.0883],
  [  0.4545 ,  -0.5417 ,  -0.7071, -435.4650],
   [ 0.7660  ,  0.6428  ,       0 , 161.1300],
   [      0  ,       0  ,       0 ,   1.0000]])

level_approach_np = np.array([
 [   0.3136 ,   0.4103 ,   0.8563,  510.9815],
 [  -0.7039  , -0.5048  ,  0.4997, -132.4847],
 [   0.6373  , -0.7595  ,  0.1305 , 155.5053],
  [       0  ,       0  ,       0  ,  1.0000]])

tamp_approach_np = np.array([
  [  0.3136 ,   0.4103  ,  0.8563,  435.3809],
 [  -0.7039 ,  -0.5048  ,  0.4997 ,  -2.9294],
  [  0.6373  , -0.7595   , 0.1305  ,132.5053],
   [      0  ,       0  ,       0 ,   1.0000]])


bstart_approach = Mat(bstart_approach_np.tolist())
bstop_approach = Mat(bstop_approach_np.tolist())
rest_approach = Mat(rest_approach_np.tolist())
lever_approach = Mat(lever_approach_np.tolist())
level_approach = Mat(level_approach_np.tolist())
tamp_approach = Mat(tamp_approach_np.tolist())

##robot.MoveJ(tamp_approach, True)
##robodk.pause(2)

# Move robot to home
robot.MoveJ(target_home, blocking=True)

# Pick up portafilter tool
robot.MoveJ(intermediate)
RDK.RunProgram('Portafilter Tool Attach (Stand)', True)
robot.MoveJ(intermediate, blocking=True)

# Place portafilter in Grinder
robot.MoveJ(grinder_intermediate, True)
robot.MoveJ(grinder_rest_approach, True)
robot.MoveL(grinder_approach, True)
robot.MoveL(grinder_mate, True)
RDK.RunProgram('Portafilter Tool Detach (Grinder)', True)
robot.MoveL(grinder_rest_approach, True)

### Pick up grinder tool
##robot.MoveJ(intermediate, True)
##RDK.RunProgram('Grinder Tool Attach (Stand)', True)
##robot.MoveJ(intermediate, True)
##
### Press grinder start button
##robot.MoveJ(grinder_start_approach, True)
##robot.MoveL(grinder_start_press, True)
##robot.MoveL(grinder_start_approach, True)
##robodk.pause(2)
##
### Press grinder stop button
##robot.MoveJ(grinder_stop_approach, True)
##robot.MoveL(grinder_stop_press, True)
##robot.MoveL(grinder_stop_approach, True)
##
### Pull grinder lever
##robot.MoveJ([-50.993480, -116.190224, -77.674069, -166.148459, 43.464147, -83.291969], True)
##robot.MoveJ(grinder_lever_approach, True)
##
##robot.MoveJ(grinder_lever_pull_0, True)
##robot.MoveL(grinder_lever_pull_1, True)
###robodk.pause(1)
##robot.MoveL(grinder_lever_pull_2, True)
##robodk.pause(1)
##robot.MoveL(grinder_lever_pull_0, True)
##robot.MoveJ(grinder_lever_approach, True)
##
### Return grinder tool to stand
##robot.MoveJ(intermediate, True)
##RDK.RunProgram('Grinder Tool Detach (Stand)', True)
##robot.MoveJ(intermediate, True)

# Pick portafilter up from grinder
robot.MoveJ(grinder_intermediate, True)
robot.MoveJ(grinder_rest_approach, True)
RDK.RunProgram("Portafilter Tool Attach (Grinder)", True)
robot.MoveL(grinder_rest_approach, True)

# Scrape coffee grinds
robot.MoveJ(tamper_level_approach, True)
robot.MoveJ(tamper_level_1, True)
robot.MoveL(tamper_level_2, True)

# Tamp coffee
robot.MoveL(tamper_press_approach, True)
robot.MoveL(tamper_press_1, True)
robot.MoveL(tamper_press_2, True)
robot.MoveL(tamper_press_1, True)
robot.MoveL(tamper_press_approach, True)

# Move to Silvia
#robot.MoveJ(silvia_deliver, True)


##robot.MoveJ(intermediate, True)
##RDK.RunProgram("Portafilter Tool Detach (Stand)", True)




# TESTING custom targets
##robot.MoveJ(grinder_start_press, True)
##robodk.pause(1)
##robot.MoveJ(grinder_stop_press, True)
##robodk.pause(1)
##robot.MoveJ(grinder_lever_pull_0, True)
##robodk.pause(1)
##robot.MoveJ(grinder_lever_pull_1, True)
##robodk.pause(1)
##robot.MoveJ(grinder_lever_pull_2, True)
##robodk.pause(1)
##robot.MoveJ(grinder_rest_approach, True)





