import numpy

connect_sonar = True
connect_lidar = False
connect_servo = False

default_repeats = 5

#ports on windows
# Only used when running on linux
servo_port = 'COM4'
sonar_port = 'COM5'

#servo_zero = 1220
#servo_range = [400, 2000]
servo_positions = numpy.linspace(200, 2500, 5)

start_freq = 40000 +1
end_freq = 40000 - 1
samples = 100
measurement_pause = 0.1
servo_pause = 1
