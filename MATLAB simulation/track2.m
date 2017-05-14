clear;
clc

%%%Properties%%%
acc = 2.07;%rate of acceleration
dis = 100;
t = 0.1;
angle = 91; %wheel direction in radians.(90 = forward)
x = 0.2;
y = 0;
theta = 0;

%%%initalising values%%%
vel = 50;%velocity
time = 0;%time
rabbot = Car2();%rabBOT
rabbot = rabbot.setloc(x,y,theta);
pos = [];%position of the robot. For ploting.

%%%simulate race%%%
%get starting position
[x,y,theta] = rabbot.getpos();
raspberry = steering_control(x);
Kp = 30;%30
Ki = 4.4;%4.4
Kd = 100;%100
raspberry = raspberry.set_control(Kp,Ki,Kd);
pos = [pos;x y theta angle];
%race starts
for i = 1:1000
    %control system
    raspberry = raspberry.update(x);%pass x offset
    angle = raspberry.get_angle()+90;
    
    %noise
    extra = floor(3*rand())-1;
    angle = angle+extra;
    
    %simulate car kinamatics
    rabbot = rabbot.input(vel,angle); %send vel and angle to rabBOT
    rabbot = rabbot.update(t); %calculate movement
    [x,y,theta] = rabbot.getpos(); %get the possition and headding of the RabBOT
    %recording simulation
    pos = [pos;x,y,theta/pi*180,angle];%(global x position, global y position,robots heading(global angle),wheel angle)
    %end race condition
    if (pos(end,2)>dis) %if it has reached the finish line then stop simulation
        time = i;
        break
    end
end

%%%results%%%
disp(('race time: '+time*t));
time*t; %the race time

subplot(1,3,1);grid;plot(pos(:,1),pos(:,2));%plot of the race
title('Running Track');xlabel('drift distance/offset');ylabel('Distance(m)')
%figure
grid on;
grid minor;
subplot(1,3,2);grid;plot(pos(:,3));%plots the robot heading
title('Robot Heading');xlabel('Distance(m)');ylabel('Degrees(rad)');
subplot(1,3,3);plot(pos(:,4));%plots the robot heading
title('Angle of Wheels');xlabel('Distance(m)');ylabel('Wheel Angle(PWM signal)');

