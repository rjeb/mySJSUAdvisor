import re

class Course(object):
    """ An object to represent a class/course in the SJSU catalogue

        Arguments: coursefile: text file containing course info

        Attributes:
        start_time: starting time of class
        seats_total:
        seats_taken:
        units: number of units the class is worth
        class_days: MW, TTH, F, etc. enum representation
        course_desc: string describing the class
        GE_TYPE: enum for the GE Type(if any) this class is in
        department: DEPT of class
        class_num: string that represents the number Ex. CS 161 <-
        section_number: number represents the section of the class
        professor: reference to the professor that teaches the class
    """

    def __init__(self, coursefile):
        self.read_course(coursefile)

    def read_course(self, coursefile):
        layout = coursefile.readlines()
        y = 0
        print(coursefile)
