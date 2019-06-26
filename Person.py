from Grade import *

class Person:
    """ This class contains data and methods for a Person """
    
    def __init__(self, first_name, last_name):
        """ Constructor """
        
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        """ Return first name """

        return self._first_name

    def get_last_name(self):
        """ Returns last name """

        return self._last_name

    def set_first_name(self, first_name):
        """ Set first name """

        self._first_name = first_name

    def set_last_name(self, last_name):
        """ Set last name """

        self._last_name = last_name

    def to_string(self):
        """ Returns first and last name """

        return (self._first_name + " " + self._last_name)

class Student(Person):
    """ This class contains data and methods for a student.
        This class inherits from the 'Person' class """

    def __init__(self, first_name, last_name, student_ID):
        """ Constructor """

        super().__init__(first_name, last_name)

        self._student_ID = student_ID
        self._grades = []

    def get_student_ID(self):
        """ Returns the student ID """

        return self._student_ID

    def set_student_ID(self, student_ID):
        """ Set the student ID to that in the parameter """

        self._student_ID = student_ID

    def get_grade_list(self):
        """ Return a reference to the list of grades """

        return self._grades

    def add_grade(self, grade):
        """ Add a grade object to the grade list """

        self._grades.append(grade)

    def remove_grade(self, grade_index):
        """ Remove grade object from the grade list """

        self._grades.pop(grade_index)

    def get_num_grades(self):
        """ Return the number of grades in the grade list """

        return len(self._grades)

    def get_max_points(self):
        """ Return total max points in all grades """

        max_points = 0

        for grade in self._grades:

            max_points = max_points + grade.get_max_points()

        return max_points

    def get_total_points(self):
        """ Return total grade points in all grades """

        total_points = 0

        for grade in self._grades:

            total_points = total_points + grade.get_grade()

        return total_points

    def get_average_grade(self):
        """ Return average grade of student """

        return (self.get_total_points() / self.get_max_points())

    def to_string(self):
        """ Returns a strin of student data:  Student ID, name, and list of grades """

        string = "Student ID: " + self._student_ID + "\nName: " + \
                 super().to_string() + "\nGrades\n"
        
        for i in range(0, len(self._grades)):
            string = string + "{:7.2f}".format(self._grades[i].get_grade() / \
                                               self._grades[i].get_max_points() * \
                                               100.0)

        return string

class Instructor(Person):
    """ This class contains data and methods for an Instructor object.
        This class inherits from the 'Person' class. """

    def __init__(self, first_name, last_name, department, office_number):
        """ Constructor """

        super().__init__(first_name, last_name)

        self._department = department
        self._office_number = office_number

    def get_department(self):
        """ Returns instructor department """

        return self._department

    def get_office_number(self):
        """ Returns office number """

        return self._office_number

    def to_string(self):
        """ Returns a string of the instructor name, department and office number """

        return (super().to_string() + "\nDepartment: " + \
                self._department + "\nOffice Number: " + \
                self._office_number)
                



    
    

        

        
