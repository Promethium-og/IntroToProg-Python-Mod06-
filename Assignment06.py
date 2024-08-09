# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   LBlas,8/7/2024,Completed Script
# ------------------------------------------------------------------------------------------ #
import json

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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    """  Performs file processing tasks """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from a file into a list of dictionary rows.

        :param file_name: (string) with name of file:
        :param student_data: (list) you want filled with file data:
        :return: (list) of student data
        """
        try:
            with open(file_name, "r") as file:
                students_data = json.load(file)
                student_data.extend(students_data)
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ Writes data to a file from a list of dictionary rows.

        :param file_name: (string) with name of file:
        :param student_data: (list) of data you want saved to the file:
        :return: nothing
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

class IO:
    """  Performs Input and Output tasks """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Displays error messages to the user

        :param message: (string) a custom error message to be displayed:
        :param error: (Exception) optional, an exception object with the error details:
        :return: nothing
        """
        print(message)
        if error:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """ Displays a menu to the user

        :param menu: (string) the menu you want displayed:
        :return: nothing
        """
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """ Gets the user's menu choice

        :return: (string) the user's menu choice
        """
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """ Displays the current student courses

        :param student_data: (list) the student data to be displayed:
        :return: nothing
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data() -> dict:
        """ Gets student data from the user

        :return: (dict) with student's first name, last name, and course name
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            return {"FirstName": student_first_name,
                    "LastName": student_last_name,
                    "CourseName": course_name}
        except ValueError as e:
            IO.output_error_messages(str(e), e)
            return {}

# When the program starts, read the file data into a list of lists (table)
FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_data = IO.input_student_data()
        if student_data:
            students.append(student_data)
            print(f"You have registered {student_data['FirstName']} {student_data['LastName']} for {student_data['CourseName']}.")

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
