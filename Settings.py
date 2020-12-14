import numpy
from scipy.interpolate import interp1d
import simpleaudio as sa

# Sounds
filename = 'ding.wav'
done_sound = sa.WaveObject.from_wave_file(filename)

# HS422
# Range 448-2400
connect_sonar = True
connect_lidar = False
connect_servo = False

f = interp1d([-90, 0, 90], [538, 1435, 2400])
servo_positions = numpy.linspace(-30,30,11)
servo_positions = f(servo_positions)
servo_positions = [0]
#print(servo_positions)

# sample rate == 300000
auto_measure_delay = 5
start_freq = 80000
end_freq = 30000
samples = 500
measurement_pause = 0.1
servo_pause = 3
default_repeats = 3
plot_start_sample = 500
