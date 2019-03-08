# Website-Blocker
A simple python code written to block any website from opening during the given time period.

# How_To_Use_It
  Manually:-
  
    Open the Command Prompt as Administrator and run the web_blocker.py with any Python-3 Compiler
    
  Automatically:-
    
    If you want to run it automatically then follow the given steps :-
    
     a)Save the same python file as .pyw extension
     b)Open Task Scheduler and perform following steps:-
        *Create New Task
        *Define the name
        *Go on New Trigger option and change "Begin the Task" menu as "At StartUp"
        *Then Go to Action,create New and browse the location of your python file with .pyw extension in "Program/Script" section
        *Then Go to Condition menu and clear all the conditions if checked by default
        *Click on OK button
        *Then Enable your task
        
Just modify Line #4 to modify the name of website and Line #11 to change the timing of blocking in the web_blocker.py file 

Make sure you have cleared and blocked the cookies of the given website to work properly
