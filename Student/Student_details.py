# To keep different components in different scripts
# model training and EDA should be kept in different scripts

# A module is a single file with a py extension which contains python code

# student details and teacher details py are modules

# package: a package is a collection of modules organised in directories
# each directory can have multiple python scripts
# examples :: student and teacher folders are packages


# for versions before python 3.3 to make a package it was necessary 
# to include __init__.py in package (to initialise package and expose required modules and functions.)

# This is not needed anymore though......

# Library: library is a collection of multiple package and modules 

from Teacher import Teacher_details  # from is used with package and import is used with modules >> generic use from wherever you want to import something from modules/packages 
import os , sys # provides functionality to operate with operating system
from os.path import dirname,join,abspath
#sys >> provides access to system specific parameters and function 

# dirname >> gives the directory containg the current  script
# join >> join two or more paths inserting a '/' as needed
# join(dirname(__file__),


# print("The path is",__file__)

# print('The directory of the script is ', dirname(__file__))

# print('The directory of the script is ', join(dirname(__file__),'..'))

# print('The directory of the script is ', abspath(join(dirname(__file__),'..')))








# at index 0 , add this directory to the beginning of module search path/ system path 

parent_dir_path = abspath(join(dirname(__file__),'..'))
sys.path.insert(0, parent_dir_path)


# to execute this code in an environment where you don't the directory use
# sys.path.insert

# __pycache__ also known as pyc file >> These are compiled python files >> source code to byte code >> stored in .pyc file inside __pycache__ directory 

# This helps to speed up the loading of module the next time its imported



#   '..' means one folder back  like Doc/Students/Student1/Student.py will be
# Doc/Students

# abspath converts the realtive path to absolute path 

def student():
    print("This is a student.")

# student()

# Teacher_details.teacher()


# To run a python file in jupyter lab 
# type %run (file location and name) 
# %run Student/Student_details.py