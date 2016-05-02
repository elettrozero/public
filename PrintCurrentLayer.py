#Name: Print Current Layer
#Info: Display layers' state
#Depend: GCode
#Type: postprocess

import re

with open(filename, "r") as f:
	lines = f.readlines()


totalLayers = 0
with open(filename, "w") as f:
	for line in lines:
		f.write(line)
		if line.startswith(';'):
			if line.startswith(';Layer count:'):
				totalLayers = line[14:-1]
			if line.startswith(';LAYER:'):
				currentLayer = str(int(line[7:-1])+1)
				f.write("M117 Layer " + currentLayer + "/" + totalLayers + "\n")
