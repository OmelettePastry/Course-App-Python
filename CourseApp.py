# Import modules

from tkinter import *
from Grade import *
from Person import *
from Course import *
import pickle

class CourseApp:
    """ This class contains the GUI Program window.
        The contents of this class include methods to update the window output, handlers to widget events
        and a constructor method to build the window. """

    def update_course_frame(self):
        """ This method updates data in the Course frame (Left frame)"""

        # Update Course name and number
        self._course_name_label.config(text="Course: " + self._course.get_course_name())
        self._course_number_label.config(text="Course #: " + self._course.get_course_number())

        # Store remaining Course and Instructor data in temporary variables
        course_average = "{:.2f}".format(self._course.get_course_average())
        course_instructor = self._course.get_instructor().get_first_name() + " " + self._course.get_instructor().get_last_name()
        course_instructor_dep = self._course.get_instructor().get_department()
        course_instructor_room = self._course.get_instructor().get_office_number()

        # Update Course and Instructor data using above variables
        self._course_average_label.config(text="Course Avg: " + course_average)
        self._course_instructor_label.config(text="Instructor: " + course_instructor)

        self._instructor_dep.config(text="Department: " + course_instructor_dep)
        self._instructor_room.config(text="Room #: " + course_instructor_room)

    def student_list_exist(self):
        """ This method determines if a Course contains Student objects in the student list """

        does_exist = False

        # Determines if the student list contains any objects
        if (len(self._course.get_student_list()) > 0):
            does_exist = True

        return does_exist

    def grade_list_exist(self):
        """ This method determines if a Student has any grades """

        does_exist = False

        # Determine if a student's grade list contains any grades
        if (self.student_list_exist()) and (len(self._course.get_student_list()[self.get_selected_student_index()].get_grade_list()) > 0):
            does_exist = True

        return does_exist

    def select_student(self, event):
        """ This method (handler) executes when the student listbox is clicked """

        # Updates (1) Student information frame, (2) Grade listbox and (3) Grade information
        self.update_student_info()
        self.update_grades_listbox()
        self.update_grade_info()       

    def select_grades(self, event):
        """ This method (handler) is called when the grades listbox is clicked """

        # Update grade information
        self.update_grade_info()

    def get_selected_student_index(self):
        """ This method returns the current selected index in the student listbox """

        index = 0

        # Get the selected student listbox index if there are students in the students list
        if (self._student_listbox.size() > 0):
            
            index = self._student_listbox.curselection()[0]

        return index

    def get_selected_grade_index(self):
        """ This method returns the current selected index in the grades listbox """

        index = 0

        # Returns the grade listbox index if there are any grades
        if (self._grades_listbox.size() > 0):

            index = self._grades_listbox.curselection()[0]

        return index

    def update_student_info(self):
        """ This method updates the data in the student information frame (middle frame) """

        # Initialize variables with empty default values
        name = ""
        student_ID = ""
        average_grade = ""

        # Determine if there are student objects in the student list
        if self.student_list_exist():
            
            student_list_index = self.get_selected_student_index()

            name = self._course.get_student_list()[student_list_index].get_first_name() + " " + self._course.get_student_list()[student_list_index].get_last_name()
            student_ID = self._course.get_student_list()[student_list_index].get_student_ID()

            # Determine if the selected student has any grades (This will be used to determine the average grade, if any)            
            if self.grade_list_exist():
                average_grade = "{:.2f}".format(self._course.get_student_list()[student_list_index].get_average_grade() * 100)

        # Update Student information labels
        self._name_label.config(text="Name: " + name)
        self._student_ID_label.config(text="Student ID: " + student_ID)
        self._average_grade_label.config(text="Average Grade: " + average_grade)

    def update_student_listbox(self):
        """ This method updates the student listbox """

        # Remove all entries from the student listbox
        self._student_listbox.delete(0, END)

        # Fill the student listbox with student names (if they exist)
        if (self.student_list_exist()):

            for student in self._course.get_student_list():
                
                self._student_listbox.insert(END, student.get_first_name() + " " + student.get_last_name())

            # Set student listbox index to first entry
            self._student_listbox.select_set(0)

    def update_grades_listbox(self):
        """ This method updates the grades listbox """

        # Remove all entries from the grades listbox
        self._grades_listbox.delete(0, END)

        # Fill the grade listbox with the selected student's grades (if they exist)
        if (self.student_list_exist() and self.grade_list_exist()):

            student_list_index = self.get_selected_student_index()
            grades_list = self._course.get_student_list()[student_list_index].get_grade_list()

            for i in range(len(grades_list)):

                self._grades_listbox.insert(END, grades_list[i].get_description())

            # Set grade listbox to select first entry
            self._grades_listbox.select_set(0)                   

    def update_student_data(self):
        """ This method updates the student information and grades frame (Bottom of middle frame and right-most frame) """

        self.update_student_info()
        self.update_grades_listbox()
        self.update_grade_info()
        
    def update_grade_info(self):
        """ This method updates the grades information (bottom section of grades frame) """

        # Initialize variables with empty values
        grade_points = ""
        max_points = ""

        # Update grades information labels (If a student and grade exists)
        if (self.student_list_exist() and self.grade_list_exist()):

            student_index = self.get_selected_student_index()
            grades_index = self.get_selected_grade_index()

            grade_points = "{:.2f}".format(self._course.get_student_list()[student_index].get_grade_list()[grades_index].get_grade())
            max_points = "{:.2f}".format(self._course.get_student_list()[student_index].get_grade_list()[grades_index].get_max_points())

        # Actual label updating
        self._grade_label.config(text="Points: " + grade_points)
        self._max_points_label.config(text="Max Points: " + max_points)

    def delete_grades(self):
        """ Deletes a grade """

        # Determine if there are grades in the grade list
        if (self.grade_list_exist()):

            # Remove selected grade object from the grade list
            self._course.get_student_list()[self.get_selected_student_index()].remove_grade(self.get_selected_grade_index())

            # Update course frame and student data
            self.update_course_frame()
            self.update_student_data()

    def delete_student(self):
        """ Deletes a student """

        # Determine if any student objects exist
        if (self.student_list_exist()):

            # Remove student object from student list
            self._course.remove_student(self.get_selected_student_index())

            # Update appropriat frames and widgets
            self.update_course_frame()
            self.update_student_listbox()
            self.update_student_data()

    def edit_student(self):
        """ Edit the student's information """

        # Determine if student list has any student objects
        if (self.student_list_exist()):

            # Call method to edit student data
            self.edit_student_popup()

    def edit_student_popup(self):
        """ This method creates a Toplevel() widget that will edit a student's data """

        # Create Toplevel() widget
        self._edit_student = Toplevel(self._master)
        self._edit_student.attributes("-topmost", 1)
        self._edit_student.title("Edit Student")

        # Create and add appropriate labels and entry boxes to the window
        edit_fname_label = Label(self._edit_student, justify=LEFT, text="First Name")
        edit_fname_label.grid(sticky=W, row=0)

        edit_lname_label = Label(self._edit_student, justify=LEFT, text="Last Name")
        edit_lname_label.grid(sticky=W, row=1)

        edit_student_ID_label = Label(self._edit_student, justify=LEFT, text="Student ID")
        edit_student_ID_label.grid(sticky=W, row=2)

        self._edit_fname_entry = Entry(self._edit_student)
        self._edit_fname_entry.grid(sticky=W, row=0, column=1)

        self._edit_lname_entry = Entry(self._edit_student)
        self._edit_lname_entry.grid(sticky=W, row=1, column=1)

        self._edit_student_ID_entry = Entry(self._edit_student)
        self._edit_student_ID_entry.grid(sticky=W, row=2, column=1)

        edit_student_ok = Button(self._edit_student, text="Change", command=self.edit_student_ok)
        edit_student_ok.grid(row=3, column=0, columnspan=2)

    def edit_student_ok(self):
        """ This method (handler) will execute is the 'Change' button is clicked in the edit student popup window """

        # Determine if data was entered in all three entry widgets
        if(self._edit_fname_entry.get() and self._edit_lname_entry.get() and self._edit_student_ID_entry.get()):

            # Updates student data in the selected student object
            self._course.get_student_list()[self.get_selected_student_index()].set_first_name(self._edit_fname_entry.get())
            self._course.get_student_list()[self.get_selected_student_index()].set_last_name(self._edit_lname_entry.get())
            self._course.get_student_list()[self.get_selected_student_index()].set_student_ID(self._edit_student_ID_entry.get())

            # Destroy "Edit Student" Toplevel() window
            self._edit_student.destroy()

            # Update appropriate frames and widgets
            self.update_student_listbox()
            self.update_student_info()     

    def create_add_student_popup(self):
        """ This method will create a Toplevel() widget that will add a student to the student list """
        
        # Create Toplevel() window widget
        self._add_student = Toplevel(self._master)
        self._add_student.attributes("-topmost", 1)
        self._add_student.title("Add Student")

        # Create and add appropriate label and entry widgets to the Toplevel() window
        add_fname_label = Label(self._add_student, justify=LEFT, text="First Name")
        add_fname_label.grid(sticky=W, row=0)

        add_lname_label = Label(self._add_student, justify=LEFT, text="Last Name")
        add_lname_label.grid(sticky=W, row=1)

        add_student_ID_label = Label(self._add_student, justify=LEFT, text="Student ID")
        add_student_ID_label.grid(sticky=W, row=2)

        self._add_fname_entry = Entry(self._add_student)
        self._add_fname_entry.grid(sticky=W, row=0, column=1)

        self._add_lname_entry = Entry(self._add_student)
        self._add_lname_entry.grid(sticky=W, row=1, column=1)

        self._add_student_ID_entry = Entry(self._add_student)
        self._add_student_ID_entry.grid(sticky=W, row=2, column=1)

        student_ok = Button(self._add_student, text="Add", command=self.student_ok)
        student_ok.grid(row=3, column=0, columnspan=2)

    def student_ok(self):
        """ This method (handler) will execute when the user clicks on the "Add" button int the student add popup """

        # Determine if data was entered in all three entry widgets
        if(self._add_fname_entry.get() and self._add_lname_entry.get() and self._add_student_ID_entry.get()):

            # Adds a student object into the student list
            self._course.add_student(Student(self._add_fname_entry.get(), self._add_lname_entry.get(), self._add_student_ID_entry.get()))

            # Destroy "Add Student" window
            self._add_student.destroy()

            # Update approrpiate frames and widgets
            self.update_student_listbox()
            self.update_student_data()

    def change_grades(self):
        """ This method (handler) will execute when the user clicks on the "Change Grades" button """

        # Determine if grade objects exist in the grade list
        if (self.grade_list_exist()):

            # Call method to create a popup to change a grade
            self.create_change_grade_popup()

    def create_change_grade_popup(self):
        """ This method creates a Toplevel() widget that allows the user to change a student's grade """

        # Create a Toplevel() widget        
        self._change_grades = Toplevel(self._master)
        self._change_grades.attributes("-topmost", 1)
        self._change_grades.focus_force()
        self._change_grades.title("Change Grade")

        # Create appropriate label and entry widgets for window
        change_grade_label = Label(self._change_grades, justify=LEFT, text="Grade")
        change_grade_label.grid(sticky=W, row=0)

        change_grade_label = Label(self._change_grades, justify=LEFT, text="Max Points   ")
        change_grade_label.grid(sticky=W, row=1)

        self._change_grade_entry = Entry(self._change_grades)
        self._change_grade_entry.grid(sticky=W, row=0, column=1)

        self._change_max_points_entry = Entry(self._change_grades)
        self._change_max_points_entry.grid(sticky=W, row=1, column=1)

        change_ok = Button(self._change_grades, text="Ok", command=self.change_ok)
        change_ok.grid(row=2, column=0, columnspan=2)

    def change_ok(self):
        """ This method (handler) will execute when the user clicks on the "Ok" button in the change grade popup """

        # Determine if any text was entered in the entry widgets
        if (self._change_grade_entry.get() and self._change_max_points_entry.get()):

            student_index = self.get_selected_student_index()
            grade_index = self.get_selected_grade_index()

            # Update grades in the selected grade object
            self._course.get_student_list()[student_index].get_grade_list()[grade_index].set_grade(float(self._change_grade_entry.get()))
            self._course.get_student_list()[student_index].get_grade_list()[grade_index].set_max_points(float(self._change_max_points_entry.get()))

            # Destroy window
            self._change_grades.destroy()

            # Update appropriate frame and widget data
            self.update_course_frame()
            self.update_student_data()

    def add_grades(self):
        """ This method (handler) executes when the user clicks on the "Add Grades" button """

        # Determine if there are any student objects in the student list
        if self.student_list_exist():

            # Call method to create a popup to add grades
            self.create_add_grade_popup()

    def create_add_grade_popup(self):
        """ This method creates a Toplevel() window to add grades to a student's grade list """

        # Create Toplevel() widget
        self._add_grades = Toplevel(self._master)
        self._add_grades.attributes("-topmost", 1)
        self._add_grades.title("Add Grade")

        # Create and add appropriate label and entry widgets
        desc_label = Label(self._add_grades, justify=LEFT, text="Grade Description    ")
        desc_label.grid(sticky=W, row=0)

        add_grade_label = Label(self._add_grades, justify=LEFT, text="Grade")
        add_grade_label.grid(sticky=W, row=1)

        add_max_points_label = Label(self._add_grades, justify=LEFT, text="Max Points")
        add_max_points_label.grid(sticky=W, row=2)

        self._AG_desc_entry = Entry(self._add_grades)
        self._AG_desc_entry.grid(sticky=W, row=0, column=1)

        self._AG_entry = Entry(self._add_grades)
        self._AG_entry.grid(sticky=W, row=1, column=1)

        self._AG_max_points_entry = Entry(self._add_grades)
        self._AG_max_points_entry.grid(sticky=W, row=2, column=1)

        add_ok = Button(self._add_grades, text="Add", command=self.add_grade_ok)
        add_ok.grid(row=3, column=0, columnspan=2)

    def add_grade_ok(self):
        """ This method (handler) executes when the user clicks on the "Add" button in the add grade popup """
        
        # Determine if the user entered data in all three entry boxes
        if (self._AG_desc_entry.get() and self._AG_entry.get() and self._AG_max_points_entry.get()):

            student_index = self.get_selected_student_index()

            # Add a grade object to the grade list
            self._course.get_student_list()[student_index].get_grade_list().append(Grade("", self._AG_desc_entry.get(), float(self._AG_max_points_entry.get()), float(self._AG_entry.get())))

            # Destroy window
            self._add_grades.destroy()

            # Update appropriate frames and widgets
            self.update_course_frame()
            self.update_student_data()


    def update_all(self):
        """ This method updates data on all the frames and widgets except those in the Course frame """

        # Update appropriate frames and widgets
        self.update_student_listbox()
        self.update_student_info()
        self.update_grades_listbox()
        self.update_grade_info()

    def create_openfile_popup(self):
        """ This method (handler) executes when the user selects "Open" from the file menu """

        # Create Toplevel() widget
        self._openfile_popup = Toplevel(self._master)
        self._openfile_popup.attributes("-topmost", 1)
        self._openfile_popup.title("Open File")

        # Create appropriate label and entry eidgets
        file_label = Label(self._openfile_popup, justify=LEFT, text="File    ")
        file_label.grid(sticky=W, row=0)

        self._file_entry = Entry(self._openfile_popup)
        self._file_entry.grid(sticky=W, row=0, column=1)

        openfile_ok = Button(self._openfile_popup, text="Open", command=self.open_ok)
        openfile_ok.grid(row=1, column=0, columnspan=2)

    def open_ok(self):
        """ This method (handler) executes when the user clicks "Open" in the openfile popup """

        # Determine if any text was entered
        if(self._file_entry.get()):

            # Open file for binary reading and load into course object
            file_object = open(self._file_entry.get(), "rb")

            self._current_file = self._file_entry.get()

            self._openfile_popup.destroy()

            self._course = pickle.load(file_object)

            file_object.close()

            # Update window title and appropriate frames and widgets
            self.update_window_title()
            self.update_course_frame()
            self.update_all()

    def save_coursefile(self):
        """ This method (handler) executes when the user clicks "Save" in the menu """

        # Determine if there is a current filename
        if (self._current_file):

            # Save object into file
            file_object = open(self._current_file, "wb")
            pickle.dump(self._course, file_object)

    def save_as_popup(self):
        """ This method (handler) executes when the user clicks "Save As" in the menu """

        # Create Toplevel() widget
        self._save_as_popup = Toplevel(self._master)
        self._save_as_popup.attributes("-topmost", 1)
        self._save_as_popup.title("Save As File")

        # Create appropriate label and entry widgets
        savefile_label = Label(self._save_as_popup, justify=LEFT, text="File    ")
        savefile_label.grid(sticky=W, row=0)

        self._savefile_entry = Entry(self._save_as_popup)
        self._savefile_entry.grid(sticky=W, row=0, column=1)

        savefile_ok = Button(self._save_as_popup, text="Save As", command=self.save_as_ok)
        savefile_ok.grid(row=1, column=0, columnspan=2)

    def save_as_ok(self):
        """ This method (handler) executes when the user clicks on the "Save As" button the save as popup """

        # Open file and save object to file
        file_object = open(self._savefile_entry.get(), "wb")
        self._current_file = self._savefile_entry.get()

        self._save_as_popup.destroy()

        pickle.dump(self._course, file_object)
        file_object.close()

    def new_course(self):
        """ This method (handler) executes when the use clicks on  "New" in the menu """

        # Create Toplevel() widget
        self._new_course = Toplevel(self._master)
        self._new_course.attributes("-topmost", 1)
        self._new_course.title("New Course")

        # Create appropriate label and entry widgets
        course_name_label = Label(self._new_course, justify=LEFT, text="Course Name")
        course_name_label.grid(sticky=W, row=0)

        course_number_label = Label(self._new_course, justify=LEFT, text="Course Number")
        course_number_label.grid(sticky=W, row=1)

        course_desc_label = Label(self._new_course, justify=LEFT, text="Course Desscription")
        course_desc_label.grid(sticky=W, row=2)

        instructor_fname_label = Label(self._new_course, justify=LEFT, text="Instructor First Name")
        instructor_fname_label.grid(sticky=W, row=3)
        
        instructor_lname_label = Label(self._new_course, justify=LEFT, text="Instructor Last Name")
        instructor_lname_label.grid(sticky=W, row=4)

        instructor_department_label = Label(self._new_course, justify=LEFT, text="Inst. Department")
        instructor_department_label.grid(sticky=W, row=5)

        instructor_room_label = Label(self._new_course, justify=LEFT, text="Inst. Room #:")
        instructor_room_label.grid(sticky=W, row=6)

        self._NC_course_name_entry = Entry(self._new_course)
        self._NC_course_name_entry.grid(sticky=W, row=0, column=1)

        self._NC_course_number_entry = Entry(self._new_course)
        self._NC_course_number_entry.grid(sticky=W, row=1, column=1)

        self._NC_course_desc_entry = Entry(self._new_course)
        self._NC_course_desc_entry.grid(sticky=W, row=2, column=1)

        self._NC_instructor_fname_entry = Entry(self._new_course)
        self._NC_instructor_fname_entry.grid(sticky=W, row=3, column=1)

        self._NC_instructor_lname_entry = Entry(self._new_course)
        self._NC_instructor_lname_entry.grid(sticky=W, row=4, column=1)

        self._NC_instructor_dep_entry = Entry(self._new_course)
        self._NC_instructor_dep_entry.grid(sticky=W, row=5, column=1)

        self._NC_instructor_room_entry = Entry(self._new_course)
        self._NC_instructor_room_entry.grid(sticky=W, row=6, column=1)

        self._course_ok = Button(self._new_course, text="Create Course", command=self.create_course_ok)
        self._course_ok.grid(row=7, column=0, columnspan=2)

    def create_course_ok(self):
        """ This method (handler) executes when the user clicks on "Create Course" in the new course popup """

        # Determine if all entry widgets were filled out
        if (self._NC_course_name_entry.get() and self._NC_course_number_entry.get() and self._NC_course_desc_entry.get() \
           and self._NC_instructor_fname_entry.get() and self._NC_instructor_lname_entry.get() and self._NC_instructor_dep_entry.get() \
           and self._NC_instructor_room_entry.get()):

            # Create Instructor object
            instructor = Instructor(self._NC_instructor_fname_entry.get(), self._NC_instructor_lname_entry.get(), self._NC_instructor_dep_entry.get(), self._NC_instructor_room_entry.get())

            # Set our course field member
            self._course = Course(self._NC_course_name_entry.get(), self._NC_course_number_entry.get(), self._NC_course_desc_entry.get(), instructor)

            # Destroy popup window
            self._new_course.destroy()

            # Update appropriate frames and widgets
            self.update_window_title()
            self.update_course_frame()
            self.update_all()

    def update_window_title(self):
        """ This method updates the window title text """

        self._master.title(self._course.get_course_name() + " " + self._course.get_course_number())
            
    def exit_app(self):
        """ Destroy the master window """

        self._master.destroy()
        
    def __init__(self, master):
        """ Constructor - This will create the frames and widgets for the master window. """

        # Fields
        self._course = []
        self._current_file = ""
        self._master = master

        # Create menubar
        menubar = Menu(master)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_course)
        filemenu.add_command(label="Open", command=self.create_openfile_popup)
        filemenu.add_command(label="Save", command=self.save_coursefile)
        filemenu.add_command(label="Save As...", command=self.save_as_popup)
        filemenu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=filemenu)

        self._master.config(menu=menubar)

        # Create Course and Instructor information frame (LEFT frame)
        course_frame = LabelFrame(master, height=340, width=200, text="Course Info", padx=5, pady=5, bd=1)

        self._course_name_label = Label(course_frame, justify=LEFT, text="Course:")
        self._course_name_label.pack(anchor=W, side=TOP)
        
        self._course_number_label = Label(course_frame, justify=LEFT, text="Course #:")
        self._course_number_label.pack(anchor=W, side=TOP)
        
        self._course_average_label = Label(course_frame, justify=LEFT, text="Course Avg:")
        self._course_average_label.pack(anchor=W, side=TOP)
        
        self._course_instructor_label = Label(course_frame, justify=LEFT, text="Instructor:")
        self._course_instructor_label.pack(anchor=W, side=TOP)

        self._instructor_dep = Label(course_frame, justify=LEFT, text="Department:")
        self._instructor_dep.pack(anchor=W, side=TOP)

        self._instructor_room = Label(course_frame, justify=LEFT, text="Room #:")
        self._instructor_room.pack(anchor=W, side=TOP)

        course_frame.pack(side=LEFT, anchor=N, fill=Y)
        course_frame.pack_propagate(0)
        
        # Create Student Data frame (MIDDLE frame)

        student_frame = LabelFrame(master, height=340, width=160, text="Students", padx=5, pady=5, bd=1)

        self._student_listbox = Listbox(student_frame, selectmode=BROWSE, exportselection=0)
        self._student_listbox.pack(anchor=N, side=TOP, fill=X, expand=1)
        self._student_listbox.bind("<<ListboxSelect>>", self.select_student)

        self._name_label = Label(student_frame, justify=LEFT, text="Name:")
        self._name_label.pack(anchor=W, side=TOP)

        self._student_ID_label = Label(student_frame, justify=LEFT, text="Student ID:")
        self._student_ID_label.pack(anchor=W, side=TOP)
        
        self._average_grade_label = Label(student_frame, justify=LEFT, text="Average Grade:")
        self._average_grade_label.pack(anchor=W, side=TOP)

        edit_student_button = Button(student_frame, text="Edit Student", command=self.edit_student)
        edit_student_button.pack(side=TOP)

        add_student_button = Button(student_frame, text="Add Student", command=self.create_add_student_popup)
        add_student_button.pack(side=TOP)

        delete_student_button = Button(student_frame, text="Delete Student", command=self.delete_student)
        delete_student_button.pack(side=TOP)
       
        student_frame.pack(side=LEFT, anchor=N, fill=Y, expand=1)
        student_frame.pack_propagate(0)

        # Create Grade Information frame (RIGHT frame)

        grades_frame = LabelFrame(master, height=340, width=160, text="Grades", padx=5, pady=5, bd=1)
        
        self._grades_listbox = Listbox(grades_frame, selectmode=BROWSE, exportselection=0)
        self._grades_listbox.pack(anchor=N, side=TOP, fill=X, expand=1)
        self._grades_listbox.bind("<<ListboxSelect>>", self.select_grades)        

        self._grade_label = Label(grades_frame, justify=LEFT, text="Points:")
        self._grade_label.pack(anchor=W, side=TOP)

        self._max_points_label = Label(grades_frame, justify=LEFT, text="Max Points:")
        self._max_points_label.pack(anchor=W, side=TOP)
        
        change_grade_button = Button(grades_frame, text="Change Grade", command=self.change_grades)
        change_grade_button.pack(side=TOP)

        add_grade_button = Button(grades_frame, text="Add Grade", command=self.add_grades)
        add_grade_button.pack(side=TOP)

        delete_grade_button = Button(grades_frame, text="Delete Grade", command=self.delete_grades)
        delete_grade_button.pack(side=TOP)

        grades_frame.pack(side=LEFT, anchor=N, fill=Y, expand=1)
        grades_frame.pack_propagate(0)

    def add_course_data(self, course):
        """ This method adds a course object into the _course field """

        # Set course object
        self._course = course

        # Update appropriate frames and widgets
        self.update_course_frame()
        self.update_all()
        
        
