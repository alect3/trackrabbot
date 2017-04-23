from pid import PID

class VelocityPID(PID):
    def __init__(self):
        PID.__init__(self)
        self.velocity = 0
        self.desired_velocity = 0

    # TODO: implement velocity pid
    def get_required_pwm(self):
        return 0

    def update_velocity(self, v):
        self.velocity = v

    def update_desired_velocity(self, v):
        self.desired_velocity = v
