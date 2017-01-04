import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os

behaviour_values = ["first", "last", "label", "gender", "size", "timer"]
meta_values = ["pic", "height", "from", "writer", "artist", "description"]
single_value_entries = 	behaviour_values + meta_values

card_cases = ["swap_hands", "good_hand", "okay_hand", "bad_hand"]
stripping_cases = ["must_strip_winning", "must_strip_normal", "must_strip_losing", "stripping", "stripped"]
self_mast_cases = ["must_masturbate_first", "must_masturbate", "start_masturbating", "masturbating", "heavy_masturbating", "finishing_masturbating", "finished_masturbating"]
game_over_cases = ["game_over_defeat", "game_over_victory"]
must_strip_cases = ["male_human_must_strip", "male_must_strip", "female_human_must_strip", "female_must_strip"]
accessory_cases = ["male_removing_accessory", "male_removed_accessory", "female_removing_accessory", "female_removed_accessory"]
minor_cases = ["male_removing_minor", "male_removed_minor", "female_removing_minor", "female_removed_minor"]
major_cases = ["male_removing_major", "male_removed_major", "female_removing_major", "female_removed_major"]
important_cases = ["male_chest_will_be_visible", "male_chest_is_visible", "male_crotch_will_be_visible", "male_small_crotch_is_visible", "male_medium_crotch_is_visible", "male_large_crotch_is_visible", "female_chest_will_be_visible", "female_small_chest_is_visible", "female_medium_chest_is_visible", "female_large_chest_is_visible", "female_crotch_will_be_visible", "female_crotch_is_visible"]
mast_cases = ["male_must_masturbate", "male_start_masturbating", "male_masturbating", "male_finished_masturbating", "female_must_masturbate", "female_start_masturbating", "female_masturbating", "female_finished_masturbating"]

clothes_names = list()


#remove the filename extension from a string. So "image.png" becomes "image".
def remove_filename_extension(filename):
	if "." not in filename:
		return filename
	parts = filename.rsplit(".", 1)
	return parts[0]

#read an xml file, and add its contents to the database
def add_xml_contents(filename, db):

	directory_name = os.path.dirname(filename)
	if len(directory_name) <= 0:
		directory_name = os.getcwd()
	directory = os.listdir(directory_name)
	image_names = list()
	for name in directory:
		if name.endswith(".png"):
			#print "appending %s" % (name)
			image_names.append(name)
	
	clothes_count = -1
	stage_count = 0
	
	try:
		tree = ET.parse(filename)
	except IOError:
		print "Error - unable to open \"%s\", skipping file." % filename
		return
		
		
	for number, entry in enumerate(tree.getroot()): #loop through "opponent", in both behaviour and meta xml files
	
		if entry.tag in single_value_entries:
			if entry.text is None:
				entry.text = ""
			text = entry.text.strip()
			if entry.tag == "pic":
				text = remove_filename_extension(text)
			db[entry.tag] = "%s=%s" % (entry.tag, text)
		
		elif entry.tag == "start":
			t = entry[0] #get the "state" variable
			start_str = "start=%s,%s" % (remove_filename_extension(t.attrib["img"]), t.text)
			db["start"] = start_str
			
		elif entry.tag == "wardrobe":
			clothes = list()
			for clothing in entry:
				clothes_str = "clothes=%s,%s,%s,%s" % (clothing.attrib["proper-name"], clothing.attrib["lowercase"], clothing.attrib["type"], clothing.attrib["position"])
				clothes.append(clothes_str)
				clothes_names.append("#lost "+clothing.attrib["lowercase"].strip())
			clothes.reverse()
			
			#complete clothing names
			clothes_names.append("#fully clothed")
			clothes_names.reverse()
			clothes_names[-1] += "/naked"
			clothes_names.extend(["#masturbating", "#finished"])
			
			db["wardrobe"] = clothes
			clothes_count = len(clothes)
		
		elif entry.tag == "behaviour":
			stages = list()
			for stage in entry:
				cases = dict()
				for case in stage:
					states = list()
					for state in case:
						state_str = "%s-%s=%s,%s" % (stage.attrib["id"].strip(), case.attrib["tag"], remove_filename_extension(state.attrib["img"]),state.text.strip())
						states.append(state_str)
					cases[case.attrib["tag"]] = states
				stages.append(cases)
			db["stages"] = stages

#get the name for a stage, usually "#lost clothing"
def get_stage_name(stage_num):
	if stage_num < 0 or stage_num >= len(clothes_names):
		return ""
	return clothes_names[stage_num]

#Does this set of cases have any entries in this stage?
def is_case_in_stage(cases, stage):
	for case in cases:
		if case in stage:
			return True
	return False
	
#get the label for a case
def get_case_group_name(case_group):
	if case_group == card_cases:
		return "#card cases"
	elif case_group == stripping_cases:
		return "#character must strip"
	elif case_group == self_mast_cases:
		return "#character masturbation cases"
	elif case_group == game_over_cases:
		return "#game over"
	elif case_group == must_strip_cases:
		return "#other player must strip"
	elif case_group == accessory_cases:
		return "#other player is removing an accessory"
	elif case_group == minor_cases:
		return "#other player is removing a minor clothing item"
	elif case_group == major_cases:
		return "#other player is removing a major clothing item"
	elif case_group == important_cases:
		return "#other player is exposing themselves"
	elif case_group == mast_cases:
		return "#other player is masturbating"
	return ""
	
#print a set of cases to the given (open) file
def print_cases(out_file, db, cases, split_half = False):
	s = db["stages"]
	f = out_file
	
	f.write(get_case_group_name(cases)+"\n")
	for stage_num, stage in enumerate(s):
	
		if is_case_in_stage(cases, stage):
			f.write(get_stage_name(stage_num)+"\n")
		for case_num, case in enumerate(cases):
		
			#because the stripped case is offset into the next stage
			if case == "stripped" and stage_num < len(s) - 1:
				stage = s[stage_num + 1]
		
			if case not in stage:
				continue #skip if there's nothing to write
			
			#print stage,"\n\n"
			
			for state in stage[case]:
				f.write(state + "\n")
				
			if split_half and case_num == ((len(cases) / 2) - 1):
				f.write("\n")
				
		f.write("\n") #put a new line in between each stage
		
	f.write("\n") #put a new line in between each type of case

#write the output to a given filename
def write_output(filename, database):
	db = database #use shorter name
		
	with open(filename, "w") as f:
		f.write("#required for behaviour.xml\n")
		for value in behaviour_values:
			f.write(db[value]+"\n")
		f.write("\n")
		
		f.write("#required for meta.xml\n")
		for value in meta_values:
			f.write(db[value]+"\n")
		f.write("\n")
		
		f.write("#player clothing\n")
		for clothing in db["wardrobe"]:
			f.write(clothing + "\n")
		f.write("\n")	
		
		f.write("#start image\n")
		f.write(db["start"]+"\n\n")
		
		print_cases(f, db, card_cases)
		print_cases(f, db, stripping_cases)
		print_cases(f, db, self_mast_cases)
		print_cases(f, db, game_over_cases)
		print_cases(f, db, must_strip_cases)
		print_cases(f, db, accessory_cases)
		print_cases(f, db, minor_cases)
		print_cases(f, db, major_cases)
		print_cases(f, db, important_cases, True)
		print_cases(f, db, mast_cases, True)

#take a behaviour file and maybe a meta file, and create a dialogue file
if __name__ == "__main__":
	behaviour_filename = "behaviour.xml"
	meta_filename = "meta.xml"
	
	database = dict()
	
	add_xml_contents(behaviour_filename, database)
	add_xml_contents(meta_filename, database)
	
	out_filename = "behaviour.txt"
	
	
	if len(sys.argv) > 1:
		out_filename = sys.argv[1]
		
	write_output(out_filename, database)
