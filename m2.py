"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Hussein, Clarence Cheng, Frank Hu

The primary author of this module is: Clarence Cheng.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
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

    Preconditions:
      :type root: tkinter.Tk
      :type dc:   m0.DataContainer
    """
    fram1 = ttk.Frame(root, padding=20, relief='raised')

    spinButton_speed = ttk.Entry(fram1)
    spinButton_speed.grid()

    spinButton_speed_label = ttk.Label(fram1, text='Speed of turning left')
    spinButton_speed_label.grid()

    spinButton = ttk.Button(fram1, text='spin Left')
    spinButton['command'] = (lambda:
                             turn_left(dc.robot, int(spinButton_speed.get())))
    spinButton.grid()

    go_back_Button_speed = ttk.Entry(fram1)
    go_back_Button_speed.grid()

    go_back_Button_speed_label = ttk.Label(fram1, text='Speed of going back')
    go_back_Button_speed_label.grid()

    go_back_Button = ttk.Button(fram1, text='go_back')
    go_back_Button['command'] = (lambda:
                                 go_back(dc.robot, int(go_back_Button_speed.get())))
    go_back_Button.grid()


    read_txt_Button = ttk.Button(fram1, text='read hours file')
    read_txt_Button['command'] = (lambda:
                                  show_contents())
    read_txt_Button.grid()


    values_of_reflectance_sensor = ttk.Button(fram1, text='Reflectance value')
    values_of_reflectance_sensor['command'] = (lambda:
                                              value_of_reflectance_sensors(dc.robot))
    values_of_reflectance_sensor.grid()

    camera_plus_proximity_sensor_speed = ttk.Entry(fram1)
    camera_plus_proximity_sensor_speed.grid()

    camera_plus_proximity_sensor_speed_label = ttk.Label(fram1, text='Speed of following object straight')
    camera_plus_proximity_sensor_speed_label.grid()

    camera_plus_proximity_sensor = ttk.Button(fram1, text='following object')
    camera_plus_proximity_sensor['command'] = (lambda:
                                               camera_and_proximity_sensor_go_straight(dc.robot, int(camera_plus_proximity_sensor_speed.get())))
    camera_plus_proximity_sensor.grid()

    Using_camera_to_turn_speed = ttk.Entry(fram1)
    Using_camera_to_turn_speed.grid()

    Using_camera_to_turn_speed_label = ttk.Label(fram1, text='Speed of following object')
    Using_camera_to_turn_speed_label.grid()

    Using_camera_to_turn = ttk.Button(fram1, text='following object ')
    Using_camera_to_turn['comman'] = (lambda:
                                      using_camera_to_turn_the_robot(dc.robot, int(Using_camera_to_turn_speed.get())))
    Using_camera_to_turn.grid()

    return fram1


def turn_left(robot, speed):
    '''
    :type robot: rg.RoseBot
    '''

    robot.motor_controller.left_wheel_pwm(-speed)
    robot.motor_controller.right_wheel_pwm(speed)


def go_back(robot, speed):
    '''
    :type robot: rg.RoseBot
    '''


    robot.motor_controller.left_wheel_pwm(-speed)
    robot.motor_controller.right_wheel_pwm(-speed)


def show_contents():
    for k in range(1, 4):
        f = open('../process/hours-' + str(k) + '.txt')

        s = f.read()
        print(s)
        f.close()


def value_of_reflectance_sensors(robot):
    '''
    :type robot: rg.RoseBot
    '''


    threshold = 925
    while True:
        robot.motor_controller.left_wheel_pwm(100)
        robot.motor_controller.right_wheel_pwm(100)
        print(robot.sensor_reader.left_reflectance_sensor.read())
        print(robot.sensor_reader.right_reflectance_sensor.read())
        if robot.sensor_reader.left_reflectance_sensor.read() > threshold and robot.sensor_reader.right_reflectance_sensor.read() > threshold:
            robot.motor_controller.left_wheel_pwm(0)
            robot.motor_controller.right_wheel_pwm(0)
            break


def camera_and_proximity_sensor_go_straight(robot, speed):
    '''
    :type robot: rg.RoseBot
    '''


    if robot.sensor_reader.left_bump_sensor.read() != 0 and robot.sensor_reader.right_bump_sensor.read() != 0:
        while True:
            temp = robot.sensor_reader.front_proximity_sensor.read()
            time.sleep(0.1)
            if robot.sensor_reader.front_proximity_sensor.read() > temp:
                robot.motor_controller.drive_pwm(speed, speed)
                time.sleep(0.1)
            else:
                robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.1)
            if robot.sensor_reader.left_bump_sensor.read() == 0 or robot.sensor_reader.right_bump_sensor.read() == 0:
                robot.motor_controller.stop()
                break


def using_camera_to_turn_the_robot(robot, speed):
    '''
    :type robot: rg.RoseBot
    '''


    a = robot.sensor_reader.front_proximity_sensor.read()
    while True:
        delta = robot.camera.get_block()

        if delta != None:
            robot.motor_controller.drive_pwm(speed, speed)
            if delta.x < 160:
                robot.motor_controller.drive_pwm(-60, 60)
            elif delta.x > 160:
                robot.motor_controller.drive_pwm(60, -60)
            else:
                robot.motor_controller.drive_pwm(speed, speed)
        if robot.sensor_reader.left_bump_sensor.read() != 0 and robot.sensor_reader.right_bump_sensor.read() != 0:
            while True:
                temp = robot.sensor_reader.front_proximity_sensor.read()
                time.sleep(0.1)
                if robot.sensor_reader.front_proximity_sensor.read() > temp:
                    robot.motor_controller.drive_pwm(speed, speed)
                    time.sleep(0.1)
                else:
                    robot.motor_controller.drive_pwm(0, 0)
                    time.sleep(0.1)
                if robot.sensor_reader.left_bump_sensor.read() == 0 or robot.sensor_reader.right_bump_sensor.read() == 0:
                    robot.motor_controller.stop()
                    break






# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
