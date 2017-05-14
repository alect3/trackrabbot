classdef steering_control
    properties
        Kp= 0.2;
        Ki= 0;
        Kd= 5;
        Lerror=0;
        error=0;
        angle = 0;
        integral = 0;
    end
    methods
        function obj = steering_control(x)%(x offset,global angle)
            obj.error = x;%offset distance form line at (t-1)
            obj.Lerror =x;%offset distance form line at (t)
            obj.integral = obj.integral +x;%itergral portion of PID controler
        end
        function obj = set_control(obj,Kp,Ki,Kd)%set PID controler values
            obj.Kp = Kp;
            obj.Ki = Ki;
            obj.Kd = Kd;
        end
        function obj = update(obj,x)%x offset,global angle
            obj.Lerror = obj.error; %update last error
            obj.error = x;%update current error
            obj.angle = obj.Kp*obj.error+obj.Ki*obj.integral+obj.Kd*(obj.error-obj.Lerror);
        end
        function angle = get_angle(obj)
            angle = obj.angle;
        end
    end
end