# Automation

Consists of various automation examples (for learning puposes) and projects (UI testing) utilizing 
Selenium and PyAutoGUI frameworks for MacOS devices. 

Each test case or suite can be ran individually from Terminal, or you can run all test suites from the console_test_suites.py file.
Feel free to explore or submit any ideas via pull request! 

All programs were developed on a M1 13" MacBook Pro (2560 × 1600)


# /UI Testing:
### Steps to set up environment:

- cd to $PATH where you cloned this repo.
- Inside /System\ Settings/ run 'bash install.sh' in Terminal to install all the dependencies for this repo.
- Once complete, you can start running all files from Terminal!

## Run Test Case:
### Steps to run a test case inside Terminal for beginners:

- cd to /System\ Settings/
- run 'python3' to open the native python3 interpreter 
- import the file where the test case you wish to run resides by entering 'from <directory>.<file_name> import <Class Name> as i'.
- run your test case by entering 'i.<name_of_test_case()>'.
- To quit the python interpreter enter 'quit()'

## Run Test Suite:
### Steps to run a test suite inside Terminal for beginners:

- cd to /System\ Settings/
- run 'python3' to open the native python3 interpreter 
- import the file where the test suite you wish to run resides by entering 'from <directory>.<file_name> import <Class Name> as i'.
- run your test suite by entering 'i.<name_of_test_suite()>'.
- To quit the python interpreter enter 'quit()'

## Run whole Test suite:
### To run the whole test suite inside Terminal for beginners:

- cd to /System\ Settings/
- run 'bash run_all_test_suites.sh'

If you encounter any issues while folling the steps provided please let me know. Enjoy!

