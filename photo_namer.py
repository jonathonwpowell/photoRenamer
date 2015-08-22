import sys
import os
import shutil

if sys.argv[1] == "-h":
	print "Usage: photo_namer.py [-h] [-f #]"
	print "-f = number changed in the first folder"
	print "-h = help"
	print "Example: photo_namer.py -f 23 (where 23 is the number renamed in the first folder)"
	print "This is useful if the photos where split into two folders"
	sys.exit()
#find file location

num_ignored = 0;
num_to_ignore = 0;

if sys.argv[1] == "-f":
	try:
		num_to_ignore = sys.argv[2]
	except:
		print "Incomplete command, please use -h for help"
		sys.exit()

while True:
	pic_location = raw_input("Please enter location of pictures: ")
	if os.path.exists(pic_location):
		break
	print "*** Location does not exist, please enter another ***"

new_pic_location = pic_location + "\\rename"
#create new folder for renamed images
if not os.path.exists(new_pic_location):
	os.makedirs(new_pic_location)
#if the location already exists, check if it should be deleted and remade
else:
	should_del = raw_input("Folder for renamed pictures already exists. Delete it to continue? (y/n) ")
	#should_del = should_del.lower()
	if should_del == "y" or should_del == "yes":
		should_del = raw_input("Are you sure you want to delete " + new_pic_location + " (y/n) ")
		if should_del == "y" or should_del == "yes":
			shutil.rmtree(new_pic_location)
			os.makedirs(new_pic_location)
		else:
			sys.exit()
	else:	
		sys.exit()
	
for filename in os.listdir(pic_location):
	if filename.startswith("DSC_"):
		shutil.copy(pic_location + "\\" + filename, new_pic_location)
	
#get all strains
num_of_strains = int(input("Enter Number of Strains: "))
list_of_strains = []
for x in range(0,num_of_strains):
	list_of_strains.append(int(input("Enter Strain Number: ")))
list_of_strains = sorted(list_of_strains)	

#get the number of duplicates and time
num_of_dups = int(input("Enter number of duplicates: "))
time_of_batch = str(input("How many hours since inoculation? "))

#define the media types and quadrant types
media_types = ["IS","LB"]
quad_types = ["A","B","C","D"]

new_filename = "empty"

found_file = False
#strain 1
for x in range(0,num_of_strains):
	#strain 2
	for b in range (x+1,num_of_strains):
		#media
		for y in range(0,len(media_types)):
			#duplicates
			for z in range(1,num_of_dups + 1):
				#quadrant
				for a in range(0,len(quad_types)):
					if int(num_ignored) < int(num_to_ignore):
						num_ignored = num_ignored + 1
						#print "ignored, " + str(num_to_ignore) + " " + str(num_ignored)
						continue
					new_filename = str(list_of_strains[x]) + "-" + str(list_of_strains[b]) + "-" + media_types[y] + "-" + time_of_batch + "-" + str(z) + "-" + quad_types[a] + ".jpg"
					found_file = False
					for pic_to_rename in os.listdir(new_pic_location):
						if pic_to_rename.startswith("DSC_"):
							os.rename(new_pic_location + "\\" + pic_to_rename,new_pic_location + "\\" + new_filename)
							found_file = True
							break
					if not found_file:
						print "***WARNING: PICTURES SPLIT BETWEEN TWO FOLDERS***"
						sys.exit()
					