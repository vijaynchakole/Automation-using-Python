# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:08:10 2020

@author: hp

ico format
The ICO file format is an image file format for computer icons in Microsoft Windows. 
ICO files contain one or more small images at multiple sizes and color depths, 
such that they may be scaled appropriately.

"""

import os
import requests
from sys import *
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url, allow_redirects = True)
    
    header = h.headers
    
    content_type = header.get('content-type')
    
    
    
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    
    return True
    
###############################################################################
    
def get_filename_from_cd(cd):
    
    a = urlparse(cd)
    
    return os.path.basename(a.path)


###############################################################################


def Download(url):
    allowed = is_downloadable(url)
    
    if allowed :
        try:
            res = requests.get(url, allow_redirects = True)
            
            filename = get_filename_from_cd(url)
            fd = open(filename, "wb")
            
            for buffer in res.iter_content(1024):
                fd.write(buffer)
                
            fd.close()
            return True
        
        except Exception as E :
            return False
    
    else:
        return False
    
    
###############################################################################

def main():
    print("inside main")
    
    url = "https://www.google.com/favicon.ico"
   
    result = Download(url)
    
    if result :
        print("file successfully download")
    else:
        print("Failed to download")


if __name__ == "__main__":
    main()