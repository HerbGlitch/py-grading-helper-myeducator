# py-grading-helper-myeducator

# SETUP

make sure python is added to your path.
git clone
cd to root of this project

run (in cmd):
pip install virtualenv
virtualenv env
env\scripts\activate
pip install -r requirements.txt
code .

create a .credentials file
in your .credentials file add the lines (using your credentials):
auth_email,your.email@email.com
auth_password,password

change this line in main.py:
myeducator = MyEducator("Introduction to Python Data Analytics (BYU w20 S1)", "Python: Iterations")
#                        ^-Course Name                                         ^-Chapter Name
