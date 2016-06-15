import os
import os.path
import sys
import time
import PIL.Image

#open image file that kkl has made, waiting until it exists and can be opened properly
def open_image_file(filename):
	retry_limit = 50 #try 50 times / 10 seconds
	retry = 0
	while True:
		try:
			image_file = PIL.Image.open(filename)
			return image_file
			
		except IOError:
			retry += 1
			if retry >= retry_limit:
				#opening the image file failed, abort the process
				raise
				
			time.sleep(0.2) #wait for the file to be available

#wait for the text file to be deleted before trying to open the image
def wait_for_file_deletion(filename):
	while os.path.isfile(filename):
		time.sleep(0.2)

#delete a file without caring if it exists
def delete_file(filename):
	try:
		os.remove(filename)
	except WindowsError:
		pass
		
#use the image data to create the images using kkl, and move them to the specified directory
def create_images(image_list, output_directory):
	kkl_dir = os.getenv('APPDATA') + "\\kkl\\Local Store"
	
	separator = "#/]"
	
	#kk version strings
	single_version = "33**"
	scene_version = single_version + "*"
	
	#the *0*0*0*0*0*0*0*0 removes any extra characters from the previous scene
	#there are 9 possible characters, so 8 *'s are needed to remove any extras
	#char_removal = "*0*0*0*0*0*0*0*0"
	
	#this scene description removes the foreground crowd, removes the censorship icon, and sets appropriate zoom & screen position settings
	scene_str = separator+"ua1.0.31.32_ub_uc8.0.30_ud7.3"
	
	#setup the scene before drawing the requested pictures
	#this sets the character position, zoom level, distables interactivity, sets the zoom level and screen position, and removes censor icon
	setup_scene = "33***bc185.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0"
	setup_filename = kkl_dir +"\\scene_setup_file.txt"
	delete_file(kkl_dir +"\\scene_setup_file..png")
	with open(setup_filename, "w") as f:
		f.write(setup_scene)
	wait_for_file_deletion(setup_filename)
	
	for image_filename, image_data in image_list:
		kkl_basename = kkl_dir + "\\" + image_filename
		data_filename = kkl_basename + ".txt"
		image_kkl_filename = kkl_basename +"..png"
		
		
		#ensure that the correct version string is used
		if not image_data.startswith(single_version):
			#assume that no version data is available
			image_data = single_version + image_data
		
		write_data = image_data
		
		#print write_data,"\n\n"
		
		#the conversion doesn't always work properly if the image file already exists
		delete_file(image_kkl_filename)
		
		#write the image data where kkl can find it
		with open(data_filename, "w") as data_file:
			data_file.write(write_data)
		
		wait_for_file_deletion(data_filename)
		
		#open the image file produced, waiting until kkl has finished making it
		#there are two .'s in the output filename, I don't know why.
		image = open_image_file(image_kkl_filename)
		
		#crop the image, and save it to the specified output directory
		cropped_image = image.crop( (0, 0, 600, 1400) ) #crop to the size used by the game
		cropped_image.save(output_directory + "\\" + image_filename + ".png") #save to output directory
		image.close()
		cropped_image.close()

#read image data in from 
def read_image_data(filename):
	image_data_list = list()
	with open(filename, "r") as f:
		for line in f:
		
			line = line.strip()
			if len(line) <= 0 or line[0] == '#':
				continue
				
			image_filename, image_data = line.split("=", 1)
			image_filename = image_filename.strip()
			image_data = image_data.strip()
			
			image_data_list.append((image_filename, image_data))
			
	return image_data_list
	
def make_images(image_data_file, output_directory):
	image_data_list = read_image_data(image_data_file)
	create_images(image_data_list, output_directory)
	
if __name__ == "__main__":
	make_images(sys.argv[1], sys.argv[2])
