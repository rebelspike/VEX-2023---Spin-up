# ------------------------------------------
# 
# 	Project:      2023 VRC Autonomous Routine
#	  Created:      1/21/23
#	  Team:         37458A
# 
# ------------------------------------------

#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
IntakeMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
ShooterMotor = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
RollerMotor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 40.5, 232.5, MM, 1)
ExpansionMotor_motor_a = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
ExpansionMotor_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
ExpansionMotor = MotorGroup(ExpansionMotor_motor_a, ExpansionMotor_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# Library imports
from vex import *

#Dropping into low goal-----------------------------------------------------------------------------
def autoNextToRoller():
    #NEXT TO ROLLER-----------------
    drivetrain.drive_for(FORWARD, 50, MM)
    RollerMotor.set_max_torque(100, PERCENT)
    RollerMotor.spin(REVERSE,100,RPM)
    wait(500,MSEC)

    RollerMotor.stop()
    drivetrain.drive_for(REVERSE, 60, MM)
    drivetrain.set_turn_velocity(50, PERCENT)
    drivetrain.turn_for(LEFT, 28, DEGREES)
    wait(100, MSEC)
    drivetrain.drive_for(FORWARD, 1330, MM)
    wait(100, MSEC)
    IntakeMotor.spin(FORWARD, 120, RPM)
    wait(4000, MSEC)
    IntakeMotor.stop()

def autoNearRoller():
    drivetrain.drive_for(FORWARD, 609, MM)
    drivetrain.set_turn_velocity(20, PERCENT)
    drivetrain.turn_for(RIGHT, 28, DEGREES)
    drivetrain.drive_for(FORWARD, 150, MM)
    RollerMotor.set_max_torque(100, PERCENT)
    RollerMotor.spin(REVERSE,100,RPM)
    wait(500,MSEC)

    RollerMotor.stop()
    drivetrain.drive_for(REVERSE, 120, MM)
    drivetrain.turn_for(RIGHT, 28, DEGREES)

    drivetrain.set_drive_velocity(80, PERCENT)

    drivetrain.drive_for(FORWARD, 1550, MM)
    IntakeMotor.spin(FORWARD, 120, RPM)
    wait(4000, MSEC)
    IntakeMotor.stop()
#---------------------------------------------------------------------------------------------------------
# Begin project code

#autoNextToRoller()
autoNearRoller()
