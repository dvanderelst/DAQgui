import numpy

connect_sonar = True
connect_lidar = False
connect_servo = True

servo_positions = numpy.linspace(400, 2000, 5)

start_freq = 60000
end_freq = 20000
samples = 1080
measurement_pause = 0.1
servo_pause = 1