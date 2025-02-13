import time
import RPi.GPIO as GPIO
import pigpio

class StepperMotorController:
    def __init__(self, frequency=1000, DIR = 0 ):
        """
        Initializes the stepper motor.
        
        DIR = 0 for clockwise, 1 for counter-clockwise
        """
        #BCM pin numbers 
        self.PUL_pin = 17
        self.DIR_pin = 18 
        #ENA is on by default - no pin 
        # self.step_delay = 1/frequency 

        #set up pwm signal 
        self.pi = pigpio.pi()
        self.f = frequency
        self.pi.set_PWM_frequency(self.PUL_pin, frequency)
        self.pi.set_PWM_dutycycle(self.PUL_pin, 0)  #128/255 = 50ish% suty cycle
        
        #set direction pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR_pin, GPIO.OUT)
        GPIO.setup(self.DIR_pin, DIR) 

    def set_pule_frequency(self, f):
        """Sets the pwm signal frequency ."""
        self.pi.set_PWM_frequency(self.PUL_pin, f)
        self.f = f

    def set_duty_cycle(self, percent):
        """Sets the pwm duty cycle."""
        self.pi.set_PWM_dutycycle(self.PUL_pin, int(percent*255/100))
    

    def step(self, pulse_count, duty =50, dir = 1):
        """
        Rotates the motor a certain number of steps.

        :param steps: Number of steps to move.
        :param direction: 1 for one direction, 0 for the other.
        """
        self.set_direction(dir)
        pulse_delay = 1/self.f 
        for _ in range(pulse_count):
            self.set_duty_cycle(duty)  # Turn on
            time.sleep(pulse_delay)  # Wait for pulse duration
            self.stop() 
            time.sleep(pulse_delay)  # Wait before next pulse

    def stop(self):
        """Stops the motor"""
        self.set_duty_cycle(0)

    def set_direction(self, d):
        #dirrection should be 0 or 1
        """Sets the direction of the motor."""
        if d ==1 or d ==0:
            GPIO.output(self.DIR_pin, d)

        
