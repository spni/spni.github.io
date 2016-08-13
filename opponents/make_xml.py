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

#default images and text for most cases
def get_cases_dictionary():
	d = {}
	#quality of hand
	d["swap_cards"] = [("calm", "I'll exchange ~cards~ cards.")]
	d["good_hand"] = [("happy", "I've got a good hand.")]
	d["okay_hand"] = [("calm", "I've got an okay hand.")]
	d["bad_hand"] = [("sad", "I've got a bad hand.")]
	
	#stripping
	d["stripped"] = [("sad", "I miss my ~clothing~ already...")]
	d["must_strip_winning"] = [("loss", "Well, I guess it had to be my turn eventually...")]
	d["must_strip_normal"] = [("loss", "I guess I lost, huh?")]
	d["must_strip_losing"] = [("loss", "I lost again? But... I have less clothes than everyone else!")]
	d["stripping"] = [("strip", "I guess I'll just take off my ~clothing~...")]
	
	#male pre-strip scenes
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

#default images and text for being nude
def get_nude_cases_dictionary():
	d = {}
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
	for key in default_dictionary.keys():
		contents = get_cases(player_dictionary, default_dictionary, key, stage)
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
		
	if elem.tag in ["stage", "wardrobe", "timer", "start", "behaviour"]:
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
		add_values(s, data, main_dict, stage)
	
	#nude stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, main_dict, stage)
	add_values(s, data, nude_dict, stage)
	
	#masturbating stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, main_dict, stage)
	add_values(s, data, mstb_dict, stage)
			
	#finished stage
	stage += 1
	s = ET.SubElement(bh, "stage", id=str(stage))
	add_values(s, data, main_dict, stage)
	add_values(s, data, fnsh_dict, stage)
	
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

#read in a character's data
def read_player_file(filename):
	main_dict = get_cases_dictionary()
	nude_dict = get_nude_cases_dictionary()
	mstb_dict = get_masturbating_cases_dictionary()
	fnsh_dict = get_finished_Cases_dictionary()
	
	case_names = main_dict.keys() + nude_dict.keys() + mstb_dict.keys() + fnsh_dict.keys()
	
	d = {}
	
	stage = -1
	
	f = open(filename, 'r')
	for line in f:
		line = line.strip()
		
		if len(line) <= 0 or line[0]=='#': #use # as a comment character, and skip empty lines
			continue
			
		key, text = line.split("=", 1)
		
		stripped = text.strip()
		
		if stripped == "" or stripped == ",":
			#if there's no entry, skip it.
			continue
		
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
			if ',' not in text:
				img, desc = "", text
			else:
				img,desc = text.split(",", 1) #split into (image, text) pairs
			if key in d:
				d[key].append( (img,desc) )
			else:
				d[key] = [ (img, desc) ]
				
		#clothes is a list
		elif key == "clothes":
			stage += 1
			if "clothes" in d:
				d["clothes"].append(text)
			else:
				d["clothes"] = [text]
				
		#other values are single lines
		else:
			d[key] = text
	
	return d

#make the meta.xml file
def make_meta_xml(data, filename):
	o = ET.Element("opponent")
	
	enabled = "true" if "enabled" not in data or data["enabled"] == "true" else "false"
	ET.SubElement(o, "enabled").text = enabled
	
	values = ["first","last","label","pic","gender","height","from","writer","artist","description"]
	
	for value in values:
		if value == "pic":
			ET.SubElement(o, value).text = data[value] + ".png"
		else:
			ET.SubElement(o, value).text = data[value]
		
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
	if len(sys.argv) > 3:
		make_xml(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		make_xml(sys.argv[1], sys.argv[2])