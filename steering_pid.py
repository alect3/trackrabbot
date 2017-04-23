from pid import PID

class SteeringPID(PID):
    def __init__(self):
        PID.__init__(self)
        self.Wangle = 0
        self.velocity = 0
		self.Lerror = 0
		self.error = 0
		self.intergral = 0;
    # TODO: implement velocity pid
	
	
    def get_required_pwm(self): #PWM signal for steering wheel
		PWM = self.Wangle+90
		if PWM>100
			PWM = 100
		elif PWM <0
			PWM = 0
        return PWM

    def update_position(theta, offset):
		self.Lerror = self.error
		self.error = offset
        self.Wangle = self.Kp*self.error+self.Ki*self.integral+self.Kd*(self.error-self.Lerror)
		
        #self.offset = offset

