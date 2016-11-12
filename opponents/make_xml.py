import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

#get a single value from the dictionary
def get_value(dictionary, key, stage, default=""):
	full_key = "%d-%s" % (stage, key)
	if full_key in dictionary:
		return dictionary[full_key]
	if key in dictionary:
		return dictionary[key]
	return default

#tags that relate to ending sequences
ending_tag = "ending" #name for the ending
ending_gender_tag = "ending_gender" #player gender the ending is shown to
screen_tag = "screen"
text_tag = "text"
x_tag = "x"
y_tag = "y"
width_tag = "width"
arrow_tag = "arrow"
ending_tags = [ending_tag, ending_gender_tag, screen_tag, text_tag, x_tag, y_tag, width_tag, arrow_tag]
	
#default images and text for most cases
def get_cases_dictionary():
	d = {}#male pre-strip scenes
	d["male_human_must_strip"] = [("interested", "What are you going to take off, ~name~?")]
	d["male_must_strip"] = [("interested", "What are you going to take off, ~name~?")]
	d["male_removing_accessory"] = [("sad", "You're only taking off your ~clothing~, ~name~? That doesn't seem fair.")]
	d["male_removing_minor"] = [("calm", "I guess you're ~clothing~ is something, at least.")]
	d["male_removing_major"] = [("interested", "Finally getting ~name~ out of their ~clothing~!")]
	d["male_chest_will_be_visible"] = [("interested", "I guess it's time to see that chest of yours, ~name~!")]
	d["male_crotch_will_be_visible"] = [("horny", "I guess you have to show 'that' to me now, ~name~...")]
	
	#male stripping
	d["male_removed_accessory"] = [("calm", "At least you have less small stuff to take off now.")]
	d["male_removed_minor"] = [("happy", "Maybe we can get you out of some large stuff now, ~name~.")]
	d["male_removed_major"] = [("interested", "You look better without your ~clothing~, ~name~.")]
	d["male_chest_is_visible"] = [("interested", "Nice chest, ~name~.")]
	d["male_small_crotch_is_visible"] = [("calm", "That's... smaller than I was expecting... not that anything is wrong with that, ~name~.")]
	d["male_medium_crotch_is_visible"] = [("awkward", "Well then... shall we continue the game?")]
	d["male_large_crotch_is_visible"] = [("shocked", "That is massive! How do you even manage with that thing, ~name~?")]
	
	#male masturbating
	d["male_must_masturbate"] = [("interested", "Time to show your skills, ~name~...")]
	d["male_start_masturbating"] = [("horny", "You're going to have to go until you're done, ~name~...")]
	d["male_masturbating"] = [("horny", "Keep going, ~name~...")]
	d["male_finished_masturbating"] = [("shocked", "Wow... uh... I guess you're done then...")]
	
	#female pre-strip
	d["female_human_must_strip"] = [("interested", "What are you going to take off, ~name~?")]
	d["female_must_strip"] = [("interested", "What are you going to take off, ~name~?")]
	d["female_removing_accessory"] = [("sad", "You're only taking off your ~clothing~, ~name~? That doesn't seem fair.")]
	d["female_removing_minor"] = [("calm", "I guess you're ~clothing~ is something, at least.")]
	d["female_removing_major"] = [("interested", "Finally getting ~name~ out of their ~clothing~!")]
	d["female_chest_will_be_visible"] = [("interested", "I guess it's time to see those tits of yours, ~name~!")]
	d["female_crotch_will_be_visible"] = [("horny", "I guess you have to show 'that' to me now, ~name~...")]
	
	#female stripping
	d["female_removed_accessory"] = [("calm", "At least you have less small stuff to take off now.")]
	d["female_removed_minor"] = [("happy", "Maybe we can get you out of some large stuff now, ~name~.")]
	d["female_removed_major"] = [("interested", "You look better without your ~clothing~, ~name~.")]
	d["female_small_chest_is_visible"] = [("interested", "Those are nice, ~name~.")]
	d["female_medium_chest_is_visible"] = [("horny", "Nice tits, ~name~.")]
	d["female_large_chest_is_visible"] = [("shocked", "How do you even manage with those things, ~name~. Is your back okay?")]
	d["female_crotch_is_visible"] = [("shocked", "It's so pretty, ~name~...")]
	
	#female masturbating
	d["female_must_masturbate"] = [("interested", "Time to show your skills, ~name~...")]
	d["female_start_masturbating"] = [("horny", "You're going to have to go until you're done, ~name~...")]
	d["female_masturbating"] = [("horny", "Keep going, ~name~...")]
	d["female_finished_masturbating"] = [("shocked", "Wow... uh... I guess you're done then...")]
	
	#victory
	d["game_over_victory"] = [("happy", "I WON!")]
	
	return d

#get the cases for when the character is still in the game (all clothed stages, and nude)
def get_playing_cases_dictionary():
	d = {}
	#quality of hand
	d["swap_cards"] = [("calm", "I'll exchange ~cards~ cards.")]
	d["good_hand"] = [("happy", "I've got a good hand.")]
	d["okay_hand"] = [("calm", "I've got an okay hand.")]
	d["bad_hand"] = [("sad", "I've got a bad hand.")]
	
	return d

#cases where the player can strip (all stages until nude)
def get_stripping_cases_dictionary():
	d = {}
	
	#stripping
	d["stripped"] = [("sad", "I miss my ~clothing~ already...")]
	d["must_strip_winning"] = [("loss", "Well, I guess it had to be my turn eventually...")]
	d["must_strip_normal"] = [("loss", "I guess I lost, huh?")]
	d["must_strip_losing"] = [("loss", "I lost again? But... I have less clothes than everyone else!")]
	d["stripping"] = [("strip", "I guess I'll just take off my ~clothing~...")]
	return d
	
#default images and text for being nude
def get_nude_cases_dictionary():
	d = {}
	d["stripped"] = [("sad", "I miss my ~clothing~ already...")] #there's still a stripped case when they're nude
	d["must_masturbate"] = [("loss", "I guess I lost...")]
	d["must_masturbate_first"] = [("loss", "Y-You want me to do what?!")]
	d["start_masturbating"] = [("starting", "I guess I have to do 'that' now, huh?")]
	
	return d

#default images and text for masturbating
def get_masturbating_cases_dictionary():
	d = {}
	d["masturbating"] = [("calm", "How long do I have to keep going for?")]
	d["heavy_masturbating"] = [("heavy", "Mmmmmmmm....")]
	d["finishing_masturbating"] = [("finishing", "I'm cumming!")]
	return d

#default images and text for being finished
def get_finished_Cases_dictionary():
	d = {}
	d["finished_masturbating"] = [("finished", "I'm done...")]
	d["game_over_defeat"] = [("calm", "Congrats, ~name~... I can't believe I lost...")]
	return d

#get a set of cases from the dictionaries. First try stage-specific from the character's data, then general entries from the character's data, then stage-specific from the default data, then general cases from the default data.
def get_cases(player_dictionary, default_dictionary, key, stage):
	out_list = []
	full_key = "%d-%s" % (stage, key)
	
	using_player = False
	
	#check character's data
	if full_key in player_dictionary:
		result_list = player_dictionary[full_key]
		using_player = True
		
	elif key in player_dictionary:
		result_list = player_dictionary[key]
		using_player = True
	
	backup_list = None
	
	#use the default data
	if full_key in default_dictionary:
		backup_list = default_dictionary[full_key]
		if not using_player:
			result_list = backup_list
		
	elif key in default_dictionary:
		backup_list = default_dictionary[key]
		if not using_player:
			result_list = backup_list
	
	#convert image formats
	for i, (image, text) in enumerate(result_list):
		if len(image) <= 0:
			#if the character entry doesn't include an image, use default image
			image = backup_list[i % len(backup_list)][0] #use i'th image in default dictionary, if possible. wrap around if backup list isn't long enough
		
		#if the image name doesn't include a stage, prepend the current stage
		if not image[0].isdigit():
			image = "%d-%s" % (stage, image)
		out_list.append( (image+".png", text) )
	
	return out_list

#add a single emenent (used so I can add a tag named "tag")
def add_subelement(base_element, name, tag_value):
	subelement = ET.SubElement(base_element, name, {"tag":tag_value})
	return subelement

#add several values to the XML tree
def add_values(base_element, player_dictionary, default_dictionary, stage):
	if type(default_dictionary) != list:
		default_dictionary = [default_dictionary]
	for d in default_dictionary:
		for key in d.keys():
			contents = get_cases(player_dictionary, d, key, stage)
			case = add_subelement(base_element, "case", key)
			for img, text in contents:
				ET.SubElement(case, "state", img=img).text = text

#manually prettify xml code (because the standard method doesn't seem to work on windows)
def manual_prettify_xml(elem, level=0, isLast=False):
	indent = "    "
	if elem.text is None and len(elem) > 0:
		elem.text = "\n" + (level + 1) * indent
	if isLast:
		elem.tail = "\n" + (level - 1) * indent
	else:
		elem.tail = "\n" + (level) * indent
		
	if elem.tag in ["stage", "wardrobe", "timer", "start", "behaviour", "epilogue", "screen", "text"]:
		elem.tail = "\n" + elem.tail
		
	if elem.tag == "opponent":
		elem.text = "\n" + elem.text
	
	for ind, subelem in enumerate(elem):
		is_last = ind == len(elem) - 1
		manual_prettify_xml(subelem, level + 1, is_last)
	return elem
			
#write the xml file to the specified filename
def write_xml(data, filename):
	main_dict = get_cases_dictionary()
	plyr_dict = get_playing_cases_dictionary()
	strp_dict = get_stripping_cases_dictionary()
	nude_dict = get_nude_cases_dictionary()
	mstb_dict = get_masturbating_cases_dictionary()
	fnsh_dict = get_finished_Cases_dictionary()
	

	#f = open(filename)
	o = ET.Element("opponent")
	ET.SubElement(o, "first").text = data["first"]
	ET.SubElement(o, "last").text = data["last"]
	ET.SubElement(o, "label").text = data["label"]
	ET.SubElement(o, "gender").text = data["gender"]
	ET.SubElement(o, "size").text = data["size"]
	ET.SubElement(o, "timer").text = data["timer"]
	
	#start image
	start = ET.SubElement(o, "start")
	start_data = get_value(data, "start", stage=0, default="0-calm,So we'll be playing strip poker... I hope we have fun.")
	start_image, start_text = start_data.split(",", 1)
	ET.SubElement(start, "state", img=start_image+".png").text = start_text
	
	#wardrobe
	clth = ET.SubElement(o, "wardrobe")
	clothes = data["clothes"]
	clothes_count = len(clothes)
	for i in range(clothes_count - 1, -1, -1):
		pname, lname, tp, pos = clothes[i].split(",")
		ET.SubElement(clth, "clothing", **{"proper-name":pname, "lowercase":lname, "type":tp, "position":pos})
	
	#behaviour
	bh = ET.SubElement(o, "behaviour")
	for stage in range(0, clothes_count):
		s = ET.SubElement(bh, "stage", id=str(stage))
		add_values(s, data, [main_dict, plyr_dict, strp_dict], stage)
	
	#nude stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, [main_dict, plyr_dict, nude_dict], stage)
	
	#masturbating stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, [main_dict, mstb_dict], stage)
			
	#finished stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, [main_dict, fnsh_dict], stage)
	
	#endings
	if "endings" in data:
		#for each ending
		for ending in data["endings"]:
			ending_xml = ET.SubElement(o, "epilogue", gender=ending["gender"])
			ET.SubElement(ending_xml, "title").text = ending["title"]
			
			#for each screen in an ending
			for screen in ending["screens"]:
				screen_xml = ET.SubElement(ending_xml, "screen", img=screen["image"])
				
				#for each text box on a screen
				for text_box in screen["text_boxes"]:
					text_box_xml = ET.SubElement(screen_xml, "text")
					ET.SubElement(text_box_xml, x_tag).text = text_box[x_tag]
					ET.SubElement(text_box_xml, y_tag).text = text_box[y_tag]
					#width and arrow are optional
					if width_tag in text_box:
						ET.SubElement(text_box_xml, width_tag).text = text_box[width_tag]
					if arrow_tag in text_box:
						ET.SubElement(text_box_xml, arrow_tag).text = text_box[arrow_tag]
					ET.SubElement(text_box_xml, "content").text = text_box[text_tag]
	
	#done
	
	
	
	#this outputs compact/non-pretty xml
	#tree = ET.ElementTree(o)
	#tree.write(filename, xml_declaration=True)
	
	#this is supposed to prettify
	#xml_prettystr = minidom.parseString(ET.tostring(o)).toprettyxml(indent="    ")
	#with open(filename, "w") as f:
	#	f.write(pretty_xml)
	
	#manual prettify
	pretty_xml = manual_prettify_xml(o)
	ET.ElementTree(pretty_xml).write(filename, xml_declaration=True)

#add an ending to the 
def add_ending(ending, d):
	ending = dict(ending)

	if len(ending.keys()) <= 0:
		#this is an empty ending, so don't add anything
		return
	
	#check for required values
	if "title" not in ending:
		print "Error - ending \"%s\" does not have a title." % (str(ending))
		return
		
	if "gender" not in ending:
		print "Error - ending \"%s\" does not have a gender specified." % (str(ending))
		return
		
	if "screens" not in ending:
		print "Error - ending \"%s\" does not have any screens." % (str(ending))
		return
	
	#either get the endings data from the dictionary, or make a new endings variable and add that to the dictionary
	endings = None
	if "endings" in d:
		endings = d["endings"]
	else:
		endings = list()
		d["endings"] = endings
		
	endings.append(ending)
	
#handle the ending data
def handle_ending_string(key, content, ending, d):
	if key == ending_tag:
		#this is a new ending, so store the previous ending (if any)
		add_ending(ending, d)
		#reset the ending data
		ending.clear()
		#and add the title of the new ending
		ending["title"] = content
		return
	elif key == ending_gender_tag:
		if len(content) <= 0: #if the gender wasn't specified, use "any"
			content = "any"
		ending["gender"] = content
		return
		
	#get the screens variable
	screens = None
	if "screens" in ending:
		screens = ending["screens"]
	else:
		#or make one, if it doesn't already exist
		screens = list()
		ending["screens"] = screens
		
	#get the current screen
	screen = None
	if len(screens) >= 1:
		screen = screens[-1]
	
	#background image for a screen - makes a new screen
	if key == screen_tag:
		screen = dict()
		screens.append(screen)
		screen["image"] = content
		screen["text_boxes"] = list()
		return
	
	#make sure we have a screen ready, because the other tags are specific to a screen
	if screen is None:
		print "Error - using tag \"%s\" with value \"%s\", without a screen varaible - use the \"%s\" tag first to put this information on that screen." % (key, content, screen_tag)
		return
	
	text_boxes = screen["text_boxes"]
	
	#the actual text of the text box. this makes a new text box
	if key == text_tag:
		text_box = dict()
		text_box[text_tag] = content
		text_boxes.append(text_box)
		return
		
	#get the current text box for the current screen
	text_box = None
	if len(text_boxes) >= 1:
		text_box = text_boxes[-1]
	else:
		print "Error - trying to use tag \"%s\" with value \"%s\", without making a text box. Use the \"%s\" tag first." % (key, content, text_tag)
		return
	
	#x position. Can be a css value, or "centered"
	if key == x_tag:
		text_box[x_tag] = content
		return
	
	#y position. Is a css value.
	elif key == y_tag:
		text_box[y_tag] = content
		return
	
	#width of a text box. defaults to 20%
	elif key == width_tag:
		text_box[width_tag] = content
		return
		
	#direction of the dialogue box arrow (if anything)
	elif key == arrow_tag:
		text_box[arrow_tag] = content
		return
		
	
#read in a character's data
def read_player_file(filename):
	main_dict = get_cases_dictionary()
	plyr_dict = get_playing_cases_dictionary()
	strp_dict = get_stripping_cases_dictionary()
	nude_dict = get_nude_cases_dictionary()
	mstb_dict = get_masturbating_cases_dictionary()
	fnsh_dict = get_finished_Cases_dictionary()
	
	case_names = main_dict.keys() + plyr_dict.keys() + strp_dict.keys() + nude_dict.keys() + mstb_dict.keys() + fnsh_dict.keys()
	
	d = {}
	
	ending = dict()
	
	stage = -1
	
	f = open(filename, 'r')
	for line_number, line in enumerate(f):
		line = line.strip()
		
		if len(line) <= 0 or line[0]=='#': #use # as a comment character, and skip empty lines
			continue
		
		#check for characters that can't be used
		skip_line = False
		for c in line:
			try:
				c.decode('utf-8')
			except UnicodeDecodeError:
				print "Unable to decode character %s in line %d: \"%s\"" % (c, line_number, line)
				skip_line = True
				break
		if skip_line:
			continue
		
		#split the lines, then check for malformed entries
		try:
			key, text = line.split("=", 1)
		except ValueError:
			#this helps to find lines that are misformed 
			print "Unable to split line %d: \"%s\"" % (line_number, line)
			continue
		
		key = key.strip().lower()
		
		stripped = text.strip()
		
		#if the key contains a -, it belongs to a specific stage
		if '-' in key:
			stg, part_key = key.rsplit('-', 1)
			
			#if it starts with a * use the current stage
			if stg[0] == '*':
				key = "%d-%s" % (stage, part_key)
			
			#negative numbers count from the end. -1 is finished, -2 is masturbating, -3 is nude. -4 is the last layer of clothing, and so on.
			#using negative numbers assumes that they are after all the clothes entries
			elif stg[0] == '-' and stg[1:].isdigit():
				key = "%d-%s" % (stage + 4 + int(stg), part_key)
		else:
			part_key = key
		
		#cases, these can be repeated
		if part_key in case_names:
		
			if stripped == "" or stripped == ",":
				#if there's no entry, skip it.
				continue
				
			if ',' not in text:
				img, desc = "", text
			else:
				img,desc = text.split(",", 1) #split into (image, text) pairs
			if key in d:
				d[key].append( (img,desc) ) #add it to existing list of responses
			else:
				d[key] = [ (img, desc) ] #make a new list of responses
				
		#clothes is a list
		elif key == "clothes":
			stage += 1
			if "clothes" in d:
				d["clothes"].append(stripped)
			else:
				d["clothes"] = [stripped]
		
		#this tag relates to an ending squence
		#use a different function, because it's quite complicated
		elif key in ending_tags:
			handle_ending_string(key, stripped, ending, d)
		
		#other values are single lines. These need to be in the data, even if the value is empty
		else:
			d[key] = text
	
	#add the final ending (if it exists)
	add_ending(ending, d)
	
	return d

#make the meta.xml file
def make_meta_xml(data, filename):
	o = ET.Element("opponent")
	
	enabled = "true" if "enabled" not in data or data["enabled"] == "true" else "false"
	ET.SubElement(o, "enabled").text = enabled
	
	values = ["first","last","label","pic","gender","height","from","writer","artist","description"]
	
	for value in values:
		content = ""
		if value in data:
			content = data[value]
		if value == "pic":
			if content == "":
				content = "0-calm"
			content += ".png"
		ET.SubElement(o, value).text = content
		
	#ET.ElementTree(o).write(filename, xml_declaration=True)
	
	pretty_xml = manual_prettify_xml(o)
	ET.ElementTree(pretty_xml).write(filename, xml_declaration=True)

#read the input data, the write the xml files
def make_xml(player_filename, out_filename, meta_filename=None):
	player_dictionary = read_player_file(player_filename)
	write_xml(player_dictionary, out_filename)
	if meta_filename is not None:
		make_meta_xml(player_dictionary, meta_filename)

#make the xml files using the given arguments
#python make_xml <character data file> <behaviour.xml output file> <meta.xml output file>
if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "Please give the name of the dialogue file to process into XML files"
		exit()
	behaviour_name = "behaviour.xml"
	meta_name = "meta.xml"
	if len(sys.argv) > 2:
		behaviour_name = sys.argv[2]
	if len(sys.argv) > 3:
		meta_name = sys.argv[3]
		
	make_xml(sys.argv[1], behaviour_name, meta_name)