import time
import RPi.GPIO as GPIO


STEP_SEQUENCE_FULL = [[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]]

STEP_SEQUENCE_HALF = [[1, 0, 0, 1],
                      [1, 0, 0, 0],
                      [1, 1, 0, 0],
                      [0, 1, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 1, 0],
                      [0, 0, 1, 1],
                      [0, 0, 0, 1]]

STEP_SEQUENCE_TORQ = [[1, 0, 0, 1],
                      [1, 1, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 1, 1]]


class Stepper(object):

    DEGREES_PER_SEQUENCE = 1.422222

    def __init__(self, pin_sequence, step_sequence, step_delay=0.00175):
        self.pins = pin_sequence
        self.sequence = step_sequence
        self.sequence_len = len(step_sequence)
        self.degrees_per_step = self.DEGREES_PER_SEQUENCE / len(self.sequence)

        self.step_delay = step_delay

        self.sequence_index = 0
        self._init()

    def _init(self):
        self.sequence_index = 0
        GPIO.setmode(GPIO.BCM)

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def _pins(self, pin1, pin2, pin3, pin4):
        GPIO.output(self.pins[0], pin1)
        GPIO.output(self.pins[1], pin2)
        GPIO.output(self.pins[2], pin3)
        GPIO.output(self.pins[3], pin4)

    def idle(self):
        self.set_pins(0, 0, 0, 0)

    def advance(self, degrees):
        self.move(degrees, 1)

    def reverse(self, degrees):
        self.move(degrees, -1)

    def move(self, degrees, direction=1):
        degrees = float(degrees)

        while degrees > 0:
            self.sequence_index += direction
            self.sequence_index %= self.sequence_len

            self._pins(*self.sequence[self.sequence_index])
            time.sleep(self.step_delay)

            degrees -= self.degrees_per_step

        return degrees
