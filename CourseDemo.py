""" Object-Oriented Programming - Honors Project

    This program uses the python Tkinter module to create a GUI that
    allows the user to create Course data containing student information, grades
    and instructor information.  This program also allows the user to save and
    open files.

    Leng Her
    12/19/2018
"""

# Import modules

from tkinter import *
from CourseApp import *
from Course import *
from Person import *
from Grade import *

import random

def main():
    """ This contains the main program """

    # Create tkinter object and set attributes
    root = Tk()
    root.title("Course and Student Data")
    root.geometry('600x340')

    # Create our class object
    app = CourseApp(root)

    # Create Empty Instructor and Course objects
    instructor = Instructor("", "", "", "")
    course = Course("", "", "", instructor)

    # Add course to our app object
    app.add_course_data(course)

    # Run the window loop
    root.mainloop()

# Call main method
main()
