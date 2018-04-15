#!/usr/bin/python
import sys
from stepper import Stepper, STEP_SEQUENCE_TORQ

PINS = [17, 27, 22, 23]
stepper = Stepper(PINS, STEP_SEQUENCE_TORQ)

adjustment_degrees = sys.argv[0]

stepper.advance(adjustment_degrees)
