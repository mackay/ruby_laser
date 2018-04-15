#!/usr/bin/python
import time
from stepper import Stepper, STEP_SEQUENCE_TORQ

PINS = [17, 27, 22, 23]
SWEEP_RANGE_DEGREES = 15.0

stepper = Stepper(PINS, STEP_SEQUENCE_TORQ)

position = 0
error = 0
while True:
    error = stepper.advance(SWEEP_RANGE_DEGREES - error)
    error = stepper.reverse(SWEEP_RANGE_DEGREES - error)

    error = stepper.advance(SWEEP_RANGE_DEGREES - error)
    error = stepper.reverse(SWEEP_RANGE_DEGREES - error)

    error = stepper.advance(SWEEP_RANGE_DEGREES - error)
    error = stepper.reverse(SWEEP_RANGE_DEGREES - error)
    time.sleep(1.0)

    error = stepper.advance(SWEEP_RANGE_DEGREES - error)
    time.sleep(1.0)

    error = stepper.reverse(SWEEP_RANGE_DEGREES - error)
    time.sleep(1.0)
