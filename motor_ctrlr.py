import time
import RPi.GPIO as GPIO

class StepperMotorController:
    def __init__(self, frequency=1000, DIR = 0 ):
        """
        Initializes the stepper motor.
        
        DIR = 0 for clockwise, 1 for counter-clockwise
        """
        #BCM pin numbers 
        self.PUL_pin = 18
        self.DIR_pin = 17 #TODO: check these pin vals 
        #ENA is on by default - no pin 
        self.step_delay = 1/frequency 
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PUL_pin, GPIO.OUT)
        GPIO.setup(self.DIR_pin, DIR) 

    def set_pule_frequency(self, f):
        """Sets the motor rpm by adjusting step delay."""
        self.step_delay = 1 / f if f > 0 else 0.01

    def step(self, steps, direction = 1):
        """
        Rotates the motor a certain number of steps.

        :param steps: Number of steps to move.
        :param direction: 1 for one direction, 0 for the other.
        """
        self.set_direction(direction)

        for _ in range(abs(steps)):
            GPIO.output(self.PUL_pin, GPIO.HIGH)
            time.sleep(self.step_delay)
            GPIO.output(self.PUL_pin, GPIO.LOW)
            time.sleep(self.step_delay)

    def stop(self):
        """Stops the motor (placeholder for any stop logic needed)."""
        pass  # Could implement braking if needed

    def set_direction(self, direction):
        """Sets the direction of the motor."""
        GPIO.output(self.DIR_pin, GPIO.HIGH if direction > 0 else GPIO.LOW)
        
