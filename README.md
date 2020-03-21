

# Clothed SuperStore
The url for the app is  https://pwitter.pythonanywhere.com/


## Project description
This is website store that I built that replicates some of the functionality of twitter. It allows the
to post, edit and delete twitters, follow and unfollow users, view users tweets once they you are following
them, etc once you have signed up.

Disclaimer
For copyright I called it pwitter.


## Technologies used
1. Python 3.6
1. Flask
1. HTML
1. Bootstrap
1. Sqlite3
1. SQLAlchemy
1. Bootstrap

##Things to do
1. Write tests
1. Finish working on the automation selenium test

## How to run this in your local system
1. Create a virtual environment optional
1. Create a **name** for your directory
1. Go into your new directory
1. Clone the repository by using the command git clone followed by a **.** The full stop at end copies all the folder and directories and sub-directories into the your chosen directory without creating the based folder.
1. Type the command "**pip install -r requirements.txt**" (making sure you are in the root directory) this will install all the dependencies on your virtual environment

1. (First time use only) Open a command terminal make sure you are in the forum root folder and type the command: 
    1. python app.py db init
    1. python app.py db migrate
    1. python app.py db upgrade
    1. Next open a python terminal and type the following command
        1. from create_app import db
        1. db.create_all()

1. Next we need to create our local database. Make sure you are in the root store folder open a terminal and type
    1. python "create_db.py" -d <name for the database with no space>.db
    1. Open the settings file and replace <name of database no spaces> with your database name
       Note it must end with ".db"

1. Open the **settings.py** and enter the full path to **imgs** folder. The path will be different depending
if it is on a Windows, Mac or Linux. Windows you must use double slash "\\" and "/" for Mac or Linux. Regardless of what OS
the final path must end either with "/imgs" or "\\imgs"
1. Next run the command ** flask run** If you get an error type in the command
    1. set FLASK_APP=app.py
    1. ** flask run **
1. Open a browser of your choice and type in **http://127.0.0.1:5000** and watch app go
1. To use or see a live demonstration of the app go to **https://pwitter.pythonanywhere.com/**

1. For any bugs found hit me up at "egbieuku@hotmail.com"

