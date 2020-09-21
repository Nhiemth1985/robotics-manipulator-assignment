clc, clear, close all

% Grinder
pt1_g = [482.29; -433.74; 314.13];
pt2_g = [370.66; -321.55; 66.86];
pt2_l = [157.61; 0; -250.45];

[T_grinder, R_grinder, deg_grinder] = zRotation(pt1_g, pt2_g, pt2_l);


% Tamper stand
pt1_g = [599.13; 0; 211.07];
pt2_g = [559; 68.77; 156.07];
pt2_l = [-80; 0; -55];

[T_tamper, R_tamper, deg_tamper] = zRotation(pt1_g, pt2_g, pt2_l);

% Cups
pt1_g = [1.49; -600.54; -20];


% Silvia
pt1_g = [-366.2; -389.8; 341.38];
pt2_g = [-577.06; -446.46; 341.38];
pt2_l = [0; 218.0; 0];

[T_silvia, R_silvia, deg_silvia] = zRotation(pt1_g, pt2_g, pt2_l);