## Windows set up instruction
If you installed Python with the default options,
you will probably need to add Python to the PATH variable.
This let's your operating system know where to look for the Python executable
when you try running it.

To add Python to your PATH variable:
1. Find the path of **python.exe** on your system.
[Look in these directories](PATH_LOCATIONS.md) or search for it.

1. Open *System Properties* and click on the *Advanced* tab

1. Click on *Environment Variables*

1. Under *System variables* find and click on the *Path* variable

1. In edit mode, go to the end of the line and add **;C:\Python38** or whatever folder *python.exe* is in. 
Note the semicolon before the path; this will separate it from the previous path.

To check that the PATH variable was set properly:
1. Open the *Command Prompt* application in Windows
or *Terminal* on Mac or Linux

1. Type `python --version` and press enter

1. Type `python3 --version` and press enter

1. Type `py --version` and press enter (Windows)

1. At least one of these commands should print 
a Python version of 3.6 or higher 
(whichever version you just downloaded)

If you are having problems:

Search the internet for "**Add python to path on Windows *10 / Vista / XP / etc***"
to find instructions for your version of Windows.
