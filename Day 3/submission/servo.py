import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
servo_pin = 5
GPIO.setup(servo_pin,GPIO,OUT)
duty_cycle = 7.5
pwm_servo = GPIO.PWM(servo_pin,50)
pwm_servo.start(duty_cycle)
try:
    while True:
        duty_cycle = float(input("Enter a Duty Cycle value:"))
        pwm_servo.ChangeDutyCycle(duty_cycle)
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

#minimum value = 
#maximum value = 

#explain the try except and finally