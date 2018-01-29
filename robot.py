#!/usr/bin/env python3

import magicbot
import wpilib

from automations.intake import IntakeAutomation
from automations.lifter import LifterAutomation
from components.intake import Intake
from components.lifter import Lifter
from ctre import WPI_TalonSRX


class Robot(magicbot.MagicRobot):
    # Add magicbot components here using variable annotations.
    # Any components that directly actuate motors should be declared after
    # any higher-level components (automations) that depend on them.

    # Automations
    intake_automation: IntakeAutomation
    lifter_automation: LifterAutomation
    # Actuators
    intake: Intake
    lifter: Lifter

    def createObjects(self):
        """Create non-components here."""
        """This is to state what channel our xbox controller is on."""
        self.xbox = wpilib.XboxController(0)
        """This controls the left motor in the intake mechanism."""
        self.intake_left = WPI_TalonSRX(1)
        """This controls the right motor in the intake mechanism."""
        self.intake_right = WPI_TalonSRX(2)
        """This controls the arm in the containment mechanism."""
        self.clamp_arm = wpilib.Solenoid(0)
        """This controls the kicker in the containment mechanism."""
        self.intake_kicker = wpilib.Solenoid(1)
        """This controls the left extension arm"""
        self.extension_arm_left = wpilib.Solenoid(2)
        """This controls the right extension arm"""
        self.extension_arm_right = wpilib.Solenoid(3)
        """This is the infrared sensor that is in the back of the
        containment mechanism."""
        self.infrared = wpilib.AnalogInput(0)

        self.lift_motor = WPI_TalonSRX(0)

    def teleopInit(self):
        """Called when teleop starts; optional"""
        self.intake.intake_clamp(False)
        self.intake.intake_push(False)
        self.intake.extension(True)

    def teleopPeriodic(self):
        """Process inputs from the driver station here.
        This is run each iteration of the control loop before magicbot
        components are executed."""

        if self.xbox.getXButtonReleased():
            self.intake_automation.engage()


if __name__ == '__main__':
    wpilib.run(Robot)
