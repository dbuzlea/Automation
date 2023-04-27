# Automation

Consists of various automation examples (for learning puposes) and projects (UI testing) utilizing 
Selenium and PyAutoGUI frameworks for MacOS devices. 

Each test case or suite can be ran individually from Terminal, or you can run all test suites from the console_test_suites.py file.
Feel free to explore or submit any ideas via pull request! 

All programs were developed on an M1 13" MacBook Pro (2560 × 1600). If the tests don't navigate correctly to the right areas on your machine, create a new branch from the main and name it after your machine model with the proper display coordinates.

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/64452847/221402853-3140e0b8-96d1-4383-bb3d-e1f48a302114.gif)


# Requirements:

* Must be running macOS 13.0 or later 
* Because the UI testing relies on PyAutoGUI display coordinates to navigate, your System Settings window must be placed in the upper-left most corner of your screen in order for the tests to work (see image below).

<img width="1440" alt="Screenshot 2023-02-26 at 3 01 59 AM" src="https://user-images.githubusercontent.com/64452847/221402098-84bdbffb-a93a-4e48-858e-a8c4e085a20e.png">

# Steps to set up environment:

- cd to $PATH where you cloned this repo.
```
cd $PATH/Automation
```
- Run install shell to install all the dependencies for this repo.
```
bash install.sh
```
- Once complete, you can start running all files from Terminal!


# /Examples
Consist of mostly experimental files that utilizes both selenium and pyautogui.

### Steps to run a file inside Terminal for beginners:

- cd to /Examples/
```
cd Examples
```
- To run a file inside /Examples folder (replace the <file_name> with the name of the file):
```
python3 <file_name>.py
```


# /UI Testing:

## Run Test Case:
### Steps to run a test case inside Terminal for beginners:

- Go to System Settings directory:
```
cd UI\ Testing/System\ Settings/
```
- Run python interpretor:
```
python3
``` 
- import the file where the test case you wish to run resides by entering 'from <directory>.<file_name> import <Class Name> as i' (example below):
```
from General.generalTestSuite import General as i
```
- run your test case by entering 'i.<name_of_test_case()>'.
```
i.test_open_about_general_settings()
```
- To quit the python interpreter:
```
quit()
```

## Run Test Suite:
### Steps to run a test suite inside Terminal for beginners:

- Go to System Settings:
```
cd UI\ Testing/System\ Settings/
```
- Run python interpretor:
```
python3
``` 
- import the file where the test suite you wish to run resides by entering 'from <directory>.<file_name> import <Class Name> as i'.
```
from General.generalTestSuite import General as i
```
- run your test suite by entering 'i.<name_of_test_suite()>'.
```
i.generalTestSuite()
```
- To quit the python interpreter:
```
quit()
```

## Run whole Test suite:
### To run the whole test suite inside Terminal for beginners:

- Go to System Settings:
```
cd UI\ Testing/System\ Settings/
```
- Run the run_all_test_suites.sh file:
```
bash run_all_test_suites.sh
```
- To quit out of script press 'Control' and 'Q'.


# Contribute:
* If you would like to add onto this repo please fork the repo and submit a pull request. I welcome all contributions!
* To add a component to /System\ Settings/ dir please use the component_template.txt for continuity. 
 

If you encounter any issues while following the steps provided please submit via issue tab to let me know. Enjoy!

