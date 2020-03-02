# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 05:39:40 2020

@author: Vijay Narsing Chakole

"""

import psutil
from sys import *
import os

# set current working directory
os.chdir("C:/Users/hp/PycharmProjects")
#os.chdir("C:/Users/hp/Desktop")


def ProcessDisplay():
    
    process_list = list()
    
    
    for proc in psutil.process_iter():
        #type(proc)
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024*1024)
            process_list.append(pinfo)
         #   type(pinfo)
        
        except (psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return process_list



def LogWriter(path, process_list):
    #path = "college"
    flag = os.path.isabs(path)
    
    if flag == False:
        path =os.path.abspath(path)
    
    exists = os.path.isdir(path)
    
    if exists:
        log_file = "log_file.txt"
        
        log_file = os.path.join(path, log_file)
        
        fd = open(log_file, 'a', encoding = 'utf-8')
        
        for element in process_list:        
            fd.write(str(element))
            fd.write("\n")
       
        print("Successfully written into log file")
        
        fd.close()
    else:
        print("invalid path")
    

def main():
    
    process_info = list()
    
    process_info = ProcessDisplay()
    
    LogWriter(argv[1], process_info)
    
   # for element in process_info:
    #    print(element)
        
    print("main End")


if __name__ == "__main__":
    main()


