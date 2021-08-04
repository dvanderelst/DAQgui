import numpy

connect_sonar = True
connect_lidar = False
connect_servo = True
default_repeats = 5

use_time_label = True

#ports on windows
servo_port = 'COM4'
sonar_port = 'COM5'

#servo_zero = 1220
#servo_range = [400, 2000]
calibrated_center = 1536
servo_positions = numpy.linspace(-500, 500, 5) + calibrated_center
servo_channel = 0

start_freq = 60000
end_freq = 30000
samples = 360
measurement_pause = 0.1
servo_pause = 1
