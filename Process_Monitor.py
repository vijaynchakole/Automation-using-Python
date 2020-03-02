# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 05:04:33 2020

@author: hp
"""

import psutil

def ProcessDisplay():
    list_process = list()
        
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name', 'username'])
            list_process.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
       
    return list_process

def main():
    
    process_info = list()
    
    process_info = ProcessDisplay()
    
    for element in process_info:
        print(element)
        


if __name__ == "__main__":
    main()