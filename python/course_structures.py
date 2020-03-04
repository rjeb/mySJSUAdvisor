import re

class Course(object):
    """ An object to represent a class/course in the SJSU catalogue

        Arguments: coursefile: text file containing course info

        Attributes:
        start_time: starting time of class
        end_time: ending time of class
        seats_total:
        seats_taken:
        units: number of units the class is worth
        class_days: MW, TTH, F, etc. enum representation
        course_desc: string describing the class
        GE_TYPE: enum for the GE Type(if any) this class is in
        department_name: DEPT of class
        class_num: string that represents the number Ex. CS 161 <-
        section_number: number represents the section of the class
        professor_name: name of the professor that teaches the class
    """

    def __init__(self, coursefile):
        self.read_course(coursefile)

    def read_course(self, coursefile):
        course_lines = coursefile.splitlines()
        y = 0

        """
        for line in course_lines:
            print(line + ": " + y.__str__())
            y += 1
        """

        self.units = re.sub("Units", "", course_lines[7], 1) #parse units
        self.start_time, self.end_time = re.split("\s", re.sub("Time", "", course_lines[13])) #parse start, end times
        self.class_days = re.sub("Days", "", course_lines[12], 1)
        self.seats_taken, self.seats_total, *trash = re.split("\s|/", re.sub("Enrollment", "", course_lines[10], 1)) #parse seats and trash rest of string
        self.section_num = re.sub("Section", "", course_lines[5], 1)
        self.course_desc = re.sub("Title", "", course_lines[2], 1)
        self.professor_name = re.sub("Instructor", "", course_lines[16], 1)
        self.class_code = re.sub("Code", "", course_lines[6], 1)
        self.class_mode = re.sub("Mode", "", course_lines[9], 1)
        self.department_name, self.class_num = re.split(" ", course_lines[17], 1)
        #print(self.department_name + " " + self.class_num)

    def to_string(self):
        print("Class: " + self.department_name + " " + self.class_num)
        print("Units:" + self.units)
        print("Duration: " + self.start_time + " to " + self.end_time)
        print("Days: " + self.class_days)
        print("Seats: " + self.seats_taken + " / " + self.seats_total)
        print("Section Num: " + self.section_num)
        print("Description: " + self.course_desc)
        print("Professor: " + self.professor_name)
        print("Class Code: " + self.class_code)
        print("Class Mode:" + self.class_mode)

class Professor(object):
    """ An object to represent a professor in SJSU

        Arguments: prof_file: text file containing course info

        Attributes:
        name: name of the professor
        rating: a professors professor rating
        hotness: how HOT a professor is
        profID: a number representing a professors ID
        dept: the department of the professor:
    """

class Department:
    """An object to represent an SJSU Department

    Arguments: deptfile: text file containing course info

    Attributes:
    name: name of Department
    classes: a collection of classes within the Department

    """