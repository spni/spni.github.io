import sys
import time
import os

CONST_MEASUREMENTS_TAB_ID = "ca"
CONST_HEIGHT_INDEX = 0
CONST_LEG_HEIGHT_INDEX = 3
CONST_VAGINA_TAB_ID = "dc"
CONST_VAGINA_INTERNAL_COLOR_INDEX = 4
CONST_VAGINA_WETNESS_LEVEL_INDEX = 0
CONST_FACE_TAB_ID = "dd"
CONST_FACE_TYPE_INDEX = 1
CONST_FACE_WIDTH_INDEX = 2
CONST_NIPPLE_TAB_ID = "dh"
CONST_NIPPLE_COLOR_INDEX = 0
CONST_BREAST_TAB_ID = "di"
CONST_BREAST_SIZE_INDEX = 0
CONST_EARS_TAB_ID = "pa"
CONST_EAR_HEIGHT_INDEX = 7
CONST_TAB_TERMINATOR = "_"

itemLocation = {
		"height":(CONST_MEASUREMENTS_TAB_ID, CONST_HEIGHT_INDEX),
		"legHeight":(CONST_MEASUREMENTS_TAB_ID, CONST_LEG_HEIGHT_INDEX),
		"faceType":(CONST_FACE_TAB_ID, CONST_FACE_TYPE_INDEX),
		"faceWidth":(CONST_FACE_TAB_ID, CONST_FACE_WIDTH_INDEX),
		"earHeight":(CONST_EARS_TAB_ID, CONST_EAR_HEIGHT_INDEX),
		"breastSize":(CONST_BREAST_TAB_ID, CONST_BREAST_SIZE_INDEX),
		"nippleColor":(CONST_NIPPLE_TAB_ID, CONST_NIPPLE_COLOR_INDEX),
		"vaginaInternalColor":(CONST_VAGINA_TAB_ID,CONST_VAGINA_INTERNAL_COLOR_INDEX),
		"vaginaWetness":(CONST_VAGINA_TAB_ID, CONST_VAGINA_WETNESS_LEVEL_INDEX)
		}
		
itemValue = {}

def getValue(data, location):
	try:
		dataReadStart = data.index(location[0]) + 1
	except ValueError:
		print data, location
	currentChar = data[dataReadStart]
	dataPointer = dataReadStart
	
	while currentChar != CONST_TAB_TERMINATOR:
		dataPointer += 1
		currentChar = data[dataPointer]

	data = data[dataReadStart + 1:dataPointer]
	data = data.split(".")
	return data[location[1]]
	

def promptValue(valueName, sampleData):
	value = itemValue[valueName]
	print ("\n\t> Current %s is: %s" % (valueName, itemValue[valueName]))
	value = raw_input("\t\t > Set to: ") or value
	print ("\t> %s is set to: %s" % (valueName, value))
	return value
	
def displayInstructions():
	print ("\t> Enter new values as prompted. \n\t> Leaving a field blank will maintain the original value\n\n\t> These are the attributes that can be altered:\n")
	
	for key in sorted(itemLocation.keys()):
		print ("\t\t%s" % key)

def displayWarning():
		print ("\n\t> This software offers no garuntee that it will work properly!")
		print ("\t> Before writing to file, please make sure you have made a back up!")
		print ("\t> The follwing values will be changed:\n")
		
		for key in sorted(itemValue.keys()):
			print ("\t\t%s: %s" % (key, itemValue[key]))
		
		while True:	
			ans = raw_input("\n\t>Would you like to write to file? (Please type yes or no): ").lower()
			if ans == 'yes' or ans == 'no':
				break
		
		if ans == 'no':
			print ("\n\t> Terminating...")
			sys.exit(0)

	
def editData(data):
	displayInstructions()
	valueName = ''
	while True:
		valueName = raw_input("\n\t> What would you like to edit? (Type done when finished): ").strip()
		if valueName == 'done':
			break
		if valueName not in itemLocation.keys():
			print ("\n\t> Invalid attribute. Try again.")
			continue
		itemValue[valueName] = promptValue(valueName, data[0])
	
	
def writeFile(fileName):
	lines = []
	with open(fileName, "r") as f:
		for lineNumber, line in enumerate(f):
			
			line = line.strip()
			if len(line) <=0 or line[0] == '#' or '***' in line:
				lines.append(line + "\n")
				continue
			
			newLine = ''
			
			try:
				imageName, imageData = line.split("=",1)
				version, imageData = imageData.split("**",1)
				tabs = imageData.split(CONST_TAB_TERMINATOR)
				
				newLine = imageName + "=" + version + "**"
				
				for tab in tabs:
					tabID = tab[:2]
					values = tab[2:]
					#values.strip()
					#if not len(values) <= 0:
					values = values.split(".")
					
					for name, location in itemLocation.iteritems():
						if tabID == location[0]:
							values[location[1]] = itemValue[name]
					
					newLine += (tabID + ".".join(values) + "_")
					
				newLine = newLine[:-1] + "\n"
			
			except ValueError:
					print("Error - unable to split line at line number %d: \"%s\"" % (lineNumber, line))
					print("Write failed. Terminating.")
					break
					
			lines.append(newLine)
	
	name, ext = os.path.splitext(fileName)
	newFile = name + "_rev" + str(time.time())[3:5] + ext
	
	with open(newFile, "w") as f:
		f.writelines(lines)
		f.close()

def readFile(fileName):
	data = list()
	with open(fileName, "r") as f:
		for lineNumber, line in enumerate(f):
			
			line = line.strip()
			if len(line) <=0 or line[0] == '#' or '***' in line:
				continue
				
			try:
				lineData = line.split("=", 1)[1]
			except ValueError:
				print("Error - unable to split line at line number %d: \"%s\"" % (lineNumber, line))
				continue
			
			lineData = lineData.strip()
			data.append(lineData)
	return data

def massModification(fileName):
	data = readFile(fileName)
	
	for name, location in itemLocation.iteritems():
		itemValue[name] = getValue(data[0], location)
		
	editData(data)
	displayWarning()
	writeFile(fileName)

if __name__ == '__main__':
	massModification(sys.argv[1])