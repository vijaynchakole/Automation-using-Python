# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 02:42:23 2020

@author: hp
"""

from google_images_download import google_images_download  # importing the libraries

response = google_images_download.googleimagesdownload() # class instantiation

arguments = {"keywords": "Python", "limit" : 200, "print_url" : True,
             "--chromedriver"  : "C:/Users/hp/Desktop/chromedriver.exe"}


paths = response.download(arguments)

print(paths)





#*********************************************************************

# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
response = google_images_download.googleimagesdownload() 


search_queries = [ 
	
'The smartphone also features an in display fingerprint sensor.', 
'The pop up selfie camera is placed aligning with the rear cameras.', 
'''In terms of storage Vivo V15 Pro could offer 
up to 6GB of RAM and 128GB of onboard storage.''', 
'The smartphone could be fuelled by a 3 700mAh battery.', 
] 


def downloadimages(query): 
	# keywords is the search query 
	# format is the image file format 
	# limit is the number of images to be downloaded 
	# print urs is to print the image file url 
	# size is the image size which can 
	# be specified manually ("large, medium, icon") 
	# aspect ratio denotes the height width ratio 
	# of images to download. ("tall, square, wide, panoramic") 
	arguments = {"keywords": "Python", 
				"format": "jpg", 
				"limit":400, 
				"print_urls":True, 
				"size": "medium", 
				"aspect_ratio" : "panoramic"} 
	try: 
		response.download(arguments) 
	
	# Handling File NotFound Error	 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "jpg", 
					"limit":600, 
					"print_urls":True, 
					"size": "medium"} 
					
		# Providing arguments for the searched query 
		try: 
			# Downloading the photos based 
			# on the given arguments 
			response.download(arguments) 
		except: 
			pass

# Driver Code 
for query in search_queries: 
	downloadimages(query) 
	print() 
