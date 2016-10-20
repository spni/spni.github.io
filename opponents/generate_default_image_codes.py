import sys

ap="ap" #appearance
im="im" #image
st="st" #stage
em="em" #emotion

#the entire label fits a single category
appearance_labels = {"ca", "db", "dh", "di", "qb", "eh", "ea", "ec", "ed", "ef", "eg", "fh", "fe", "ff", "fg", "pb", "pc", "pd", "ga", "gb", }
image_labels = {"aa", "bb", "bd", "be", "cb", "fb", "ge", "gh", "gf", "gg", "gd", "ha", "hb", "hd", }
stage_labels = {"ab", "ac", "ia", "if", "ib", "ib", "ic", "jc", "id", "ie", "ja", "jb", "jd", "je", "jf", "jg", "ka", "kb", "kc", "kd", "ke", "kf", "la", "lb", "oa", "os", "ob", "oc", "od", "oe", "of", "lc", "og", "oh", "oo", "op", "oq", "or", "om", "on", "ok", "ol", "oi", "oj", }
emotion_labels = {"gc", }

#the contents of a label go into multiple categories
mixed_labels = {"bc":(im,im,im,im,ap),
"da":(ap,im,im,im),
"dd":(em,ap,ap,ap,ap),
"qa":(ap,ap,ap,ap,ap,ap,ap,ap,em,ap,ap,ap),
"dc":(st,ap,ap,ap,ap),
"fa":(im,ap,ap,ap,ap,im,ap),
"fc":(im,ap,ap,im,ap,ap,im,ap,ap,im,im,im),
"fd":(ap,ap,im,ap,ap),
"pa":(ap,ap,ap,ap,ap,im,ap,ap,ap,ap),
"pe":(ap,ap,ap,ap,ap,im,ap),
"hc":(ap,im,im,ap,im,im),

}

#add numbered labels
for ind in range(0,9 + 1):
	appearance_labels.add("r%d" % ind)
	image_labels.add("t%d" % ind)
	stage_labels.add("m%d" % ind) #ribbons
	stage_labels.add("n%d" % ind)
	stage_labels.add("s%d" % ind) #belts
	

labels = {ap:appearance_labels, im:image_labels, st:stage_labels, em:emotion_labels}
	
character_separator = "**"
scene_separator = "***"
multi_char_separator = "*"
data_separator = "#/]"

appearance_tag = "appearance" #general appearance of the character
image_tag = "image_name" #image/emotion filename
image_description_tag = "image_desc" #emotion/image name description
image_emotion_tag = "image_emotion" #modifier for emotion level from image name
emotion_tag = "emotion" #descripotion of emotion/blush level/blue face values
stage_tag = "stage" #stage description. mostly clothes, but also has emotion and love juice values
stage_modification = "stage_emotion" #base emotion level for a stage
love_juice_tag = "stage_lj" #love juice level for a tag

#get the starting letters of a string (stop when seeing a digit or non-alphabetic character)
def get_letter_part(s):
	output = ""
	for c in s:
		if c.isalpha():
			output += c
		else:
			break
	return output

#the description is actually just the first two characters
def get_description_label(s):
	return s[:2]

#break a description line into its components
def get_desc_parts(description_line):
	parts = description_line.split("_")
	output = list()
	for part in parts:
		label, component_str = part[:2], part[2:]
		
		if label == "ga":
			#make sure that automatic/manual emotions is set to "manual"
			output.append((label, "0"))
		else:
			output.append((label, component_str.split(".")))
	return output
	
#get just the description part of the line, not any other parts
def get_description(line):
	#get to just the description part
	parts = None
	if scene_separator in line:
		parts = line.split(scene_separator)
		line = parts[1]
	if character_separator in line:
		parts = line.split(character_separator)
		line = parts[1]
	if multi_char_separator in line:
		parts = line.split(multi_char_separator, 1)
		line = parts[0]
	if data_separator in line:
		parts = line.split(data_separator, 1)
		line = parts[0]
	
	return line

#take the given line and return a dictionary containing the descriptions specified in the whole_ and part_labels
def read_description_string(description_type, line):
	desc_parts = get_desc_parts(get_description(line))
	desc = dict()
	
	whole_labels = labels[description_type]
	
	for label, values in desc_parts:
	
		#if it's a whole label, put the whole thing in
		if label in whole_labels:
			desc[label] = values
			
		#if it's a partial label, add the parts that are relevant to this description type
		elif label in mixed_labels:
			using = mixed_labels[label] #which type uses this part?
			#part_values = [x if (using[i] == description_type) else None for i, x in enumerate(values)]
			l = len(values)
			part_values = [None] * l
			for i in range(l):
				part_values[i] = values[i] if (using[i] == description_type) else None
			desc[label] = part_values
	
	return desc
	
#read a character's description file
def read_description_files(in_filename):
	appearance = dict() #single description part
	emotions = list() #list of description parts
	stages = list() #list of description parts
	images = list() #list of different image names
	
	image = None #current image name (mostly pose/emotion)
	stage = None #current stange (mostly clothing)
	
	with open(in_filename, "r") as f:
		for linenumber, line in enumerate(f):
			line = line.strip()
			if (len(line) <= 0) or (line[0] == '#'):
				#comment or blank line, skip it
				continue
			
			if "=" not in line:
				print "Error - no = in line %d: %s" % (linenumber, line)
				
			key, value = line.split("=")
			
			key = key.strip()
			value = value.strip()
			#desc = description #shorter name
			
			#skip empty lines
			if len(value) <= 0:
				continue
			
			#character's general appearance
			if key == appearance_tag:
				appearance = read_description_string(ap, value)
			
			#emotion stage
			elif key == emotion_tag:
				#dict()emotion, 
				emotion = read_description_string(em, value)
				emotions.append(emotion)
				
			#marks a new stage, and gives the clothing, etc, for a stage
			elif key == stage_tag:
				stage = [None, 0, 0] #[dictionary of description parts, base emotion level, love juice level]dict()
				stage[0] = read_description_string(st, value)
				stages.append(stage)
			
			#stage's base emotion level
			elif key == stage_modification:
				if stage is None:
					print "Error - trying to give a stage an emotion level before giving a stage on line %d: %s" % (linenumber, line)
					continue
				stage[1] = int(value)
				
			#stage's love juice level
			elif key == love_juice_tag:
				if stage is None:
					print "Error - trying to give a stage an love juice level before giving a stage on line %d: %s" % (linenumber, line)
					continue
				stage[2] = int(value)
			
			#image filename
			elif key == image_tag:
				image = [None, 0, ""] #[description parts, emotion level modifier, image_name]dict()
				image[2] = value
				images.append(image)
			
			#description for an image's appearance/pose
			elif key == image_description_tag:
				if image is None:
					print "Error - trying to give an image description before giving a image on line %d: %s" % (linenumber, line)
					continue
				image[0] = read_description_string(im, value)
			
			#an image's emotion modifier
			elif key == image_emotion_tag:
				if image is None:
					print "Error - trying to give an image an emotion modifier before giving a image on line %d: %s" % (linenumber, line)
					continue
				image[1] = int(value)
				
			else:
				print "Error - unknown key \"%s\" on line %d: %s" % (key, linenumber, line)
				
	return (appearance, emotions, stages, images)

#take a (complete) description variable and turn them into a description string
#(but no version header)
def desc_to_string(description):
	s = "" #the string to be built, then returned
	for key, values in description.items():
		if len(s) > 0:
			s += "_" #underscore between different labels
		s += "%s%s" % (key, values[0]) #no period between label and first value
		for value in values[1:]:
			s += ".%s" % value #additional values are separation with periods
			
	return s
	
#take a partially completed description and add components from a description dictionary
def combine_descriptions(partial_desc, desc_dict):
	desc = partial_desc
	for key, values in desc_dict.items():
	
		#if the key is already present, it has a partial description so fill in missing parts
		if key in desc:
			partial_values = desc[key]
			for ind, value in enumerate(values):
				if value is not None:
					partial_values[ind] = value
					
		#if the key isn't present, just use (a copy of) it's entire list
		else:
			desc[key] = list(values)
	
#take the four sets of descriptions and return a completed description string
def complete_description(apr, stg, img, emo):
	desc_parts = dict()
	
	#just copy the initial description
	for label, parts in apr.items():
		desc_parts[label] = list(parts)
		
	#combine the parts from the other description categories
	for desc_dict in (stg, img, emo):
		combine_descriptions(desc_parts, desc_dict)
	
	version_string = "40**"
	
	return version_string + desc_to_string(desc_parts)
	
#get appropriate emotion level, capping at emotion level zero or the last emotion in the list
def get_emotion_description(emotions, emotion_level):
	if emotion_level < 0:
		emotion_level = 0
	if emotion_level >= len(emotions):
		emotion_level = len(emotions) - 1
	return emotions[emotion_level]

#take a set of image description dictionaries and write their contents out to a given image list file
def write_image_list(descriptions, image_list_filename):
	appearance, emotions, stages, images = descriptions
	with open(image_list_filename, "w") as f:
		for stage_number, stage in enumerate(stages):
			stage_desc, emotion, lj = stage
			
			for image in images:
				image_desc, emotion_mod, image_name = image
				
				emotion_desc = get_emotion_description(emotions, emotion + emotion_mod)
				
				description = complete_description(appearance, stage_desc, image_desc, emotion_desc)
				
				image_filename = "%d-%s" % (stage_number, image_name)
				
				f.write("%s=%s\n" % (image_filename, description))
				
			f.write("\n")

#take a set of descriptions and generate a list of image descriptions to be sent to kisekae
if __name__ == "__main__":
	l = len(sys.argv)
	image_description_filename = ""
	if l > 1:
		image_description_filename = sys.argv[1]
	image_list_filename = "default_images.txt"
	if l > 2:
		image_list_filename = sys.argv[2]
		
	descriptions = read_description_files(image_description_filename)
	
	write_image_list(descriptions, image_list_filename)