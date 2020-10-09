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
#swap between intermediate and int...pt2 to change elbow direction for easier access to silvia
intermediate = [-80.640000, -85.030000, -72.070000, -113.070000, 89.500000, -185.690000]
intermediate_pt2 = [38.290695, -103.137039, 114.532374, -61.135172, 67.923789, -79.650850]
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
#grinder_lever_pull_2 = [-39.433879, -103.776906, -114.550852, -141.671506, -76.958955, -129.997793]
grinder_lever_pull_2 = [-36.615796, -101.373065, -117.680736, -140.945553, -71.640872, -129.997801]

tamper_level_approach = [-8.063858, -114.463801, -111.981385, -124.030028, -127.943230, 145.889671]
tamper_press_approach = [130.247688, -87.550834, -208.082242, -101.577011, 12.462490, 176.553340]
tamper_level_1 = [-8.063843, -112.915219, -111.371733, -126.188263, -127.943216, 145.889668]
tamper_level_2 = [-18.107326, -106.294823, -121.562597, -120.935006, -137.824646, 148.353094]
tamper_press_1 = [148.796873, -79.567094, -222.797280, -73.042598, 29.420526, 153.496873]
tamper_press_2 = [7.321906, -98.160660, -134.443571, -119.261240, -112.735810, 143.161025]

silvia_deliver_1 = [-22.012830, -96.710934, -146.480964, -65.766794, -9.661230, 89.359257]
silvia_deliver_2 = [-72.302374, -107.859273, 266.687385, -167.255511, -297.054130, 143.855340]

#cup_get_1 = [-53.09,  -94.54, -158.58, 73.12, 53.09, -40.00]
#cup_get_2 = [-67.09, -105.09, -142.27, 67.36, 67.09, -40.00]
#cup_got_1 = [-67.09,  -87.74, -137.06, 44.80, 67.09, -40.00]
#cup_got_2 = [-53.10,  -68.21, -150.70, 38.91, 53.10, 140.00]
cup_get_1 = [ 53.324239, -97.393798, 156.574035, -59.180493, 53.324034, -39.999341]
#cup_get_1 = [-53.324707, -82.606202, -156.574035, -120.819507, -53.324912, -39.999647]
cup_get_2 = [ 67.303327, -82.065674, 141.093869, -59.028418, 67.303122, -39.999409]
cup_got_1 = [ 67.303327, -97.012459, 134.231551, -37.219315, 67.303122, -39.999409]
cup_got_2 = [ 50.808510, -120.143402, 147.951690, -27.808553, 50.808305, -39.999327]
#cup_got_3 = [ 54.453591, -123.107305, 134.504375, -11.397323, 54.453386,  140.000]
cup_got_3 = [54.453591, -123.107305, 134.504375, -11.397323, 54.453386, 140.000000]

#silvia_cup_1 = [-23.975574, -61.085049, 105.484535, -44.399486, -23.975574, -40.002176]
#silvia_cup_2 = [0.244494, -55.349720, 95.334369, -39.984645, -19.755506, -40.002181]
#silvia_cup_1 = [86.524128, -95.697889, 131.839345, 323.858559, -197.225863, 140.000000]
#silvia_cup_1 = [-50.192258, -115.061650, -140.975626, 76.037287, -26.057751, -40.000023]
silvia_cup_1 = [86.524128, -95.697888, 131.839344, -36.141440, 162.774137, 140.000002]
#silvia_cup_2 = [52.710196, -85.775029, 123.476767, 322.536165, -231.039405, 140.000188]  #might need to be better
silvia_cup_2 = [-91.877414, -94.319312, -123.373899, -142.993502, -15.627841, 140.511926]

silvia_but_all_a=[-11.223930, -81.315641, 128.851895, 132.463120,  26.231573, -130.001561]

silvia_but_1_a = [  0.667095, -58.565224,  94.804271, 143.759837,  14.340548, -130.001041]
silvia_but_1_c = [  3.369485, -58.084892,  93.985987, 144.097533,  11.638158, -130.000780]
silvia_but_1_on= [  3.784337, -57.829304,  95.368749, 142.459133,  11.223306, -130.000729]
silvia_but_1_off=[  3.784333, -59.039831,  94.705995, 144.332414,  11.223310, -130.000729]

silvia_but_2_a = [ -1.517774, -64.571542, 104.751372, 139.819197,  16.525416, -130.001191]
silvia_but_2_c = [  1.932265, -64.688816, 104.939937, 139.747656,  13.075378, -130.000932]
silvia_but_2_on= [  2.512842, -63.773848, 105.387370, 138.385199,  12.494801, -130.000875]
silvia_but_2_off=[  2.512837, -65.136388, 104.703740, 140.431368,  12.494806, -130.000875]

cup_drop_1 = [47.441334, -130.826791, 150.195265, 340.630484, -265.058656, 139.999631]
cup_drop_2 = [4.074385, -112.974729, 148.826667, 324.105159, -357.175603, 140.041143]
cup_dest = [42.231443, -82.043133, 134.097830, -52.054697, 42.231443, 138.747817]


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

cup_approach_np = np.array([
   [-0.7660  , -0.6428  ,       0 ,   1.4900],
    [     0  ,       0  , -1.0000 ,-314.4300],
   [ 0.6428  , -0.7660  ,       0 , 231.0000],
     [    0  ,       0  ,       0 ,   1.0000]])

cup_get_np = np.array([
   [-0.7660  , -0.6428  ,       0 ,   1.4900],
    [     0  ,       0  , -1.0000 ,-414.4300],
   [ 0.6428  , -0.7660  ,       0 , 231.0000],
     [    0  ,       0  ,       0 ,   1.0000]])

silvia_cup_np = np.array([
   [-0.7399  , -0.6209  ,  0.2588 ,-464.8896],
   [-0.1983  , -0.1664  , -0.9659 ,-233.9617],
   [ 0.6428  , -0.7660  ,       0 , 187.0000],
   [      0  ,       0  ,       0 ,   1.0000]])

silvia_capproach_np = np.array([
   [-0.7660  , -0.6428  ,       0 ,-458.2414],
   [      0  ,       0  , -1.0000 , -73.1014],
   [ 0.6428  , -0.7660  ,       0 , 187.0000],
   [      0  ,       0  ,       0 ,   1.0000]])

silvia_but1_np = np.array([
   [ 0.6209  , -0.7399  ,  0.2588 ,-501.3279],
   [ 0.1664  , -0.1983  , -0.9659 ,-267.1753],
   [ 0.7660  ,  0.6428  ,       0 , 313.4900],
   [      0  ,       0  ,       0 ,   1.0000]])

bstart_approach = Mat(bstart_approach_np.tolist())
bstop_approach = Mat(bstop_approach_np.tolist())
rest_approach = Mat(rest_approach_np.tolist())
lever_approach = Mat(lever_approach_np.tolist())
level_approach = Mat(level_approach_np.tolist())
tamp_approach = Mat(tamp_approach_np.tolist())
silvia_approach = Mat(silvia_approach_np.tolist())
cup_approach = Mat(cup_approach_np.tolist())
cup_get = Mat(cup_get_np.tolist())
silvia_cup = Mat(silvia_cup_np.tolist())
silvia_capproach = Mat(silvia_capproach_np.tolist())
silvia_but1 = Mat(silvia_but1_np.tolist())

##robot.MoveJ(silvia_approach, True)
##robodk.pause(2)

# Move robot to home
robot.MoveJ(target_home, blocking=True)

#Aidan Code Start
     #Pick up cup tool
robot.MoveJ(intermediate, blocking=True)
RDK.RunProgram('Cup Tool Attach (Stand)', True)
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(intermediate_pt2, blocking=True)
    #Get cup
robot.MoveJ(cup_get_1, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
robot.MoveL(cup_get_2, blocking=True)
RDK.RunProgram('Cup Tool Close', True)
    #lift
robot.MoveL(cup_got_1, blocking=True)
    #back
robot.MoveL(cup_got_2, blocking=True)
robot.MoveJ(cup_got_3, blocking=True)
    #approach silvia
robot.MoveJ(silvia_cup_1, blocking=True) #problem here. also note: am approaching from the side because it seemed better in the model. This might need to be changed
    #place cup
robot.MoveL(silvia_cup_2, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
robot.MoveL(silvia_cup_1, blocking=True)
RDK.RunProgram('Cup Tool Close', True)
    #lose tool
robot.MoveJ(intermediate_pt3, blocking=True)
RDK.RunProgram('Cup Tool Detach (Stand)', True)
    #get button presser
RDK.RunProgram('Grinder Tool Attach (Stand)', True)
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(intermediate_pt2, blocking=True)
    #press buttons
robot.MoveJ(silvia_but_all_a, blocking=True)
    #button 1
robot.MoveL(silvia_but_1_a, blocking=True)
robot.MoveL(silvia_but_1_on, blocking=True)
robot.MoveL(silvia_but_1_a, blocking=True)
    #button 2
robot.MoveL(silvia_but_2_a, blocking=True)
robot.MoveL(silvia_but_2_on, blocking=True)
robot.MoveL(silvia_but_2_a, blocking=True)
    #wait
robodk.pause(3)
    #button 2
robot.MoveL(silvia_but_2_a, blocking=True)
robot.MoveL(silvia_but_2_off, blocking=True)
robot.MoveL(silvia_but_2_a, blocking=True)
    #button 1
robot.MoveL(silvia_but_1_a, blocking=True)
robot.MoveL(silvia_but_1_off, blocking=True)
robot.MoveL(silvia_but_1_a, blocking=True)
robot.MoveL(silvia_but_all_a, blocking=True)
    #drop tool
RDK.RunProgram('Grinder Tool Detach (Stand)', True)
    #get cup tool
RDK.RunProgram('Cup Tool Attach (Stand)', True)
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(intermediate_pt2, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
    #get cup of coffee
robot.MoveJ(cup_got_3, blocking=True)
robot.MoveJ(silvia_cup_1, blocking=True) #problem here
robot.MoveL(silvia_cup_2, blocking=True)
RDK.RunProgram('Cup Tool Close', True)
robot.MoveL(silvia_cup_1, blocking=True)
    #place cup on table
robot.MoveL(cup_drop_1, blocking=True)
robot.MoveL(cup_drop_2, blocking=True)
robot.MoveL(cup_dest, blocking=True)
RDK.RunProgram('Cup Tool Open', True)
robot.MoveL(cup_drop_2, blocking=True)
    #return tool
robot.MoveJ(intermediate, blocking=True) #problem here
RDK.RunProgram('Cup Tool Close', True)
RDK.RunProgram('Cup Tool Detach (Stand)', True)
    #be done
robot.MoveJ(intermediate, blocking=True)
robot.MoveJ(target_home, blocking=True)