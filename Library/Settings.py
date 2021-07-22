import numpy

connect_sonar = False
connect_lidar = False
connect_servo = False
default_repeats = 5

use_time_label = True

#ports on windows
servo_port = 'COM4'
sonar_port = 'COM5'

#servo_zero = 1220
#servo_range = [400, 2000]
servo_positions = numpy.linspace(200, 2500, 5)
servo_channel = 5

start_freq = 30000
end_freq = 60000
samples = 360
measurement_pause = 0.1
servo_pause = 1
