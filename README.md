# Introduction to Python Programming Live Training

This is the code for the *O'Reilly Live Training* - **Introduction to Python Programming** presented by Arianne Dee

If you are looking for the code for the LiveLessons video, go here [https://github.com/ariannedee/intro-to-python-livelessons](https://github.com/ariannedee/intro-to-python-livelessons)

Before the class, please follow these instructions:
1. [Install Python](#1-install-python-36-or-higher)
2. [Install PyCharm](#2-download-pycharm-community-edition)
3. [Download the code](#3-download-the-course-files)
4. [Make sure that you can run Python in PyCharm](#4-make-sure-that-you-can-run-python-in-pycharm)

## Set up instructions
### 1. Install Python 3.6 or higher
Go to https://www.python.org/downloads/

Click the yellow button at the top to download the latest version of Python.

#### On Mac or Linux
Follow the prompts and install using the default settings.

#### On Windows
The default settings don't add Python to your PATH 
so your computer doesn't know where to look for it when Python runs 
(for some inexplicable reason).

##### If you're just installing Python now
Follow the instructions here: [Windows Python installer instructions](docs/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 2. Download PyCharm (Community Edition)
Download here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 3. Download the course files
If you're viewing this on GitHub already, stay on this page.
Otherwise, go to the GitHub repository: https://github.com/ariannedee/intro-to-python

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the green "↓ Code" button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **intro-to-python-master** folder to a convenient location

### 4. Make sure that you can run Python in PyCharm
1. Open PyCharm (skip any configuration/tip windows)
   
1. Navigate to the **intro-to-python-master** folder and click **Open**

1. You should now have PyCharm open with the folder structure in the left side panel
   
1. In the left panel, navigate to `Examples/example_1_first_code.py` and double click to open it in the editor

1. On the open file, right click and select **Run 'example_1_first_code'**

1. In the Run tab on the bottom, you should see
`Process finished with exit code 0`

1. Otherwise, if you got an error (exit code 1 in red), follow the instructions for setting your Python version in PyCharm below


### If you received an error running example_1_first_code, set your Python version in PyCharm

On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
- Go to **Project: intro-to-python** > **Project Interpreter**
- Look for your Python version in the Project Interpreter dropdown and select it. Please use Python 3.6 or higher.
- If you found it, click OK and try running `example_1_first_code` again
- Otherwise, if your version wasn't there, click **gear icon** > **Add...**
- In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
- If it's not there, click the **...** button and navigate to your Python location
- **Note:** For this last step, you may have to search the internet for where Python gets installed by default on your operating system

If you are having trouble configuring your Python version,
you can find visual instructions here: [Python interpreter setup](docs/PyCharm_interpreter.md)

## FAQs
### Can I use Python 2?

Yes, but I highly recommend using Python 3. If you are using Python 2, a few commands will be different. Refer to the last page of the PDF handout provided in the class resources.

### Can I use a different code editor besides PyCharm?

Yes, but it is only recommended if you are already know it and are comfortable navigating to different files and running commands in the command line. If it has syntax highlighting for Python, that is ideal.

### PyCharm can't find Python 3

Follow the instructions for [Python interpreter setup](docs/PyCharm_interpreter.md)
