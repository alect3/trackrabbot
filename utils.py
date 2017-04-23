def calc_required_velocity(next_checkpoint, current_time, current_distance):
    delta_distance = next_checkpoint.distance - current_distance
    delta_time = next_checkpoint.time - current_time
    if delta_time < 0: return 100 # return large velocity value if checkpoint time has passed.
    if delta_distance < 0: return 0 # return 0 if checkpoint has been passed.
    return delta_distance/delta_time

