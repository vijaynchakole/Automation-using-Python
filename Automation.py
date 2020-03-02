# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:46:52 2020

@author: Vijay Narsing Chakole


Automation is consider as process which executes certain task without any human interaction. 
By using the automation technique we can automate multiple tasks as 
 •Moving , renaming or deleting files
 •Downloading multiple files 
 •Updating and searching in files
 •Sending and receiving mails
 •Schedule task through the process 
We can perform this kind of Automations by using Python.  
We are going to follow some rules while writing Automation Scripts as 
 •Accept input through command line or through file.
 •Display any message in log file instead of console. 
 •For separate task define separate function.
 •For robustness handle every expected exception. 
 •Perform validations before taking any action.
 •Create user defined modules to store the functionality. 
 
 
Consider below template of Automation Script

"""

from os import *
from sys import *

def fun(parameter):
    #Logic of script
    pass



def main():
    
    print("Application Name : "+ argv[0])
    
    if(len(argv)!= 2):
        print("Error : invalid number of arguments ")
        exit()
    
    if(argv[1] == '-h'):
        print("Script is designed for ")
        exit()
    
    if (argv[1] == '-u'):
        print("Usage : Application Name ")
        exit()
        
        
    try:
        fun(argv[1])        
    except Exception as E:
        print("ERROR : Invalid Input :"+E)
        
    if (len(argv)<2) or (len(argv)>3):
        print("ERROR : Invalid number of arguments ")
        

if __name__ == "__main__":
    main()
    