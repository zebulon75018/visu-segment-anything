import numpy as np 
import cv2 
import argparse
import glob
import os
import jinja2


#jinja 
templateLoader = jinja2.FileSystemLoader(searchpath="./template/")
templateEnv = jinja2.Environment(loader=templateLoader)


# chatgpt make me this argumeny parser piece of code ... thank's...
# Create the argument parser
parser = argparse.ArgumentParser(description="Script for processing input files and directories")

# Add inputfile argument
parser.add_argument("-f", "--inputfile", type=str, help="Input file path")

# Add inputdir argument
parser.add_argument("-d", "--inputdir", type=str, help="Input directory path")

# Add output argument
parser.add_argument("-o", "--output", type=str, help="Output path")

# Parse the arguments
args = parser.parse_args()

# Access the argument values
inputfile = args.inputfile
inputdir = args.inputdir
output = args.output
namemaskoutput = []
image = cv2.imread(inputfile)
height, width = image.shape[:2]

for imgmask in glob.glob("%s/*.png" %( inputdir )):
   mask = cv2.imread(imgmask,cv2.IMREAD_COLOR)
   masked = cv2.bitwise_and(image,mask)

   # https://www.geeksforgeeks.org/removing-black-background-and-make-transparent-using-python-opencv/
   # Convert image to image gray
   tmp = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
  
   # Applying thresholding technique
   _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
  
   # Using cv2.split() to split channels 
   # of coloured image
   b, g, r = cv2.split(masked)
  
   # Making list of Red, Green, Blue
   # Channels and alpha
   rgba = [b, g, r, alpha]
  
   # Using cv2.merge() to merge rgba
   # into a coloured/multi-channeled image
   dst = cv2.merge(rgba, 4)
   cv2.imwrite("%s/masked_%s" % ( output , os.path.basename(imgmask)),dst)
   namemaskoutput.append("masked_%s" % (  os.path.basename(imgmask)))


cv2.imwrite("%s/original.png" % ( output ),image)



template = templateEnv.get_template("threejs.html")
outputText = template.render(namemaskoutput=namemaskoutput,w=width, h= height, scale = width/height)  # this is where to put args to the template renderer
with open("%s/index.html" % ( output ) , 'w') as f:
    f.write(outputText)
