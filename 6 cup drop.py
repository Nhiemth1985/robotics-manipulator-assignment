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
#intermediate_pt2 = [38.290695, -103.137039, 114.532374, -61.135172, 67.923789, -79.650850]
intermediate_pt2 = [70.150000, -94.990000, 72.160000, -67.260000, -90.5200000, 145.100000]
intermediate_pt3 = [86.300000, -93.210000, 61.070000, -36.250000, 162.340000, 139.000000]
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
grinder_lever_pull_2 = [-33.143411, -98.457705, -121.299577, -140.242213, -64.418488, -129.997781]
#grinder_lever_pull_2 = [-35.891320, -99.516541, -120.008226, -140.474584, -70.916396, -129.997810]

tamper_level_approach = [-9.244861, -113.499031, -113.575156, -123.244162, -129.107685, 146.141503]
tamper_press_approach = [130.247688, -87.550834, -208.082242, -101.577011, 12.462490, 176.553340]
tamper_level_1 = [-9.244831, -110.400855, -112.261502, -127.655996, -129.107656, 146.141497]
tamper_level_2 = [-18.107311, -104.576578, -120.812969, -123.402882, -137.824630, 148.353090]
tamper_press_1 = [148.796873, -79.567094, -222.797280, -73.042598, 29.420526, 153.496873]
tamper_press_2 = [7.321906, -98.160660, -134.443571, -119.261240, -112.735810, 143.161025]

silvia_deliver_1 = [-22.012830, -96.710934, -146.480964, -65.766794, -9.661230, 89.359257]
silvia_deliver_2 = [-72.300000, -119.290000, -109.030000, 39.900000, -45.000000, -36.140000]

cup_get_1 = [ 53.324239, -97.393798, 156.574035, -59.180493, 53.324034, -39.999341]
#cup_get_1 = [-53.324707, -82.606202, -156.574035, -120.819507, -53.324912, -39.999647]
cup_get_2 = [ 67.303327, -82.065674, 141.093869, -59.028418, 67.303122, -39.999409]
cup_got_1 = [ 67.303327, -97.012459, 134.231551, -37.219315, 67.303122, -39.999409]
cup_got_2 = [ 50.808510, -120.143402, 147.951690, -27.808553, 50.808305, -39.999327]
#cup_got_3 = [ 54.453591, -123.107305, 134.504375, -11.397323, 54.453386,  140.000]
cup_got_3 = [54.453591, -123.107305, 134.504375, -11.397323, 54.453386, 140.000000]

silvia_cup_1 = [86.524128, -95.697888, 131.839344, -36.141440, 162.774137, 140.000002]
#silvia_cup_2 = [52.710196, -85.775029, 123.476767, 322.536165, -231.039405, 140.000188]  #might need to be better
silvia_cup_2 = [-91.877414, -92.664577, -121.998134, -146.024001, -15.627840, 140.511925]

#silvia_but_all_a=[-11.223930, -81.315641, 128.851895, -227.53688,  26.231573, -130.001561]
silvia_but_all_a=[-11.223930, -96.652221, 112.051698, -15.400103, -26.231573, 49.998439]

silvia_but_2_a = [ -1.517778, -65.017866, 104.515054, 140.501838, 16.525420, -130.001191]
silvia_but_2_c = [  2.512836, -65.136388, 104.703740, 140.431369, 12.494806, -130.000875]
silvia_but_2_off=[  2.512839, -64.689016, 104.940262, 139.747474, 12.494804, -130.000875]
silvia_but_2_on= [  2.512835, -65.576850, 104.458604, 141.116966, 12.494808, -130.000875]

#cup_drop_1 = [47.441334, -130.826791, 150.195265, 340.630484, -265.058656, 139.999631]
cup_drop_1 = [4.074385, -112.974729, 148.826667, 324.105159, -357.175603, 140.041143]
cup_drop_2 = [4.071791, -124.418215, 125.024500, 359.350773, -357.178197, 140.041182]
cup_dest = [42.231462, -82.043086, 134.097959, -52.055087, 42.231603, 138.748587]

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

silvia_approach_np = np.array([
   [ 0.6010 ,   0.3838 ,  -0.7011,  -48.9496],
    [0.4823 ,   0.5252 ,   0.7011, -401.0504],
   [ 0.6373  , -0.7595  ,  0.1305 , 276.4353],
     [    0  ,       0  ,       0 ,   1.0000]])


bstart_approach = Mat(bstart_approach_np.tolist())
bstop_approach = Mat(bstop_approach_np.tolist())
rest_approach = Mat(rest_approach_np.tolist())
lever_approach = Mat(lever_approach_np.tolist())
level_approach = Mat(level_approach_np.tolist())
tamp_approach = Mat(tamp_approach_np.tolist())
silvia_approach = Mat(silvia_approach_np.tolist())

# Move robot to home
##robot.MoveJ(target_home, blocking=True)
##
### Pick up portafilter tool
##robot.MoveJ(intermediate)
##RDK.RunProgram('Portafilter Tool Attach (Stand)', True)
##robot.MoveJ(intermediate, blocking=True)
##
### Place portafilter in Grinder
##robot.MoveJ(grinder_intermediate, True)
##robot.MoveJ(grinder_rest_approach, True)
##robot.MoveL(grinder_approach, True)
##robot.MoveL(grinder_mate, True)
##RDK.RunProgram('Portafilter Tool Detach (Grinder)', True)
##robot.MoveL(grinder_rest_approach, True)
##
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
##robot.MoveL(grinder_lever_pull_2, True)
##robot.MoveL(grinder_lever_pull_1, True)
##robot.MoveL(grinder_lever_pull_0, True)
##
##robot.MoveL(grinder_lever_pull_1, True)
##robot.MoveL(grinder_lever_pull_2, True)
##robot.MoveL(grinder_lever_pull_1, True)
##robot.MoveL(grinder_lever_pull_0, True)
##
##robot.MoveL(grinder_lever_pull_1, True)
##robot.MoveL(grinder_lever_pull_2, True)
##robot.MoveL(grinder_lever_pull_1, True)
##robot.MoveL(grinder_lever_pull_0, True)
##robot.MoveJ(grinder_lever_approach, True)
##
### Return grinder tool to stand
##robot.MoveJ(intermediate, True)
##RDK.RunProgram('Grinder Tool Detach (Stand)', True)
##robot.MoveJ(intermediate, True)
##
# Pick portafilter up from grinder
##robot.MoveJ(grinder_intermediate, True)
##robot.MoveJ(grinder_rest_approach, True)
##RDK.RunProgram("Portafilter Tool Attach (Grinder)", True)
##robot.MoveL(grinder_rest_approach, True)
##
### Scrape coffee grinds
##robot.MoveJ(tamper_level_approach, True)
##robot.MoveJ(tamper_level_1, True)
##robot.MoveL(tamper_level_2, True)
##
### Tamp coffee
##robot.MoveL(tamper_press_approach, True)
##robot.MoveL(tamper_press_1, True)
##robot.MoveL(tamper_press_2, True)
##robot.MoveL(tamper_press_1, True)
##robot.MoveL(tamper_press_approach, True)
##
### Move to Silvia
##robot.MoveL(silvia_deliver_1, True)
##robot.MoveL(silvia_deliver_2, True)
##robodk.pause(30)
##
##
# Pick up cup tool
##robot.MoveJ(intermediate, blocking=True)
##RDK.RunProgram('Cup Tool Attach (Stand)', True)
##robot.MoveJ(intermediate, blocking=True)
##robot.MoveJ(intermediate_pt2, blocking=True)
##
### Get cup
##robot.MoveJ(cup_get_1, blocking=True)
##RDK.RunProgram('Cup Tool Open', True)
##robot.MoveL(cup_get_2, blocking=True)
##RDK.RunProgram('Cup Tool Close', True)
##    #lift
##robot.MoveL(cup_got_1, blocking=True)
##    #back
##robot.MoveL(cup_got_2, blocking=True)
##robot.MoveJ(cup_got_3, blocking=True)
##    #approach silvia
##robot.MoveJ(silvia_cup_1, blocking=True) 
##    #place cup
##robot.MoveL(silvia_cup_2, blocking=True)
##RDK.RunProgram('Cup Tool Open', True)
##robot.MoveL(silvia_cup_1, blocking=True)
##RDK.RunProgram('Cup Tool Close', True)
##    #lose tool
##robot.MoveJ(intermediate_pt3, blocking=True)
##RDK.RunProgram('Cup Tool Detach (Stand)', True)
##    #get button presser
##RDK.RunProgram('Grinder Tool Attach (Stand)', True)
##robot.MoveJ(intermediate, blocking=True)
##robot.MoveJ(intermediate_pt2, blocking=True)
##    #press buttons
##robot.MoveJ(silvia_but_all_a, blocking=True)
##    #button
##robot.MoveL(silvia_but_2_a, blocking=True)
##robot.MoveL(silvia_but_2_on, blocking=True)
##robot.MoveL(silvia_but_2_a, blocking=True)
##    #wait
##robodk.pause(3)
##    #button
##robot.MoveL(silvia_but_2_a, blocking=True)
##robot.MoveL(silvia_but_2_off, blocking=True)
##robot.MoveL(silvia_but_2_a, blocking=True)
##    #escape
##robot.MoveL(silvia_but_all_a, blocking=True)
##    #drop tool
##robot.MoveJ(intermediate_pt2, blocking=True)
##RDK.RunProgram('Grinder Tool Detach (Stand)', True)
    #get cup tool
RDK.RunProgram('Cup Tool Attach (Stand)', True)
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(intermediate_pt2, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
    #get cup of coffee
robot.MoveJ(cup_got_3, blocking=True)
robot.MoveJ(silvia_cup_1, blocking=True)
robot.MoveL(silvia_cup_2, blocking=True)
RDK.RunProgram('Cup Tool Close', True)
robot.MoveL(silvia_cup_1, blocking=True)
    #place cup on table
robot.MoveL(cup_drop_1, blocking=True)
robot.MoveL(cup_dest, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
robot.MoveL(cup_drop_1, blocking=True)
RDK.RunProgram('Cup Tool Close', True)
robot.MoveL(cup_drop_2, blocking=True)
    #return tool
robot.MoveJ(intermediate_pt2, blocking=True)
RDK.RunProgram('Cup Tool Detach (Stand)', True)
    #be done
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(target_home, blocking=True)
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





