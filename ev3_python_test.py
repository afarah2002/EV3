#----------imports----------#
import ev3dev.ev3 as ev3

# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
# from ev3dev2.sensor import INPUT_1
# from ev3dev2.sensor.lego import TouchSensor
# from ev3dev2.led import Leds

m = ev3.LargeMotor('outA')
m.run_timed(time_sp=3000, speed_sp=500)