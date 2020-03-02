# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 05:21:50 2020

@author: Vijay Narsing Chakole

"""
import psutil
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


def main():
    
    process_info = list()
    
    process_info = ProcessDisplay()
    
    for element in process_info:
        print(element)
        


if __name__ == "__main__":
    main()


