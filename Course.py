# Import windows

import operator
from Person import *
from Grade import *

class Course:
    """ This class will contain data and methods for a Course object """

    def __init__(self, course_name, course_number, course_description, instructor):
        """ Constructor """
        
        self._course_name = course_name
        self._course_number = course_number
        self._course_description = course_description
        self._course_instructor = instructor
        self._students = []

    def get_course_name(self):
        """ Returns course name """

        return self._course_name

    def get_course_number(self):
        """ Returns course number """

        return self._course_number

    def get_course_description(self):
        """ Returns course description """

        return self._course_description

    def get_course_average(self):
        """ Returns average of all grades of all students in course """

        # Initialize variables with default values of 0
        total_points = 0
        max_points = 0
        average = 0

        # Iterate through all the students in the course
        for student in self._students:

            # Add total grades and total max points
            total_points = total_points + student.get_total_points()
            max_points = max_points + student.get_max_points()

        # Calculate average if the max points is not empty
        if not (max_points == 0):

            average = (total_points / max_points) * 100.0

        # Will return average (returns 0 if there are no grades)
        return average

    def get_student_list(self):
        """ Returns a reference to the student list """

        return self._students

    def get_num_students(self):
        """ Returns the number of students in the course """

        return len(self._students)

    def set_instructor(self, instructor):
        """ Set the _instructor field to that in the parameter """

        self._instructor = instructor

    def get_instructor(self):
        """ Return a reference to the _instructor field """

        return self._course_instructor

    def add_student(self, student):
        """ Add a student to the student list """

        self._students.append(student)

    def remove_student(self, student_index):
        """ Remove a student from the student list """

        self._students.pop(student_index)

    def sort_by_first(self):
        """ Sort the student list by first name """

        self._students.sort(key=lambda x: x.get_first_name(), reverse = False)

    def sort_by_last(self):
        """ Sort the student list by last name """

        self._students.sort(key=lambda x: x.get_last_name(), reverse = False)

    def sort_by_avg(self):
        """ Sort the student list by student grade average """

        self._students.sort(key=lambda x: x.get_average_grade(), reverse = True)

    def to_string(self):
        """ Returns a string containing student names """

        string = ""

        for i in range(0, len(self._students)):
            string = string + "Student #" + str(i + 1) + "\n" + \
                     self._students[i].to_string() + "\n\n"

        return string
                
                     
            
        

        

        

    
