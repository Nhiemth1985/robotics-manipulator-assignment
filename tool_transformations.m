clc, clear, close all

Rtcp_tool = rotz(-50);
noRot = rotz(0);

% Grinder tool
Ttcp_grinderTool = [Rtcp_tool [0; 0; 0]; 0 0 0 1];
TgrinderTool_push = [noRot [0; 0; 102.82]; 0 0 0 1];
TgrinderTool_pull = [rotx(180) [-50; 0; 67.06]; 0 0 0 1];

Ttcp_grinderPush = Ttcp_grinderTool*TgrinderTool_push;
Ttcp_grinderPull = Ttcp_grinderTool*TgrinderTool_pull;

% Portafilter tool
Ttcp_portaTool = [Rtcp_tool [0; 0; 0]; 0 0 0 1];
TportaTool_rest = [roty(-7.5) [-32; 0; 27.56]; 0 0 0 1];
TportaTool_center = [roty(-7.5) [4.71; 0; 144.76]; 0 0 0 1];

Ttcp_portaRest = Ttcp_portaTool*TportaTool_rest;
Ttcp_portaCenter = Ttcp_portaTool*TportaTool_center;

% Cup tool
Tc_center = [Rtcp_tool [-47; 0; 186.11]; 0 0 0 1];

save("Tool Transformations")

