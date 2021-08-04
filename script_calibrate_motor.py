from Library import Device, Logger, Sonar, Settings, DAQmisc
import platform
from pyBat import Ports

offset = 40

os_name = platform.system()
p = Ports.Ports()

if os_name == 'Linux': servo_board = Device.BoardDevice()
if os_name == 'Windows': servo_board = Device.BoardDevice(Settings.servo_port)

servo_board.device.set_target(Settings.servo_channel, 1500 + offset)