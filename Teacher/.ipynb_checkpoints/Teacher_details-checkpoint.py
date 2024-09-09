import os,sys
from os.path import dirname,join,abspath
from Student import Student_details


parent_dir_path = abspath(join(dirname(__file__), ".."))
sys.path.insert(0,parent_dir_path)



def teacher():
    print("This is a teacher.")

Student_details.student()


# teacher() 
# if you uncomment teacher() it will be called when the package is imported