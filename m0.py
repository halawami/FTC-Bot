"""
The Python Capstone Project.

This file contains data SHARED by the other modules in this project.

CSSE 120 - Introduction to Software Development.
Team members: Hussein Alawami, Haolen Cheng, and Dongrui Hu (all of them).
"""
# Done: Put the names of ALL team members in the above where indicated.

import m1
import m2
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb

# ----------------------------------------------------------------------
# Done: TEAM-PROGRAM this module so that it runs your entire program,
#       incorporating parts from m1 .. m3.
# ----------------------------------------------------------------------

class DataContainer(object, metaclass=rb.__FreezeClass__):
    """
    A container for the data shared across the application.
    Remember to CONSTRUCT a DataContainer with:
       dc = DataContainer()
    """
    def __init__(self):
        """ Initializes instance variables (fields). """

        # Add     self.FOO = BLAH     here as needed.
        # Choose meaningful names!

        self.robot = rb.RoseBot()
        self.robot.is_stopped = False


def main():
    """ Runs the MAIN PROGRAM. """
    print('----------------------------------------------')
    print('Integration Testing of the INTEGRATED PROGRAM:')
    print('----------------------------------------------')

    root = tkinter.Tk()
    dc = DataContainer()
    frame1 = m1.my_frame(root, dc)
    frame2 = m2.my_frame(root, dc)
    frame3 = m3.my_frame(root, dc)
    frame4 = m4.my_frame(root, dc)

    frames = [frame1, frame2, frame3, frame4]

    for k in range(len(frames)):

        if frames[k]:

            frames[k].grid(row=1, column=k + 1)

    root.mainloop()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
