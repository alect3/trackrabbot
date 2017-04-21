from pid import PID

class VelocityPID(PID):
    def __init__(self):
        PID.__init__(self)
        self.angle = 0
        self.velocity = 0

    # TODO: implement velocity pid
    def get_required_pwm(self):
        return 0

    def update_position(angle, offset):
        self.angle = angle
        self.offset = offset

