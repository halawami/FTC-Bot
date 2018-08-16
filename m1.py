"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Hussein Alawami, Frank, and Clarence (all of them).

The primary author of this module is: Hussein Alawami.
Hussein Alawami, Haolun Cheng, Dongrui (Frank) Hu
"""
# done: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

import time
import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import tweepy


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

    # Creates my frame, where I put all my buttons on
    frame1 = ttk.Frame(root, padding=20, relief='raised')

    # Creates the entry box and label for the port number to connect the robot
    portLabel = ttk.Label(frame1, text='Enter port number to connect')
    portLabel.grid()
    portentry = ttk.Entry(frame1, text='Enter port')
    portentry.grid()

    # Creates a button that connects the robot to the computer with wire
    connectButton = ttk.Button(frame1, text='Connect')
    connectButton['command'] = (lambda:
                                connect(dc.robot, portentry))
    connectButton.grid()

    # Creates the sudden death button that makes the robot stop moving
    suddenDeath = ttk.Button(frame1, text='Stop')
    suddenDeath['command'] = (lambda:
                              sudden_death(dc.robot))
    suddenDeath.grid()

    # Creates a button the print he biography of the robot.
    bioButton = ttk.Button(frame1, text='Print biography')
    bioButton['command'] = (lambda:
                            print_bio(dc.robot))
    bioButton.grid()

    # Creates a button that disconnects the robot from the computer
    disconnectButton = ttk.Button(frame1, text='Disconnect')
    disconnectButton['command'] = (lambda:
                                   disconnect(dc.robot))
    disconnectButton.grid()

    # Creates a button that moves the robot and stops it (practice)
    moveTillStop = ttk.Button(frame1, text='Move-Stop')
    moveTillStop['command'] = (lambda:
                               move(dc.robot))
    moveTillStop.grid()

    moveTillStopMove = ttk.Button(frame1, text='Move-Stop-Move')
    moveTillStopMove['command'] = (lambda:
                                   move_stop_changedirection(dc.robot))
    moveTillStopMove.grid()


    # Creates a button that prints out the hours for every member in
    # each sprint
    hours_counter = ttk.Button(frame1, text='Print hours')
    hours_counter['command'] = (lambda:
                                hours_display())
    hours_counter.grid()

    # Creates a button that plays a song
    songButton = ttk.Button(frame1, text='Play a song')
    songButton['command'] = (lambda:
                             play_song(dc.robot))
    songButton.grid()

    # Creates a button that makes the robot follow a black line
    followLineButton = ttk.Button(frame1, text='Follow black line')
    followLineButton['command'] = (lambda:
                                   follow_black_line(dc.robot, root))
    followLineButton.grid()

    # Creates a button the displays happy emotion with buzzer
    displayEmotionHappy = ttk.Button(frame1, text='HAPPYYY!')
    displayEmotionHappy['command'] = (lambda:
                                  display_emotion_happy(dc.robot))
    displayEmotionHappy.grid()

    # Creates a button the display sad/mad emotion with buzzer
    displayEmotionSad = ttk.Button(frame1, text='SADDD:(')
    displayEmotionSad['command'] = (lambda:
                                  display_emotion_sad(dc.robot))
    displayEmotionSad.grid()

    # Creates a button that makes the robot try to tweet
    tweetButton = ttk.Button(frame1, text="Trying to tweet")
    tweetButton['command'] = (lambda:
                              tweet(dc.robot))
    tweetButton.grid()

    # Creates a button that 'talks' to another robot
    talkButton = ttk.Button(frame1, text='Make friends')
    talkButton['command'] = (lambda:
                             be_social(dc.robot))
    talkButton.grid()


    # Creates a function the moves in a straight line until it detects
    # something and changes direction
    moveDetectObject = ttk.Button(frame1, text='Move till you detect something')
    moveDetectObject['command'] = (lambda:
                                   front_detect(dc.robot))
    moveDetectObject.grid()

    # Creates a function that moves in a straight line until it detects
    # something or detects a line. Stops at lines and changes direction
    # when it detects something
    moveDetectLine = ttk.Button(frame1, text='Move till you detect a line')
    moveDetectLine['command'] = (lambda:
                                 detect_lines_and_things(dc.robot))
    moveDetectLine.grid()


    # Creates a button for staying on the table
    dontFly = ttk.Button(frame1, text='Move on table')
    dontFly['command'] = (lambda:
                          dont_fly(dc.robot))
    dontFly.grid()


    # Creates an entry box and a button that tweets
    tweetEntry = ttk.Entry(frame1, text='Enter something to tweet')
    twitterButton = ttk.Button(frame1, text='Press to send to twitter!!!!')
    twitterButton['command'] = (lambda:
                               twitter_tweet(tweetEntry))
    tweetEntry.grid()
    twitterButton.grid()


    # Creates a button that makes it go in a square
    squareGoButton = ttk.Button(frame1, text='Go in a square')
    squareGoButton['command'] = (lambda:
                            draw_square(dc.robot))
    squareGoButton.grid()

    return frame1

# Print the bio of robot
def print_bio(robot):
    print("Hi my name is robot, and I was just created by this amazaing team, they took good care of me!\n They we so kind to me and I hope that you can give them a good grade because they have been\n working hard on making me the best I can and making me move without them controlling me.")

# Connects the robot to the computer
def connect(robot, entry):
    '''
    :type robot: rb.RoseBot
    '''
    robot.connector.connect(int (entry.get()))

# Disconnects the robot from the computer
def disconnect(robot):
    '''
    :type robot: rb.RoseBot
    '''
    robot.connector.disconnect()

# Just a practice function for myself
def move(robot):
    '''
    :type robot: rb.RoseBot
    '''
    robot.motor_controller.drive_pwm(100, 100)
#     if robot.sensor_reader.front_proximity_sensor == False:
#         robot.motor_controller.stop()
    print(robot.sensor_reader.front_proximity_sensor)

# Just a practice function for myself
def move_stop_changedirection(robot):
    '''
    :type robot: rb.RoseBot
    '''
    move(robot)
    robot.motor_controller.drive_pwm(100, 100)
    time.sleep(2)
    robot.motor_controller.drive_pwm(100, 100)

# Shows the hours written in the sprint
def hours_display():
    for j in range(1, 4):
        print("Student " + str(j) + " :")
        total = 0
        f = open('../process/hours-' + str(j) + '.txt')
        s = f.read()
        lines = s.split('\n')
        for k in lines:
            if '*' in k:
                total += int(k[2])
        print("Sprint1: " + str(total))
        total1 = 0
        for l in lines:
            if '#' in l:
                total1 += int(l[2])
        print("Sprint2: " + str(total1))
        total2 = 0
        for q in lines:
            if '@' in q:
                total2 += int(q[2])
        print("Sprint3: " + str(total2))
        f.close()
        print(total + total1 + total2)



# Plays a song using the buzzer
def play_song(robot):
    '''
    :type robot: rb.RoseBot
    '''
    sequence = []
    for k in range(1):
        f = open('../process/parsing')
        s = f.read()
        numbers = s.split(',')
        for j in range(len(numbers)):
            sequence += [int(numbers[j].strip())]
    for k in range(len(sequence)):
        robot.buzzer.play_tone(sequence[k])
        time.sleep(0.1)
    robot.buzzer.stop()
# strip
# Follows a black line using the reflectance sensors
def follow_black_line(robot, root):
    '''
    :type robot: rb.RoseBot
    '''
    x = 0
    threshholdLeft = robot.sensor_reader.left_reflectance_sensor.read()
    threshholdRight = robot.sensor_reader.right_reflectance_sensor.read()
    print("left sensor(T): " + str(robot.sensor_reader.left_reflectance_sensor.read()))
    print("Right sensor(T): " + str(robot.sensor_reader.right_reflectance_sensor.read()))
    while not robot.is_stopped:
        left_Sensor = robot.sensor_reader.left_reflectance_sensor.read()
        right_Sensor = robot.sensor_reader.right_reflectance_sensor.read()
        x += 1
        if left_Sensor < threshholdLeft - 75:
            robot.motor_controller.drive_pwm(50, 0)
            print("left sensor: " + str(robot.sensor_reader.left_reflectance_sensor.read()))
        elif right_Sensor < threshholdRight - 75:
            robot.motor_controller.drive_pwm(0, 50)
            print("Right sensor: " + str(robot.sensor_reader.right_reflectance_sensor.read()))
        else:
            robot.motor_controller.drive_pwm(60, 60)
            print('straight')

        root.update()

# Displays happy emotions using the buzzer
def display_emotion_happy(robot):
    '''
    :type robot: rb.RoseBot
    '''
    happySong = [40, 40, 48, 48, 48, 56, 41, 42, 42, 48, 48, 48, 56, 41,
                 42, 42, 48, 48, 48, 48, 56, 41, 42, 42, 48, 48, 48, 56]
    for k in range (len(happySong)):
        robot.buzzer.play_tone(happySong[k])
        time.sleep(0.1)
        robot.motor_controller.drive_pwm(50 + k, -(50 + k))
    robot.buzzer.stop()

# Display sad/mad emoztions using the buzzer
def display_emotion_sad(robot):
    '''
    :type robot: rb.RoseBot
    '''

    sadSong = [56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56]
    for k in range (len(sadSong)):
        robot.buzzer.play_tone(sadSong[k])
        time.sleep(0.3)
    robot.buzzer.stop()

# Creates a function that makes the robot tweet using two frequencies
def tweet(robot):
    '''
    :type robot: rb.RoseBot
    '''
    x = 0
    while True:
        robot.buzzer.play_tone(45)
        time.sleep(0.2)
        robot.buzzer.play_tone(59)
        x += 1
        if x == 14:
            break

# Creates a function that stops the robot from whatever it is doing
def sudden_death(robot):
    '''
    :type robot: rb.RoseBot
    '''
    robot.is_stopped = True
    robot.motor_controller.stop()

# Creates a function that makes it social by rotating and getting closer
def be_social(robot):
    '''
    :type robot: rb.RoseBot
    '''
    robot.motor_controller.drive_pwm(-100, 100)
    time.sleep(1)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(60, 60)
    time.sleep(0.5)
    robot.motor_controller.stop()


# Creates a function that goes straight until it detects somethings and
# then it just drives back.
def front_detect(robot):
    '''
    :type robot: rb.RoseBot
    '''

    while True:
        frontProx = (robot.sensor_reader.front_proximity_sensor.read())
        robot.motor_controller.drive_pwm(50, 50)
        if frontProx > 400:
            robot.motor_controller.drive_pwm(-50, -50)
            time.sleep(1)
            robot.motor_controller.drive_pwm(50, -50)
            time.sleep(1)
            robot.motor_controller.stop()
        print(frontProx)


# Creates a function that avoids objects and stops after it passes a line
def detect_lines_and_things(robot):
    '''
    :type robot: rb.RoseBot
    '''
    while True:
        threshholdLeft = robot.sensor_reader.left_reflectance_sensor.read()
        threshholdRight = robot.sensor_reader.right_reflectance_sensor.read()
        threshholdCenter = robot.sensor_reader.middle_reflectance_sensor.read()
        robot.motor_controller.drive_pwm(50, 50)
        print(threshholdCenter)
        print(threshholdLeft)
        print(threshholdRight)
        frontProx = (robot.sensor_reader.front_proximity_sensor.read())
        robot.motor_controller.drive_pwm(50, 50)
        if frontProx > 400:
            robot.motor_controller.drive_pwm(-50, -50)
            time.sleep(1)
            robot.motor_controller.drive_pwm(50, -50)
            time.sleep(1)
#             robot.motor_controller.stop()
        elif threshholdCenter > 200 or threshholdLeft > 200 or threshholdRight > 200:
            robot.motor_controller.drive_pwm(0, 0)
            robot.motor_controller.stop()
            display_emotion_happy(robot)
            break


# Creates a function that stops the robot if it left the parameter of the table
def dont_fly(robot):
    '''
    :type robot: rb.RoseBot
    '''
    while True:
        threshholdLeft = robot.sensor_reader.left_reflectance_sensor.read()
        threshholdRight = robot.sensor_reader.right_reflectance_sensor.read()
        threshholdCenter = robot.sensor_reader.middle_reflectance_sensor.read()
        robot.motor_controller.drive_pwm(30, 30)
        if threshholdCenter > 600 or threshholdLeft > 600 or threshholdRight > 600:
            robot.motor_controller.drive_pwm(0, 0)
            robot.motor_controller.stop()
            robot.motor_controller.drive_pwm(-30, -30)
            break

# Creates a function that tweets something in TWITTER!
def twitter_tweet(tweet):
    '''
    :type robot: rb.RoseBot
    :type entry_box: ttk.Entry
    '''
    auth = tweepy.OAuthHandler('b6s4A0KWJq3W3qW8tLUbermxa',
                               'aXn17fUfavK8MZAOIrz055mnMpwkMXVTFNLjsth7syKIebqxd2')
    auth.set_access_token('797236049370091521-6XJ3djw0QUor5PCcwPApqMn4JxFff0m',
                          '9vnpyc28G220rGiQHAXKxzqmz2ru4agBWY0ZviFp9mnPz')
    api = tweepy.API(auth)  # http://docs.tweepy.org/en/v3.5.0/api.html#tweepy-api-twitter-api-wrapper
    text = tweet.get()
    api.update_status(text)



# Creates a function that draws a square with the robot
def draw_square(robot):
    '''
    :type robot: rb.RoseBot
    '''
    robot.motor_controller.drive_pwm(50, 50)
    time.sleep(1.5)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, -50)
    time.sleep(1.1)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, 50)
    time.sleep(1.5)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, -50)
    time.sleep(1.1)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, 50)
    time.sleep(1.5)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, -50)
    time.sleep(1.1)
    robot.motor_controller.stop()
    robot.motor_controller.drive_pwm(50, 50)
    time.sleep(1.5)
    robot.motor_controller.stop()



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
