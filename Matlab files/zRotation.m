function [T, Rz, deg] = zRotation(global_pt1, global_pt2, local_pt2)
%ZROTATION Returns the rotation matrix relating Frame A to Frame B
%   Requries two points in the global frame that are along the same axis of
%   the local frame
%   global_pt2 must be the same point as local_pt2
%   local_pt2 is used to determine which axis is defined by the two global
%   poiints, and in what direction
%   Assumes there is a roation about the z axis
%   Assumes global_pt1 is the origin of Frame B in global coords


for i = 1:3
    if (local_pt2(i) == 0)
        break
    end
end

% Determines which axis is defined by the two global points
if (i == 1)
    k = 2;
elseif (i == 2)
    k = 1;
end

% Ignore z
if (local_pt2(k) > 0)
    local_ax = global_pt2(1:2) - global_pt1(1:2);
else
    local_ax = global_pt1(1:2) - global_pt2(1:2);
end

% Normalize
local_ax = local_ax ./ norm(local_ax);

if (i == 1)
    dot_p = dot([0;1], local_ax);
elseif (i == 2)
    dot_p = dot([1;0], local_ax);
end

rad = acos(dot_p);
deg = acosd(dot_p);

% If the two global points define an axis in the negative direction, 
% flip it to get the positive direction
if (local_pt2(k) < 0)
    rad = 2*pi - rad;
    deg = 360 - deg;
end
    

Rz = [cos(rad) -sin(rad) 0;sin(rad) cos(rad) 0; 0 0 1];

T = [Rz global_pt1; 0 0 0 1];

end

