# visu-segment-anything
visualisation of the product of segment-anything


# First install : 
* https://github.com/facebookresearch/segment-anything

use the script amg.py in the directory scripts on this image : 

![image](https://github.com/facebookresearch/segment-anything/blob/main/notebooks/images/dog.jpg?raw=true) 

You will have this result with the masked images ( black /white ) in the directory : 
![image](https://github.com/zebulon75018/visu-segment-anything/blob/main/2023-04-07_21-51.png?raw=true)

to install maskimg , you need pip install python-opencv jinja2 numpy

#use maskimg.py: 

    usage: maskimg.py [-h] [-f INPUTFILE] [-d INPUTDIR] [-o OUTPUT]

    Script for processing input files and directories

    options:
      -h, --help            show this help message and exit
      -f INPUTFILE, --inputfile INPUTFILE
                            Input file path
      -d INPUTDIR, --inputdir INPUTDIR
                            Input directory path
      -o OUTPUT, --output OUTPUT
                            Output path




The maskimg.py will give you this result in the output directory: 


![image](https://github.com/zebulon75018/visu-segment-anything/blob/main/2023-04-07_21-51_1.png?raw=true)

In the directory , a index.html will be created , so launch a http server IN THE DIRECTORY : python3 -m http.server 9000 

[![3D mask threejs](https://img.youtube.com/vi/4O1ok93kV4g/default.jpg)](https://www.youtube.com/watch?v=4O1ok93kV4g "3D mask threejs")





