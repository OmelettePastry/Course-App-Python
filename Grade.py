class Grade:
    """ This class contains data and methods for a grade object """
    
    def __init__(self, grade_ID, grade_description, max_points, grade):
        """ Constructor """

        self._grade_ID = grade_ID
        self._grade_description = grade_description
        self._max_points = max_points
        self._grade = grade

    def get_grade_ID(self):
        """ Returns grade ID """

        return self._grade_ID

    def get_max_points(self):
        """ Returns maximum points possible for a grade """

        return self._max_points

    def get_grade(self):
        """ Return the grade """

        return self._grade

    def get_average(self):
        """ Return the grade (0 to 1) """

        return self.get_grade() / self.get_max_points()

    def get_description(self):
        """ Return the grade description """

        return self._grade_description    

    def set_grade(self, grade):
        """ Set the current grade to that of the parameter value """

        self._grade = grade

    def set_max_points(self, max_points):
        """ Set the max points to that of the parameter value """

        self._max_points = max_points

    

        
