clc, clear, close all

load("Machine Transforms")
load("Tool Transformations")

% Forward slash operator to inverse Ttcp_tool transform


% Grinder approach with portafilter tool
T_grinder_rest / Ttcp_portaRest;

% Grinder Start Button
T_grinder_start / Ttcp_grinderPush;

% Grinder stop button
T_grinder_stop / Ttcp_grinderPush;

% Grinder lever
T_grinder_lever / Ttcp_grinderPull;

% Tamper level
T_tamper_level / Ttcp_portaCenter;

% Tamper press
T_tamper_press / Ttcp_portaCenter;


% Silvia deliver
T_silvia_deliver / Ttcp_portaCenter;

% Silvia Cup
T_silvia_cup / Ttcp_cupCenter;
T_silvia_approach / Ttcp_cupCenter;

%Silvia buttons
T_silvia_but1 / Ttcp_grinderPush

% Cup
T_cup_approach / Ttcp_cupCenter;
T_cup_get / Ttcp_cupCenter;

