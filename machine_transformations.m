% Script to find the equipment transformations and to assign frames to
% the points of interest on the equipment
clc, clear, close all

% Find local frame transformations
% Grinder
grinder_frame_offset = [482.29; -433.74; 314.13];
grinder_rest_global = [370.66; -321.55; 66.86];
grinder_rest_local = [157.61; 0; -250.45];

[Tw_grinder, Rw_grinder, deg_grinder] = zRotation(grinder_frame_offset, grinder_rest_global, grinder_rest_local);

% Tamper stand
tamper_frame_offset = [599.13; 0; 211.07];
tamper_global = [559; 68.77; 156.07];
tamper_local = [-80; 0; -55];

[Tw_tamper, Rw_tamper, deg_tamper] = zRotation(tamper_frame_offset, tamper_global, tamper_local);

% Cups
cups_frame_offset = [1.49; -600.54; -20];
deg_cups = 180;
Rw_cups = rotz(deg_cups);
Tw_cups = [Rw_cups cups_frame_offset; 0 0 0 1];


% Silvia
silvia_frame_offset = [-366.2; -389.8; 341.38];
silvia_pt2_global = [-577.06; -446.46; 341.38];
silvia_pt2_local = [0; 218.0; 0];

[Tw_silvia, Rw_silvia, deg_silvia] = zRotation(silvia_frame_offset, silvia_pt2_global, silvia_pt2_local);


% Find local point transfomrations
% Local points
grinder_rest_local = [157.61; 0; -250.45];
grinder_start_local = [-80.71; 94.26; -227.68];
grinder_stop_local = [-64.42; 89.82; -227.68];
grinder_lever_local = [-35.82; 83.8; -153];

tamper_level_local = [70; 0; -32]; 
tamper_press_local = [-80; 0; -55];

cup_approach_local = [0; -100; 204];
cup_get_local = [0; 0; 204];

silvia_cup_local = [-10; 55.00; -201.38];
silvia_approach_local = [150; 55.00; -201.38];

silvia_but1_local = [50.67; 98.75; -27.89];
silvia_but2_local = [50.67; 35.75; -27.89];
silvia_but3_local = [50.67; 35.75; -61.39];
silvia_but4_local = [50.67; 35.75; -94.89];

% Global points
grinder_rest_global = Tw_grinder*[grinder_rest_local;1];
grinder_start_global = Tw_grinder*[grinder_start_local;1];
grinder_stop_global = Tw_grinder*[grinder_stop_local;1];
grinder_lever_global = Tw_grinder*[grinder_lever_local;1];

tamper_level_global = Tw_tamper*[tamper_level_local;1];
tamper_press_global = Tw_tamper*[tamper_press_local;1];

cup_approach_global = Tw_cups*[cup_approach_local;1];
cup_get_global = Tw_cups*[cup_get_local;1];

silvia_cup_global = Tw_silvia*[silvia_cup_local;1];
silvia_approach_global = Tw_silvia*[silvia_approach_local;1];

silvia_but1_global = Tw_silvia*[silvia_but1_local;1];

% Define transformation matricies, need to determine the orientation of the
% frames
T_grinder_rest = [rotz(deg_grinder)*roty(-90) grinder_rest_global(1:3); 0 0 0 1];
T_grinder_start = [roty(90)*rotx(-32.5) grinder_start_global(1:3); 0 0 0 1];
T_grinder_stop = [roty(90)*rotx(-32.5) grinder_stop_global(1:3); 0 0 0 1];
T_grinder_lever = [rotz(45)*rotx(-90) grinder_lever_global(1:3); 0 0 0 1];

T_tamper_level_local = [roty(-90)*rotx(-90) tamper_level_local; 0 0 0 1];
T_tamper_press_local = [roty(-90)*rotx(-90) tamper_press_local; 0 0 0 1];

T_tamper_level = Tw_tamper*T_tamper_level_local;
T_tamper_press = Tw_tamper*T_tamper_press_local;

T_cup_approach = [rotz(90)*roty(-90) cup_approach_global(1:3); 0 0 0 1];
T_cup_get = [rotz(90)*roty(-90) cup_get_global(1:3); 0 0 0 1];

T_silvia_cup = [rotz(105)*roty(-90) silvia_cup_global(1:3); 0 0 0 1];
T_silvia_approach = [rotz(90)*roty(-90) silvia_approach_global(1:3); 0 0 0 1];
T_silvia_but1 = [rotz(15)*rotx(90) silvia_but1_global(1:3); 0 0 0 1];

% Silvia deliver
silvia_deliver_global = [-150; -300; 300];
T_silvia_deliver = [roty(-90)*rotx(-45) silvia_deliver_global; 0 0 0 1];


save('Machine Transforms')