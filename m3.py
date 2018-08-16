"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
Hussein Alawami, Haolun Cheng, Dongrui (Frank) Hu
"""
# Done: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m4
import time

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb


def my_frame(root, dc):
    """
    Constructs and returns a   ttk.Frame   on the given root window.
    The frame contains all of this module's widgets.
    Does NOT   grid   the Frame, since the caller will do that.
    Also sets up callbacks for this module's widgets.

    The first argument is the  root  window (a tkinter.Tk object)
    onto which the   ttk.Frame  returned from this function
    will be placed.  The second argument is the shared DataContainer
    object that is CONSTRUCTED in m0 but USED in m1, m2, m3 and m4.

    Peconditions:
      :type root: tkinter.Tk
      :type dc:   m0.DataContainer
    """

    frame_frank = ttk.Frame(root, padding=30)

    spin_right_button = ttk.Button(frame_frank, text='Let us Party')
    spin_right_button['command'] = (lambda: Spin_Right_Bot(dc.robot))
    spin_right_button.grid()

# Go forward for a certain amount of distance
    label_distance = ttk.Label(frame_frank, text='Enter distance')
    label_distance.grid()

    entry_go_straight = ttk.Entry(frame_frank)
    entry_go_straight.grid()

    label_speed = ttk.Label(frame_frank, text='Enter speed')
    label_speed.grid()

    entry_go_straight_speed = ttk.Entry(frame_frank)
    entry_go_straight_speed.grid()

    go_straight_time_button = ttk.Button(frame_frank, text='Run')
    go_straight_time_button['command'] = (lambda: Forward_Specified_Distance(dc.robot, int(entry_go_straight.get()), int(entry_go_straight_speed.get())))
    go_straight_time_button.grid()

# Turn for 90 degrees
    Straight_Turn_Button = ttk.Button(frame_frank, text='90 degrees Turns')
    Straight_Turn_Button['command'] = (lambda: Turn_Turn(dc.robot))
    Straight_Turn_Button.grid()

# Wireless Connection Entry and Button
    label_port = ttk.Label(frame_frank, text='Enter Connection Port Here')
    label_port.grid()

    Wireless_Port_Entry = ttk.Entry(frame_frank)
    Wireless_Port_Entry.grid()

    Wireless_Button = ttk.Button(frame_frank, text='Connect Wireless')
    Wireless_Button['command'] = (lambda: connect_wireless(dc.robot, int(Wireless_Port_Entry.get())))
    Wireless_Button.grid()

# The robot can move in a list of specified waypoints
    follow_track_button = ttk.Button(frame_frank, text='Follow a List of Coordinates')
    follow_track_button['command'] = (lambda: tracking_waypoints(dc.robot))
    follow_track_button.grid()

# Piano Control
    root.bind_all('<Key-z>', lambda event: duo(event, dc.robot))
    root.bind_all('<Key-x>', lambda event: rai(event, dc.robot))
    root.bind_all('<Key-c>', lambda event: mi(event, dc.robot))
    root.bind_all('<Key-v>', lambda event: fa(event, dc.robot))
    root.bind_all('<Key-b>', lambda event: so(event, dc.robot))
    root.bind_all('<Key-n>', lambda event: la(event, dc.robot))
    root.bind_all('<Key-m>', lambda event: ti(event, dc.robot))
    root.bind_all('<Key-,>', lambda event: Duo(event, dc.robot))

    root.bind_all('<KeyRelease-z>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-x>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-c>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-v>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-b>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-n>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-m>', lambda event: Stop_Beep(event, dc.robot))
    root.bind_all('<KeyRelease-,>', lambda event: Stop_Beep(event, dc.robot))

# Kyeboard Control
    root.bind_all('<Key-w>', lambda event: go_front(event, dc.robot))
    root.bind_all('<Key-q>', lambda event: spin_left(event, dc.robot))
    root.bind_all('<Key-s>', lambda event: go_back(event, dc.robot))
    root.bind_all('<Key-e>', lambda event: spin_right(event, dc.robot))
    root.bind_all('<Key-a>', lambda event: turn_left(event, dc.robot))
    root.bind_all('<Key-d>', lambda event: turn_right(event, dc.robot))
    root.bind_all('<Key-j>', lambda event: Beep_Beep(event, dc.robot))

    root.bind_all('<KeyRelease-w>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-a>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-s>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-d>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-q>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-e>', lambda event: Pause_Motion(event, dc.robot))
    root.bind_all('<KeyRelease-j>', lambda event: Stop_Beep(event, dc.robot))

    return frame_frank

# Press P to start to track or not to track an object
def Press_P(event, Bool):

    if Bool == False:

        Bool = True

    else:

        Bool = False

# Perfect Turn
def Turn_Turn(robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(-60, 60)
    time.sleep(0.5)
    robot.motor_controller.drive_pwm(0, 0)

# Play notes
def duo(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(37)
def rai(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(39)
def mi(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(41)
def fa(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(43)
def so(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(45)
def la(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(47)
def ti(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(49)
def Duo(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.buzzer.play_tone(51)

# Track the input coordinates
def tracking_waypoints(robot):
    '''
    :type robot: rg.RoseBot
    '''

    Origin = [0, 0]
    lists = [[120, 120], [240, 240], [360, 360], [480, 480]]

    for k in range(len(lists)):

        dx = -Origin[0] + lists[k][0]

        dy = -Origin[1] + lists[k][1]

        Origin = [dx, dy]
        robot.motor_controller.drive_pwm(int(dx / 2), int(dx / 2))
        time.sleep(3)
        robot.motor_controller.drive_pwm(-60, 60)
        time.sleep(0.5)
        robot.motor_controller.drive_pwm(int(dy / 2), int(dy / 2))
        time.sleep(3)

    robot.motor_controller.stop()

# Robot goes forward for a specified distance with a specified speed
def Forward_Specified_Distance(robot, distance, speed):
    '''
    :type robot: rg.rosebot
    '''
    robot.motor_controller.drive_pwm(speed, speed)
    t = distance / speed
    time.sleep(t)
    robot.motor_controller.stop()

# Robot Buzzer Beeps or not
def Beep_Beep(event, robot):
    '''
    :type robot: rg.RoseBot
    '''

    robot.buzzer.play_tone(56)
    robot.led.turn_on()

def Stop_Beep(event, robot):
    '''
    :type robot: rg.RoseBot
    '''

    robot.buzzer.stop()
    robot.led.turn_off()

# Six Programs that uses keyboard to control the robot
def turn_left(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(20, 100)

def turn_right (event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(100, 20)

def go_front(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(100, 100)

def spin_left(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(-50, 50)

def go_back(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(-100, -100)


def spin_right (event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(50, -50)

# A program to pause the motion of the robot
def Pause_Motion(event, robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.stop()

# A program for the robot to go forward for an input amount of time
def Sprint_in_sec(robot, n):

    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(255, 255)
    time.sleep(n)
    robot.motor_controller.stop()

# A program for the robot to connect wirelessly and to be tele-operated
def connect_wireless(robot, n):
    '''
    :type robot: rg.RoseBot
    '''
    robot.connector.connect_wireless(n)

# A program for the robot to move a certain amount of the distance
# n, the input speed should be from -255 to 255
def Go_Straight(robot, n):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(n, n)
    time.sleep(1)
    robot.motor_controller.stop()

# A program to let the robot spin right
def Spin_Right_Bot(robot):
    '''
    :type robot: rg.RoseBot
    '''
    robot.motor_controller.drive_pwm(150, -150)
    time.sleep(2)
    robot.motor_controller.stop()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
