
#!/usr/bin/env python3

import os, sys
from PIL import Image
import pathlib
import glob

for file in glob.glob("ic_*"):
    im = Image.open(file)
    im.rotate(-90).resize((128,128)).save("/opt/icons/" + file,"JPEG")
