import os
import os.path
import sys
import time
import PIL.Image

setup_string_33 = "33***bc185.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0"
setup_string_36 = "36***bc185.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]a00_b00_c00_d00_w00_x00_y00_z00_ua1.0.0.0_ub_u0_v0_uc7.0.30_ud7.0"
setup_string_40 = "40***bc185.500.0.0.1*0*0*0*0*0*0*0*0#/]a00_b00_c00_d00_w00_x00_y00_z00_ua1.0.0.0.100_uf0.3.0.0_ue_ub_u0_v0_uc7.2.24_ud7.8"


#create error if not exist (not on windows)
if not getattr(__builtins__, "WindowsError", None):
    class WindowsError(OSError): pass

#open image file that kkl has made, waiting until it exists and can be opened properly
def open_image_file(filename):
	retry_time_limit = 10 #try for at most 10 seconds before saying there's a problem
	retry_interval = 0.2 #re-check for the existance of the image every 200 milliseconds
	retry_limit = retry_time_limit / retry_interval #try 50 times
	retry = 0 #number of times we've retried
	while True:
		try:
			image_file = PIL.Image.open(filename)
			return image_file
			
		except IOError:
			retry += 1
			if retry >= retry_limit:
				#opening the image file failed, abort the process
				raise
				
			time.sleep(retry_interval) #wait for the file to be available

#wait for the text file to be deleted before trying to open the image
def wait_for_file_deletion(filename):
	while os.path.isfile(filename):
		time.sleep(0.2)

#delete a file without caring if it exists
def delete_file(filename):
	try:
		os.remove(filename)
	except (WindowsError, OSError):
		pass

#check if the string starts with a kisekae version string (a number, followed by at least two *'s)
def starts_with_version_string(s):
	#check for numbers
	i = 0
	found_digit = False
	while i < len(s):
		if s[i].isdigit():
			found_digit = True #found at least one digit
		elif not found_digit:
			return False #not a digit, and we haven't found a digit yet, so it's not a version string
		else:
			break #this isn't a digit, but we found one previously, so proceed to the next stage of the check
		i += 1
	#we need at least 2 characters left in the string for there to be two *'s left
	if len(s) - i < 2:
		return False
	#check for the two *'s
	return s[i] == '*' and s[i+1] == '*'

#get the version string appropriate for the version of image codes used
def get_setup_string(image_list):
	if len(image_list) <= 0:
		return setup_string_33 #use default string
		
	first_code = image_list[0][1] #get the first image value in the list [0], then the second part of the value (the image description string) [1]
	
	if first_code.startswith("33"):
		return setup_string_33
	elif first_code.startswith("36"):
		return setup_string_36
	elif first_code.startswith("40"):
		return setup_string_40
		
	return setup_string_33 #default setup string
	
	
#use the image data to create the images using kkl, and move them to the specified directory
def create_images(image_list, output_directory):
	if sys.platform == 'darwin':
		kkl_dir = os.path.join( os.path.expanduser("~") , "Library", "Application Support" , "kkl" , "Local Store" )
	else :
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
	
	crop_pixels = (0, 0, 600, 1400)
	
	#setup the scene before drawing the requested pictures
	#this sets the character position, zoom level, distables interactivity, sets the zoom level and screen position, and removes censor icon
	#get a setup string, based on the version of the image descriptions being used
	setup_scene = get_setup_string(image_list)
	setup_filename = os.path.join(kkl_dir ,"scene_setup_file.txt")
	delete_file(os.path.join(kkl_dir , "scene_setup_file..png"))
	with open(setup_filename, "w") as f:
		f.write(setup_scene)
	wait_for_file_deletion(setup_filename)
	
	for image_filename, image_data in image_list:
		kkl_basename = os.path.join(kkl_dir , image_filename)
		data_filename = kkl_basename + ".txt"
		image_kkl_filename = kkl_basename +"..png"
		
		#user can set their own crop values, for easier centering of images
		#should have a format of:
		#crop_pixels=0, 0, 600, 1400
		#or
		#crop_pixels=0,0
		#to have the other sizes set to automatically produce a 600x1400 pixel image
		#note that these values can go off the side of the screen - the offscreen area will be transparent
		if image_filename == "crop_pixels":
			parts = image_data.split(",")
			new_pixels = [int(part.strip()) for part in parts]
			if len(parts) < 3:
				new_pixels.append(new_pixels[0]+600)
			if len(parts) < 4:
				new_pixels.append(new_pixels[1]+1400)
			crop_pixels = tuple(new_pixels)
			#print "new crop pixels:",crop_pixels
			continue
		
		#ensure that the correct version string is used
		if not starts_with_version_string(image_data):
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
		cropped_image = image.crop( crop_pixels ) #crop to the size used by the game
		cropped_image.save(os.path.join(output_directory , image_filename + ".png")) #save to output directory
		image.close()
		cropped_image.close()

#read image data in from 
def read_image_data(filename):
	image_data_list = list()
	with open(filename, "r") as f:
		for line_number, line in enumerate(f):
		
			line = line.strip()
			if len(line) <= 0 or line[0] == '#':
				continue
			
			try:
				image_filename, image_data = line.split("=", 1)
			except ValueError:
				print "Error - unable to split line number %d: \"%s\"" % (line_number, line)
				continue
			image_filename = image_filename.strip()
			image_data = image_data.strip()
			
			image_data_list.append((image_filename, image_data))
			
	return image_data_list
	
def make_images(image_data_file, output_directory):
	image_data_list = read_image_data(image_data_file)
	create_images(image_data_list, output_directory)

#python make_images.xml <character_image_file.txt> <output_directory>
if __name__ == "__main__":
	output_directory = "."
	if len(sys.argv) > 2:
		output_directory = sys.argv[2]
	make_images(sys.argv[1], output_directory)
