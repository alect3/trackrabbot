classdef Car2
    %Car: simulates the RC cars kinamatics
    %   Detailed explanation goes here
    
    properties
        %input
        steering_angle= 0;
        velocity = 0;

        %perameters
        max_angle=15/180*pi;
        max_velocity=50/3.6;
        max_acceleration=0;
        wheel_base = 0.255;

        %properties
        x = 0;
        y = 0;
        headding = 0;
    end
    
    methods
        function obj = Car2()
            obj.steering_angle= 0;
            obj.velocity = 0;

            %properties
            obj.x = 0;
            obj.y = 0;
            obj.headding = 0;
        end
        function obj = setloc(obj,x,y,theta)%set global x,y,heading
            %properties
            obj.x = x;
            obj.y = y;
            obj.headding = theta/180*pi;
        end
        
        function [x, y,theta] = getpos(obj)
            x = obj.x;
            y = obj.y;
            theta = obj.headding;
        end
        
        function obj = input(obj, vel,angle)
            if(vel>180)
                vel = 180;
            elseif(vel<0)
                vel = 0;
            else
                vel = floor(vel);
            end
            
            obj.velocity = obj.max_velocity/180*vel;
            if(angle>180);
                angle = 180;
            elseif(angle<0);
                angle = 0;
            else
                angle = floor(angle);
            end
            temp = obj.max_angle/90*(angle-90);
            obj.steering_angle = temp;
        end
        
        function obj = update(obj,t)
            %update headding
            if obj.steering_angle ~=0
                r = tan(obj.steering_angle)*obj.wheel_base;
                %w = obj.velocity*t/r %mine
                %w = obj.velocity*t*obj.wheel_base/sin(obj.steering_angle);%theirs
                w = obj.velocity*t*sin(obj.steering_angle)/obj.wheel_base;
                obj.headding = obj.headding+w;
                obj.headding = mod(obj.headding+pi,2*pi)-pi;
            end
            %update x
            if (obj.headding ~= 0)||(obj.headding ~= 180)
                obj.x = obj.x - t*obj.velocity*sin(obj.headding);
            end
            %update y
            if (obj.headding ~= 90)||(obj.headding ~= 270)
                obj.y = obj.y + t*obj.velocity*cos(obj.headding);
            end
            %print(obj.x)
            %print(obj.y)
        end
    end
end

