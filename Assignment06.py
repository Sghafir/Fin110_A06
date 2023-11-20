# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   SGhafir, 11/19/2013, Created scrip with the intention of using functions, classes
# and separation of concerns
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json
from typing import IO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Processing functions
class FileProcessor:
    '''
    A collection of functions used to process JSON data

    change log: (Who, When, What)
    Sghafir, 11/19/23, Created Class
    '''

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            print('Data Saved!')
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()

# Presentation functions
class IO:
    '''
    A collection of presentation functions

    change log: (Who, When, What)
    SGhafir, 11/19/23, Created Class
    '''

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        '''
        This function displays a certain error to the user
        when an exception is triggered
        :param message:
        :param error:
        :return: None
        '''
        print(message, end = "\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep = '\n')
            print('=' * 30)

    @staticmethod
    def output_menu(menu: str):
        '''
        This functions displays the menu to the user
        :param menu:
        :return: None
        '''
        print('=' * 30)
        print(menu)
        print('=' * 30)

    @staticmethod
    def input_menu_choice():
        '''
        This function processes the menu choice from user
        :return: None
        '''
        choice = '0'
        try:
            choice = input('Select an option from the Menu: ')
            if choice not in ('1', '2', '3', '4'):
                raise Exception('Please select a number displayed on the menu')
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        '''
        This function is supposed to output all of the registration data collected from the student
        :param student_data:
        :return: None
        '''
        #processing the data
        print()
        print("=" * 30)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("=" * 30)
        print()


    @staticmethod
    def input_student_data(student_data: list):
        '''
        This function collects all the student data and then inputs it into a list
        :param student_data:
        :return: str
        '''
        try:
            print()
            print('Welcome to student registration')
            print()
            # input the data
            student_first_name = input('what is the students first name?: ')
            if not student_first_name.isalpha():
                raise ValueError('the first name can not contain any numbers')
            student_last_name = input('what is the students last name?: ')
            if not student_last_name.isalpha():
                raise ValueError('the last name can not contain any numbers')
            try:
                course_name = str(input('what is the course name?: '))
            except ValueError:
                raise ValueError('course name must have the name & number combination')

            student = {"FirstName": student_first_name, "LastName": student_last_name,
                   "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("Value is not the correct format needed", e)
        except Exception as e:
            IO.output_error_messages("There was a non specfic error", e)
        return student_data

# Data Layer: Reading data from the file

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Processing Layer: collecting data from the user

while(True):
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == '1':
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == '2':
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    elif menu_choice == '4':
        print('program ending')
        break



