clc, clear, close all

load("Machine Transforms")
load("Tool Transformations")

% Forward slash operator to inverse Ttcp_tool transform


% Grinder approach with portafilter tool
T_grinder_rest / Ttcp_portaRest

% Grinder Start Button
T_grinder_start / Ttcp_grinderPush;

% Grinder stop button
T_grinder_stop / Ttcp_grinderPush;

