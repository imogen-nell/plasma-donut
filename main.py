import motor_ctrlr

class SCIENCE_SET_UP():

    motor_ctrlr: motor_ctrlr.StepperMotorController # type: ignore

    #maybe for later ??
    # data_logger: DataLogger
    # sensor: Sensor
    # camera: Camera
    
    def __init__(self):
        self.motor_ctrlr = motor_ctrlr.StepperMotorController()
        # self.data_logger = DataLogger()
        # self.sensor = Sensor()
        # self.camera = Camera()
        self.run()
    
    def run(self):
        self.motor_ctrlr.step(10)
        self.motor_ctrlr.step(10, dir = 0)
        
if __name__ == "__main__":
    SCIENCE_SET_UP()