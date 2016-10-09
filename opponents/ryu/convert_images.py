
def convert_data(in_name, out_name):
	stage = 0
	label = ""
	with open(in_name, "r") as fin:
		with open(out_name, "w") as fout:
			for line in fin:
				line = line.strip()
				
				if len(line) <= 0:
					#line is empty, don't do anything
					continue
				
				parts = line.split()
				try:
					number = int(parts[0])
					
					#if continuing here, it is a stage description
					if number < 0:
						number += 9 #properly set negative numbers
					stage = number
					fout.write("\n")
					continue
				except ValueError:
					pass
				
				parts = line.split("**")
				try:
					number = int(parts[0])
					#is a description
					fout.write("%d-%s=%s\n\n" % (stage, label, line))
					continue
				except ValueError:
					pass
					
				#is a label
				parts = line.split(":")
				label = parts[0].lower()
				

if __name__ == "__main__":
	in_name = "images.txt"
	out_name = "image_codes.txt"
	convert_data(in_name, out_name)