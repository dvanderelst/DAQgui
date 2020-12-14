import numpy

connect_sonar = True
connect_lidar = False
connect_servo = False

default_repeats = 5

#ports on windows
# Only used when running on linux
servo_port = 'COM4'
sonar_port = 'COM5'

servo_zero = 1220
servo_range = [400, 2000]

max_deviation = min(servo_zero - servo_range[0], servo_range[1] - servo_zero)
min_position = servo_zero - max_deviation
max_position = servo_zero + max_deviation

servo_positions = numpy.linspace(min_position, max_position, 9)

start_freq = 40001
end_freq = 39999
samples = 100
measurement_pause = 0.1
servo_pause = 1
