# ------------------------------------------
# 
# 	Project:    2023 VRC Controller Code
#   Created:    1/21/22
#	  Team:       37458A
# 
# ------------------------------------------

#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
IntakeMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
ShooterMotor = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
RollerMotor = Motor(Ports.PORT7, GearSetting.RATIO_36_1, False)
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 40.5, 232.5, MM, 1)
ExpansionMotor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)


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



# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True
controller_1_x_b_buttons_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, controller_1_x_b_buttons_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
            # check the buttonL1/buttonL2 status
            # to control IntakeMotor
            if controller_1.buttonL1.pressing():
                IntakeMotor.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                IntakeMotor.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                IntakeMotor.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control ShooterMotor
            if controller_1.buttonR1.pressing():
                ShooterMotor.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                ShooterMotor.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                ShooterMotor.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
            # check the buttonX/buttonB status
            # to control RollerMotor
            if controller_1.buttonX.pressing():
                RollerMotor.spin(FORWARD)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif controller_1.buttonB.pressing():
                RollerMotor.spin(REVERSE)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif not controller_1_x_b_buttons_control_motors_stopped:
                RollerMotor.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_x_b_buttons_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# Library imports
from vex import *
#Controller Code

IntakeMotor.set_velocity(120, RPM)
RollerMotor.set_velocity(70, RPM)
ExpansionMotor.set_velocity(200, RPM)
RollerMotor.set_max_torque(100, PERCENT)
ShooterMotor.set_velocity(430, RPM)
drivetrain.set_drive_velocity(100, PERCENT)

drivetrain.set_turn_velocity(30, PERCENT)
ExpansionMotor.set_velocity(100, PERCENT)

def ex():
    ExpansionMotor.spin_for(FORWARD, 90, DEGREES)
controller_1.buttonDown.pressed(ex)
