% Assigning frames to points of interest on the coffee making tools
% with reference to the UR5 master tool frame
% Calculates and saves the HT for each point on each tool

clc, clear, close all

% All tools have a -50 deg rotation from the master tool frame, 0 offset
Ttcp_tool = [rotz(-50) [0; 0; 0]; 0 0 0 1];

% Grinder tool
Ttcp_grinderTool = Ttcp_tool
TgrinderTool_push = [zeros(3) [0; 0; 102.82]; 0 0 0 1];
TgrinderTool_pull = [roty(180) [-50; 0; 67.06]; 0 0 0 1];

Ttcp_grinderPush = Ttcp_grinderTool*TgrinderTool_push;
Ttcp_grinderPull = Ttcp_grinderTool*TgrinderTool_pull;

% Portafilter tool
Ttcp_portaTool = Ttcp_tool;
TportaTool_rest = [roty(-7.5) [-32; 0; 27.56]; 0 0 0 1];
TportaTool_center = [roty(-7.5) [4.71; 0; 144.76]; 0 0 0 1];

Ttcp_portaRest = Ttcp_portaTool*TportaTool_rest;
Ttcp_portaCenter = Ttcp_portaTool*TportaTool_center;

% Cup tool
Ttcp_cupTool = Ttcp_tool;
TcupTool_center = [noRot [-47; 0; 186.11]; 0 0 0 1];
Ttcp_cupCenter = Ttcp_cupTool*TcupTool_center;


save("Tool Transformations")

