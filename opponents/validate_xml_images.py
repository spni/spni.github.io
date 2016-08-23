import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os

def check_referenced_images(filename):
	directory_name = os.path.dirname(filename)
	if len(directory_name) <= 0:
		directory_name = os.getcwd()
	directory = os.listdir(directory_name)
	image_names = list()
	for name in directory:
		if name.endswith(".png"):
			#print "appending %s" % (name)
			image_names.append(name)

	tree = ET.parse(filename)
	for number, entry in enumerate(tree.getroot()):
		if entry.tag == "behaviour":
			for stage in entry:
				for case in stage:
					for state in case:
						image_filename = state.attrib["img"]
						if image_filename not in image_names:
							print "Image filename \"%s\" used by %s-%s-%s has not been found" % (image_filename, stage.attrib["id"].strip(), case.attrib["tag"].strip(), state.text.strip())
		
if __name__ == "__main__":
	xml_filename = "behaviour.xml"
	if len(sys.argv) > 1:
		xml_filename = sys.argv[1]
	check_referenced_images(xml_filename)
